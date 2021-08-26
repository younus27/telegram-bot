from telegram import *
from telegram.ext import *

# import constraints
import responses

from resources import spark
from resources import constraints
from resources import datasources
from resources import operations
from resources import deltalake
from resources import kafka
from resources import streaming
from resources import structured_streaming


bot = Bot(constraints.API_KEY)

def start_command(update, context):
	update.message.reply_text("""
		Hello! Welcome to myj_spark\n
		This is a quick Spark guide\n

		View Commands:
		/commands\n

		Author:
		/personal_info
		""")

def personal_info(update, context):
	update.message.reply_text("""
		This Bot was created By:\n
		Mohammad Younus Jameel -\n
		github: https://github.com/younus27
		""")


def help_command(update, context):
	update.message.reply_text("""
		Start:
		/start\n

		View Commands:
		/commands\n

		Author:
		/personal_info
		""")


def commands(update, context):
	update.message.reply_text("""
		The following commands are available:

		/start - Welcome Message
		/dataset - Retail dataset

		/spark - Spark info

		1. Data Sources
			/datasources\n

		2. Spark Operations
			/operations\n

		3. Delta Lake
			/deltalake\n

		4. Spark Streaming
			/kafka
			/streaming
			/structured_streaming
		""")

# User message
def handle_message(update, context):
	text = str(update.message.text.lower())
	response = responses.responses(text)
	update.message.reply_text(response)


def dataset(update,context):
	update.message.reply_text("""
		Retail Dataset 
		https://drive.google.com/drive/folders/1_lAoOQu1tQRK-Eo1p5j660nFuSwhwho5?usp=sharing
		""" )


# def options(update,context):
#     keyboard = [
#         [
#             InlineKeyboardButton("Option 1", callback_data='1'),
#             InlineKeyboardButton("Option 2", callback_data='2'),
#             InlineKeyboardButton("Option 3", callback_data='3'),
#         ],
#         [InlineKeyboardButton("Option 4", callback_data='4')],
#     ]

#     reply_markup = InlineKeyboardMarkup(keyboard)

#     update.message.reply_text('Please choose:', reply_markup=reply_markup)

# def button(update, context):
#     query = update.callback_query
#     query.answer()
#     query.edit_message_text(text=f"Selected option: {query.data}")

def error(update,context):
	print(f"Update {update} cause error {context.error}")




def main():
	
	updater = Updater(constraints.API_KEY, use_context = True)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler("start", start_command))
	dispatcher.add_handler(CommandHandler("help", help_command))
	dispatcher.add_handler(CommandHandler("commands", commands))
	dispatcher.add_handler(CommandHandler("personal_info", personal_info))
	

	dispatcher.add_handler(CommandHandler("dataset",dataset))

	dispatcher.add_handler(CommandHandler("spark",spark.spark_info))
	dispatcher.add_handler(CommandHandler("spark_info",spark.spark_info))
	dispatcher.add_handler(CommandHandler("spark_features",spark.spark_features))

	dispatcher.add_handler(CommandHandler("datasources", datasources.datasources_info))
	dispatcher.add_handler(CommandHandler("datasources_info", datasources.datasources_info))
	dispatcher.add_handler(CommandHandler("pyspark_local", datasources.pyspark_local))
	dispatcher.add_handler(CommandHandler("pyspark_hdfs", datasources.pyspark_hdfs))
	dispatcher.add_handler(CommandHandler("pyspark_mysql", datasources.pyspark_mysql))
	dispatcher.add_handler(CommandHandler("pyspark_s3", datasources.pyspark_s3))


	dispatcher.add_handler(CommandHandler("operations", operations.operations_info))
	dispatcher.add_handler(CommandHandler("operations_info", operations.operations_info))
	dispatcher.add_handler(CommandHandler("compression_codec", operations.compression_codec))
	dispatcher.add_handler(CommandHandler("partition_bucketting", operations.partition_bucketting))

	dispatcher.add_handler(CommandHandler("deltalake", deltalake.deltalake_info))
	dispatcher.add_handler(CommandHandler("deltalake_info", deltalake.deltalake_info))
	dispatcher.add_handler(CommandHandler("deltalake_features", deltalake.deltalake_features))
	dispatcher.add_handler(CommandHandler("deltatable_operations", deltalake.deltatable_operations))


	dispatcher.add_handler(CommandHandler("kafka", kafka.kafka_info))
	dispatcher.add_handler(CommandHandler("kafka_info", kafka.kafka_info))
	dispatcher.add_handler(CommandHandler("kafka_download", kafka.kafka_download))
	dispatcher.add_handler(CommandHandler("kafka_getting_started", kafka.kafka_getting_started))
	dispatcher.add_handler(CommandHandler("kafka_env", kafka.kafka_env))
	dispatcher.add_handler(CommandHandler("kafka_topic", kafka.kafka_topic))
	dispatcher.add_handler(CommandHandler("kafka_producer", kafka.kafka_producer))
	dispatcher.add_handler(CommandHandler("kafka_consumer", kafka.kafka_consumer))
	dispatcher.add_handler(CommandHandler("kafka_terminate", kafka.kafka_terminate))


	dispatcher.add_handler(CommandHandler("streaming", streaming.streaming_info))
	dispatcher.add_handler(CommandHandler("streaming_info", streaming.streaming_info))
	dispatcher.add_handler(CommandHandler("streaming_setup", streaming.streaming_setup))
	dispatcher.add_handler(CommandHandler("streaming_wordcount", streaming.streaming_wordcount))
	dispatcher.add_handler(CommandHandler("streaming_start", streaming.streaming_start))
	dispatcher.add_handler(CommandHandler("streaming_executefile", streaming.streaming_executefile))
	dispatcher.add_handler(CommandHandler("streaming_input", streaming.streaming_input))



	dispatcher.add_handler(CommandHandler("structured_streaming", structured_streaming.structured_streaming_info))
	dispatcher.add_handler(CommandHandler("structured_streaming_info", structured_streaming.structured_streaming_info))
	dispatcher.add_handler(CommandHandler("structured_streaming_setup", structured_streaming.structured_streaming_setup))
	dispatcher.add_handler(CommandHandler("structured_streaming_wordcount", structured_streaming.structured_streaming_wordcount))
	dispatcher.add_handler(CommandHandler("structured_streaming_start", structured_streaming.structured_streaming_start))
	dispatcher.add_handler(CommandHandler("structured_streaming_executefile", structured_streaming.structured_streaming_executefile))
	dispatcher.add_handler(CommandHandler("structured_streaming_input", structured_streaming.structured_streaming_input))
	dispatcher.add_handler(CommandHandler("structured_streaming_window", structured_streaming.structured_streaming_window))
	dispatcher.add_handler(CommandHandler("structured_streaming_watermark", structured_streaming.structured_streaming_watermark))

	# dispatcher.add_handler(CommandHandler("options",options))
	# dispatcher.add_handler(CallbackQueryHandler(button))

	
	dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
	dispatcher.add_error_handler(error)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()

