1)Save the weather.msg file inside the msg folder of the package.

2)In the CMakeLists.txt, add the file name (weather.msg) to the add_message_files section:

cmake
Copy code
add_message_files(
   FILES
   weather.msg
)
3)Copy the weather_publisher.py and weather_subscriber.py files to our workspace.

4)Make the scripts executable -> chmod +x weather_publisher.py weather_subscriber.py

5)Build the workspace using catkin_make.

6)Start ROS with roscore.

7)First, run the weather_publisher.py file, then in another terminal, run the weather_subscriber.py file.

7)In the terminal where weather_publisher.py is running, enter the name of a city. (You can enter the name of any city worldwide.)

8)Received data -> Country information, City information, Temperature information, Weather condition information, Date and Time information.
