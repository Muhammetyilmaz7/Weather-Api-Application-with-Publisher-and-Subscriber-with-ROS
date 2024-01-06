#!/usr/bin/env python3
import rospy
from ros_essentials_cpp.msg import weather

def weather_callback(weather_message):
    rospy.loginfo("new Weather data received: (%s, %s, %s ,%s, %s)", 
        weather_message.ulke,weather_message.sehir,
        weather_message.sicaklik,weather_message.durum, weather_message.tarih_saat)


rospy.init_node('weather_subscriber_node', anonymous=True)

rospy.Subscriber("weather_topic", weather, weather_callback)
rospy.spin()