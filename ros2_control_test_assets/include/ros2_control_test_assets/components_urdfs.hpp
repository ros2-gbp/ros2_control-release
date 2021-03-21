// Copyright (c) 2021 Stogl Robotics Consulting
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef ROS2_CONTROL_TEST_ASSETS__COMPONENTS_URDFS_HPP_
#define ROS2_CONTROL_TEST_ASSETS__COMPONENTS_URDFS_HPP_

#include <string>

namespace ros2_control_test_assets
{

// 1. Industrial Robots with only one interface
const auto valid_urdf_ros2_control_system_one_interface =
  R"(
  <ros2_control name="RRBotSystemPositionOnly" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/RRBotSystemPositionOnlyHardware</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
  </ros2_control>
)";

// 2. Industrial Robots with multiple interfaces (cannot be written at the same time)
// Note, joint parameters can be any string
const auto valid_urdf_ros2_control_system_multi_interface =
  R"(
  <ros2_control name="RRBotSystemMultiInterface" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/RRBotSystemMultiInterfaceHardware</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <command_interface name="velocity">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <command_interface name="effort">
        <param name="min">-0.5</param>
        <param name="max">0.5"</param>
      </command_interface>
      <state_interface name="position"/>
      <state_interface name="velocity"/>
      <state_interface name="effort"/>
    </joint>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
      <state_interface name="velocity"/>
      <state_interface name="effort"/>
    </joint>
  </ros2_control>
)";

// 3. Industrial Robots with integrated sensor
const auto valid_urdf_ros2_control_system_robot_with_sensor =
  R"(
  <ros2_control name="RRBotSystemWithSensor" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/RRBotSystemWithSensorHardware</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <sensor name="tcp_fts_sensor">
      <state_interface name="fx"/>
      <state_interface name="fy"/>
      <state_interface name="fz"/>
      <state_interface name="tx"/>
      <state_interface name="ty"/>
      <state_interface name="tz"/>
      <param name="frame_id">kuka_tcp</param>
      <param name="lower_limits">-100</param>
      <param name="upper_limits">100</param>
    </sensor>
  </ros2_control>
)";

// 4. Industrial Robots with externally connected sensor
const auto valid_urdf_ros2_control_system_robot_with_external_sensor =
  R"(
  <ros2_control name="RRBotSystemPositionOnlyWithExternalSensor" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/RRBotSystemPositionOnlyHardware</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
  </ros2_control>
  <ros2_control name="RRBotForceTorqueSensor2D" type="sensor">
    <hardware>
      <plugin>ros2_control_demo_hardware/ForceTorqueSensor2DHardware</plugin>
      <param name="example_param_read_for_sec">0.43</param>
    </hardware>
    <sensor name="tcp_fts_sensor">
      <state_interface name="fx"/>
      <state_interface name="fy"/>
      <state_interface name="fz"/>
      <state_interface name="tx"/>
      <state_interface name="ty"/>
      <state_interface name="tz"/>
      <param name="frame_id">kuka_tcp</param>
      <param name="lower_limits">-100</param>
      <param name="upper_limits">100</param>
    </sensor>
  </ros2_control>
)";

// 5. Modular Robots with separate communication to each actuator
const auto valid_urdf_ros2_control_actuator_modular_robot =
  R"(
  <ros2_control name="RRBotModularJoint1"  type="actuator">
    <hardware>
      <plugin>ros2_control_demo_hardware/PositionActuatorHardware</plugin>
      <param name="example_param_write_for_sec">1.23</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
  </ros2_control>
  <ros2_control name="RRBotModularJoint2"  type="actuator">
    <hardware>
      <plugin>ros2_control_demo_hardware/PositionActuatorHardware</plugin>
      <param name="example_param_write_for_sec">1.23</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
  </ros2_control>
)";

// 6. Modular Robots with actuators not providing states and with additional sensors
// Example for simple transmission
const auto valid_urdf_ros2_control_actuator_modular_robot_sensors =
  R"(
  <ros2_control name="RRBotModularJoint1" type="actuator">
    <hardware>
      <plugin>ros2_control_demo_hardware/VelocityActuatorHardware</plugin>
      <param name="example_param_write_for_sec">1.23</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="velocity">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="velocity"/>
    </joint>
    <transmission name="transmission1">
      <plugin>transmission_interface/SimpleTansmission</plugin>
      <param name="joint_to_actuator">${1024/PI}</param>
    </transmission>
  </ros2_control>
  <ros2_control name="RRBotModularJoint2" type="actuator">
    <hardware>
      <plugin>ros2_control_demo_hardware/VelocityActuatorHardware</plugin>
      <param name="example_param_write_for_sec">1.23</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="joint2">
      <command_interface name="velocity">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="velocity"/>
    </joint>
  </ros2_control>
  <ros2_control name="RRBotModularPositionSensorJoint1" type="sensor">
    <hardware>
      <plugin>ros2_control_demo_hardware/PositionSensorHardware</plugin>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <state_interface name="position"/>
    </joint>
  </ros2_control>
  <ros2_control name="RRBotModularPositionSensorJoint2" type="sensor">
    <hardware>
      <plugin>ros2_control_demo_hardware/PositionSensorHardware</plugin>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint2">
      <state_interface name="position"/>
    </joint>
  </ros2_control>
)";

// 7. Modular Robots with separate communication to each "actuator" with multi joints
// Example for complex transmission (multi-joint/multi-actuator) - (system component is used)
const auto valid_urdf_ros2_control_system_muti_joints_transmission =
  R"(
  <ros2_control name="RRBotModularWrist" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/ActuatorHardwareMultiDOF</plugin>
      <param name="example_param_write_for_sec">1.23</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <transmission name="transmission1">
      <plugin>transmission_interface/SomeComplex2by2Transmission</plugin>
      <param name="joints">{joint1, joint2}</param>
      <param name="output">{output2, output2}</param>
      <param name="joint1_output1">1.5</param>
      <param name="joint1_output2">3.2</param>
      <param name="joint2_output1">3.1</param>
      <param name="joint2_output2">1.4</param>
    </transmission>
  </ros2_control>
)";

// 8. Sensor only
const auto valid_urdf_ros2_control_sensor_only =
  R"(
  <ros2_control name="CameraWithIMU" type="sensor">
    <hardware>
      <plugin>ros2_control_demo_hardware/CameraWithIMUSensor</plugin>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <sensor name="sensor1">
      <state_interface name="roll"/>
      <state_interface name="pitch"/>
      <state_interface name="yaw"/>
    </sensor>
    <sensor name="sensor2">
      <state_interface name="image"/>
    </sensor>
  </ros2_control>
)";

// 9. Actuator Only
const auto valid_urdf_ros2_control_actuator_only =
  R"(
  <ros2_control name="ActuatorModularJoint1" type="actuator">
    <hardware>
      <plugin>ros2_control_demo_hardware/VelocityActuatorHardware</plugin>
      <param name="example_param_write_for_sec">1.13</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="velocity">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="velocity"/>
    </joint>
    <transmission name="transmission1">
      <plugin>transmission_interface/RotationToLinerTansmission</plugin>
      <param name="joint_to_actuator">${1024/PI}</param>
    </transmission>
  </ros2_control>
)";

// Errors
const auto invalid_urdf_ros2_control_invalid_child =
  R"(
  <ros2_control name="2DOF_System_Robot_Position_Only" type="system">
    <hardwarert>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardwarert>
  </ros2_control>
  )";

const auto invalid_urdf_ros2_control_missing_attribute =
  R"(
  <ros2_control type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
  </ros2_control>
  )";

const auto invalid_urdf_ros2_control_component_missing_class_type =
  R"(
  <ros2_control name="2DOF_System_Robot_Position_Only" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <param name="min_position_value">-1</param>
      <param name="max_position_value">1</param>
    </joint>
  </ros2_control>
)";

const auto invalid_urdf_ros2_control_parameter_missing_name =
  R"(
  <ros2_control name="2DOF_System_Robot_Position_Only" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param>2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <plugin>ros2_control_components/PositionJoint</plugin>
      <param name="min_position_value">-1</param>
      <param name="max_position_value">1</param>
    </joint>
  </ros2_control>
)";


const auto invalid_urdf_ros2_control_component_class_type_empty =
  R"(
  <ros2_control name="2DOF_System_Robot_Position_Only" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <plugin></plugin>
      <param name="min_position_value">-1</param>
      <param name="max_position_value">1</param>
    </joint>
  </ros2_control>
)";

const auto invalid_urdf_ros2_control_component_interface_type_empty =
  R"(
  <ros2_control name="2DOF_System_Robot_Position_Only" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <plugin>ros2_control_components/PositionJoint</plugin>
      <state_interface></state_interface>
      <param name="min_position_value">-1</param>
      <param name="max_position_value">1</param>
    </joint>
  </ros2_control>
)";

const auto invalid_urdf_ros2_control_parameter_empty =
  R"(
  <ros2_control name="2DOF_System_Robot_Position_Only" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/2DOF_System_Hardware_Position_Only</plugin>
      <param name="example_param_write_for_sec"></param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min_position_value">-1</param>
        <param name="max_position_value">1</param>
      </command_interface>
    </joint>
  </ros2_control>
)";

}  // namespace ros2_control_test_assets

#endif  // ROS2_CONTROL_TEST_ASSETS__COMPONENTS_URDFS_HPP_
