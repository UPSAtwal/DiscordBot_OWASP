import discord
from scrapper import Scraper
from config import Config


class Client(discord.Client):

    async def on_ready(self):
        print("Bot is online!")
        self.scraper = Scraper()
        self.config = Config('config')
        self.prefix = self.config.val('prefix')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(f'{self.prefix}hi'):
            await message.channel.send(f"Hi! {message.author.mention}")

        elif message.content.startswith(f'{self.prefix}search'):
            x = ' '.join(message.content.split()[1:])
            await message.channel.send(f"Looking up twitter for {x}")

            try:
                data = self.scraper.scrape(x, int(self.config.val('num')), self.config.val(
                    'likes'), self.config.val('ldate'), self.config.val('sdate'))
            except:
                await message.channel.send(f"Couldn't find anything about {x} on twitter")
                return

            desc = ""

            for content, link in data.items():
                content = content[:30] + \
                    '...' if len(content) > 30 else content
                desc += f"- [{content}]({link})\n\n"

            await message.channel.send(embed=discord.Embed(color=discord.Colour.blurple(), title=x, description=desc))

        elif message.content.startswith(f'{self.prefix}setlikes'):
            try:
                x = int(message.content.split()[1])
                self.config.update('likes', x)
                await message.channel.send(f"Done! Minimum likes set to {x}")
            except:
                await message.channel.send("Please enter an integer value")

        elif message.content.startswith(f'{self.prefix}setnum'):
            try:

                x = int(message.content.split()[1])
                self.config.update('num', x)
                await message.channel.send(f"Done! Number of entries set to {x}")
            except:
                await message.channel.send("Please enter an integer value")

        elif message.content.startswith(f'{self.prefix}date'):
            x = message.content.split()[1]
            y = message.content.split()[2]
            self.config.update('sdate', x)
            self.config.update('ldate', y)
            await message.channel.send(f"Done! Only Tweets made after {x} and before {y} will be shown")
        
        elif message.content.startswith(f'{self.prefix}prefix'):
            x = message.content.split()[1]
            self.prefix = x
            self.config.update('prefix', x)
            await message.channel.send(f'Success! Prefix has been updated to **{x}**')

        elif message.content.startswith(f'{self.prefix}help'):
            desc = f"""
            **List of Commands**
            1. **{self.prefix}search**: Search Twitter for anything
            2. **{self.prefix}hi**: Hi :)
            3. **{self.prefix}setlikes**: Set minimum likes for tweets to have
            4. **{self.prefix}setnum**: Set number of tweets to show
            5. **{self.prefix}date**: Set date range of tweets. Use YYYY-MM-DD format
            6. **{self.prefix}prefix**: Set the prefix for the bot
            7. **{self.prefix}help**: This command

            **The prefix for the bot is set to {self.prefix}**
            """
            await message.channel.send(embed=discord.Embed(color=discord.Colour.blurple(), title="Commands", description=desc))

def main():
    # only works if command is invoked from the working directory itself
    with open(".env", "r") as file:
        token = file.readline()

    intent = discord.Intents.default()
    intent.message_content = True

    client = Client(intents=intent)
    client.run(token)


if __name__ == "__main__":
    main()
