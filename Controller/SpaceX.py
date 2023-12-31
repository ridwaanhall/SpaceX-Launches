import requests


class ReadUrl:

  def read_json(self, response):
    if response.status_code == 200:
      return response.json()
    else:
      return []


class SpaceXLaunches:

  BASE_URL = "https://api.spacexdata.com"
  
  def __init__(self):
    self.url_web = f"{self.BASE_URL}/v4/launches"
    self.url_v2 = f"{self.BASE_URL}/v2/launches"
    self.url_v3 = f"{self.BASE_URL}/v3/launches"
    self.url_v4 = f"{self.BASE_URL}/v4/launches"
    self.url_v5 = f"{self.BASE_URL}/v5/launches"


  # ================== WEBSITE ===================
  def web_categorize(self):
    reader = ReadUrl()
    response = requests.get(self.url_web)
    launches = reader.read_json(response)
    return launches


  # ================== VERSION ==================
  # v2
  def spacex_v2(self):
    reader = ReadUrl()
    response = requests.get(self.url_v2)
    launches = reader.read_json(response)
    return launches

  # v3
  def spacex_v3(self):
    reader = ReadUrl()
    response = requests.get(self.url_v3)
    launches = reader.read_json(response)
    return launches

  # v4
  def spacex_v4(self):
    reader = ReadUrl()
    response = requests.get(self.url_v4)
    launches = reader.read_json(response)
    return launches

  # v5
  def spacex_v5(self):
    reader = ReadUrl()
    response = requests.get(self.url_v5)
    launches = reader.read_json(response)
    return launches

  # ========================= CATEGORY =============================
  # successful
  def successful(self, launches):
    successful = list(
      filter(lambda x: x["success"] and not x["upcoming"], launches))

    return {
      "successful": successful
    }

  # failed
  def failed(self, launches):
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))

    return {
      "failed": failed
    }

  # upcoming
  def upcoming(self, launches):
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {
      "upcoming": upcoming
    }

  # successful, failed, upcoming
  def categorize_launches(self, launches):
    successful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {
      "successful": successful, 
      "failed": failed, 
      "upcoming": upcoming
    }