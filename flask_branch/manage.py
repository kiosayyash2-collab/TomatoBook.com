from flask import Flask
from flask import Flask, render_template, url_for

#make the main app 
app = Flask(__name__)
if app == "__main__":
    app.run(debug=True)

#import the routes from main/ folder
@app.route("/")
def hello():

    #  Just put all html in index.html
    #  return render_template('index.html')
    return """
<body>
    <a href="{{ url_for('main_finance') }}">Coin Toss</a>
    <a href="{{ url_for('main_notes') }}">Weather App</a>
</body>
"""

#function to open and trigger app when get request from user
#fucntion to open and  trigger main/finance route
@app.route("/main/finance")
def main_finance():

    #main Code for coin toss
    return render_template('finance_app.html')


#fucntion to open and  trigger main/notes route
@app.route("/main/notes")
def main_notes():

    #main Code for weather app
    return render_template('notes_app.html')
