###  Filtering of Lidar (laserscan) data for the angles 0-120 deg of a custom-defined robot in Rviz and Gazebo with Lidar and camera plugin controlled with teleoperation.

## Discription: 
The main additions to this repo are main a launch file (which visualizes the robot in a custom gazebo and rviz configurations) and a Python file named reading_laser reposible for reading the laser scan topic and filtering it only for DEG 0-120.

# How to use it:

1. Clone the repo
2. Run the primary launch file, i.e., main using the command: ros2 launch bot_description main.launch
3. This will open a Gazebo and Rviz in custom configuration.
4. Then run the Python file reading_laser using the command: python3 reading_laser.py
5. The intended visualization of laser scan data being filtered for 0-120 deg can be seen in rviz.

# Screen shot & Video:

![Screenshot from 2024-06-04 13-31-06](https://github.com/AjayAdit/ajay_adit_ws_2/assets/62584240/0bcfee8c-5ab6-4c75-931e-502468f5476c)


![Screenshot from 2024-06-04 13-30-09](https://github.com/AjayAdit/ajay_adit_ws_2/assets/62584240/f5042fad-645d-442a-b767-897444ed5108)


[Screencast from 06-04-2024 12:05:10 PM.webm](https://github.com/AjayAdit/ajay_adit_ws_2/assets/62584240/0a582d8b-3673-4c4d-8865-4656ade3ff34)





    
    
    
