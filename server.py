from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') #index,about,works,work,contact
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try: 
            data = request.form.to_dict()
            with open('database.csv', 'a', newline='') as database_file:
                writer = csv.writer(database_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([data['email'], data['subject'], data['message']])
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else: 
        return 'something went wrong. Try again!'


#with debug mode, changes can be applied on the go 

#https://flask.palletsprojects.com/en/3.0.x/quickstart/
#https://learn.microsoft.com/de-de/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3
