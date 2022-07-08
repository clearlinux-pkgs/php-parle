#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-parle
Version  : 0.8.2
Release  : 10
URL      : https://pecl.php.net/get/parle-0.8.2.tgz
Source0  : https://pecl.php.net/get/parle-0.8.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSL-1.0
BuildRequires : buildreq-php

%description
[![Build Status](https://secure.travis-ci.org/weltling/parle.svg?branch=master)](http://travis-ci.org/weltling/parle)
[![Build status](https://ci.appveyor.com/api/projects/status/w857q34tke5dbt91?svg=true)](https://ci.appveyor.com/project/weltling/parle)

%prep
%setup -q -n parle-0.8.2
cd %{_builddir}/parle-0.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)
