import settings
from discord import Intents, Message
from discord.ext import commands, tasks
from responses import get_response, json_save
import time
import json

#Bot set up
intents: Intents = Intents.default()
intents.message_content = True #NOQA
bot = commands.Bot(command_prefix="!", intents=intents)

#Handling start up
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')
    hourly_messages.start()

#Handle incoming messages
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_messages(message, user_message)

#Message Functionality
async  def send_messages(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled properly)')
        return

    is_private = user_message[0] == '?'

    if message.mentions:
        for mention in message.mentions:
            # Fetch the user information from the Discord API
            user = await bot.fetch_user(mention.id)

            user_message = user_message.replace(f'<@{mention.id}>', f'@{user}')
            
    try:
        response: str = get_response(str(message.author), user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@tasks.loop(hours=1)
async def hourly_messages():
    channel_id = 1205932199837437952
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send(f'`some10n3` บอกรัก `akira_sannn` ตอน `{time.ctime()}`')

        json_data = open('data.json', encoding='utf-8').read()
        json_obj = json.loads(json_data)

        for i in json_obj['count']:
            if i['name'] == 'some10n3':
                for j in i['reciever']:
                    if j['name'] == 'akira_sannn':
                        j['count'] += 1
                        json_save(json_obj)
                        return
                i['reciever'].append({'name': 'akira_sannn', 'count': 1})
                json_save(json_obj)
                return

#Main entry point
def main() -> None:
    bot.run(settings.TOKEN)


if __name__ == '__main__':
    main()