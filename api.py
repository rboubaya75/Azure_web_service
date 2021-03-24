

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


from flask import Flask, render_template, request

from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'r.boubaya@gmail.com'
app.config['MAIL_PASSWORD'] = 'Leouf2017.'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def send_mail(customer, rating, comments, email):

    msg = Message('Hello', sender = 'r.boubaya@gmail.com', recipients = [email])
    msg.body = f"New Feedback Submission:Customer: {customer}, Rating: {rating}, Comments: {comments}"

    mail.send(msg)
    return "sent"



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
       
        customer= request.form.get("customer")
        rating= float(request.form.get("rating"))
        comments= request.form.get("comments")
        email=request.form.get("email")
        cursor.execute("INSERT INTO contact (customer, rating, comments) VALUES (%s,%s,%s) ",(customer, rating, comments))
        send_mail(customer,rating,comments, email)
        
        conn.commit()
        
        return render_template('success.html')
  




if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=4200, debug = True)


