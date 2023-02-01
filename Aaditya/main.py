import discord

class Client(discord.Client):
    async def on_ready(self):
        print("Bot is online!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("!hi"):
            await message.channel.send(f"Hi! {message.author.mention}")
        elif message.content.startswith("!search"):
            x = ' '.join(message.content.split()[1:])
            print(x) #TODO

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