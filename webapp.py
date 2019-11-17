from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
  return render_template('home.html')

@app.route("/p1")
def render_page1():
  return render_template('page1.html', horoscope = "")


if __name__=="__main__":
  app.run(debug=False)
