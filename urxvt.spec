#
# TODO: unpackaded perl stuff:
#	/usr/lib/urxvt/perl/digital-clock
#	/usr/lib/urxvt/perl/example-refresh-hooks
#	/usr/lib/urxvt/perl/selection
#	/usr/lib/urxvt/urxvt.pm
#
Summary:	Rxvt terminal with unicode support and some improvements
Summary(pl):	Terminal Rxvt z obs³ug± unicode i kilkoma usprawnieniami
Name:		urxvt
Version:	6.3
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	411799866fa89ab31f2b19662c36e7ce
Source1:	%{name}.desktop
Patch0:		%{name}-link.patch
URL:		http://software.schmorp.de/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	xft-devel
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URxvt is a Rxvt modification which includes:
- unicode support
- xft font support (antialiasing)
- background pixmaps
- background tinting

%description -l pl
URxvt jest modyfikacj± Rxvt uwzglêdniaj±c±:
- obs³ugê unicode
- obs³ugê czcionek xft (antialiasing)
- mo¿liwo¶æ ustawienia grafiki jako t³a
- cieniowanie t³a

%prep
%setup -q -n rxvt-unicode-%{version}
%patch0 -p1

rm -f autoconf/libtool.m4
ln -sf autoconf/configure.in .

%build
%{__libtoolize}
%{__aclocal} -I autoconf
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
%doc doc/menu/* Changes doc/README.*
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/urxvt.desktop
%{_mandir}/man*/*
