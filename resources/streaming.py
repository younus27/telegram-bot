from telegram import *
from telegram.ext import *

import constraints

bot = Bot(constraints.API_KEY)

def streaming_info(update, context):
	bot.send_message(
		chat_id = update.effective_chat.id, 
		text="""
			Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.\n
			Data can be ingested from many sources like Kafka, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.\n
			Finally, processed data can be pushed out to filesystems, databases, and live dashboards.
			<a href="https://spark.apache.org/docs/latest/img/streaming-arch.png">&#8205;</a>
			""",
		parse_mode=ParseMode.HTML)

	update.message.reply_text("""
		The following commands are available:\n

		Set up a python file for Streaming
		/streaming_setup\n

		Word Count Program 
		/streaming_wordcount\n

		Essential code to Start Streaming
		/streaming_start\n

		Execute python file
		/streaming_executefile\n

		Provide Stream input
		/streaming_input\n

		Spark streaming document:
		https://spark.apache.org/docs/latest/streaming-programming-guide.html
		""")

def streaming_setup(update, context):
	update.message.reply_text("""
		For spark streaming we are using python file to write the commands and execute the file using spark-submit\n
		
		Initialize SparkContext:
		from pyspark import SparkContext
		from pyspark.streaming import StreamingContext\n

		#Create a local StreamingContext with two working thread and batch interval of 1 second
		sc = SparkContext("local[2]", "NetworkWordCount")
		ssc = StreamingContext(sc, 1) 
		""")

def streaming_wordcount(update, context):
	update.message.reply_text("""
		# Create a DStream that will connect to hostname:port, like localhost:9999
		lines = ssc.socketTextStream("localhost", 9999)\n

		# Split each line into words
		words = lines.flatMap(lambda line: line.split(" "))\n

		# Count each word in each batch
		pairs = words.map(lambda word: (word, 1))
		wordCounts = pairs.reduceByKey(lambda x, y: x + y)\n

		# Print the first ten elements of each RDD generated in this DStream to the console
		wordCounts.pprint()\n
		""")

def streaming_start(update, context):
	update.message.reply_text("""
		When a code is written, Spark Streaming only sets up the computation it will perform when it is started, and no real processing has started yet.\n
		To start the processing after all the transformations have been setup, we finally call\n

		# Start the computation
		ssc.start()\n

		# Wait for the computation to terminate
		ssc.awaitTermination()
		""")

def streaming_executefile(update, context):
	update.message.reply_text("""
		To execute a Python File:
		spark-submit folder/wordcount.py localhost 9999
		""")

def streaming_input(update, context):
	update.message.reply_text("""
		Run Netcat on local host to provide stream input
		$ nc -lk 9999
		""")

	



