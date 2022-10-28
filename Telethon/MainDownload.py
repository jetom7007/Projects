import datetime

from telethon import functions
from telethon.sync import TelegramClient, events

# Use your own values from my.telegram.org
api_id = 21767556
api_hash = '80e2ef1f848ffdd325c0a87592dc33ca'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    # print(client.download_profile_photo('me'))

    result = client(functions.messages.GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer='username',
        limit=500,
        hash=0,
        folder_id=0,
    ))

for chat in result.chats:
    print(chat)