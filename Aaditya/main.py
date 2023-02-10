import discord
from scrapper import Scraper
from config import Config

class Client(discord.Client):

    async def on_ready(self):
        print("Bot is online!")
        self.scraper = Scraper()
        self.config = Config('config')

    async def on_message(self, message):
        if message.author == self.user:
            return
            
        if message.content.startswith("!hi"):
            await message.channel.send(f"Hi! {message.author.mention}")

        elif message.content.startswith("!search"):
            x = ' '.join(message.content.split()[1:])
            await message.channel.send(f"Looking up twitter for {x}")

            try:
                data = self.scraper.scrape(x, int(self.config.val('num')), self.config.val('likes'))
            except:
                await message.channel.send(f"Couldn't find anything about {x} on twitter")
                return
            
            desc = ""

            for content, link in data.items():
                content = content[:30] + '...' if len(content) > 30 else content
                desc += f"- [{content}]({link})\n\n"

            await message.channel.send(embed=discord.Embed(color=discord.Colour.blurple(), title=x, description=desc))

        elif message.content.startswith('!setlikes'):
            try:
                x = int(message.content.split()[1])
                self.config.update('likes', x)
                await message.channel.send(f"Done! Minimum likes set to {x}")
            except:
                await message.channel.send("Please enter an integer value")

        elif message.content.startswith('!setnum'):
            try:

                x = int(message.content.split()[1])
                self.config.update('num', x)
                await message.channel.send(f"Done! Number of entries set to {x}")
            except:
                await message.channel.send("Please enter an integer value")

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