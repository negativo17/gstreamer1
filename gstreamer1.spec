%global         majorminor      1.0

%global         _glib2                  2.32.0
%global         _libxml2                2.4.0
%global         _gobject_introspection  1.31.1
%global         __python %{__python3}

Name:           gstreamer1
Version:        1.14.4
Release:        1%{?dist}
Summary:        GStreamer streaming media framework runtime
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
## For GStreamer RPM provides
Patch0:         gstreamer-inspect-rpm-format.patch
Source1:        gstreamer1.prov
Source2:        gstreamer1.attr

BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  check-devel
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  ghostscript
BuildRequires:  glib2-devel >= %{_glib2}
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}
BuildRequires:  gtk-doc >= 1.3
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel >= %{_libxml2}
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  netpbm-progs
BuildRequires:  openjade
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  texlive-dvips
BuildRequires:  texlive-jadetex
BuildRequires:  transfig

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything from
real-time sound processing to playing videos, and just about anything else
media-related. Its plugin-based architecture means that new data types or
processing capabilities can be added simply by installing new plugins.

%package devel
Summary:        Libraries/include files for GStreamer streaming media framework
Requires:       %{name}%{?isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa} >= %{_glib2}
Requires:       libxml2-devel%{?_isa} >= %{_libxml2}
Requires:       check-devel

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package devel-docs
Summary:         Developer documentation for GStreamer streaming media framework
Requires:        %{name} = %{version}-%{release}
BuildArch:       noarch

%description devel-docs
This %{name}-devel-docs contains developer documentation for the GStreamer
streaming media framework.

%prep
%autosetup -p1 -n gstreamer-%{version}
sed -i -e 's/-Wno-portability 1.14/-Wno-portability/g' configure.ac

%build
autoreconf -vif

%configure \
  --disable-examples \
  --disable-fatal-warnings \
  --disable-silent-rules \
  --disable-tests \
  --enable-debug \
  --enable-gtk-doc \
  --with-package-name='Fedora GStreamer package' \
  --with-package-origin='https://negativo17.org' \
  --with-ptp-helper-permissions=capabilities

%make_build V=1

%install
%make_install

%find_lang gstreamer-%{majorminor}
# Clean out files that should not be part of the rpm.
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
# Add the provides script
install -m0755 -D %{SOURCE1} %{buildroot}%{_rpmconfigdir}/gstreamer1.prov
# Add the gstreamer plugin file attribute entry (rpm >= 4.9.0)
install -m0644 -D %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/gstreamer1.attr

%ldconfig_scriptlets

%files -f gstreamer-%{majorminor}.lang
%license COPYING
%doc AUTHORS NEWS README RELEASE
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstbase-%{majorminor}.so.*
%{_libdir}/libgstcheck-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*
%{_libexecdir}/gstreamer-%{majorminor}/
%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoretracers.so
%{_libdir}/girepository-1.0/Gst-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstBase-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstCheck-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstController-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstNet-%{majorminor}.typelib
%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-stats-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}
%{_rpmconfigdir}/gstreamer1.prov
%{_rpmconfigdir}/fileattrs/gstreamer1.attr
%doc %{_mandir}/man1/gst-inspect-%{majorminor}.*
%doc %{_mandir}/man1/gst-launch-%{majorminor}.*
%doc %{_mandir}/man1/gst-stats-%{majorminor}.*
%doc %{_mandir}/man1/gst-typefind-%{majorminor}.*
%{_datadir}/bash-completion/completions/gst-inspect-1.0
%{_datadir}/bash-completion/completions/gst-launch-1.0
%{_datadir}/bash-completion/helpers/gst

%files devel
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%dir %{_includedir}/gstreamer-%{majorminor}/gst/base
%dir %{_includedir}/gstreamer-%{majorminor}/gst/check
%dir %{_includedir}/gstreamer-%{majorminor}/gst/controller
%dir %{_includedir}/gstreamer-%{majorminor}/gst/net
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/base/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/check/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/controller/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/*.h
%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstbase-%{majorminor}.so
%{_libdir}/libgstcheck-%{majorminor}.so
%{_libdir}/libgstcontroller-%{majorminor}.so
%{_libdir}/libgstnet-%{majorminor}.so
%{_datadir}/gir-1.0/Gst-%{majorminor}.gir
%{_datadir}/gir-1.0/GstBase-%{majorminor}.gir
%{_datadir}/gir-1.0/GstCheck-%{majorminor}.gir
%{_datadir}/gir-1.0/GstController-%{majorminor}.gir
%{_datadir}/gir-1.0/GstNet-%{majorminor}.gir
%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-check-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-net-%{majorminor}.pc

%files devel-docs
%doc %{_datadir}/gtk-doc/html/gstreamer-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-plugins-%{majorminor}

%changelog
* Sun Nov 10 2019 Simone Caronni <negativo17@gmail.com> - 1.14.4-1
- Rebase on 1.14.4.
