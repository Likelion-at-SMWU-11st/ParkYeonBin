import requests
import json

city = "Paris"
apikey = "3e0f2d1b497758ae72c999e7d03bd52b"
lang="kr"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

# print(type(result.text))
# print(type(data))

print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["description"], "입니다.")
print("현재 온도는", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는", data["main"]["feels_like"], "입니다.")