%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ros2controlcli
Version:        2.50.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2controlcli package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-pygraphviz
Requires:       ros-humble-controller-manager
Requires:       ros-humble-controller-manager-msgs
Requires:       ros-humble-rcl-interfaces
Requires:       ros-humble-rclpy
Requires:       ros-humble-ros2cli
Requires:       ros-humble-ros2node
Requires:       ros-humble-ros2param
Requires:       ros-humble-rosidl-runtime-py
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-controller-manager
BuildRequires:  ros-humble-controller-manager-msgs
BuildRequires:  ros-humble-rcl-interfaces
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-ros2cli
BuildRequires:  ros-humble-ros2node
BuildRequires:  ros-humble-ros2param
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
BuildRequires:  ros-humble-ament-xmllint
%endif

%description
The ROS 2 command line tools for ROS2 Control.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu Apr 10 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.50.0-1
- Autogenerated by Bloom

* Tue Mar 18 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.49.0-1
- Autogenerated by Bloom

* Fri Feb 07 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.48.0-1
- Autogenerated by Bloom

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

* Thu Jan 25 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.38.0-1
- Autogenerated by Bloom

* Sat Jan 20 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.37.0-1
- Autogenerated by Bloom

* Mon Jan 08 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.36.1-1
- Autogenerated by Bloom

* Tue Dec 12 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.36.0-1
- Autogenerated by Bloom

* Mon Nov 27 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.35.1-1
- Autogenerated by Bloom

* Tue Nov 14 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.35.0-1
- Autogenerated by Bloom

* Wed Nov 08 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.34.0-1
- Autogenerated by Bloom

* Wed Oct 11 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.33.0-1
- Autogenerated by Bloom

* Tue Oct 03 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.32.0-1
- Autogenerated by Bloom

* Mon Sep 11 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.31.0-1
- Autogenerated by Bloom

* Mon Aug 14 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.30.0-1
- Autogenerated by Bloom

* Sun Jul 09 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.29.0-1
- Autogenerated by Bloom

* Fri Jun 23 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.28.0-1
- Autogenerated by Bloom

* Wed Jun 14 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.27.0-1
- Autogenerated by Bloom

* Sat May 20 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.26.0-1
- Autogenerated by Bloom

* Sat Apr 29 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.25.3-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.25.2-1
- Autogenerated by Bloom

* Fri Apr 14 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.25.1-1
- Autogenerated by Bloom

* Sun Apr 02 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.25.0-1
- Autogenerated by Bloom

* Thu Mar 09 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.24.1-1
- Autogenerated by Bloom

* Tue Feb 28 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.24.0-1
- Autogenerated by Bloom

* Mon Feb 20 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.23.0-1
- Autogenerated by Bloom

* Tue Jan 31 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.22.0-1
- Autogenerated by Bloom

* Tue Jan 24 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.21.0-1
- Autogenerated by Bloom

* Thu Jan 12 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.20.0-1
- Autogenerated by Bloom

* Fri Jan 06 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.19.0-1
- Autogenerated by Bloom

* Sat Dec 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.18.0-1
- Autogenerated by Bloom

* Sun Nov 27 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.17.0-1
- Autogenerated by Bloom

* Mon Oct 17 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.16.0-1
- Autogenerated by Bloom

* Mon Sep 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.15.0-1
- Autogenerated by Bloom

* Wed Aug 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.13.0-1
- Autogenerated by Bloom

* Thu Jul 14 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.1-1
- Autogenerated by Bloom

* Sat Jul 09 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.0-1
- Autogenerated by Bloom

* Sun Jul 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.11.0-1
- Autogenerated by Bloom

* Sat Jun 18 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.10.0-1
- Autogenerated by Bloom

* Thu May 19 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.9.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.5.0-2
- Autogenerated by Bloom

* Fri Mar 25 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.5.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.4.0-1
- Autogenerated by Bloom

* Fri Feb 18 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.3.0-1
- Autogenerated by Bloom

* Wed Feb 09 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.1.0-3
- Autogenerated by Bloom

