import requests


class ReadUrl:

  def read_json(self, response):
    if response.status_code == 200:
      return response.json()
    else:
      return []


class SpaceXLaunches:

  def __init__(self):
    self.url = "https://api.spacexdata.com/v4/launches"

  def spacex_launches_web(self):
    reader = ReadUrl()
    response = requests.get(self.url)
    launches = reader.read_json(response)
    return launches

  def categorize_launches(self, launches):
    successful = list(
      filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(
      filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {"successful": successful, "failed": failed, "upcoming": upcoming}
