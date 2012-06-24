%include	/usr/lib/rpm/macros.perl
Summary:	Rxvt terminal with unicode support and some improvements
Summary(pl):	Terminal Rxvt z obs�ug� unicode i kilkoma usprawnieniami
Name:		urxvt
Version:	7.9
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	7a0c73ccf0e31808ad37b61e730cd10e
Source1:	%{name}.desktop
Patch0:		%{name}-link.patch
URL:		http://software.schmorp.de/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URxvt is a Rxvt modification which includes:
- unicode support
- xft font support (antialiasing)
- background pixmaps
- background tinting
- real transparency

%description -l pl
URxvt jest modyfikacj� Rxvt uwzgl�dniaj�c�:
- obs�ug� unicode
- obs�ug� czcionek xft (antialiasing)
- mo�liwo�� ustawienia grafiki jako t�a
- cieniowanie t�a
- prawdziw� przezroczysto��

%prep
%setup -q -n rxvt-unicode-%{version}
%patch0 -p1

%build
%{__autoheader}
%{__autoconf}
%configure \
	--enable-shared \
	--disable-static \
	--enable-everything \
	--enable-xgetdefault \
	--enable-mousewheel \
	--disable-menubar \
	--enable-next-scroll \
	--enable-ttygid \
	--with-term=rxvt \
	--enable-half-shadow \
	--enable-smart-resize \
	--enable-256-color \
	--enable-24bit
%{__make} \
	CXXFLAGS="%{rpmcxxflags}" \
	CFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,7}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
echo '.so urxvtc.1' >$RPM_BUILD_ROOT%{_mandir}/man1/urxvtd.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes doc/README.*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_desktopdir}/urxvt.desktop
%{_mandir}/man*/*
