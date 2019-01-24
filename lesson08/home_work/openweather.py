
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

#  Melchuk A.B.
#  Due to not responding or restricted OWeather service through usual http connection (from Moscow)
#  I was made to try Tor as proxy socks


import urllib.request
import gzip
import json
import requests
import socks    # pip install PySocks
import socket
import os
import sqlite3
import datetime
import pickle

try:
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket
    response = requests.get('http://icanhazip.com')
    print('Our ip is {}'.format(response.text))
except Exception as e:
        print("*** Error. No Tor found as service on port 9050!!! Run it to continue...\n", e)
        print("""
    Use Expert Bundle version of Tor
    tor.exe --service install
    netstat -aon | findstr ":9050"
        """)
        exit(-1)






search_city = "Moskva"
search_country = "RU"
city_list_file_name = 'city_list.serialized'

# Load new city db or using loaded

if os.path.isfile(city_list_file_name):
    print('Cities list found.')
    f = open(city_list_file_name, 'rb')
    json_cities = pickle.load(f)
    print('Found {} items'.format(len(json_cities)))
else:
    print('Cities list is not found. Downloading...')
    webf = urllib.request.urlopen('http://bulk.openweathermap.org/sample/city.list.json.gz',)
    txt = webf.read()
    print('Done.')
    print('File len is ', len(txt))
    j_text = gzip.decompress(txt)
    json_cities = json.loads(j_text)
    print('Decompressed {} items'.format(len(json_cities)))
    with open(city_list_file_name, 'wb') as f:
        pickle.dump(json_cities, f)
    print('Saved.')


# Finding city id by name

city_id = -1   # DEST CITY ID
for i, city in enumerate(json_cities):
    if city['name'] == search_city and city['country'] == search_country:
        print(city)
        city_id = city['id']
print('Moscow id is', city_id)


# Loading appid

appid = '-1'
with open('app.id', 'r') as f2:
    appid = f2.read()
    appid = appid.strip()
    print('APPID = {}'.format(appid))


# Getting weather by city id

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'id': city_id, 'appid': appid, 'units': 'metric'})
    # res = requests.get("http://api.openweathermap.org/data/2.5/find",
    # params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    if not data["cod"] == 200:
        print(data["message"])
    else:
        print(data)
except Exception as e:
    print("Exception (weather):", e)
    pass
#
# response_example = {'coord': {'lon': 37.61, 'lat': 55.76}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}], 'base': 'stations', 'main': {'temp': -13.61, 'pressure': 1014, 'humidity': 92, 'temp_min': -16, 'temp_max': -11}, 'visibility': 10000, 'wind': {'speed': 4, 'deg': 290}, 'clouds': {'all': 40}, 'dt': 1548347400, 'sys': {'type': 1, 'id': 9027, 'message': 0.004, 'country': 'RU', 'sunrise': 1548308207, 'sunset': 1548337637}, 'id': 524894, 'name': 'Moskva', 'cod': 200}

weather_city_id = data["id"]
weather_temp = float(data["main"]["temp"])
weather_conds = str(data["weather"])
weather_date = datetime.datetime.now().date()
weather_city_name = data["name"]
weather_country = data["sys"]["country"]

print(weather_temp)
print(weather_date)
print(weather_conds)
print(weather_city_name)
print(weather_country)

def db_connection(db_filename):
    conn = sqlite3.connect(db_filename)
    # add connection permissions check
    return conn


def db_connection_close(conn):
    conn.close()


def db_delete(db_filename):
    os.remove(db_filename)


def db_create(conn):
    conn.execute("""
        create table if not exists weather (
            weather_city_id     INTEGER,
            weather_date        NUMERIC,
            weather_city_name   VARCHAR(255),
            weather_country        VARCHAR(255),
            weather_temp         REAL,
            weather_conds        VARCHAR(500),
            CONSTRAINT new_pk   PRIMARY KEY (weather_city_id, weather_date)
        );
        """)


def db_prep_data(city, date, city_name, country, temp, conds):
    return [(city, date, city_name, country, temp, conds)]


def db_insert(conn, weather_rows_list):
    try:
        for row_data in weather_rows_list:
            conn.execute("""
                insert into weather (weather_city_id, weather_date, weather_city_name, weather_country, weather_temp, weather_conds) VALUES ( ?, ?, ?, ?, ?, ?)""",
                         row_data
            )
            conn.commit()
    except Exception as e:
        print("Exception db_insert :: Not inserted. Such weather_date exists for this weather_city_id!!!")
        pass

def db_select(conn, check_id, check_date):
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from weather {} {} {} {}".format('where' if (int(check_id)) > 0 or len(check_date) > 0 else '',
                                                            'weather_city_id = ' + str(check_id) if (int(check_id)) > 0 else '',
                                                            'and' if (int(check_id)) > 0 and len(check_date) > 0 else '',
                                                            "weather_date = '" + check_date + "'" if (len(check_date)) > 0 else ''))
        selected = []
        for row in cur.fetchall():
            selected.append(row)
            w_city_id, w_date, w_city_name, w_country, w_temp, w_conds = row
            # print('db_select:: ', w_city_id, w_date, w_city_name, w_country, w_temp, w_conds)
        return selected
    except Exception as e:
        print("Exception db_select:", e)
        pass


def db_update(conn, wcity, wdate, wtemp, wconds):
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        update_string = "update weather set weather_temp = {wtemp}, weather_conds = \"{wconds}\"  where weather_city_id={wcity} and weather_date=\'{wdate}\'".format_map(
                    {'wcity': wcity,'wdate': wdate,'wtemp': wtemp,'wconds': wconds})
        print(update_string)
        cur.execute(update_string)
        print("db_update:: Updated!!!")
        conn.commit()
    except Exception as e:
        print("Exception db_update::", e)
        pass


def db_update_is_neeeded(conn, city, date):
    sel = db_select(conn, city, date)
    if len(sel)>0:
        print ("Update is needed!")
        return True
    print("Update is not needed!")
    return False

db_file = 'open_weather.db'


# db_delete(db_file)
c = db_connection(db_file)
db_create(c)
db_insert(c, db_prep_data(weather_city_id, weather_date, weather_city_name, weather_country, weather_temp, weather_conds))

s = db_select(c, city_id, str(weather_date))
for data in s:
    print(*data)

if db_update_is_neeeded(c, city_id, str(weather_date)):
    db_update(c, city_id, str(weather_date), weather_temp, weather_conds)

s = db_select(c, city_id, str(weather_date))
for data in s:
    print(*data)

db_connection_close(c)


