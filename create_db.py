from app import db
from models import APICounter

""" This file is to create the db for app using
1. Drop the db first in order to reset the counter to 0 every time.
2. Create the db
3. Insert the data for api counter. only need the counter of proxy api now.
4. Commit the db
"""

db.drop_all()
# create the database and the db table
db.create_all()

new_entry = APICounter('proxy', 0)
db.session.add(new_entry)

# commit the changes
db.session.commit()
