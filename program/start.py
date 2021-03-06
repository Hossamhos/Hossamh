from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    ASSISTANT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **مرحبا عزيزي ↤ {message.from_user.mention()} !**\n
🤖 **[H𝗢𝗦𝗦𝗔𝗠 𝑀𝑈𝑆𝐼𝐶࿃
 🎶](https://t.me/x3j_xj3) **
**⌯ انا بوت  استطيع تشغيل الموسيقي والفيديو في محادثتك الصوتية**

⌯ تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  » 📚 اوامر التشغيل !

⌯ لتعلم طريقة تشغيلي بمجموعتك اضغط علي » ❓طريقة التفعيل !

⌯لعرض قائمه الاوامر في مجموعتك اكتب » »  اغاني او اوامر اغاني او الاوامر .
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                  "⌯ H𝗢𝗦𝗦𝗔𝗠 𝑀𝑈𝑆𝐼𝐶࿃ 🎶 ⌯",
                        url=f"https://t.me/x3j_xj3"),
                ],
                [
                    InlineKeyboardButton("⌯ H𝗢𝗦𝗦𝗔𝗠⌯", url=f"https://t.me/H_OS_S_AM"),
                ],
                [InlineKeyboardButton("⌯❓ طريقة التفعيل ⌯", callback_data="cbhowtouse")],
                [InlineKeyboardButton("⌯  الاوامر بالعربي ⌯", callback_data="cbvamp")],                 
                [
                    InlineKeyboardButton("⌯ 📚 اوامر التشغيل ⌯ ", callback_data="cbcmds"),
                    InlineKeyboardButton("⌯ الــمــطــور ⌯", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "⌯ جروب البوت ⌯", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "⌯ قناة البوت ⌯", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton("⌯ اضافه البوت اللي مجموعتك ⌯", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["برمج السورس" ,"ؤمن" ,"ورس", "alive", "لسورس", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("• H𝗢𝗦𝗦𝗔𝗠•", url=f"https://t.me/H_OS_S_AM"),
              
            ],
             
                [       
                    InlineKeyboardButton(
                      "⌯ H𝗢𝗦𝗦𝗔𝗠 𝑀𝑈𝑆𝐼𝐶࿃ 🎶 ⌯", url=f"https://t.me/x3j_xj3"
                    ),
                ],
                [
                    InlineKeyboardButton("⌯ اضافه البوت اللي مجموعتك ⌯", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
    ) 

    alive = f"**⌯ اهلا بك يا  {message.from_user.mention()}   \n ⌯في سورس حسام ميوزك 🎵 الجمدان ❤️ \n ⌯ لو عايز تنصيب بوت ميوزك بأسعار حلوة  كلمنا  من هنا ⬇️ ** "

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["لمطور", "طور"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5db1e9940a55de6c46625.jpg",
      caption=f"""⌯ مطور سورس حسام ميوزك 🎵""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓆩 آݪــمــطور حسام 𓆪", url=f"https://t.me/H_OS_S_AM"),
            ],
            
            [
                InlineKeyboardButton("⌯ اضافه البوت اللي مجموعتك ⌯", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(command(["وامراغاني", f"وامر", f"لاوامراغاني", f"لاوامر", f"اغاني", f"غاني"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/51b6e6a9cdc94f2d392eb.jpg",
        caption=f"""**⌯ ها هي الاوامر  الكامله بالعربي ⌯ \n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n⌯ تشغيل + 「اسم الأغنية او / رابط」تشغيل الصوت  mp3\n\n⌯ فديو +  「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة  .\n\n⌯ فيديو + لينك + | جودة < 360 - 480- 720 >| » » تشغيل فيديو مباشر من يوتيوب .\n\n⌯ ايقاف او انهاء » »  لايقاف التشغيل .\n\n⌯ وقف » » ايقاف التشغيل موقتآ  .\n\n⌯ مواصله  » »  استئناف التشغيل  .\n\n⌯ تقدم » » تخطي الئ التالي  .\n\n⌯  كتم او سكوت  » »   لكتم البوت .\n\n⌯ الغاء الكتم » »  لرفع كتم البوت  .\n\n⌯ تحكم » » تظهر لك قائمة التشغيل .\n\n⌯ تنزيل + اسم فيديو » » لتحميل فيديوهات من يوتيوب .\n\n⌯ تحميل  + اسم اغنية  » لتحميل اغاني mP3 من يوتيوب .\n\n⌯ لمعرفة المزيد من الاوامر ادخل علي البوت .\n\n✦┅━╍━╍╍━━╍━━╍━┅✦**""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓆩 آݪــمــطور حسام 𓆪", url=f"https://t.me/H_OS_S_AM"),
               
            ],
   
            [
                InlineKeyboardButton(
                  "⌯ H𝗢𝗦𝗦𝗔𝗠 𝑀𝑈𝑆𝐼𝐶࿃ 🎶 ⌯", url=f"https://t.me/x3j_xj3"
                ),
            ],
            [
                InlineKeyboardButton("⌯ اضافه البوت اللي مجموعتك ⌯", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["ping", "ينج", "يست", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime","لوقت", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )




