import discord
from  random import randint
from time import sleep

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # print(f'Message from {message.author}: {message.content}')
        list_of_poems = open('C:\\Users\\Glc\\list_of_poems.txt', encoding="utf8")  # Файл со стихотворениями
        flag = False
        channel = message.channel
        message_line = message.content
        flag = False
        if message.content == 'Hi':
            # print(f'Hello {message.author}')
            await channel.send(f'Hello {str(message.author)[:-5]}')
        for i in list_of_poems:
            i = i[:-1]  # Строка из файла
            if flag:
                if message_line != i:
                    await channel.send(i)
                    message_line = i
                else:
                    flag = False
                    break
                continue
            if i == message_line:
                flag = True
                await channel.send(i)








intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA3Njk0MjU2NjU4MDMwNjA2MQ.GL4iIE.dX4Qnex12sEz-MBZcCV-fGDL4KkFx0SFB6ifGQ')
