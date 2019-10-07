from flask import Flask, render_template, request, redirect
from datetime import datetime
from time import gmtime, strftime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    apple_amount_form = request.form['apple']
    blackberry_amount_form = request.form['blackberry']
    raspberry_amount_form = request.form['raspberry']
    strawberry_amout_form = request.form['strawberry']
    first_name_form_form = request.form['first_name']
    last_name_form = request.form['last_name']
    student_id_form = request.form['student_id']
    now = datetime.now()
    date_form=now.strftime("%B %d %Y, %I:%M %p")
    count = int(apple_amount_form) + int(blackberry_amount_form) + int(raspberry_amount_form) + int(strawberry_amout_form)

    return render_template("checkout.html", apple_temp=apple_amount_form, blackberry_temp=blackberry_amount_form, raspberry_temp=raspberry_amount_form, strawberry_temp=strawberry_amout_form, first_name_temp=first_name_form_form, last_name_temp=last_name_form, student_id_temp=student_id_form, date_temp=date_form, count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)   