from peewee import *

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


def populate_table():
    pass



if __name__ == '__main__':
    list_of_tables = [STUDENTS, TEACHERS]
    # list_of_tables = [STUDENTS, TEACHERS, SUBJECTS, SCHEDULE, ROOMS, PERIODS, CLASSES]
    print("The following table(s) were created successfully")
    for table in list_of_tables:
        create_table(table)
        print(str(table))

