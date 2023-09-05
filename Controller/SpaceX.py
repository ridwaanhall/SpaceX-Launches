import requests


class SpaceXLaunches:

  def __init__(self):
    self.url = "https://api.spacexdata.com/v4/launches"

  def fetch_spacex_launches(self):
    response = requests.get(self.url)
    if response.status_code == 200:
      return response.json()
    else:
      return []

  def categorize_launches(self, launches):
    successful = list(
      filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(
      filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {"successful": successful, "failed": failed, "upcoming": upcoming}
