def deltalake_info(update, context):
	update.message.reply_text("""
		Delta Lake is an open format storage layer that delivers reliability, security and performance on your data lake — for both streaming and batch operations.\n
		It runs on top of your existing data lake and is fully compatible with Apache Spark's API\n

		# Delta table Features
		/deltalake_features\n

		# Delta Table Operation:
		/deltatable_operations\n
		""")

def deltalake_features(update, context):
	update.message.reply_text(""" 
		# Deltalake Features are:\n
		1. ACID Transactions on Spark
		2. Scalable metadata handling
		3. Unified Batch and Stream Source
		4. Schema Enforcement
		5. Time Travel
		6. Audit History
		7. Full DML support
		""")


def deltatable_operations(update, context):
	update.message.reply_text("""
		# Start pyspark with delta core package
		pyspark  --packages io.delta:delta-core_2.11:0.4.0\n

		# Save DataFrame as Delta table
		df.write.format('delta')\
			.mode('overwrite')\
			.save('file:///home/folder\n

		# Read Delta table as DataFrame
		deltadf = spark.read\
			.format('delta')\
			.load('file:///home/ak/folder')\n     

		# Read Delta Table as DeltaTable
		deltaTable = DeltaTable.forPath(spark, "file:///home/ak/folder")\n

		# Delete Operation:
		deltaTable.delete('<column_name>==<value>')\n
		deltaTable.toDF().show()\n

		# Update Operation:\n
		deltaTable.update(col('<column_name>')=='<value>',{'<column_name2>':lit('new_value<>')})\n
		deltaTable.toDF().show()
		""")



