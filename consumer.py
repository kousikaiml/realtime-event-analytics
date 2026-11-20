import json,os
from collections import Counter
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
def main():
 topic="quote-events"
 es=Elasticsearch(os.getenv("ELASTICSEARCH_URL","http://localhost:9200"))
 if not es.indices.exists(index=topic):
  es.indices.create(index=topic,mappings={"properties":{
   "eventId":{"type":"keyword"},"policyNumber":{"type":"keyword"},
   "eventType":{"type":"keyword"},"lob":{"type":"keyword"},
   "premium":{"type":"double"},"eventTime":{"type":"date"}}})
 consumer=KafkaConsumer(topic,bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092"),
  auto_offset_reset="earliest",enable_auto_commit=True,group_id="quote-analytics-demo",
  value_deserializer=lambda b:json.loads(b.decode()))
 counts=Counter()
 print("Waiting for quote events. Ctrl+C to stop.")
 try:
  for msg in consumer:
   event=msg.value
   if not {"eventId","policyNumber","lob","premium","eventTime"}.issubset(event):
    print("Skipping malformed event"); continue
   es.index(index=topic,id=event["eventId"],document=event)
   counts[event["lob"]]+=1
   print("Indexed",event["policyNumber"],"counts:",dict(counts))
 except KeyboardInterrupt: pass
 finally: consumer.close()
if __name__=="__main__": main()
