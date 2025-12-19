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
print("توکن دریافتی خود را از @BotFather دریافت کنید در کادر زیر وارد کنید در صورت نداشتن مهارت فیلم اموزش را از کانال ____ تماشا کنید ")
token = input("->")
app = BotClient(token)

@app.on_update(filters.group)
async def handle_all_group_messages(client: BotClient, update: Update):
    try:
        # 1. استخراج اطلاعات
        message = update.new_message
        chat_guid = update.chat_id
        message_id = message.message_id
        user_guid = message.sender_id
        
        # 2. بررسی متن پیام
        message_text = getattr(message, 'text', '')
        if not message_text:
            return
        
        has_link = any(pattern in message_text.lower() 
                      for pattern in ['http://', 'https://', 't.me/', 'rubika.ir/', '@'])
        
        if not has_link:
            return
        
        print(f"\n{'🚨'*3} لینک تشخیص داده شد! {'🚨'*3}")
        print(f"   کاربر: {user_guid}")
        print(f"   متن: {message_text[:50]}...")
        
        try:
            await client.delete_message(
                chat_id=chat_guid,
                message_id=message_id
            )
            print("   ✅ پیام حذف شد.")
            
            print("   📝 عملیات حذف پیام کامل شد.")
            
            try:
                if hasattr(client, 'ban_chat_member'):
                    
                    try:
                        result = await client.ban_chat_member(
                            chat_id=chat_guid,
                            user_id=user_guid
                        )
                        print(f"   ✅ کاربر حذف شد! نتیجه: {result}")
                    except Exception as ban_error:
                        try:
                            await client.ban_chat_member(
                                object_guid=chat_guid,
                                member_guid=user_guid
                            )
                        except:
                            pass
                else:
                    pass                    
                    methods = [m for m in dir(client) if 'ban' in m.lower() or 'kick' in m.lower()]
                    
            except Exception as test_error:
                pass
            # 4.4 ارسال پیام اخطار
            try:
                warning_msg = "⚠️ ارسال لینک در این گروه مجاز نیست. پیام حذف شد."
                await client.send_message(
                    object_guid=chat_guid,
                    text=warning_msg
                )
            except Exception as warn_error:
                pass
        except Exception as e:
            pass            
    except Exception as e:
        pass
if __name__ == "__main__":
    print("🤖 ربات آنتی‌لینک فعال شد...")
    app.run()
#
