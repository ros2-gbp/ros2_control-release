%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-hardware-interface-testing
Version:        2.47.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS hardware_interface_testing package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-control-msgs
Requires:       ros-humble-hardware-interface
Requires:       ros-humble-lifecycle-msgs
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp-lifecycle
Requires:       ros-humble-ros2-control-test-assets
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-control-msgs
BuildRequires:  ros-humble-hardware-interface
BuildRequires:  ros-humble-lifecycle-msgs
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp-lifecycle
BuildRequires:  ros-humble-ros2-control-test-assets
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gmock
%endif

%description
ros2_control hardware interface testing

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Dec 31 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.47.0-1
- Autogenerated by Bloom

* Mon Dec 16 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.46.0-1
- Autogenerated by Bloom

* Tue Dec 03 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.45.0-1
- Autogenerated by Bloom

* Sat Nov 09 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.44.0-1
- Autogenerated by Bloom

* Wed Sep 11 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.43.1-1
- Autogenerated by Bloom

* Thu Aug 22 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.43.0-1
- Autogenerated by Bloom

* Tue Jul 23 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.42.0-1
- Autogenerated by Bloom

* Tue Apr 30 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.41.0-1
- Autogenerated by Bloom

* Sat Mar 02 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.40.0-1
- Autogenerated by Bloom

* Wed Feb 14 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.39.1-1
- Autogenerated by Bloom

* Mon Feb 12 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.39.0-1
- Autogenerated by Bloom

