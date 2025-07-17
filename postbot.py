from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup
from datetime import datetime, timezone, timedelta
import asyncio
from pytz import timezone

# Bot and channel configuration
BOT_TOKEN = "7627783522:AAEqAlJ6O42wFv0SS7HzsAR8xFadu75FKn4"
CHANNEL_ID = "@Tech_Pulse_Proxy_MTProto"
ADMIN_ID = 1878312179

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Pakistan Standard Time (PST)
pst = timezone('Asia/Karachi')

# 16 formatted posts
POSTS = [
    """🤖 Android Trick: Reduce animations

🎨 Make your phone feel quicker by turning off system animations in Developer Options.

📂 #Android #SpeedBoost #PhoneTips
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 PC Tip: Ctrl + Shift + Esc

🎨 Instantly open Task Manager and monitor system performance with a quick shortcut.

📂 #WindowsTips #TaskManager #PCShortcuts
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Jazz Offer: Weekly TikTok 5GB Rs. 25

🎨 Enjoy 5GB TikTok data for 7 days using this offer code.

📂 #Jazz #TikTok #WeeklyOffer
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 App: Pure Tuber – YouTube without ads

🎨 Watch YouTube videos ad-free with background play and popup mode.

🌐 Try: https://puretuber.com

📂 #YouTubeApp #NoAds #VideoApp
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Chrome Update: Version 126

🎨 Latest Chrome update includes better battery optimization for laptops.

📂 #ChromeUpdate #BatterySaver #BrowserTips
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 AI Tool: Cleanup.pictures

🎨 Remove unwanted objects from images in seconds using AI.

🌐 Try: https://cleanup.pictures

📂 #AI #ImageCleanup #PhotoEdit
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 WhatsApp Tip: Lock Chats

🎨 Secure your private chats by locking them from Settings > Privacy > Lock Chats.

📂 #WhatsAppTips #Privacy #ChatLock
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Tip: Restart Your Phone Weekly

🎨 Boost performance and fix minor issues by restarting your device regularly.

📂 #PhoneCare #PerformanceTip #MobileHack
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Zong Offer: Weekly 8GB YouTube Rs. 120

🎨 Activate this YouTube bundle for a full week of video streaming.

📂 #ZongOffer #YouTubeData #InternetBundle
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 PC Shortcut: Win + Shift + S

🎨 Quickly capture a custom screenshot using the Snipping Tool shortcut.

📂 #Windows #ScreenshotTip #PCShortcuts
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 App: SnapDrop – Airdrop Alternative

🎨 Share files instantly between devices without any app installs.

🌐 Try: https://snapdrop.net

📂 #FileSharing #SnapDrop #TechTools
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Free Software: Malwarebytes Antivirus

🎨 Protect your system from malware, ransomware, and viruses — free version available.

📂 #Antivirus #FreeSoftware #Malwarebytes
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Tip: Use a Password Manager

🎨 Stay secure online by using unique strong passwords and managing them with a vault.

📂 #CyberSecurity #PasswordTip #OnlineSafety
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 Android Tip: Enable Dark Mode

🎨 Save battery and reduce eye strain by enabling dark mode on your device.

📂 #AndroidTips #DarkMode #BatterySaver
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 PC Tool: Everything Search

🎨 Instantly search all files and folders on your PC — faster than Windows Search.

🌐 Try: https://voidtools.com

📂 #PCTools #FileSearch #EverythingApp
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto""",

    """🤖 AI Tool: ClipDrop Relight

🎨 Turn normal pics into pro lighting studio shots in 1 click!

🌐 Try: https://clipdrop.co/relight

📂 #AIPhoto #ClipDrop #ViralTool
📣 Tech 👉 @Tech_Pulse_Apps_AI_Hacks
🔗 Proxies 👉 @Tech_Pulse_Proxy_MTProto"""
]

def get_post_keyboard():
    return InlineKeyboardMarkup()

async def send_hourly_post():
    post_count = 0
    while post_count < 16:
        try:
            # Get the current time in PST
            current_hour = datetime.now(pst).hour
            print(f"Current Hour: {current_hour} (PST)")  # Debugging line to check the hour
            
            # Post between 6 AM and 10 PM PST
            if 6 <= current_hour <= 22:
                post_index = current_hour - 6  # Map the hour to the correct post
                if 0 <= post_index < len(POSTS):
                    await bot.send_message(CHANNEL_ID, POSTS[post_index], reply_markup=get_post_keyboard())
                    print(f"✅ Posted at hour {current_hour} (PST)")
                    post_count += 1
                else:
                    print("❌ Post index out of range.")
            else:
                print(f"⏳ Waiting... Current hour {current_hour} (PST) not in range.")
        except Exception as e:
            print(f"❌ Error: {e}")
        await asyncio.sleep(3600)  # Wait for 1 hour before checking again

@dp.message_handler()
async def handle_command(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.reply("❌ You are not authorized to control this bot.")
        return

    if message.text.startswith("/updateposts"):
        new_text = message.text.replace("/updateposts", "").strip()
        # Split posts using '###' delimiter
        new_posts = new_text.split('###')  
        if len(new_posts) != 16:
            await message.reply(f"⚠️ Please send exactly 16 posts (you sent {len(new_posts)}).")
        else:
            global POSTS
            POSTS = new_posts
            await message.reply("✅ Posts updated successfully.")

    elif message.text.startswith("/testpost"):
        try:
            await bot.send_message(CHANNEL_ID, "🧪 Test Post\n\nThis is a test message.")
            await message.reply("✅ Test post sent.")
        except Exception as e:
            await message.reply(f"❌ Failed to send test post: {e}")

    elif message.text.startswith("/post"):
        try:
            num = int(message.text.replace("/post", "").strip())
            if 1 <= num <= 16:
                await bot.send_message(CHANNEL_ID, POSTS[num - 1], reply_markup=get_post_keyboard())
                await message.reply(f"✅ Post {num} sent.")
            else:
                await message.reply("⚠️ Use /post 1 to /post 16 only.")
        except:
            await message.reply("⚠️ Invalid command. Use /post 1 to /post 16.")
    else:
        await message.reply("🤖 Commands:\n/updateposts <16 posts>\n/post 1-16\n/testpost")

async def main():
    await asyncio.gather(
        dp.start_polling(),
        send_hourly_post()
    )

if __name__ == "__main__":
    asyncio.run(main())
