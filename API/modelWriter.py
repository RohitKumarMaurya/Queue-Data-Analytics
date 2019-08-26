import TargetedWebCam as t
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import _thread as th
import datetime

app = Flask(__name__)

@app.route("/livecount")
@cross_origin()
def main():
    with open("countdata.txt","r") as f:
        count = str(f.read())
    return str(count)

@app.route("/historicaldata")
@cross_origin()
def hist():
    data = []
    x = ""
    with open("historical.txt","r")as f:
        data = f.readlines()
    for i in data:
        x += '<p>' + i + '</p>'
    return str(x)

def file():
    count = str(t.model())
    with open("countdata.txt","r+") as f:
        f.write(count)
    with open("historical.txt","a+") as f:

        data = str(datetime.date.today()) + "&nbsp; &nbsp; &nbsp;" +\
               str(datetime.datetime.now().hour)+ ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) +\
               "&nbsp; &nbsp;" + "\t&nbsp; &nbsp; : &nbsp; &nbsp; " + count + "\n"
        f.write(data)

def simulate():
    while True :
        file()

if __name__ == '__main__':
    th.start_new_thread(simulate,())
    app.run(debug=True, host='0.0.0.0', port=5000)