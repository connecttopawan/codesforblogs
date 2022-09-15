from random_row_generate import generate_new_row
from conn_string import  cursor,db
import random
import time

def insert_to_table():
    while True:
        command = "INSERT INTO users values" + str(generate_new_row())
        cursor.execute(command)
        db.commit()
        time.sleep(random.random())
