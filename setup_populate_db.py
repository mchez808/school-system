from peewee import *

import os

db = SqliteDatabase('school.db')


class STUDENTS(Model):
    """ MySQL Table """
    ID = IntegerField(primary_key=True)
    FIRST_NAME = CharField()
    LAST_NAME = CharField()
    GRADE = IntegerField(default=0)

    class Meta:
        database = db


db.connect()
db.create_tables([STUDENTS], safe=True)
STUDENTS.create(ID=10387,
                 FIRST_NAME='Jarrod',
                 LAST_NAME='Sam',
                 GRADE=8);

select_all = STUDENTS.select()
descending_option = STUDENTS.GRADE.desc()
sorted_query = select_all.order_by(descending_option)
one_record = sorted_query.get()

print("One student is: {0.ID}  {0.FIRST_NAME}  {0.LAST_NAME}.".format(one_record))


input("Entry will now be deleted. Press <Enter>")
one_record.delete_instance()
db.close()
