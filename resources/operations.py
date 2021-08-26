def operations_info(update, context):
	update.message.reply_text("""
		Spark Operations:\n

		File Formats and Compression Codecs
		/compression_codec\n

		Partition & Bucketing
		/partition_bucketting\n
		""")

def compression_codec(update, context):
	update.message.reply_text("""

	Save File in diffrent formats (parquet, orc, json)
	with diffrent compression techniques (gzip, bzip, snappy)\n

	# GZIP
	df.write.format("parquet").option("compression","gzip").save("file:///home/folder1")\n
	df.write.format("orc").option("compression","gzip").save("file:///home/folder2")\n
	df.write.format("json").option("compression","gzip").save("file:///home/folder3")\n\n

	# BZIP
	df.write.option("codec","bzip2").parquet("file:///home/folder4")\n
	df.write.option("compression","bzip2").orc("file:///home/folder5")\n
	df.write.option("compression","bzip2").json("file:///home/folder6")\n\n

	# SNAPPY
	df.write.format("parquet").option("compression","snappy").save("file:///home/folder7")\n
	df.write.format("orc").option("compression","snappy").save("file:///home/folder8")
		""")

def partition_bucketting(update, context):
	update.message.reply_text("""
		Partition is used to partition data based on keys (column names).
		Partiton workes of folder level - It removes the columns from daatset and forms a directory.
		Number of partitions are based on the cardinality of key columns.\n

		Bucketing is used to further divide the data in partitons.
		Bucketting is also used when the cardinality of key columns is very high and partitioning results in high number of partitons.
		We can provide the required number of buckets.\n

		df2 = df.write\
		.partitionBy('<partitionby_key>')\
		.bucketBy(5,'bucketby_key')\
		.mode('overwrite')\
		.options(path='file:///home/folder_name')
		.saveAsTable('<table_name>')
		""")
