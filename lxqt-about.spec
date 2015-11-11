%define git 0
Name: lxqt-about
Version: 0.10.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://github.com/lxde/%{name}/archive/%{version}.tar.gz
%endif
Summary: About application for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5LinguistTools)
%rename	razorqt-about

%description
About application for the LXQt desktop.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%cmake_qt5

%build
%make -C build

%install
%makeinstall_std -C build
%find_lang lxqt-about --with-qt

%files -f lxqt-about.lang
%{_bindir}/lxqt-about
%{_datadir}/applications/lxqt-about.desktop
%dir %{_datadir}/lxqt/translations/lxqt-about
