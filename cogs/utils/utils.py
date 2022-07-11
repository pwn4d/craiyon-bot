import base64
import os
import cv2
from dotenv import load_dotenv
import numpy as np
import aiohttp

load_dotenv("../../.env")
BORDER_WIDTH = os.getenv("BORDER_WIDTH", 4)  # px
GENERATED_FILE_NAME = os.getenv("GENERATED_FILE_NAME", "latest_craiyon.jpg")

file_path = os.path.join('image', 'latest_craiyon.jpg')


class NoImageError(Exception):
    pass


async def generate_image(search_query: str) -> str:
    data = {"prompt": search_query}
    url = "https://backend.craiyon.com/generate"

    # Generate Image from Search Query
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            # If status is not ok
            if response.status != 200:
                print(await response.text())
                raise NoImageError
            image_dict = await response.json()

    # Decode and combine images
    for i, _image in enumerate(image_dict["images"]):
        image_string = base64.b64decode(_image)
        np_arr = np.frombuffer(image_string, dtype=np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        horizontal_border = 0  # px
        vertical_border = 0  # px
        # Borders on top and bottom of the center row
        if 2 < i < 6:
            horizontal_border = BORDER_WIDTH
        # Borders on sides of the center column
        if (i - 1) % 3 == 0:
            vertical_border = BORDER_WIDTH

        image = cv2.copyMakeBorder(
            image, 
            horizontal_border, 
            horizontal_border, 
            vertical_border,
            vertical_border,
            borderType=cv2.BORDER_CONSTANT, 
            value=[0, 0, 0]
        )

        # Combine images
        match i:
            case 0:  # First image
                image_row = image
            case 3:  # First column, second row
                compound_image = image_row
                image_row = image
            case 6:  # First column, third row
                compound_image = cv2.vconcat([compound_image, image_row])
                image_row = image
            case _:  # 1 | 2 | 4 | 5 | 7 | 8
                image_row = cv2.hconcat([image_row, image])

    compound_image = cv2.vconcat([compound_image, image_row])

    cv2.imwrite(file_path, compound_image)

    return file_path
