from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADkwMAAoQw2Ff0pyzi760bgwI")
    await message.reply_text(
        f"""**- 𝙃𝙚𝙮 𝘼𝙢 𝘼𝙆 𝙓𝘿 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏 💛🐬,

- 𝙄 𝙘𝙖𝙣 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥'𝙨 𝙫𝙤𝙞𝙘𝙚 𝙘𝙖𝙡𝙡. 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮 [𝘼𝙠](https://t.me/AK_XD_MUSIC) 💛🤞.

𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥 𝙖𝙣𝙙 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙛𝙧𝙚𝙚𝙡𝙮 🐬💕**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         " 𝙊𝙬𝙣𝙚𝙧 ", url="https://t.me/Kingofkohnoor")
                  ],[
                    InlineKeyboardButton(
                        "😈  𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/A_4_AMAN_0fficial"
                    ),
                    InlineKeyboardButton(
                        "✌️ 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/+A6SAM9IsE1tmODVl"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝘼𝙙𝙙 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕", url="https://t.me/AK_XD_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** 𝘼𝙡𝙤𝙣𝙚 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧 𝙄𝙨 𝙊𝙣𝙡𝙞𝙣𝙚 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝙈𝙖𝙣𝙖𝙜𝙚𝙧", url="https://t.me/A_4_AMAN_0fficial")
                ]
            ]
        )
   )


