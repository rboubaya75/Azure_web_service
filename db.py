
import psycopg2
import logging
host="localhost"
user="postgres"
dbname="postgres"
password="123"



logging.basicConfig(filename='logging.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')



# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()


def create_table():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS contact (id serial NOT NULL,customer VARCHAR(255), rating VARCHAR(255), comments VARCHAR(255))")
    print("table created")
    conn.commit()

create_table()

cursor.close()
conn.close()



"""
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

from send_email import send_mail

app = Flask(__name__)


db = SQLAlchemy(app)





class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


"""