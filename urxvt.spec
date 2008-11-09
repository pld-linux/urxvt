%include	/usr/lib/rpm/macros.perl
Summary:	Rxvt terminal with unicode support and some improvements
Summary(pl.UTF-8):	Terminal Rxvt z obsługą unicode i kilkoma usprawnieniami
Name:		urxvt
Version:	9.06
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	4cb9330e99fc0b0b05cebf3581557dd8
Source1:	%{name}.desktop
URL:		http://software.schmorp.de/
BuildRequires:	autoconf >= 2.50
BuildRequires:	fontconfig-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
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

%description -l pl.UTF-8
URxvt jest modyfikacją Rxvt uwzględniającą:
- obsługę unicode
- obsługę czcionek xft (antialiasing)
- możliwość ustawienia grafiki jako tła
- cieniowanie tła
- prawdziwą przezroczystość

%prep
%setup -q -n rxvt-unicode-%{version}

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
echo '.so urxvtc.1' >$RPM_BUILD_ROOT%{_mandir}/man1/urxvtd.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes doc/README.xvt
%attr(755,root,root) %{_bindir}/urxvt*
%{_libdir}/%{name}
%{_desktopdir}/urxvt.desktop
%{_mandir}/man1/urxvt*.1*
%{_mandir}/man3/urxvtperl.3*
%{_mandir}/man7/urxvt.7*
