
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
# import lesson08.home_work.openweather as ow
import openweather as ow

country = ''
print('sys.argv = ', sys.argv)
print(len(sys.argv))
if len(sys.argv) >= 4:
    cmd = sys.argv[1]
    file = sys.argv[2]
    city = sys.argv[3]
    if len(sys.argv) == 5:
        country = sys.argv[4]
else:
    print("""USAGE:
    export_openweather.py --csv filename [<город>] [Country]
    export_openweather.py --json filename [<город>] [Country]
    export_openweather.py --html filename [<город>] [Country]
    
    example:
        export_openweather.py --csv filename Moskva RU
    """)
    exit(-1)
# ow.get_weather_by_city("Moskva", "RU")
s = ow.get_weather_by_city(city, country)

print('Exporting to', file)
if sys.argv[1] == '--csv':
    print(str(s))
    with open(file,'w') as f:
        output = csv.writer(f)
        output.writerow(ow.db_names)  # header row
        for row in s:
            output.writerow(row.values())
elif sys.argv[1] == '--json':
    print(str(s))
    with open(file, 'w') as f:
        f.write(str(s))
elif sys.argv[1] == '--html':
    print('Under construction.')
    print(str(s))



