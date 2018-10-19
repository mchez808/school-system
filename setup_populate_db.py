from peewee import *

mysql_db = MySQLDatabase('school')


class Students(Model):
    """ MySQL Table """
    ID = IntegerField(primary_key=True)
    FIRST_NAME = CharField()
    LAST_NAME = CharField()
    GRADE = IntegerField(default=0)

    class Meta:
        database = mysql_db


def initialize():
	"""Create the database and table (only if they don't already exist)."""
	db.connect()
	db.create_tables([Students], safe=True)


# Create table STUDENTS

