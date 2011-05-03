%define		status		stable
%define		pearname	Horde_Injector
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde dependency injection container
Name:		php-horde-Horde_Injector
Version:	1.0.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	ae9e0374a8ca213863b5574fcaa4aab8
URL:		https://github.com/horde/horde/tree/master/framework/Injector/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A depedency injection container for Horde.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Horde_Injector/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Injector.php
%{php_pear_dir}/Horde/Injector
