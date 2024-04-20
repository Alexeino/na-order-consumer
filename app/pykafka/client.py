from kafka.admin import NewTopic, KafkaAdminClient
from kafka.errors import TopicAlreadyExistsError
from kafka import KafkaProducer, KafkaConsumer
from core.settings import settings
import json

class KafkaClient:
        
    def create_topic(self,topic_name=settings.KAFKA_TOPIC_NAME,
                     num_partitions=settings.KAFKA_NUM_PARTITION,
                     replication_factor=settings.KAFKA_REPLICATION_FACTOR
                     ):
        client = KafkaAdminClient()
        try:
            topic = NewTopic(
                name=topic_name,
                num_partitions=num_partitions,
                replication_factor=replication_factor
            )
            client.create_topics([topic])
            return topic_name
        
        except TopicAlreadyExistsError:
            print(f"Topic {topic_name} Already Exists!")
            return topic_name
        finally:
            print("Closing the client!")
            client.close()
            
    def create_producer(self,**kwargs):
        return KafkaProducer(**kwargs)
    
    def key_deserializer(self,key:bytes):
        return key.decode('utf-8')
    
    def value_deserializer(self,value):
        return json.loads(value.decode('utf-8'))
    
    def create_consumer(self,**kwargs):
        consumer = KafkaConsumer(
                                group_id='orders.grp-0',
                                key_deserializer=self.key_deserializer,
                                value_deserializer=self.value_deserializer                             
                                )
        consumer.subscribe(settings.KAFKA_TOPIC_NAME)
        return consumer