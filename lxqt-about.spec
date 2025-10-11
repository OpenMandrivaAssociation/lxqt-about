#define git 0
Name: lxqt-about
Version: 2.2.0
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-about/releases/download/%{version}/lxqt-about-%{version}.tar.xz
%endif
Release: %{?git:0.%{git}.}2
Summary: About application for the LXQt desktop
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
Obsoletes: lxqt-l10n < %{EVRD}

%description
About application for the LXQt desktop.

%prep
%autosetup -p1 -n %{name}-%{?git:%{git}}%{!?git:%{version}}

%cmake -DPULL_TRANSLATIONS=NO -G Ninja

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
