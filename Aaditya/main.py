import discord
from scrapper import Scraper

class Client(discord.Client):

    async def on_ready(self):
        print("Bot is online!")
        self.scraper = Scraper()

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("!hi"):
            await message.channel.send(f"Hi! {message.author.mention}")
        elif message.content.startswith("!search"):
            x = ' '.join(message.content.split()[1:])
            await message.channel.send(f"Looking up twitter for {x}")
            file = self.scraper.scrape(x)
            await message.channel.send(file=discord.File(fp=file, spoiler=False))

def main():
    #only works if command is invoked from the working directory itself
    with open(".env", "r") as file: 
        token = file.readline()
    
    intent = discord.Intents.default()
    intent.message_content = True
    
    client = Client(intents=intent)
    client.run(token)

if __name__ == "__main__":
    main()