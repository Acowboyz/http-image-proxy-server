from app import db


class APICounter(db.Model):
    __tablename__ = 'apicounter'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_name = db.Column(db.TEXT, unique=True, nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, api_name, count):
        self.api_name = api_name
        self.count = count

    def __repr__(self):
        return f'<title {self.body}>'
