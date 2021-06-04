Summary:	OCI container runtime monitor
Name:		conmon
Version:	2.0.29
Release:	1
License:	Apache v2.0
Group:		Applications/System
#Source0Download: https://github.com/containers/conmon/releases
Source0:	https://github.com/containers/conmon/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c789bde7cb2c3164f0dfadf4d8a27cc3
URL:		https://github.com/containers/conmon
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig
BuildRequires:	systemd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conmon is a monitoring program and communication tool between a
container manager (like Podman or CRI-O) and an OCI runtime (like runc
or crun) for a single container.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
        PREFIX=%{_prefix} \
        BINDIR=%{_bindir} \
        LIBEXECDIR=%{_libexecdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md  changelog.txt
%attr(755,root,root) %{_bindir}/conmon
%{_mandir}/man8/conmon.8*
