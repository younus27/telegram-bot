def datasources_info(update, context):
	update.message.reply_text("""
		Different Data Sources available Spark:\n

		Local File System
		/pyspark_local\n

		HDFS
		/pyspark_hdfs\n

		MySQL
		/pyspark_mysql\n

		AWS S3
		/pyspark_s3
		""")
def pyspark_local(update, context):
	update.message.reply_text("""
		# Read file from local\n

		from pyspark.sql.types import StructType,StructField, StringType,IntegerType,DoubleType,DateType\n

		EmpSchema = StructType([  \
			StructField('empid', IntegerType(), True), \
			StructField('name'  , StringType(), True), \
			StructField('salary', DoubleType(), True), \
		])\n

		df=spark.read.option("header","true")\
			.schema(<Schema_Name>)\
			.csv('file:///home/path/file_name.csv',sep=',')
		df.show()
		""")


def pyspark_hdfs(update, context):
	update.message.reply_text("""
		Move File from local to hdfs directory
		hdfs dfs -put <source> <destination>\n

		Read from HDFS\n

		df=spark.read.option('inferschema','true')\
			.csv('hdfs:///database_name/file_name.csv',sep='\t')
		""")


def pyspark_mysql(update, context):
	update.message.reply_text("""
		# Connect to mysql
		sudo mysql -u root -p 
		create database <database_name>;
		use <database_name>;\n

		# Create a Table in mysql
		CREATE TABLE emp (
		empid    INT PRIMARY KEY,
		name  	 VARCHAR(200),
		salary    FLOAT,
		);\n

		# Load csv into mysql table
		LOAD DATA LOCAL INFILE '/home/path/file_name.csv' 
		INTO TABLE emp 
		FIELDS TERMINATED BY ','
		ENCLOSED BY '"'
		LINES TERMINATED BY '\\n' 
		IGNORE 1 ROWS;\n

		# Execute SQL queries
		Select * from emp;\n

		#Read Mysql Table in Spark\n

		df = spark.read.format("jdbc")\
			.option("url", "jdbc:mysql://localhost:3306/<database_name>?useSSL=false")\
			.option("driver", "com.mysql.jdbc.Driver")\
			.option("dbtable", "<table_name>")\
			.option("user", "hiveuser")\
			.option("password", "hivepassword").load()

		""")






def pyspark_s3(update, context):
	update.message.reply_text("""
		# Start pyspark with aws pakages
		pyspark --packages com.amazonaws:aws-java-sdk-pom:1.10.34, org.apache.hadoop:hadoop-aws:2.6.0\n

		# Provide AccessId and SecretAccessKey
		access_id = ("<your_AccessId>")
		secretAccessKey = ("<your_SecretAccessKey>")\n

		# Setup Hadoop Configuration
		hadoop_conf = spark._jsc.hadoopConfiguration()
		hadoop_conf.set("fs.s3.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
		hadoop_conf.set("fs.s3.awsAccessKeyId", access_id)
		hadoop_conf.set("fs.s3.awsSecretAccessKey", secretAccessKey)\n

		# Read a file
		df=spark.read\
			.option('inferschema','true')\
			.option('header','true')\
			.option('sep',',')\
			.csv("s3://bucket-name/file_name.csv")\n

		df.show()\n

		# Write Dataframe to S3
		df.write.csv("s3://bucket-name/file_name.csv",mode="overwrite")\n
		""")