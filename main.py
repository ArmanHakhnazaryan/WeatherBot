import telebot

from api_utils import get_city_weather
from constants import BOT_TOKEN, WEATHER_SYMBOLS


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi, please write name of the city.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    data = get_city_weather(city)

    if data:
        temp = data.get("main", {}).get("temp")
        icons = [item.get("icon") for item in data.get("weather")]
        bot.reply_to(
            message,
            f'The weather in {city.capitalize()} is now {temp} degrees Celsius '
            f'{",".join([WEATHER_SYMBOLS[icon] for icon in icons])}'
        )
    else:
        bot.reply_to(message, 'Name of city is not correct')


bot.polling(none_stop=True)
