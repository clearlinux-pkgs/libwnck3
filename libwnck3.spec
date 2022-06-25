#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwnck3
Version  : 40.1
Release  : 25
URL      : https://download.gnome.org/sources/libwnck/40/libwnck-40.1.tar.xz
Source0  : https://download.gnome.org/sources/libwnck/40/libwnck-40.1.tar.xz
Summary  : Window Navigator Construction Kit library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libwnck3-bin = %{version}-%{release}
Requires: libwnck3-data = %{version}-%{release}
Requires: libwnck3-filemap = %{version}-%{release}
Requires: libwnck3-lib = %{version}-%{release}
Requires: libwnck3-license = %{version}-%{release}
Requires: libwnck3-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libstartup-notification-1.0)
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
Requires: libwnck3-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the libwnck3 package.
Group: Default

%description filemap
filemap components for the libwnck3 package.


%package lib
Summary: lib components for the libwnck3 package.
Group: Libraries
Requires: libwnck3-data = %{version}-%{release}
Requires: libwnck3-license = %{version}-%{release}
Requires: libwnck3-filemap = %{version}-%{release}

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
%setup -q -n libwnck-40.1
cd %{_builddir}/libwnck-40.1
pushd ..
cp -a libwnck-40.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656134559
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libwnck3
cp %{_builddir}/libwnck-40.1/COPYING %{buildroot}/usr/share/package-licenses/libwnck3/ba8966e2473a9969bdcab3dc82274c817cfd98a1
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libwnck-3.0
## install_append content
mv %{buildroot}/usr/bin/wnck-urgency-monitor %{buildroot}/usr/bin/wnck-urgency-monitor-3
mv %{buildroot}/usr/bin/wnckprop %{buildroot}/usr/bin/wnckprop-3
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wnck-urgency-monitor-3
/usr/bin/wnckprop-3
/usr/share/clear/optimized-elf/bin*

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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libwnck3

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libwnck-3.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libwnck-3.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libwnck-3.so.0.3.0
/usr/lib64/libwnck-3.so.0
/usr/lib64/libwnck-3.so.0.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwnck3/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f libwnck-3.0.lang
%defattr(-,root,root,-)

