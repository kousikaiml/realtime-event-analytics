# Real-Time Event Analytics
Python event producer and consumer using Kafka, with Elasticsearch indexing and live per-LOB
event counts. Synthetic quote events only.

## Run
Requires Docker and Python 3.10+.
`docker compose up -d`
`python -m venv .venv` then activate and `pip install -r requirements.txt`.
Terminal 1: `python consumer.py`
Terminal 2: `python producer.py --count 20`
Search indexed events: `curl http://localhost:9200/quote-events/_search?pretty`

This single-broker, unsecured compose setup is for local learning only. Production systems should
use TLS/SASL, schema management, retry and dead-letter topics, consumer lag monitoring and durable
aggregation state.
