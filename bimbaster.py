import requests

#координаты
coords = (57.919610, 59.942701)
#токен
API_KEY = '65011347-23b4-4b34-bcbe-8e7dc77b287e'
#юрл погоды
url = 'https://api.weather.yandex.ru/v2/forecast?'
headers = {'X-Yandex-API-Key': API_KEY}
params = {'lat': coords[0],
          'lon': coords[1],
          'lang': 'ru_RU'}
data = requests.get(url, headers=headers, params=params).json()
# отдельно сохраняем информацию о погоде на текущий момент времени
fact = data['fact']
# текущая температура
print(f"Температура: {fact['temp']} град.")
# есть ли гроза
thunder = {
    True: 'есть',
    False: 'нету',
}
print(f"Гроза(ы) {thunder[fact['is_thunder']].lower()}")
#тип осадков
prec = {
    0: 'без осадков', 
    0.5: 'дождик',
    1: 'дождь',
    2: 'дождь со снегом',
    3: 'снег',
    4: 'град',
}
print(f"Тип осадков: {prec[fact['prec_strength']].lower()}")
# сила осадков
strength_prec = {
    0: 'без осадков',
    0.25: 'слабый дождь или слабый снег',
    0.5: 'дождь или снег',
    0.75: 'сильный дождь или сильный снег',
    1: 'сильный ливень или очень сильный снег',
}
print(f"Сила осадков: {strength_prec[fact['prec_strength']].lower()}")