import ast
import random
import requests
import base64
import discord

working = False

with open(".token", "r") as f:
    TOKEN = f.readlines()

file_name = ''



client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is up and running')


@client.event
async def on_message(message):
    if 'c!craiyon' in message.content:
        global working
        craiyon_embed = discord.Embed(title=f"Generating{message.content.replace('c!craiyon','')}", url="https://craiyon.com",
                                      description="Craiyon is thinking.. (This may take up to 3 minutes)",
                                      color=0xffae00)
        wait = await message.reply(embed=craiyon_embed)
        print(f"Requesting {message.content.replace('c!craiyon','')}")
        try:
            if working == False:
                working = True
                get_image(message.content.replace('c!craiyon',''))
                print('Got Image | Sending...')
                await wait.delete()
                working = False
            else:
                await message.channel.send('Bot in use please wait...')

        except Exception:
            embed = discord.Embed(title="Error", url="https://craiyon.com",
                                  description="An Error Occured | This may be too mass requests, consider waiting a few minutes before retrying",
                                  color=0xffae00)
            embed=discord.Embed(title="Error", url="https://craiyon.com", description="An Error Occured | This may be too mass requests, consider waiting a few minutes before retrying", color=0xffae00)
            await message.channel.send(embed=embed)
        await message.reply(file=discord.File(file_name))
    if message.content == 'c!help':
        help_embed = discord.Embed(title="Craiyon Bot", url="https://craiyon.com",
                              description="Generates Images From https://craiyon.com | Prefix is c!help   `c!craiyon` - Generates an image based on a word  e.g `c!craiyon tree` will generate a tree on https://craiyon.com",
                              color=0xffae00)
        await message.channel.send(embed=help_embed)

def get_image(word):
    global file_name
    data = {"prompt": word}
    url = "https://backend.craiyon.com/generate"
    response = requests.post(url, json=data)
    file_name = f'images/{word[1:]}{random.randint(0,1000000)}.jpg'
    image_dict = (ast.literal_eval(response.content.decode('utf-8')))
    image_string = image_dict['images'][0]
    dec_data = base64.b64decode(image_string)
    image_result = open(file_name, 'wb')
    image_result.write(dec_data)


client.run(TOKEN[0])

