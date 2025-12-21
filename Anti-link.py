import re
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from rubpy.bot import BotClient, filters
    from rubpy.bot.models import Update
except ImportError:
    install("rubpy")
    from rubpy.bot import BotClient, filters
    from rubpy.bot.models import Update

token = input("توکن ربات را وارد کنید: ")
app = BotClient(token)

@app.on_update(filters.group)
async def handle_all_group_messages(client: BotClient, update: Update):
    message = update.new_message
    chat_guid = update.chat_id
    message_id = message.message_id
    user_guid = message.sender_id
    
    message_text = getattr(message, 'text', '')
    if not message_text:
        return
    
    has_link = any(pattern in message_text.lower() 
                  for pattern in ['http://', 'https://', 't.me/', 'rubika.ir/', '@'])
    
    if not has_link:
        return
    
    await client.delete_message(
        chat_id=chat_guid,
        message_id=message_id
    )
    
    try:
        await client.ban_chat_member(
            chat_id=chat_guid,
            user_id=user_guid
        )
    except:
        pass
    
    try:
        await client.send_message(
            object_guid=chat_guid,
            text="⚠️ ارسال لینک در این گروه مجاز نیست. پیام حذف شد."
        )
    except:
        pass

if __name__ == "__main__":
    app.run()
