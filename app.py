#   Import repositories

from os import getenv
from dotenv import load_dotenv

from model.system.botSetup import DiscordSetup

load_dotenv()

def run_bot ():
        
    #   Initializing class
    disc = DiscordSetup()
    
    disc.SystemSetup()
    disc.GamersModule()
    disc.CommunityModule()

    #   Run the bot
    disc.bot.run(getenv("Token"))

if __name__ == '__main__':
    run_bot()