def kafka_info(update, context):
	update.message.reply_text("""
		Kafka is an open source distributed event streaming platform\n

		Event streaming is the practice of capturing data in real-time from event sources like databases, sensors, mobile devices, cloud services, and software applications in the form of streams of events; storing these event streams durably for later retrieval; manipulating, processing, and reacting to the event streams in real-time as well as retrospectively; and routing the event streams to different destination technologies as needed.\n
		Event streaming thus ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time.\n

		Kafka provides three key capabilities for event streaming end-to-end with a single battle-tested solution:\n

		1. To publish (write) and subscribe to (read) streams of events, including continuous import/export of your data from other systems.\n
		2. To store streams of events durably and reliably for as long as you want.\n
		3. To process streams of events as they occur or retrospectively.\n

		To download Kafka pakages:
		/kafka_download\n
		To Execute kafka commands:
		/kafka_getting_started\n

		For apache kafka quickstart:
		https://kafka.apache.org/quickstart
		""")

def kafka_download(update, context):
	update.message.reply_text("""
		Download the latest Kafka release\n
		https://www.apache.org/dyn/closer.cgi?path=/kafka/2.8.0/kafka_2.13-2.8.0.tgz\n

		Extract packages:\n
		$ tar -xzf kafka_2.13-2.8.0.tgz
		$ cd kafka_2.13-2.8.0
		""")

def kafka_getting_started(update, context):
	update.message.reply_text("""
		\nInitialize Kafka Enviornment:
		/kafka_env\n

		Create topic:
		/kafka_topic\n

		Start Producer:
		/kafka_producer\n

		Start Consumer:
		/kafka_consumer\n

		Terminate Kafka:
		/kafka_terminate
		"""
		)


def kafka_env(update, context):
	update.message.reply_text(
		"""
		Start Enviornment:\n

		# Start the ZooKeeper service:\n
		$ bin/zookeeper-server-start.sh config/zookeeper.properties\n

		# Start the Kafka broker service:\n
		$ bin/kafka-server-start.sh config/server.properties
		"""
		)


def kafka_topic(update, context):
	update.message.reply_text("""
		Create a Topic:\n
		$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092\n

		View / Describe a Topic:\n
		$ bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
		""")

def kafka_producer(update, context):
	update.message.reply_text("""
		Start Kafka Producer in Console:\n
		$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092\n
		Write some events into the topic
		""")

def kafka_consumer(update, context):
	update.message.reply_text("""
		Start Kafka Consumer in Console:\n
		$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
		""")


def kafka_terminate(update, context):
	update.message.reply_text("""
		TERMINATE THE KAFKA ENVIRONMENT:\n\n
		1. Stop the producer and consumer clients with Ctrl-C, if you haven't done so already.\n
		2. Stop the Kafka broker with Ctrl-C.\n
		3. Lastly, stop the ZooKeeper server with Ctrl-C.\n\n
		If you also want to delete any data of your local Kafka environment including any events you have created along the way, run the command:\n
		$ rm -rf /tmp/kafka-logs /tmp/zookeeper
		""")