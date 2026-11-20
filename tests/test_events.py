from events import create_event
def test_event_fields():
 event=create_event()
 assert event["eventType"]=="QUOTE_CREATED"
 assert event["policyNumber"].startswith("DEMO-")
 assert event["premium"]>0
