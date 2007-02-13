Summary:	Library for reading PhotoCD images
Summary(pl.UTF-8):	Biblioteka do odczytu plików PhotoCD
Name:		libpcd
Version:	1.0.1
Release:	2
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://bytesex.org/misc/%{name}_%{version}.tar.gz
# Source0-md5:	c9127a6aae3c7510498990d82bb0b68a
URL:		http://bytesex.org/libpcd.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for reading PhotoCD images.

%description -l pl.UTF-8
Biblioteka do odczytu plików PhotoCD.

%package devel
Summary:	libpcd header file
Summary(pl.UTF-8):	Plik nagłówkowy libpcd
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
libpcd header file.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libpcd.

%package static
Summary:	libpcd static library
Summary(pl.UTF-8):	Biblioteka statyczna libpcd
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of libpcd.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libpcd.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	libdir=%{_libdir} \
	CFLAGS="%{rpmcflags} \$(WARN)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
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
%{_includedir}/pcd.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcd.a
