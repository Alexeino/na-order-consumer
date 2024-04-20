from pykafka.client import KafkaClient


kclient = KafkaClient()

def main():
    print("Starting Consumer...")
    consumer = kclient.create_consumer()
    for record in consumer:
        print(f"""
              Order Details - {record.value} with key {record.key}
              """)
        
        
if __name__ == '__main__':
    main()