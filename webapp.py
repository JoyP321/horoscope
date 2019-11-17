from flask import Flask, url_for, render_template, request
import os
import json
import random
import datetime
app = Flask(__name__)

@app.route("/")
def render_main():
  with open('horoscope_data.json') as horoscope_data:
    fortunes = json.load(horoscope_data)
  return render_template('home.html')

@app.route("/p1")
def render_page1():
  with open('horoscope_data.json') as horoscope_data:
    fortunes = json.load(horoscope_data)
  return render_template('page1.html', horoscope = "")


@app.route("/response")
def render_page1_response():
  with open('horoscope_data.json') as horoscope_data:
    fortunes = json.load(horoscope_data)
  sign = request.args['sign']
  return render_template('page1.html', horoscope = get_horoscope(fortunes, sign))


def get_horoscope(fortunes, sign):
  val = 1+ int(random.random() *6)
  return "Hey " + sign + "! Your horoscope is: \n\t" +fortunes[sign][str(val)] + datetime.datetime.now()
  

if __name__=="__main__":
  app.run(debug=True)
