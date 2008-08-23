%define		orgname kdeextragear-libs
%define		snap	812803

Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		kde4-kdeextragear-libs
Version:	4.1.63
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/%{orgname}-%{snap}.tar.bz2
# Source0-md5:	88f731f3b48e96f6b783b1e98ec30a18
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	phonon-devel >= 4.1.83
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDcraw Library is part of the KIPI Project.

%description -l pl.UTF-8
Biblioteka KDcraw jest częścią projektu KIPI.

%package devel
Summary:	Header files for libkdcraw development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkdcraw
Group:		X11/Development/Libraries

%description devel
Header files for libkdcraw development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkdcraw.

%package libkdcraw
Summary:	libkdcraw
Summary(pl.UTF-8):	libkdcraw
Group:		X11/Libraries
Provides:	libkdcraw

%description libkdcraw
libkdcraw.

%description libkdcraw -l pl.UTF-8
libkdcraw.

%package kipiplugins
Summary:	kipiplugins
Summary(pl.UTF-8):	kipiplugins
Group:		X11/Libraries
Provides:	kipiplugins

%description kipiplugins
kipiplugins.

%description kipiplugins -l pl.UTF-8
kipiplugins.

%package libkexiv2
Summary:	libkexiv2
Summary(pl.UTF-8):	libkexiv2
Group:		X11/Libraries
Provides:	libkexiv2

%description libkexiv2
libkexiv2.

%description libkexiv2 -l pl.UTF-8
libkexiv2.

#%package libksane
#Summary:	libksane
#Summary(pl.UTF-8):	libksane
#Group:		X11/Libraries
#Provides:	libksane

#%description libksane
#libksane.

#%description libksane -l pl.UTF-8
#libksane.

%prep
%setup -q -n %{orgname}-%{snap}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files libkdcraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdcraw.so.?.?.?
%attr(755,root,root) %ghost %{_libdir}/libkdcraw.so.5
%dir %{_libdir}/libkdcraw5
%attr(755,root,root) %{_libdir}/libkdcraw5/kdcraw
%{_libdir}/libkdcraw5/CAMERALIST
%{_iconsdir}/hicolor/*x*/*/*.*
%dir %{_datadir}/apps/libkdcraw
%dir %{_datadir}/apps/libkdcraw/profiles
%{_datadir}/apps/libkdcraw/profiles/*.icm

%files kipiplugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_acquireimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_gpssync.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_jpeglossless.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_metadataedit.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_rawconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_sendimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_simpleviewer.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_slideshow.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_timeadjust.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_htmlexport.so
%attr(755,root,root) %ghost %{_libdir}/libkipi.so.5
%attr(755,root,root) %{_libdir}/libkipi.so.?.?.?
%attr(755,root,root) %ghost %{_libdir}/libkipiplugins.so.1
%attr(755,root,root) %{_libdir}/libkipiplugins.so.?.?.?
%attr(755,root,root) %{_pkgconfigdir}/libkipi.pc
%{_datadir}/apps/kipi
%{_datadir}/apps/kipiplugin_metadataedit
%{_datadir}/apps/kipiplugin_simpleviewerexport
%{_datadir}/apps/kipiplugin_htmlexport
%{_datadir}/kde4/services/kipiplugin_*.desktop
%{_datadir}/kde4/servicetypes/kipiplugin.desktop

%files libkexiv2
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkexiv2.so.6
%attr(755,root,root) %{_libdir}/libkexiv2.so.?.?.?
%attr(755,root,root) %{_pkgconfigdir}/libkexiv2.pc

#%files libksane
#%defattr(644,root,root,755)
#%attr(755,root,root) %ghost %{_libdir}/libksane.so.0
#%attr(755,root,root) %{_libdir}/libksane.so.?.?.?
#%attr(755,root,root) %{_pkgconfigdir}/libksane.pc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdcraw.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so
%attr(755,root,root) %{_libdir}/libkipi.so
%attr(755,root,root) %{_libdir}/libkexiv2.so
#%attr(755,root,root) %{_libdir}/libksane.so
%{_includedir}/libkdcraw
%{_pkgconfigdir}/libkdcraw.pc
%{_includedir}/libkexiv2
%{_includedir}/libkipi
#%{_includedir}/libksane
