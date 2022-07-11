# craiyon-bot
A Discord bot that uses the AI at [craiyon](https://www.craiyon.com/) to generate images

## Setup
### Prerequisites
You must have Git and Python 3.10+ installed.

### Clone the Repo
Clone the repo down: `git clone https://github.com/based-jace/craiyon-bot.git`

Once cloned, add a `.env` file in the top-level directory (the directory containing `bot.py`).

### Install Dependencies
Create a new virtual environment: 
```
python -m venv env
```

Activate your virtual environment.
```
# Unix
source env/bin/activate

# Windows
/env/Scripts/activate
```

Install the dependencies from requirements.txt:
```
pip install -r requirements.txt
```

### Create a Discord Bot
Create an account on the [Discord Developer Portal](https://discord.com/developers/applications)

Create a new Application called "Craiyon Bot" 

*Or name it anything else you'd like*

Give the app an icon, description, and tags

Go to the "Bot" tab

Click "Add Bot"

Change the icon if you want

Under "Bot Permissions," select "Read Messages/View Channels," "Send Messages," and "Manage Messages," "Attach Files," and "Read Message History."

Generate a new token (the button might say "Reset Token").

Copy the token

In the `.env` file we generated earlier, add the key/value: 
```
DISCORD_TOKEN={{YOUR_TOKEN}}
```

Under the OAuth2 tab, click "URL Generator"

Select the "bot" Scope, then give the bot the same permissions that we gave it above.

Copy the Generated URL at the bottom of the page, paste it into your browser, then select the server you would like to add the bot to.

## Running the Bot

Ensure you are inside of your virtual environment:
```
# Unix
source env/bin/activate

# Windows
/env/Scripts/activate
```

Then activate the bot:
```
python bot.py
```
