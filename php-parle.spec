#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-parle
Version  : 0.8.1
Release  : 3
URL      : https://pecl.php.net//get/parle-0.8.1.tgz
Source0  : https://pecl.php.net//get/parle-0.8.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSL-1.0
Requires: php-parle-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
[![Build Status](https://secure.travis-ci.org/weltling/parle.svg?branch=master)](http://travis-ci.org/weltling/parle)
[![Build status](https://ci.appveyor.com/api/projects/status/w857q34tke5dbt91?svg=true)](https://ci.appveyor.com/project/weltling/parle)

%package lib
Summary: lib components for the php-parle package.
Group: Libraries

%description lib
lib components for the php-parle package.


%prep
%setup -q -n parle-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/parle.so
