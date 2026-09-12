from pyrogram import filters
from anony import app, db


@app.on_message(filters.command("autoplay"))
async def autoplay_cmd(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "**Usage:**\n/autoplay on\n/autoplay off"
        )

    mode = message.command[1].lower()

    if mode == "on":
        await db.set_autoplay(message.chat.id, True)
        await message.reply_text("✅ AutoPlay Enabled")

    elif mode == "off":
        await db.set_autoplay(message.chat.id, False)
        await message.reply_text("❌ AutoPlay Disabled")

    else:
        await message.reply_text("⚠️ Use only: /autoplay on or /autoplay off")
