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

@app.on_update(filters.group) #فیلترگروه
async def handle_all_group_messages(client: BotClient, update: Update):
    #دریافت ورودی ها
    message = update.new_message
    chat_guid = update.chat_id
    message_id = message.message_id
    
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
    ) #حذف پیام کاربر
    
if __name__ == "__main__":
    print("ربات انتی لینک فعال هست")
    app.run()
