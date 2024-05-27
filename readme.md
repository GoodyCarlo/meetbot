# Setup Instructions
### Create and activate virtual environment
`python3 -m venv venv`
`source venv/bin/activate`
### Install requirements
`pip install -r requirements.txt`
### Create .env file and add TOKEN
`mkdir .env`
`TOKEN = <YOUR DISCORD BOT TOKEN HERE>`
### Start Bot
`python .\main.py`
### For background Running
`nohup python .\main.py &`

# For auto rerun of `main.py`
Run `python .\run_bot.py` instead of `python .\main.py`