from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

OWNER_ID = 7236575607
REPLY_TEXT = "تم إرسال رسالتك السرية بنجاح 📩"

async def forward_secret(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.text:
        await context.bot.send_message(chat_id=OWNER_ID, text=f"رسالة سرية:\n\n{msg.text}")
    elif msg.photo:
        await context.bot.send_photo(chat_id=OWNER_ID, photo=msg.photo[-1].file_id, caption="صورة سرية")
    elif msg.video:
        await context.bot.send_video(chat_id=OWNER_ID, video=msg.video.file_id, caption="فيديو سري")
    elif msg.voice:
        await context.bot.send_voice(chat_id=OWNER_ID, voice=msg.voice.file_id, caption="ملاحظة صوتية سرية")
    elif msg.audio:
        await context.bot.send_audio(chat_id=OWNER_ID, audio=msg.audio.file_id, caption="رسالة صوتية سرية")
    elif msg.document:
        await context.bot.send_document(chat_id=OWNER_ID, document=msg.document.file_id, caption="ملف سري")
    elif msg.sticker:
        await context.bot.send_sticker(chat_id=OWNER_ID, sticker=msg.sticker.file_id)

    await msg.reply_text(REPLY_TEXT)

if __name__ == "__main__":
    import os
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_secret))
    print("البوت يعمل الآن...")
    app.run_polling()
