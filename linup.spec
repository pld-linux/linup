Summary:	Linup - Uptime client
Summary(pl):	Linup - Klient mierzenia uptime'u
Name:		linup
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/Network
URL:		http://www.uptimes.prv.pl/
Source0:	ftp://ftp.smux.net/people/sena/linup/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client count uptime in project Uptime - Polska. It supports
5.0 version of protocol.

%description -l pl
Klient do mierzenia czasu uptime w projekcie Uptime - Polska. Wspiera
wersjê 5.0 protoko³u.

%prep
%setup -q -n %{name}

%build
%{__make} CC="gcc %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
