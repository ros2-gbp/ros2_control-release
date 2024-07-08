# Copyright (c) 2021 PAL Robotics S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression

from launch_ros.actions import Node


def generate_load_controller_launch_description(
    controller_name, controller_type=None, controller_params_file=None, extra_spawner_args=[]
):
    """
    Generate launch description for loading a controller using spawner.

    Returns a list of LaunchDescription actions adding the 'controller_manager_name' and
    'unload_on_kill' LaunchArguments and a Node action that runs the controller_manager
    spawner node to load and activate a controller

    Examples # noqa: D416
    --------
      # Assuming the controller type and controller parameters are known to the controller_manager
      generate_load_controller_launch_description('joint_state_broadcaster')

      # Passing controller type and controller parameter file to load
      generate_load_controller_launch_description(
        'joint_state_broadcaster',
        controller_type='joint_state_broadcaster/JointStateBroadcaster',
        controller_params_file=os.path.join(get_package_share_directory('my_pkg'),
                                            'config', 'controller_params.yaml'),
        extra_spawner_args=[--load-only]
        )

    """
    declare_controller_mgr_name = DeclareLaunchArgument(
        "controller_manager_name",
        default_value="controller_manager",
        description="Controller manager node name",
    )
    declare_unload_on_kill = DeclareLaunchArgument(
        "unload_on_kill",
        default_value="false",
        description="Wait until the node is interrupted and then unload controller",
    )

    spawner_arguments = [
        controller_name,
        "--controller-manager",
        LaunchConfiguration("controller_manager_name"),
    ]

    if controller_type:
        warnings.warn(
            "The 'controller_type' argument is deprecated and will be removed in future releases."
            " Declare the controller type parameter in the param file instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        spawner_arguments += ["--controller-type", controller_type]

    if controller_params_file:
        spawner_arguments += ["--param-file", controller_params_file]

    # Setting --unload-on-kill if launch arg unload_on_kill is "true"
    # See https://github.com/ros2/launch/issues/290
    spawner_arguments += [
        PythonExpression(
            [
                '"--unload-on-kill"',
                ' if "true" == "',
                LaunchConfiguration("unload_on_kill"),
                '" else ""',
            ]
        )
    ]

    if extra_spawner_args:
        spawner_arguments += extra_spawner_args

    spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=spawner_arguments,
        shell=True,
        output="screen",
    )

    return LaunchDescription(
        [
            declare_controller_mgr_name,
            declare_unload_on_kill,
            spawner,
        ]
    )
