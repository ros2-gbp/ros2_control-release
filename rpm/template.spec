%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2controlcli
Version:        4.28.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2controlcli package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-pygraphviz
Requires:       ros-rolling-controller-manager
Requires:       ros-rolling-controller-manager-msgs
Requires:       ros-rolling-rcl-interfaces
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-ros2cli
Requires:       ros-rolling-ros2node
Requires:       ros-rolling-ros2param
Requires:       ros-rolling-rosidl-runtime-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-controller-manager
BuildRequires:  ros-rolling-controller-manager-msgs
BuildRequires:  ros-rolling-rcl-interfaces
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ros2cli
BuildRequires:  ros-rolling-ros2node
BuildRequires:  ros-rolling-ros2param
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The ROS 2 command line tools for ros2_control.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Apr 17 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.28.1-1
- Autogenerated by Bloom

* Thu Apr 10 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.28.0-1
- Autogenerated by Bloom

* Sat Mar 01 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.27.0-1
- Autogenerated by Bloom

* Fri Feb 07 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.26.0-1
- Autogenerated by Bloom

* Wed Jan 29 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.25.0-1
- Autogenerated by Bloom

* Mon Jan 13 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.24.0-1
- Autogenerated by Bloom

* Sun Dec 29 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.23.0-1
- Autogenerated by Bloom

* Fri Dec 20 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.22.0-1
- Autogenerated by Bloom

* Fri Dec 06 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.21.0-1
- Autogenerated by Bloom

* Fri Nov 08 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.20.0-1
- Autogenerated by Bloom

* Sat Oct 26 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.19.0-1
- Autogenerated by Bloom

* Mon Oct 07 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.18.0-1
- Autogenerated by Bloom

* Wed Sep 11 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.17.0-1
- Autogenerated by Bloom

* Sat Aug 24 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.16.1-1
- Autogenerated by Bloom

* Thu Aug 22 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.16.0-1
- Autogenerated by Bloom

* Mon Aug 05 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.15.0-1
- Autogenerated by Bloom

* Tue Jul 23 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.14.0-1
- Autogenerated by Bloom

* Mon Jul 08 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.13.0-1
- Autogenerated by Bloom

* Mon Jul 01 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.12.0-1
- Autogenerated by Bloom

* Tue May 14 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.11.0-1
- Autogenerated by Bloom

* Wed May 08 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.10.0-1
- Autogenerated by Bloom

* Tue Apr 30 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.9.0-1
- Autogenerated by Bloom

* Wed Mar 27 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.8.0-1
- Autogenerated by Bloom

* Fri Mar 22 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.7.0-1
- Autogenerated by Bloom

* Wed Mar 13 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.6.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.5.0-2
- Autogenerated by Bloom

