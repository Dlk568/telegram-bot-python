from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Reemplaza este token por el tuyo
TOKEN = "8025298642:AAFBcj1aMXJI6Rw6lmgZ40tfX3lFx2g86bw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to Psique Oculta!\n"
        "🎉 We're excited to have you join our community. This is a space to explore, share, and learn about the mysteries of the mind, the subconscious, and everything related to the world of the occult. 🌙✨\n\n"
        "👁️‍🗨️ As a thank you for joining, we're giving you an exclusive e-book completely free. 🎁\n"
        "Click the link below to download your gift and begin your journey into the unknown.\n\n"
        "🔮 May your journey be enriching and full of discoveries! If you have any questions or want to share something interesting, feel free to interact. We’d love to hear your thoughts! "
    )

def main():
    # Crea una aplicación y pasa el token
    application = Application.builder().token(TOKEN).build()

    # Añade el manejador para el comando /start
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Comienza a escuchar por mensajes
    application.run_polling()

if __name__ == "__main__":
    main()
