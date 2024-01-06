#!/usr/bin/env python

import rospy
from ros_essentials_cpp.msg import weather
from datetime import datetime, timedelta
import requests

def hava_durumu(api_key, sehir):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': sehir,
        'appid': api_key,
        'units': 'metric',
        'lang': 'tr'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
		
        hava_durumu_bilgisi = {
            'ulke': data['sys']['country'],
            'sehir': data['name'],
            'sıcaklık': data['main']['temp'],
            'durum': hava_durumu_durumlar.get(data['weather'][0]['description'], data['weather'][0]['description']),
            'tarih_saat': (datetime.utcfromtimestamp(data['dt']) + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
        }
        return hava_durumu_bilgisi

    except requests.exceptions.HTTPError as errh:
        rospy.logerr(f"HTTP Hatası: {errh}")
    except requests.exceptions.ConnectionError as errc:
        rospy.logerr(f"Bağlantı Hatası: {errc}")
    except requests.exceptions.Timeout as errt:
        rospy.logerr(f"Zaman Aşımı Hatası: {errt}")
    except requests.exceptions.RequestException as err:
        rospy.logerr(f"Diğer Hata: {err}")

    return None

# Hava durumu durumlarını Türkçe'ye çevirmek için bir sözlük
hava_durumu_durumlar = {
    'Thunderstorm': 'Firtina',
    'Drizzle': 'Cisenti',
    'Rain': 'Yagmur',
    'Snow': 'Kar',
    'Mist': 'Sis',
    'Clear': 'Acik',
    'Clouds': 'Bulutlu',
    'Fog': 'Sisli',
    'Haze': 'Hafif Sis',
    'Smoke': 'Dumanli',
    'Dust': 'Tozlu',
    'Sand': 'Kumlu',
    'Ash': 'Kül',
    'Squall': 'Siddetli Firtina',
    'Tornado': 'Tornado'
}

def publisher():
    rospy.init_node('hava_durumu_publisher', anonymous=True)
    pub = rospy.Publisher('weather_topic', weather, queue_size=10)

    api_key = '068e9069278b7209164e650fd0849292'
    sehir = input("Şehir giriniz:")

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        hava_durumu_bilgisi = hava_durumu(api_key, sehir)
        
        weather_info = weather()
        weather_info.ulke = f"{hava_durumu_bilgisi['ulke']}"
        weather_info.sehir = f"{hava_durumu_bilgisi['sehir']}"
        weather_info.sicaklik = f"{hava_durumu_bilgisi['sıcaklık']}"
        weather_info.durum = f"{hava_durumu_bilgisi['durum']}"
        weather_info.tarih_saat = f"{hava_durumu_bilgisi['tarih_saat']}"
        print("New weather data sent: ("+f"{hava_durumu_bilgisi['ulke']}"+", "+f"{hava_durumu_bilgisi['sehir']}"+", "+f"{hava_durumu_bilgisi['sıcaklık']}"+", "+f"{hava_durumu_bilgisi['durum']}"+", "+f"{hava_durumu_bilgisi['tarih_saat']}"+")")
        pub.publish(weather_info)

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass