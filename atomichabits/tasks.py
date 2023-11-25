import os
from celery import shared_task

import telebot
from datetime import date

from atomichabits.models import Habit


@shared_task
def remind_me_habit():
    """Направляем пользователю уведомление в Telegram"""

    TG_API_TOKEN = os.getenv("TG_API_TOKEN")
    bot = telebot.TeleBot(TG_API_TOKEN, parse_mode=None)
    today = date.today()
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time is None:
            continue
        if habit.time.date() == today:
            bot.send_message(
                chat_id=habit.user.chat_id,
                text=f"Пришло время привычки {habit.action}, "
                f"Привычку необходимо выполнить в {habit.time} в {habit.place}",
            )
