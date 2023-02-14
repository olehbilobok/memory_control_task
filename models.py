import datetime
from config import db


class Memory(db.Document):
    id = db.StringField(primary_key=True)
    consumption = db.DecimalField()
    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    def to_json(self):
        return {
            "id": self.id,
            "consumption": self.consumption,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }



