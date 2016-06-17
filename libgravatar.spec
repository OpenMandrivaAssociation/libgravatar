%define major 5
%define libname %mklibname KF5Gravatar %{major}
%define devname %mklibname KF5Gravatar -d

Name: libgravatar
Version:	16.04.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for Gravatar support
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(KF5PimCommon)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Gpgmepp)

%description
KDE library for Gravatar support

%package -n %{libname}
Summary: KDE library for Gravatar support
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for Gravatar support

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
cd ../
%ninja -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/libgravatar.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri