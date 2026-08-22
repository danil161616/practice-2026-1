import telebot
import os
import time

# Инициализация бота (токен нужно получить у @BotFather)
TOKEN = os.environ.get('TELEGRAM_TOKEN', 'YOUR_BOT_TOKEN_HERE')
bot = telebot.TeleBot(TOKEN)

# Данные состояния робота (заглушка)
robot_state = {
    "status": "online",
    "battery": 85,
    "speed": 0
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Обработчик команд /start и /help"""
    welcome_text = (
        "🤖 Привет! Я бот проекта «Робокрафт».\n"
        "С моей помощью ты можешь узнать статус робота или получить документацию.\n\n"
        "Доступные команды:\n"
        "/status - Узнать текущее состояние робота\n"
        "/docs - Ссылка на документацию\n"
        "/ping - Проверка связи с роботом"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['status'])
def check_status(message):
    """Отправляет текущий статус робота"""
    status_msg = (
        f"📊 **Статус Робокрафт**\n"
        f"🔋 Заряд батареи: {robot_state['battery']}%\n"
        f"⚙️ Состояние: {robot_state['status']}\n"
        f"🚀 Текущая скорость: {robot_state['speed']} км/ч"
    )
    bot.send_message(message.chat.id, status_msg, parse_mode="Markdown")

@bot.message_handler(commands=['docs'])
def send_docs(message):
    """Отправляет ссылку на материалы"""
    bot.reply_to(message, "Документацию по проекту можно найти в нашем [GitHub репозитории](https://github.com/mospol/practice-2025-1).", parse_mode="Markdown")

@bot.message_handler(commands=['ping'])
def ping_robot(message):
    """Модификация: проверка пинга до робота"""
    start_time = time.time()
    msg = bot.send_message(message.chat.id, "Отправка запроса роботу...")
    # Имитация задержки сети
    time.sleep(0.5)
    ping_time = round((time.time() - start_time) * 1000)
    bot.edit_message_text(f"✅ Ответ получен!\nЗадержка: {ping_time} мс", chat_id=message.chat.id, message_id=msg.message_id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Эхо-ответ на неизвестные сообщения"""
    bot.reply_to(message, "Я не понимаю эту команду. Введи /help для списка команд.")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
