# ScrambleBot
Discord bot that creates random presentation orders for voice channels

## Building the project

### Set up virtualenv
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Create secrets file
``` 
vim .env
```

Contents:
```
BOT_TOKEN="<bot_token_here>"
```

### Run the bot
```
python3 scramble.py
```

## Virtualenv Cheatsheet

### Install virtualenv
```
pip install virtualenv
```

### Create a virtual environment
```
python3 -m venv <env_name>
```

### Activate the virtual environment

#### Linux/MacOS

```
source env/bin/activate
```

#### Windows
```
env/Scripts/activate.bat // In CMD
env/Scripts/Activate.ps1 // In Powershel
```

### Exit the virtual environment
```
deactivate
```

### Create requirements.txt
```
pip freeze > requirements.txt
```

### Install from requirements.txt
```
pip install -r requirements.txt
```

### View installed libraries
```
pip list
```
