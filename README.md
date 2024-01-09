# ROS Weather Data Publishing and Subscription Package

This ROS package facilitates weather data publishing and subscription, allowing users to receive real-time weather information for a specified city.

## Installation

1. **Save the Message File:**
   - Save the `weather.msg` file inside the `msg` folder of the package.

2. **Update CMakeLists.txt:**
   - In the `CMakeLists.txt` file, add the file name (`weather.msg`) to the `add_message_files` section:

     ```cmake
     add_message_files(
        FILES
        weather.msg
     )
     ```

3. **Copy Python Script Files:**
   - Copy the `weather_publisher.py` and `weather_subscriber.py` files to your ROS workspace.

4. **Make Scripts Executable:**
   - Make the script files executable using the following commands:

     ```bash
     chmod +x weather_publisher.py weather_subscriber.py
     ```

5. **Build the Workspace:**
   - Build your workspace using the `catkin_make` command.

     ```bash
     catkin_make
     ```

## Usage

1. **Start ROS:**
   - Start ROS by running the following command:

     ```bash
     roscore
     ```

2. **Run the Publisher:**
   - In one terminal, run the `weather_publisher.py` file:

     ```bash
     ./weather_publisher.py
     ```

3. **Run the Subscriber:**
   - In another terminal, run the `weather_subscriber.py` file:

     ```bash
     ./weather_subscriber.py
     ```

4. **Enter City Name:**
   - In the terminal where `weather_publisher.py` is running, enter the name of a city when prompted. You can enter the name of any city worldwide.

5. **View Received Data:**
   - Observe the received data in the terminal where `weather_subscriber.py` is running. The data will include Country information, City information, Temperature information, Weather condition information, Date, and Time information.

Feel free to contribute, provide feedback, or report issues. Contributions are welcomed through pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
