#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-ipaddress
Version  : 1.0.22
Release  : 48
URL      : http://pypi.debian.net/ipaddress/ipaddress-1.0.22.tar.gz
Source0  : http://pypi.debian.net/ipaddress/ipaddress-1.0.22.tar.gz
Summary  : IPv4/IPv6 manipulation library
Group    : Development/Tools
License  : Python-2.0
Requires: deprecated-ipaddress-license = %{version}-%{release}
Requires: deprecated-ipaddress-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3

%description
ipaddress
=========
Python 3.3+'s [ipaddress](http://docs.python.org/dev/library/ipaddress) for Python 2.6, 2.7, 3.2.

%package legacypython
Summary: legacypython components for the deprecated-ipaddress package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-ipaddress package.


%package license
Summary: license components for the deprecated-ipaddress package.
Group: Default

%description license
license components for the deprecated-ipaddress package.


%package python
Summary: python components for the deprecated-ipaddress package.
Group: Default

%description python
python components for the deprecated-ipaddress package.


%prep
%setup -q -n ipaddress-1.0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554321203
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 test_ipaddress.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-ipaddress
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-ipaddress/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-ipaddress/LICENSE

%files python
%defattr(-,root,root,-)
