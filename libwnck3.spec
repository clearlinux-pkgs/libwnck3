#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwnck3
Version  : 3.32.0
Release  : 16
URL      : https://download.gnome.org/sources/libwnck/3.32/libwnck-3.32.0.tar.xz
Source0  : https://download.gnome.org/sources/libwnck/3.32/libwnck-3.32.0.tar.xz
Summary  : Library to manage X windows and workspaces (via pagers, tasklists, etc.)
Group    : Development/Tools
License  : LGPL-2.0
Requires: libwnck3-bin = %{version}-%{release}
Requires: libwnck3-data = %{version}-%{release}
Requires: libwnck3-lib = %{version}-%{release}
Requires: libwnck3-license = %{version}-%{release}
Requires: libwnck3-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cairo-xlib-xrender)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xres)

%description
libwnck
=======
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package bin
Summary: bin components for the libwnck3 package.
Group: Binaries
Requires: libwnck3-data = %{version}-%{release}
Requires: libwnck3-license = %{version}-%{release}

%description bin
bin components for the libwnck3 package.


%package data
Summary: data components for the libwnck3 package.
Group: Data

%description data
data components for the libwnck3 package.


%package dev
Summary: dev components for the libwnck3 package.
Group: Development
Requires: libwnck3-lib = %{version}-%{release}
Requires: libwnck3-bin = %{version}-%{release}
Requires: libwnck3-data = %{version}-%{release}
Provides: libwnck3-devel = %{version}-%{release}
Requires: libwnck3 = %{version}-%{release}

%description dev
dev components for the libwnck3 package.


%package lib
Summary: lib components for the libwnck3 package.
Group: Libraries
Requires: libwnck3-data = %{version}-%{release}
Requires: libwnck3-license = %{version}-%{release}

%description lib
lib components for the libwnck3 package.


%package license
Summary: license components for the libwnck3 package.
Group: Default

%description license
license components for the libwnck3 package.


%package locales
Summary: locales components for the libwnck3 package.
Group: Default

%description locales
locales components for the libwnck3 package.


%prep
%setup -q -n libwnck-3.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557018829
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libwnck3
cp COPYING %{buildroot}/usr/share/package-licenses/libwnck3/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libwnck-3.0
## install_append content
mv %{buildroot}/usr/bin/wnck-urgency-monitor %{buildroot}/usr/bin/wnck-urgency-monitor-3
mv %{buildroot}/usr/bin/wnckprop %{buildroot}/usr/bin/wnckprop-3
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wnck-urgency-monitor-3
/usr/bin/wnckprop-3

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Wnck-3.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libwnck-3.0/libwnck/application.h
/usr/include/libwnck-3.0/libwnck/class-group.h
/usr/include/libwnck-3.0/libwnck/libwnck.h
/usr/include/libwnck-3.0/libwnck/pager.h
/usr/include/libwnck-3.0/libwnck/screen.h
/usr/include/libwnck-3.0/libwnck/selector.h
/usr/include/libwnck-3.0/libwnck/tasklist.h
/usr/include/libwnck-3.0/libwnck/util.h
/usr/include/libwnck-3.0/libwnck/version.h
/usr/include/libwnck-3.0/libwnck/window-action-menu.h
/usr/include/libwnck-3.0/libwnck/window.h
/usr/include/libwnck-3.0/libwnck/wnck-enum-types.h
/usr/include/libwnck-3.0/libwnck/workspace.h
/usr/lib64/libwnck-3.so
/usr/lib64/pkgconfig/libwnck-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwnck-3.so.0
/usr/lib64/libwnck-3.so.0.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwnck3/COPYING

%files locales -f libwnck-3.0.lang
%defattr(-,root,root,-)

