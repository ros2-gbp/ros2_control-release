%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-transmission-interface
Version:        4.28.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS transmission_interface package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-hardware-interface
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-cmake-gen-version-h
BuildRequires:  ros-jazzy-hardware-interface
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-ros2-control-cmake
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gmock
BuildRequires:  ros-jazzy-ros2-control-test-assets
%endif

%description
data structures for representing mechanical transmissions, methods for
propagating values between actuator and joint spaces and tooling to support
this.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
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

* Fri Apr 19 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.8.0-2
- Autogenerated by Bloom

* Wed Mar 27 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.8.0-1
- Autogenerated by Bloom

* Fri Mar 22 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.7.0-1
- Autogenerated by Bloom

* Wed Mar 13 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.6.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.5.0-2
- Autogenerated by Bloom

