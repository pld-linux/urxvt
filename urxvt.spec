# TODO: utempter support
#
# Conditional build:
%bcond_without	256colors	# build without 256 color support
#
Summary:	Rxvt terminal with unicode support and some improvements
Summary(pl.UTF-8):	Terminal Rxvt z obsługą unicode i kilkoma usprawnieniami
Name:		urxvt
Version:	9.31
Release:	3
License:	GPL v3+
Group:		X11/Applications
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	3d0ec83705c9b9ff301a4b9965b3cd9f
Source1:	%{name}.desktop
Patch0:		broken-perl-5.38.patch
URL:		http://software.schmorp.de/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	libptytty-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel
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
%patch0 -p1

%build
%{__aclocal} -I.
%{__autoheader}
%{__autoconf}
%configure \
%if %{with 256colors}
	--enable-256-color \
%endif
	--enable-everything \
	--enable-mousewheel \
	--enable-next-scroll \
	--enable-smart-resize \
	--with-term=rxvt

%{__make}

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
%attr(755,root,root) %{_bindir}/urclock
%attr(755,root,root) %{_bindir}/urxvt*
%{_libdir}/%{name}
%{_desktopdir}/urxvt.desktop
%{_mandir}/man1/urclock.1*
%{_mandir}/man1/urxvt*.1*
%{_mandir}/man3/urxvtperl.3*
%{_mandir}/man7/urxvt.7*
