Summary:	Linup - Uptime client
Summary(pl):	Linup - Klient mierzenia uptime'u
Name:		linup
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/Network
URL:		http://www.wonko.com/
Source0:	ftp://ftp.smux.net/people/sena/linup/%{name}-%{version}.tar.bz2
Source1:	%{name}.sysconfig
Source2:	%{name}.crond
Source3:	%{name}-polska.sysconfig
Source4:	%{name}-polska.crond
Patch0:		%{name}-polska.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client count uptime in project Uptime. It supports version 5.0
of protocol.

%description -l pl
Klient do mierzenia czasu uptime w projekcie Uptime. Wspiera
wersjê 5.0 protoko³u.

%package polska
Summary:	Linup - Uptime client - Poland
Summary(pl):	Linup - Uptime - Polska
Group:		Applications/Network
URL:		http://www.uptimes.prv.pl/

%description polska
This client count uptime in project Uptime - Polska. It supports version 5.0
of protocol.

%description polska -l pl
Klient do mierzenia czasu uptime w projekcie Uptime - Polska. Wspiera
wersjê 5.0 protoko³u.

%prep
%setup -q -n %{name}
rm -rf ../%{name}-polska
mkdir ../%{name}-polska
cp -r ../%{name}/* ../%{name}-polska
cd ../%{name}-polska
%patch0 -p1
cd ../%{name}

%build
%{__make} CC="gcc %{rpmcflags}"

cd ../%{name}-polska
%{__make} CC="gcc %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/sysconfig,%{_sysconfdir}/cron.d}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cd ../%{name}-polska
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}-polska

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/%{name}

install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}-polska
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/%{name}-polska

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/cron.d/%{name}
%{_sysconfdir}/sysconfig/%{name}

%files polska
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-polska
%{_sysconfdir}/cron.d/%{name}-polska
%{_sysconfdir}/sysconfig/%{name}-polska
