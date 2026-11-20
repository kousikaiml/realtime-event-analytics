import argparse,json,time
from kafka import KafkaProducer
from events import create_event
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--count",type=int,default=10)
 parser.add_argument("--bootstrap",default="localhost:9092")
 args=parser.parse_args()
 producer=KafkaProducer(bootstrap_servers=args.bootstrap,
  value_serializer=lambda x:json.dumps(x).encode(),
  key_serializer=lambda x:x.encode())
 try:
  for _ in range(args.count):
   event=create_event()
   producer.send("quote-events",key=event["policyNumber"],value=event)
   print("Produced",event["eventId"],event["lob"])
   time.sleep(.2)
  producer.flush()
 finally: producer.close()
if __name__=="__main__": main()
