Summary:	Library for reading PhotoCD images
Summary(pl):	Biblioteka do odczytu plików PhotoCD
Name:		libpcd
Version:	1.0
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://bytesex.org/misc/%{name}_%{version}.tar.gz
URL:		http://bytesex.org/libpcd.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for reading PhotoCD images.

%description -l pl
Biblioteka do odczytu plików PhotoCD.

%package devel
Summary:	libpcd header file
Summary(pl):	Plik nag³ówkowy libpcd
Group:		Development/Libraries
Requires:	libpcd = %{version}

%description devel
libpcd header file.

%description devel -l pl
Plik nag³ówkowy biblioteki libpcd.

%package static
Summary:	libpcd static library
Summary(pl):	Biblioteka statyczna libpcd
Group:		Development/Libraries
Requires:	libpcd-devel = %{version}

%description static
Static version of libpcd.

%description static -l pl
Statyczna wersja biblioteki libpcd.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} \$(WARN)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libpcd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc pcd.css pcd.html
%attr(755,root,root) %{_libdir}/libpcd.so
%attr(644,root,root) %{_includedir}/pcd.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcd.a
