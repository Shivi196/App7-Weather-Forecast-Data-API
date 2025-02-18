import requests

API_key = "f815b29bdd8da50d79e2f0a124cdda5e"

def get_data(place,forecast_days=None,option=None):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
  response = requests.get(url)
  data = response.json()
  return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))

