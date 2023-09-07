from flask import Flask, render_template
from Controller.SpaceX import SpaceXLaunches
from datetime import datetime

app = Flask(__name__)


# website using v4
@app.route("/")
def index():
  spacex = SpaceXLaunches()
  launches = spacex.categorize_launches(spacex.spacex_launches_web())
  return render_template("spacex.html", launches=launches)


# v2
@app.route("/v2")
def api_all_v2():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_launches_v2()
  return launches


# v3
@app.route("/v3")
def api_all_v3():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_launches_v3()
  return launches


# v4
@app.route("/v4")
def api_all_v4():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_launches_v4()
  return launches


# date filter
@app.template_filter("date_only")
def date_only_filter(s):
  date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
  return date_object.date()
