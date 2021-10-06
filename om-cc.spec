Name:		om-cc
Version:	0.2.0.4
Release:	1
Summary:	OpenMandriva Lx Control Center
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/rugyada/om-cc
Source0:	%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%version.tar.gz
Requires:	kdialog
Requires:	dnf-plugins-core
Requires:	htmlscript >= 1.0.1
BuildRequires:	make
BuildArch:	noarch
%rename om-control-center

%description
OpenMandriva Lx Control Center.

%prep
%setup -q
%autopatch -p1

%build
# Nothing to do here...

%install
%make_install

%find_lang om-cc

mkdir -p %{buildroot}%{_datadir}/icons/
cp om-cc.svg %{buildroot}%{_datadir}/icons/

%files -f om-cc.lang
%{_bindir}/om-cc
%{_datadir}/%{name}/*
%{_datadir}/applications/om-cc.desktop
%{_datadir}/icons/om-cc.svg
