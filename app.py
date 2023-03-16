import telebot
from config import keys, TOKEN
from extensions import ConvertionException, ConverterCurrency

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', ])
def send_welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.chat.username}')
    bot.send_message(message.from_user.id, 'Чтобы подробно узнать о функционале данного бота, необходимо '
                                           'воспользоваться /help')
    pass


@bot.message_handler(commands=['help', ])
def send_help(message: telebot.types.Message):
    bot.send_message(message.from_user.id, "Для того, чтобы получить сведения о валюте, необходимо вводить: \
<валюта><в какую валюту переводим><количество>, чтобы увидеть доступную валюту, введите: /values")

@bot.message_handler(commands=['values', ])
def send_values(message: telebot.types.Message):
    text = 'Доступная валюта:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)
pass


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        quote, base, amount = values
        total_base = ConverterCurrency.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Стоимость {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
