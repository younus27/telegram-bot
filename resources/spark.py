from telegram import *
from telegram.ext import *

import constraints

bot = Bot(constraints.API_KEY)

def spark_info(update, context):
	bot.send_message(
		chat_id = update.effective_chat.id, 
		text="""
			Apache Spark is a lightning fast unified analytics engine for large scale data processing.
			<a href="https://spark.apache.org/images/spark-logo-trademark.png">&#8205;</a>
			
			Spark 2.4 Documentation
			https://spark.apache.org/docs/2.4.0/
			""",
		parse_mode=ParseMode.HTML)

	update.message.reply_text("""
		Spark Features:
		/spark_features\n

		Commands:
		/commands\n
		""")

def spark_features(update, context):

	bot.send_message(
	chat_id = update.effective_chat.id, 
	text="""
			# Spark Features:\n
			1. Fault Tolerance
			2. Reusability
			3. Dynamic in Nature
			4. Speed
			5. Lazy Evaluation
			6. In Memory Computation
			7. Advance Analytics
			8. Realtime Processing
	
			<a href="https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/05/features-of-spark.jpg">&#8205;</a>\n
			""",
	parse_mode=ParseMode.HTML)


