%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-controller-manager
Version:        3.10.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS controller_manager package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ament-index-cpp
Requires:       ros-rolling-backward-ros
Requires:       ros-rolling-controller-interface
Requires:       ros-rolling-controller-manager-msgs
Requires:       ros-rolling-diagnostic-updater
Requires:       ros-rolling-hardware-interface
Requires:       ros-rolling-launch
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-pluginlib
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-realtime-tools
Requires:       ros-rolling-ros2-control-test-assets
Requires:       ros-rolling-ros2param
Requires:       ros-rolling-ros2run
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-python
BuildRequires:  ros-rolling-ament-index-cpp
BuildRequires:  ros-rolling-backward-ros
BuildRequires:  ros-rolling-controller-interface
BuildRequires:  ros-rolling-controller-manager-msgs
BuildRequires:  ros-rolling-diagnostic-updater
BuildRequires:  ros-rolling-hardware-interface
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-pluginlib
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-realtime-tools
BuildRequires:  ros-rolling-ros2-control-test-assets
BuildRequires:  ros-rolling-ros2param
BuildRequires:  ros-rolling-ros2run
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gmock
%endif

%description
Description of controller_manager

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
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
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Mar 16 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.10.0-1
- Autogenerated by Bloom

* Thu Mar 09 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.9.1-1
- Autogenerated by Bloom

* Tue Feb 28 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.9.0-2
- Autogenerated by Bloom

* Tue Feb 28 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.9.0-1
- Autogenerated by Bloom

* Fri Feb 10 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.8.0-1
- Autogenerated by Bloom

* Tue Jan 24 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.7.0-1
- Autogenerated by Bloom

* Thu Jan 12 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.6.0-1
- Autogenerated by Bloom

* Fri Jan 06 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.5.1-1
- Autogenerated by Bloom

* Tue Dec 06 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.5.0-1
- Autogenerated by Bloom

* Sun Nov 27 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.4.0-1
- Autogenerated by Bloom

* Sun Nov 27 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.3.0-2
- Autogenerated by Bloom

* Tue Nov 15 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.3.0-1
- Autogenerated by Bloom

* Sat Oct 15 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.2.0-1
- Autogenerated by Bloom

* Wed Oct 05 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.1.0-1
- Autogenerated by Bloom

* Mon Sep 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.0.0-1
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

* Sat Jun 18 2022 karsten <karsten@osrfoundation.org> - 2.10.0-1
- Autogenerated by Bloom

* Thu May 19 2022 karsten <karsten@osrfoundation.org> - 2.9.0-1
- Autogenerated by Bloom

* Fri May 13 2022 karsten <karsten@osrfoundation.org> - 2.8.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 karsten <karsten@osrfoundation.org> - 2.7.0-1
- Autogenerated by Bloom

* Wed Apr 20 2022 karsten <karsten@osrfoundation.org> - 2.6.0-1
- Autogenerated by Bloom

* Fri Mar 25 2022 karsten <karsten@osrfoundation.org> - 2.5.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 karsten <karsten@osrfoundation.org> - 2.4.0-1
- Autogenerated by Bloom

* Fri Feb 18 2022 karsten <karsten@osrfoundation.org> - 2.3.0-1
- Autogenerated by Bloom

* Wed Feb 09 2022 karsten <karsten@osrfoundation.org> - 2.1.0-3
- Autogenerated by Bloom

