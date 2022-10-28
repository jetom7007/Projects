from telethon import TelegramClient, events

api_id = 21767556
api_hash = '80e2ef1f848ffdd325c0a87592dc33ca'

client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hi' in event.raw_text:
        await event.reply('Hello, How Are You?')


client.start()
client.run_until_disconnected()
