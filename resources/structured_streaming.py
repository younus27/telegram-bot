from telegram import *
from telegram.ext import *

import constraints

bot = Bot(constraints.API_KEY)

def structured_streaming_info(update, context):
	bot.send_message(
		chat_id = update.effective_chat.id, 
		text="""
		Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.\n

		The key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended.
		This leads to a new stream processing model that is very similar to a batch processing model.
		You will express your streaming computation as standard batch-like query as on a static table, and Spark runs it as an incremental query on the unbounded input table.\n

			<a href="https://spark.apache.org/docs/latest/img/structured-streaming-stream-as-a-table.png">&#8205;</a>
			""",
		parse_mode=ParseMode.HTML)

	update.message.reply_text("""
		The following commands are available:\n

		Set up a python file for Streaming
		/structured_streaming_setup\n

		Word Count Program 
		/structured_streaming_wordcount\n

		Essential code to Start Streaming
		/structured_streaming_start\n

		Execute python file
		/structured_streaming_executefile\n

		Provide Stream input
		/structured_streaming_input

		Window
		/structured_streaming_window

		Watermarking
		/structured_streaming_watermark
		""")

def structured_streaming_setup(update, context):
	update.message.reply_text("""
		For spark streaming we are using python file to write the commands and execute the file using spark-submit\n

		from pyspark.sql import SparkSession
		from pyspark.sql.functions import explode
		from pyspark.sql.functions import split

		spark = SparkSession \
		    .builder \
		    .appName("StructuredNetworkWordCount") \
		    .getOrCreate()
		""")

def structured_streaming_wordcount(update, context):
	update.message.reply_text("""
		lines = spark \
			.readStream \
			.format("socket") \
			.option("host", "localhost") \
			.option("port", 9999) \
			.load()

		# Split the lines into words
		words = lines.select(
			explode(
				split(lines.value, " ")
			).alias("word")
		)

		# Generate running word count
		wordCounts = words.groupBy("word").count()
		""")

def structured_streaming_start(update, context):
	update.message.reply_text("""

		# Start running the query that prints the running counts to the console
		query = wordCounts \
			.writeStream \
			.outputMode("complete") \
			.format("console") \
			.start()

		query.awaitTermination()
		""")

def structured_streaming_executefile(update, context):
	update.message.reply_text("""
		To execute a Python File:
		spark-submit folder/wordcount.py localhost 9999
		""")

def structured_streaming_input(update, context):
	update.message.reply_text("""
		Run Netcat on local host to provide stream input
		$ nc -lk 9999
		""")


def structured_streaming_output_modes(update, context):
	update.message.reply_text("""
		\nComplete Mode:
		The entire updated Result Table will be written to the external storage. It is up to the storage connector to decide how to handle writing of the entire table.\n

		Append Mode:
		Only the new rows appended in the Result Table since the last trigger will be written to the external storage. This is applicable only on the queries where existing rows in the Result Table are not expected to change.\n

		Update Mode:
		Only the rows that were updated in the Result Table since the last trigger will be written to the external storage (available since Spark 2.1.1). Note that this is different from the Complete Mode in that this mode only outputs the rows that have changed since the last trigger. If the query doesn’t contain aggregations, it will be equivalent to Append mode.
		""")



def structured_streaming_window(update, context):
	bot.send_message(
		chat_id = update.effective_chat.id, 
		text="""

			Aggregations over a sliding event-time window are straightforward with Structured Streaming and are very similar to grouped aggregations. 
			In a grouped aggregation, aggregate values (e.g. counts) are maintained for each unique value in the user-specified grouping column.
			In case of window-based aggregations, aggregate values are maintained for each window the event-time of a row falls into. Let’s understand this with an illustration.\n

			Imagine our quick example is modified and the stream now contains lines along with the time when the line was generated. 
			Instead of running word counts, we want to count words within 10 minute windows, updating every 5 minutes. 
			That is, word counts in words received between 10 minute windows 12:00 - 12:10, 12:05 - 12:15, 12:10 - 12:20, etc. Note that 12:00 - 12:10 means data that arrived after 12:00 but before 12:10.
			Now, consider a word that was received at 12:07.
			This word should increment the counts corresponding to two windows 12:00 - 12:10 and 12:05 - 12:15. 
			So the counts will be indexed by both, the grouping key (i.e. the word) and the window (can be calculated from the event-time).\n

			<a href="https://spark.apache.org/docs/latest/img/structured-streaming-window.png">&#8205;</a>
			""",
		parse_mode=ParseMode.HTML)

	update.message.reply_text("""
		words = ...  # streaming DataFrame of schema { timestamp: Timestamp, word: String }\n

		# Group the data by window and word and compute the count of each group
		windowedCounts = words.groupBy(
			window(words.timestamp, "10 minutes", "5 minutes"),
			words.word
		).count()
		""")


def structured_streaming_watermark(update, context):
	bot.send_message(
		chat_id = update.effective_chat.id, 
		text="""
			Watermarking is used to handle the events that arrive late to the application.\n
			For example, say, a word generated at 12:04 (i.e. event time) could be received by the application at 12:11.
			The application should use the time 12:04 instead of 12:11 to update the older counts for the window 12:00 - 12:10.
			This occurs naturally in our window-based grouping – Structured Streaming can maintain the intermediate state for partial aggregates for a long period of time such that late data can update aggregates of old windows correctly
			Watermarking lets the engine automatically track the current event time in the data and attempt to clean up old state accordingly.
			<a href="https://spark.apache.org/docs/latest/img/structured-streaming-late-data.png">&#8205;</a>
			<a href="https://spark.apache.org/docs/latest/img/structured-streaming-watermark-update-mode.png">&#8205;</a>
			<a href="https://spark.apache.org/docs/latest/img/structured-streaming-watermark-append-mode.png">&#8205;</a>

			""",
		parse_mode=ParseMode.HTML)

	update.message.reply_text("""
		words = ...  # streaming DataFrame of schema { timestamp: Timestamp, word: String }\n

		# Group the data by window and word and compute the count of each group
		windowedCounts = words \
			.withWatermark("timestamp", "10 minutes") \
			.groupBy(
				window(words.timestamp, "10 minutes", "5 minutes"),
				words.word) \
			.count()
		""")
	



