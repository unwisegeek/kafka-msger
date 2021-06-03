from confluent_kafka import Producer
from confluent_kafka import Consumer
import os, socket, sys, time

hostname = socket.gethostname()
kafkahost = sys.argv[1]

pconf = {'bootstrap.servers': "localhost:9092", 
         'client.id': hostname
         }
cconf = {'bootstrap.servers': "localhost:9092",
         'group.id': "reader",
         'auto.offset.reset': 'smallest'
         }

if "--input" in sys.argv: # Act in Producer Mode
    producer = Producer(pconf)

    while True:
        message_to_send = input("Message: ")
        try:
            producer.produce('messages', key="msg", value="{}: {}".format(hostname, message_to_send))
            os.system('clear')
        except:
            print("Message failed.")
            time.sleep(1)
            os.system('clear')



if "--msg" in sys.argv: # Act in Consumer
    consumer = Consumer(cconf)
    running = True
    try:
        consumer.subscribe(['messages'])

        msg_count = 0
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: 
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' % 
                                    (msg.topic(), msg.partition(), msg.offset())) 
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value().decode('utf-8'))
    finally:
        consumer.close()

