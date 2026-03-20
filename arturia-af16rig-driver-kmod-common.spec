#
# SPDX-FileCopyrightText: 2026 Phil Willoughby <willerz@gmail.com>
# SPDX-License-Identifier: GPL-2.0
#

%if 0%{?fedora}
%global buildforkernels akmod
%endif
%global debug_package %{nil}
%global _kmodtool_zipmodules 0

Name:          arturia-af16rig-driver-kmod-common
Epoch:         1
Version:       0.0.2
Release:       1%{?dist}
Summary:       Unofficial Arturia AudioFuse 16Rig driver kernel module common package
License:       GPLv2 and MIT
URL:           https://github.com/WillerZ/arturia-af16rig-driver

%description
This package has no content and exists only because kmodtool requires that it exists.

%install
rm -rf %{buildroot}
# _datadir is typically /usr/share/
install -d -m 0755 %{buildroot}/%{_datadir}/arturia-af16rig-driver-kmod-common/
echo "This package has no content and exists only because kmodtool requires that it exists." > %{buildroot}/%{_datadir}/arturia-af16rig-driver-kmod-common/README

%files
%{_datadir}/arturia-af16rig-driver-kmod-common/README

%changelog
* Mon Mar 16 2026 Phil Willoughby <willerz@gmail.com> - 1:0.0.2
- Version changed

* Mon Mar 16 2026 Phil Willoughby <willerz@gmail.com> - 1:0.0.1
- First attempt
