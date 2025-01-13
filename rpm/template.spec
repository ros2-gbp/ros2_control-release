%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2-control
Version:        4.24.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_control package

License:        Apache License 2.0
URL:            https://control.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-controller-interface
Requires:       ros-rolling-controller-manager
Requires:       ros-rolling-controller-manager-msgs
Requires:       ros-rolling-hardware-interface
Requires:       ros-rolling-joint-limits
Requires:       ros-rolling-ros2-control-test-assets
Requires:       ros-rolling-ros2controlcli
Requires:       ros-rolling-transmission-interface
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Metapackage for ROS2 control related packages

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

