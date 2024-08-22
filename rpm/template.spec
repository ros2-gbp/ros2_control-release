%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rqt-controller-manager
Version:        2.43.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_controller_manager package

License:        Apache License 2.0
URL:            http://ros.org/wiki/rqt_controller_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-controller-manager
Requires:       ros-humble-controller-manager-msgs
Requires:       ros-humble-rclpy
Requires:       ros-humble-rqt-gui
Requires:       ros-humble-rqt-gui-py
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Graphical frontend for interacting with the controller manager.

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

