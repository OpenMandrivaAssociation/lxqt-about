%define git 0
Name: lxqt-about
Version: 1.2.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 3
Source0: https://github.com/lxqt/lxqt-about/releases/download/%{version}/lxqt-about-%{version}.tar.xz
%endif
Summary: About application for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5LinguistTools)
Obsoletes: lxqt-l10n < %{EVRD}
%rename	razorqt-about

%description
About application for the LXQt desktop.

%prep
%if %git
%autosetup -p1 -n %{name}-%{git}
%else
%autosetup -p1
%endif

%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/lxqt-about
%{_datadir}/applications/lxqt-about.desktop
%{_datadir}/icons/hicolor/scalable/apps/lxqt-about.svg
