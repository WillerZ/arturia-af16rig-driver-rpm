#
# SPDX-FileCopyrightText: 2026 Phil Willoughby <willerz@gmail.com>
# SPDX-License-Identifier: GPL-2.0
#

%if 0%{?fedora}
%global buildforkernels akmod
%endif
%global debug_package %{nil}
%global _kmodtool_zipmodules 0

Name:          arturia-af16rig-driver
Epoch:         1
Version:       0.0.1
# Taken over by kmodtool
Release:       1%{?dist}
Summary:       Unofficial Arturia AudioFuse 16Rig driver kernel module
License:       GPLv2 and MIT
URL:           https://github.com/WillerZ/arturia-af16rig-driver

Source:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

# get the needed BuildRequires (in parts depending on what we build for)
%global AkmodsBuildRequires %{_bindir}/kmodtool, gcc-c++, elfutils-libelf-devel
BuildRequires:  %{AkmodsBuildRequires}

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }
# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name}  %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
The unofficial Arturia AudioFuse 16Rig kernel driver module version %{version} for kernel %{kversion}.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}
# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null
%setup -q -c
# patch loop

for kernel_version  in %{?kernel_versions} ; do
    cp -a arturia-af16rig-driver-%{version} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
  pushd _kmod_build_${kernel_version%%___*}
    %make_build \
    KDIR=/lib/modules/""${kernel_version%%___*}""/build \
	KERNEL_UNAME="${kernel_version%%___*}" SYSSRC="${kernel_version##*___}" \
	IGNORE_CC_MISMATCH=1 IGNORE_XEN_PRESENCE=1 IGNORE_PREEMPT_RT_PRESENCE=1 \
	modules
  popd
done


%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p  %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -D -m 0755 _kmod_build_${kernel_version%%___*}/build/*.ko \
         %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Mon Mar 16 2026 Phil Willoughby <willerz@gmail.com> - 1:0.0.1
- First attempt
