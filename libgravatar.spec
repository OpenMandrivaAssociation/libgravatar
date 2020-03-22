%define major 5
%define libname %mklibname KF5Gravatar %{major}
%define devname %mklibname KF5Gravatar -d

Name: libgravatar
Version:	20.03.80
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for Gravatar support
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(KF5PimCommon)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: boost-devel

%description
KDE library for Gravatar support.

%package -n %{libname}
Summary: KDE library for Gravatar support
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for Gravatar support.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/libgravatar.categories
%{_datadir}/qlogging-categories5/libgravatar.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
