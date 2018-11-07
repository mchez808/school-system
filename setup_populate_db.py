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


def create_table(TABLE):
	"""Create the database and table (only if they don't already exist)."""
	db.connect()
	db.create_tables([TABLE], safe=True)


def populate_table(TABLE):
    pass
    # TABLE.create()


if __name__ == '__main__':
    table = STUDENTS
    print("The following table(s) were created successfully")
    create_table(table)
    print(str(table))
input("End of file. Press <Enter> to clear screen and exit.")
os.system('clear')
