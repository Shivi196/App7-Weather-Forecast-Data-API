import requests

API_key = "f815b29bdd8da50d79e2f0a124cdda5e"

def get_data(place,forecast_days=None):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
  response = requests.get(url)
  data = response.json()
  filtered_data = data["list"]
  nr_values = 8 * forecast_days #this api generate report every 3hr in 24hr/1day that's 8 times in single day so if you want to forecast data for week so type in forecast_days as 5 and it will give 8 * 5 = 40 observations
  filtered_data = filtered_data[:nr_values] #filtering the list values with the no of forecasted days entered by user

  return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=3))

