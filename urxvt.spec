Summary:	urxvt - terminal emulator in an X window
Summary(pl):	Emulator terminala dla X Window
Name:		urxvt
Version:	3.1
Release:	1
Group:		X11/Applications
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-utmp98.patch
Patch1:		%{name}-utmp98-2.patch
Patch2:		%{name}-xim.patch
Patch3:		%{name}-utmpx.patch
URL:		http://software.schmorp.de
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rxvt is a VT100 terminal emulator for X. It is intended as a
replacement for xterm(1) for users who do not require the more
esoteric features of xterm. Specifically urxvt does not implement the
Tektronix 4014 emulation, session logging and toolkit style
configurability. As a result, urxvt uses much less swap space than
xterm - a significant advantage on a machine serving many X sessions.

%description -l pl
Rxvt jest emulatorem terminala VT100 dla X Window. Jest on
interesuj±cym zamiennikiem dla programu xterm(1) dla u¿ytkowników,
którzy nie potrzebuj± bardziej wyszukanych mo¿liwo¶ci xterma jak
emulacja terminala Tektronix 4014, logowanie sesji czy pewne
mo¿liwo¶ci konfiguracyjnye na poziomie X toolkit. Rezygnacja z tych
mo¿liwo¶ci zaowocowa³a tym, ¿e urxvt potrzebuje o wiele mniej pamiêci
do uruchomienia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mv -f autoconf/{configure.in,xpm.m4} .
CFLAGS="%{rpmcflags} -DLINUX_KEYS"
%{__libtoolize}
%{__aclocal} -I .
%{__autoheader}
%{__autoconf}
%{__automake} || :
%configure \
	--enable-shared \
	--disable-static \
	--enable-everything \
	--enable-xgetdefault \
	--enable-mousewheel \
	--disable-menubar \
	--enable-next-xcroll \
	--enable-ttygid \
	--with-term=urxvt \
	--enable-half-shadow \
	--enable-smart-resize \
	--enable-256-color
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/menu/* ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/urxvt.desktop
%{_mandir}/man1/*
