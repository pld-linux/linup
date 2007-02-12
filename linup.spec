Summary:	Linup - uptime client
Summary(pl.UTF-8):   Linup - klient mierzenia uptime'u
Name:		linup
Version:	1.1.1
Release:	6
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.smux.net/people/sena/linup/%{name}-%{version}.tar.bz2
# Source0-md5:	aa6e0154e49590977e050a13b0271f94
Source1:	%{name}.sysconfig
Source2:	%{name}.crond
Source3:	%{name}-polska.sysconfig
Source4:	%{name}-polska.crond
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-polska.patch
URL:		http://www.wonko.com/
Requires:	crondaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client count uptime in project Uptime. It supports version 5.0 of
protocol.

%description -l pl.UTF-8
Klient do mierzenia czasu uptime w projekcie Uptime. Wspiera wersję
5.0 protokołu.

%package polska
Summary:	Linup - Uptime client - Poland
Summary(pl.UTF-8):   Linup - Uptime - Polska
Group:		Applications/Networking
URL:		http://www.uptimes.tkb.pl/
Requires:	crondaemon

%description polska
This client count uptime in project Uptime - Polska. It supports
version 5.0 of protocol.

%description polska -l pl.UTF-8
Klient do mierzenia czasu uptime w projekcie Uptime - Polska. Wspiera
wersję 5.0 protokołu.

%prep
%setup -q -n %{name}
%patch0 -p1
rm -rf ../%{name}-polska
mkdir ../%{name}-polska
cp -r ../%{name}/* ../%{name}-polska
cd ../%{name}-polska
%patch1 -p1
cd ../%{name}

%build
%{__make} CC="%{__cc} %{rpmcflags}"

cd ../%{name}-polska
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/{sysconfig,cron.d}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cd ../%{name}-polska
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}-polska

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.d/%{name}

install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/%{name}-polska
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/%{name}-polska

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
/etc/cron.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files polska
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-polska
/etc/cron.d/%{name}-polska
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}-polska
