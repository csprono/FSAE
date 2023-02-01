import os
import yaml
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
   config = os.path.join(
      get_package_share_directory('EBS'),
      'config',
      'ebs_config.yaml'
      )
   
   with open(config, 'r') as f:
      params = yaml.safe_load(f)
   print(params)   

   return LaunchDescription([
      Node(
         package='EBS',
         executable='ebs_node',
         name='ebs',
         namespace='namespace',
         parameters=[params]
      )
   ])
