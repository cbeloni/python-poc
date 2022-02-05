kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic

kafka-topics.sh --list --zookeeper zookeeper:2181

kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --from-beginning --max-messages 100


kafka-run-class.sh kafka.admin.ConsumerGroupCommand --group <GROUP_NAME> --bootstrap-server localhost:9092 --describe
kafka-run-class.sh kafka.admin.ConsumerGroupCommand --all-groups --bootstrap-server localhost:9092 --describe

pip install kafka-python