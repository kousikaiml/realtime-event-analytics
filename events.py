from datetime import datetime,timezone
from uuid import uuid4
from random import choice,uniform
LOBS=["Property","GeneralLiability","WorkersCompensation"]
def create_event():
 return {"eventId":str(uuid4()),"eventType":"QUOTE_CREATED",
         "policyNumber":"DEMO-"+uuid4().hex[:8].upper(),"lob":choice(LOBS),
         "premium":round(uniform(500,5000),2),"eventTime":datetime.now(timezone.utc).isoformat()}
