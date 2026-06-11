from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing', methods=['GET'])
def welcome():
    return 'Charie is a website storage kind of site for storing your personalised original characters'
