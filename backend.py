import requests

API_KEY = "279c068dcf4621ab6c6b85ccd2087f0a"


def get_data(place, forecast_days=None, kind=None):
    # Fixed the typo in the query parameter from 'aprid' to 'appid'
    url = (
        f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))