from flask import Flask,render_template, request, redirect, url_for

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./project-sw-tool-firebase-adminsdk-xlabq-7281acf22f.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# def adddata(name, username):
#         doc_ref = db.collection(u'users').document('yotsanan'
#         doc_ref.set({
#             u'name': name,
#             u'username': username,
#             u'born': 1815
#         })
   

app = Flask(__name__)

@app.route('/')


@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/sellpage')
def sellpage():
    return render_template("sellpage.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/new')
def new():
    doc_ref = db.collection(u'News').document(u'news_trash')
    news = doc_ref.get()
   

    return render_template("new.html", new=news.to_dict())

@app.route('/map')
def map():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    url = 'https://www.google.com/maps/'
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)

    time.sleep(4)

    searchbox = browser.find_element(By.ID, 'searchboxinput')
    searchbox.click()
    searchbox.send_keys('ร้านขายขยะใกล้ฉัน')
    searchicon = browser.find_element(By.ID, 'searchbox-searchbutton')
    searchicon.click()

    return render_template("index.html")


# @app.route('/success/<name>')
# def success(name):
#         doc_ref = db.collection(u'users').document('yotsanan')
#         doc_ref.set({
#             u'name': name,
#             u'username': 'hhh',
#             u'born': 1815
#         }) 

# @app.route('/login1',methods = ['POST', 'GET'])
# def login1():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


@app.route('/addfirebase/<email>/<password>')
def addfirebase(email, password):
        doc_ref = db.collection(u'users').document(email)
        doc_ref.set({
            u'email': email,
            u'password': password,
            u'type': 'user'
        })
        return redirect(url_for('login'))


@app.route('/addregister',methods = ['POST', 'GET'])
def addregister():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      return redirect(url_for('addfirebase',email=email, password=password))
   else:
      email = request.args.get('email')
      password = request.args.get('password')
      return redirect(url_for('addfirebase',email=email, password=password))


if __name__ == '__main__':
    app.run(debug= True, port=8081, host="0.0.0.0")