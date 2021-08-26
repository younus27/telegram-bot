from datetime import datetime
import random

def responses(input_text):
	user_message =  str(input_text).lower()

	if user_message in {"hello","hi","hey","what's up"}:
		return "Hi"

	if user_message in {"who are you","who are you?","what are you?"}:
		return "I am a myj_spark_bot"

	if user_message in {"time","time?"}:
		now = datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")
		return str(date_time)

	return "Sorry I didn't understand"
