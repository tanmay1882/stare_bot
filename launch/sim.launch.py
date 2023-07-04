import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = "stare_bot"
    
    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),"launch","robot.launch.py")]),
        launch_arguments={"use_sim_time":"true"}.items())
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")]))
    
    spawnner = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic","robot_description","-entity","stare_bot"],
        output="screen")
    
    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        spawnner
    ])