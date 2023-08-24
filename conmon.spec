Summary:	OCI container runtime monitor
Name:		conmon
Version:	2.1.8
Release:	1
License:	Apache v2.0
Group:		Applications/System
#Source0Download: https://github.com/containers/conmon/releases
Source0:	https://github.com/containers/conmon/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	753a2d554c6b5c55c93f069a20d9ebf9
URL:		https://github.com/containers/conmon
BuildRequires:	glib2-devel
BuildRequires:	go-md2man
BuildRequires:	libseccomp-devel >= 2.5.2
BuildRequires:	pkgconfig
BuildRequires:	systemd-devel
Requires:	libseccomp >= 2.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conmon is a monitoring program and communication tool between a
container manager (like Podman or CRI-O) and an OCI runtime (like runc
or crun) for a single container.

%prep
%setup -q

%{__rm} -r tools/vendor

%build
# prevent build of go-md2man
install -d tools/build
: > tools/build/go-md2man
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDLAGS="%{rpmldflags}" \

%{__make} docs \
        GOMD2MAN=/usr/bin/go-md2man

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
