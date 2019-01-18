#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : x11perf
Version  : 1.6.0
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/app/x11perf-1.6.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/x11perf-1.6.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : HPND
Requires: x11perf-bin
Requires: x11perf-doc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xft)
BuildRequires : pkgconfig(xmuu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xrender)

%description
All questions regarding this software should be directed at the
Xorg mailing list:

%package bin
Summary: bin components for the x11perf package.
Group: Binaries

%description bin
bin components for the x11perf package.


%package doc
Summary: doc components for the x11perf package.
Group: Documentation

%description doc
doc components for the x11perf package.


%prep
cd ..
%setup -q -n x11perf-1.6.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/X11/x11perfcomp/Xmark
/usr/lib64/X11/x11perfcomp/fillblnk
/usr/lib64/X11/x11perfcomp/perfboth
/usr/lib64/X11/x11perfcomp/perfratio

%files bin
%defattr(-,root,root,-)
/usr/bin/x11perf
/usr/bin/x11perfcomp

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
