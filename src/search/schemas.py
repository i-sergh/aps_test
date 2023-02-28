from pydantic import BaseModel

#from datetime import datetime
import datetime

class Document(BaseModel):
    id: int
    rubrics: str
    text: str
    created_date: datetime.datetime

