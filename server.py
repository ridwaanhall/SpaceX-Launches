from flask import Flask, render_template, url_for, redirect
from Controller.SpaceX import SpaceXLaunches
from datetime import datetime

app = Flask(__name__)


# website using v4
@app.route("/")
def index():
  spacex = SpaceXLaunches()
  launches = spacex.categorize_launches(spacex.web_categorize())
  return render_template("spacex.html", launches=launches)


# ================ ALL LAUNCHES DATA ===================
# v2
@app.route("/v2/")
def redirect_to_v2():
  return redirect(url_for("api_categorize_v2"))


@app.route("/v2")
def api_categorize_v2():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_v2()
  return launches


# v3
@app.route("/v3/")
def redirect_to_v3():
  return redirect(url_for("api_categorize_v3"))


@app.route("/v3")
def api_categorize_v3():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_v3()
  return launches


# v4
@app.route("/v4/")
def redirect_to_v4():
  return redirect(url_for("api_categorize_v4"))


@app.route("/v4")
def api_categorize_v4():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_v4()
  return launches


# v5
@app.route("/v5/")
def redirect_to_v5():
  return redirect(url_for("api_categorize_v5"))


@app.route("/v5")
def api_categorize_v5():
  spacex = SpaceXLaunches()
  launches = spacex.spacex_v5()
  return launches


# ================ LAUNCHES CATEGORIZE ================
# v4
@app.route("/v4/launches/")
def redirect_to_v4_all():
  return redirect(url_for("api_all_v4"))


@app.route("/v4/launches")
def api_all_v4():
  spacex = SpaceXLaunches()
  launches = spacex.categorize_launches(spacex.spacex_v4())
  return launches


# v5
@app.route("/v5/launches/")
def redirect_to_v5_all():
  return redirect(url_for("api_all_v5"))


@app.route("/v5/launches")
def api_all_v5():
  spacex = SpaceXLaunches()
  launches = spacex.categorize_launches(spacex.spacex_v5())
  return launches


# ================ LAUNCHES DETAIL CATGORIZE ===============
# v4 successful
@app.route("/v4/launches/successful")
def redirect_to_v4_successful():
  return redirect(url_for("api_successful_v4"))


@app.route("/v4/launches/successful")
def api_successful_v4():
  spacex = SpaceXLaunches()
  launches = spacex.successful(spacex.spacex_v4())
  return launches

# v4 failed
@app.route("/v4/launches/failed/")
def redirect_to_v4_failed():
  return redirect(url_for("api_failed_v4"))


@app.route("/v4/launches/failed")
def api_failed_v4():
  spacex = SpaceXLaunches()
  launches = spacex.failed(spacex.spacex_v4())
  return launches


# v4 upcoming
@app.route("/v4/launches/upcoming/")
def redirect_to_v4_upcoming():
  return redirect(url_for("api_upcoming_v4"))

@app.route("/v4/launches/upcoming")
def api_upcoming_v4():
  spacex = SpaceXLaunches()
  launches = spacex.upcoming(spacex.spacex_v4())
  return launches

# v5 successful
@app.route("/v5/launches/successful/")
def redirect_to_v5_successful():
  return redirect(url_for("api_successful_v5"))


@app.route("/v5/launches/successful")
def api_successful_v5():
  spacex = SpaceXLaunches()
  launches = spacex.successful(spacex.spacex_v5())
  return launches

# v5 failed
@app.route("/v5/launches/failed/")
def redirect_to_v5_failed():
  return redirect(url_for("api_failed_v5"))


@app.route("/v5/launches/failed")
def api_failed_v5():
  spacex = SpaceXLaunches()
  launches = spacex.failed(spacex.spacex_v5())
  return launches


# v5 upcoming
@app.route("/v5/launches/upcoming/")
def redirect_to_v5_upcoming():
  return redirect(url_for("api_upcoming_v5"))


@app.route("/v5/launches/upcoming")
def api_upcoming_v5():
  spacex = SpaceXLaunches()
  launches = spacex.upcoming(spacex.spacex_v5())
  return launches


# date filter
@app.template_filter("date_only")
def date_only_filter(s):
  date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
  return date_object.date()


# Error handler for 404 (Not Found) errors
@app.errorhandler(404)
def page_not_found(e):
  return [], 404
