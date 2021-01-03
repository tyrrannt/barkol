import requests
from authapp.models import Weather, Country, City, Person
from datetime import datetime as dt

appid = '52f3273beefd4ef8f61085589e9622e9'


# Перевод градусов в направление
def get_wind_direction(deg):
    l = ['С ', 'СВ', ' В', 'ЮВ', 'Ю ', 'ЮЗ', ' З', 'СЗ']
    for i in range(0, 8):
        step = 45.
        min = i * step - 45 / 2.
        max = i * step + 45 / 2.
        if i == 0 and deg > 360 - 45 / 2.:
            deg = deg - 360
        if min <= deg <= max:
            res = l[i]
            break
    return res


# Проверка наличия в базе информации о нужном населенном пункте
def get_city_id(s_city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass
    assert isinstance(city_id, int)
    return city_id


def save_weather(date, data):
    model = Weather.objects.create(weather_date=date.date(), coord_lon=data['coord']['lon'],
                                   coord_lat=data['coord']['lat'],
                                   weather_id=data['weather'][0]['id'],
                                   weather_main=data['weather'][0]['main'],
                                   weather_description=data['weather'][0]['description'],
                                   weather_icon=data['weather'][0]['icon'],
                                   main_temp=data['main']['temp'],
                                   main_feels_like=data['main']['feels_like'],
                                   main_temp_min=data['main']['temp_min'],
                                   main_temp_max=data['main']['temp_max'],
                                   main_pressure=(data['main']['pressure']*7.501)/10,  # (pressure*7,501/10) перевод в мм рт. ст.
                                   main_humidity=data['main']['humidity'],
                                   visibility=data['visibility'], wind_speed=data['wind']['speed'],
                                   wind_deg=data['wind']['deg'],
                                   country=Country.objects.get(code=data['sys']['country']),
                                   city=City.objects.get(city_id=data['id']))
    try:
        model.save()
        return True
    except Exception as err:
        print(err)
        return False


def weather(city_id):
    date = dt.today()
    result = {}
    data = {}
    weather_class = {'Snow': 'flaticon-weather-3', 'Light snow': 'flaticon-weather-3',
                     'Clear sky': 'flaticon-sun-fill', 'Broken clouds': 'flaticon-sky-sun',
                     'Light rain': 'flaticon-weather', }
    try:
        model = Weather.objects.get(weather_date=date.date(), city__city_id=city_id)
        result.update({'conditions': model.weather_description})
        result.update({'temp': model.main_temp})
        result.update({'temp_min': model.main_temp_min})
        result.update({'temp_max': model.main_temp_max})
        result.update({'humidity': model.main_humidity})
        result.update({'city': model.city})
        result.update({'country': model.country})
        result.update({'wclass': weather_class[model.weather_main]})
    except Weather.DoesNotExist:
        try:
            res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            if save_weather(date, data):
                model = Weather.objects.get(weather_date=date.date(), city__city_id=city_id)
                result.update({'conditions': model.weather_description})
                result.update({'temp': model.main_temp})
                result.update({'temp_min': model.main_temp_min})
                result.update({'temp_max': model.main_temp_max})
                result.update({'humidity': model.main_humidity})
                result.update({'city': model.city})
                result.update({'country': model.country})
                result.update({'wclass': weather_class[model.weather_main]})
        except Exception as e:
            print('2: ', e)
            result.update({'conditions:': '0'})
    return result


def main_menu_generate(menu_items):
    menu_dict = {}
    result = {}
    for item in menu_items:
        if not item.parent_category:
            menu_dict.update({item.hash_view: list([item.name, item.url_address], )})
        else:
            menu_dict[item.parent_category.hash_view].append([item.name, item.url_address])
    result.update({'nav_menu': menu_items})
    result.update({'nav_hash': menu_dict})
    return result


def footer_info_generator(counteragent):
    result = {}
    result.update({'address': counteragent.juridical_address})
    result.update({'phone_number': counteragent.phone})
    result.update({'email': counteragent.email})
    return result
