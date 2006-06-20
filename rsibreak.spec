Summary:	RSIBreak - a small utility which bothers you at certain intervals
SUmmary(de):	RSIBreak - ein kleines Programm dass dich in bestimmten Zeitabständen nervt
Summary(pl):	RSIBreak - ma³e narzêdzie, które bêdzie ciê wnerwiaæ w okre¶lonych odstêpach czasu
Name:		rsibreak
%define		_name	%(echo %{name}|%{__sed} s/r/R/)
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.rsibreak.org/images/e/e2/%{_name}-%{version}.tar.bz2
# Source0-md5:	7846a2122805b6da3cc050d4664a52df
URL:		http://www.kde-apps.org/content/show.php?content=39085
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of this utility is to let you know when it is time to have a
break from your computer.

%description -l de
Das Ziel dieses Programms ist es dir bescheid zu sagen wann es Zeit
wird eine kleine Pause von den Komputer einzulegen.

%description -l pl
Celem tego programu jest daæ Ci znaæ kiedy nale¿a³oby zrobiæ przerwe
od komputera.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/kde/%{name}.desktop
%{_datadir}/apps/rsibreak/icons/hicolor/16x16/actions/%{name}?.png
%{_datadir}/apps/rsibreak/icons/hicolor/32x32/actions/*.png
%{_datadir}/autostart/rsibreak.desktop
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
