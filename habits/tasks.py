import logging

from celery import shared_task
from config.celery import app
from habits.models import Habit
import logging

from habits.services.telegram import telegram_bot_message, telebot_send


@shared_task(bind=True)
def task_send_tg(self, habit_id):

    try:

        habit = Habit.objects.get(pk=habit_id)

        logging.info(habit.user.telegram_uid)
        print('>>>habit.user.telegram_uid', habit.user.telegram_uid)
        logging.info(habit.operation)

        telebot_send(message=habit.operation, chat_id=habit.user.telegram_uid)
        logging.info(telebot_send.__dict__)

    except Exception as e:
        print(str(e), type(e))
