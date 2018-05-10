#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwnck3
Version  : 3.24.1
Release  : 11
URL      : https://download.gnome.org/sources/libwnck/3.24/libwnck-3.24.1.tar.xz
Source0  : https://download.gnome.org/sources/libwnck/3.24/libwnck-3.24.1.tar.xz
Summary  : Window Navigator Construction Kit library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libwnck3-bin
Requires: libwnck3-lib
Requires: libwnck3-doc
Requires: libwnck3-locales
Requires: libwnck3-data
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cairo-xlib-xrender)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(libxml-2.0)
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
Requires: libwnck3-data

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
Requires: libwnck3-lib
Requires: libwnck3-bin
Requires: libwnck3-data
Provides: libwnck3-devel

%description dev
dev components for the libwnck3 package.


%package doc
Summary: doc components for the libwnck3 package.
Group: Documentation

%description doc
doc components for the libwnck3 package.


%package lib
Summary: lib components for the libwnck3 package.
Group: Libraries
Requires: libwnck3-data

%description lib
lib components for the libwnck3 package.


%package locales
Summary: locales components for the libwnck3 package.
Group: Default

%description locales
locales components for the libwnck3 package.


%prep
%setup -q -n libwnck-3.24.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501160598
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%configure --disable-static -program-suffix=-3
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1501160598
rm -rf %{buildroot}
%make_install
%find_lang libwnck-3.0

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

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libwnck-3.0/WnckApplication.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckClassGroup.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckPager.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckScreen.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckSelector.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckTasklist.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckWindow.html
/usr/share/gtk-doc/html/libwnck-3.0/WnckWorkspace.html
/usr/share/gtk-doc/html/libwnck-3.0/annotation-glossary.html
/usr/share/gtk-doc/html/libwnck-3.0/core.html
/usr/share/gtk-doc/html/libwnck-3.0/getting-started.html
/usr/share/gtk-doc/html/libwnck-3.0/home.png
/usr/share/gtk-doc/html/libwnck-3.0/index.html
/usr/share/gtk-doc/html/libwnck-3.0/indexes.html
/usr/share/gtk-doc/html/libwnck-3.0/ix01.html
/usr/share/gtk-doc/html/libwnck-3.0/ix02.html
/usr/share/gtk-doc/html/libwnck-3.0/ix03.html
/usr/share/gtk-doc/html/libwnck-3.0/ix04.html
/usr/share/gtk-doc/html/libwnck-3.0/ix05.html
/usr/share/gtk-doc/html/libwnck-3.0/ix06.html
/usr/share/gtk-doc/html/libwnck-3.0/ix07.html
/usr/share/gtk-doc/html/libwnck-3.0/ix08.html
/usr/share/gtk-doc/html/libwnck-3.0/ix09.html
/usr/share/gtk-doc/html/libwnck-3.0/ix10.html
/usr/share/gtk-doc/html/libwnck-3.0/ix11.html
/usr/share/gtk-doc/html/libwnck-3.0/ix12.html
/usr/share/gtk-doc/html/libwnck-3.0/ix13.html
/usr/share/gtk-doc/html/libwnck-3.0/ix14.html
/usr/share/gtk-doc/html/libwnck-3.0/left-insensitive.png
/usr/share/gtk-doc/html/libwnck-3.0/left.png
/usr/share/gtk-doc/html/libwnck-3.0/libwnck-3.0.devhelp2
/usr/share/gtk-doc/html/libwnck-3.0/libwnck-Icons-Functions.html
/usr/share/gtk-doc/html/libwnck-3.0/libwnck-Miscellaneous-Functions.html
/usr/share/gtk-doc/html/libwnck-3.0/libwnck-Resource-Usage-of-X-Clients.html
/usr/share/gtk-doc/html/libwnck-3.0/libwnck-Version-Information.html
/usr/share/gtk-doc/html/libwnck-3.0/libwnck-Window-Action-Menu.html
/usr/share/gtk-doc/html/libwnck-3.0/overview.html
/usr/share/gtk-doc/html/libwnck-3.0/right-insensitive.png
/usr/share/gtk-doc/html/libwnck-3.0/right.png
/usr/share/gtk-doc/html/libwnck-3.0/style.css
/usr/share/gtk-doc/html/libwnck-3.0/up-insensitive.png
/usr/share/gtk-doc/html/libwnck-3.0/up.png
/usr/share/gtk-doc/html/libwnck-3.0/utils.html
/usr/share/gtk-doc/html/libwnck-3.0/widgets.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwnck-3.so.0
/usr/lib64/libwnck-3.so.0.3.0

%files locales -f libwnck-3.0.lang
%defattr(-,root,root,-)

