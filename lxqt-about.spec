#define git 0
Name: lxqt-about
Version: 2.2.0
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-about/releases/download/%{version}/lxqt-about-%{version}.tar.xz
%endif
Release: %{?git:0.%{git}.}3
Summary: About application for the LXQt desktop
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildSystem: cmake
BuildOption: -DPULL_TRANSLATIONS:BOOL=OFF
Obsoletes: lxqt-l10n < %{EVRD}

%patchlist
lxqt-about-qt-6.10.patch

%description
About application for the LXQt desktop.

%build -p
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -p
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%files -f %{name}.lang
%{_bindir}/lxqt-about
%{_datadir}/applications/lxqt-about.desktop
%{_datadir}/icons/hicolor/scalable/apps/lxqt-about.svg
