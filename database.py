# we will use this function to add offers to the DB
import pymysql


def add_to_database():

    # open a DB connection
    db = pymysql.connect(host="localhost",
                         user="username",
                         password="my_password",
                         db="indeed",
                         charset="utf8"
                         )

    # prepare a cursor object using cursor() method
    cursor =db.cursor()