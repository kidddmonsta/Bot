#! /usr/bin/env python
# -*- coding: utf-8 -*-#
import telebot;
bot = telebot.TeleBot('%993816933:AAGd2-4dHklhJTagU2hBMNzIPXoOvxZPo5s%');

#
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

#
#@bot.message_handler(content_types=['text', 'document', 'audio'])

#
#
if message.text == "Hi":
    bot.send_message(message.from_user.id, "Hi, can I help you?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Type Hi")
else:
    bot.send_message(message.from_user.id, "I do't undersnand, type /help.")

#
bot.polling(none_stop=True, interval=0)
