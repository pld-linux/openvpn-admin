#
# TODO:
# - find R and BR's (don't know how in C# :/)
#
Summary:	GUI for OpenVPN
Summary(pl.UTF-8):	Graficzny interfejs dla OpenVPN
Name:		openvpn-admin
Version:	1.9.3
Release:	0.1
License:	LGPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/openvpnadmin/%{name}-%{version}b.tar.gz
# Source0-md5:	34899a0d7b6532684897001d8cf8b349
URL:		http://sourceforge.net/projects/openvpnadmin/
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	mono-csharp
BuildRequires:	perl-XML-Parser
Requires:	gksu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI for OpenVPN.

%description -l pl.UTF-8
Graficzny interfejs dla OpenVPN.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_sbindir}/*
/etc/pam.d/%{name}
/etc/security/console.apps/%{name}
%{_libdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
