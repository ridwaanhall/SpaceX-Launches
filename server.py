from flask import Flask, render_template
from Controller.SpaceX import SpaceXLaunches
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
  spacex = SpaceXLaunches()
  launches = spacex.categorize_launches(spacex.spacex_launches_web())
  return render_template("spacex.html", launches=launches)


#@app.route("/v5")
#def api_all():
#  spacex = SpaceXLaunches()
#  launches = spacex.categorize_launches(spacex.spacex_launches_web())
#  return launches


@app.template_filter("date_only")
def date_only_filter(s):
  date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
  return date_object.date()
