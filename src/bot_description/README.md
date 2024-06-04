# Rviz and Gazebo simulation of lidar data (laser scan) filtered for degrees 0-120 deg

## Discription:
This repo is essentially a feature addition to the previous repo, where a custom-defined robot in Rviz and Gazebo with Lidar and camera plugins was controlled using teleoperation. The new additions to this repo are the launch file main.launch(bot_control) and the Python file reading_laser.py. (The script responsible for filtration of laser scan data for degrees 0-120 deg)

### How to run it:

1. Clone this repo.
2. In the workspace directory, run the launch file with the command  ros2 launch bot_description main.launch 
3. The above command will launch both gazebo and rviz with custom configuration.
4. Next, run the command python3 reading_laser.py in the directory  ajay_adit_ws/src/bot_description/src/.
5. The above file will filter the laser scan data for deg 0-120 in Rviz.

### Screenshot:

![Screenshot from 2024-06-04 13-30-09](https://github.com/AjayAdit/ajay_adit_ws_2/assets/62584240/670b671f-be56-4680-b564-107334094ce0)


![Screenshot from 2024-06-04 13-31-06](https://github.com/AjayAdit/ajay_adit_ws_2/assets/62584240/04a05c23-8c83-4bef-8f64-8428957dce32)



[Screencast from 06-04-2024 12:05:10 PM.webm](https://github.com/AjayAdit/ajay_adit_ws_2/assets/62584240/c747b878-8e63-4d78-8c72-f52967dca220)



