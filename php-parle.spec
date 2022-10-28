#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-parle
Version  : 0.8.3
Release  : 24
URL      : https://pecl.php.net/get/parle-0.8.3.tgz
Source0  : https://pecl.php.net/get/parle-0.8.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSL-1.0
Requires: php-parle-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
Parle provides lexing and parsing facilities for PHP
=============================================
Lexing and parsing is used widely in the PHP core and extensions. Usually such a functionality is packed into a piece of C/C++ and depends on tools like [flex](http://flex.sourceforge.net/), [re2c](http://re2c.org/), [Bison](http://www.gnu.org/software/bison/), [LEMON](http://www.hwaci.com/sw/lemon/) or similar. With Parle, it is possible to implement lexing and parsing in PHP while relying on features and principles of the parser/lexer generator tools for C/C++. The Lexer and Parser classes are there in the Parle namespace.
The implementation bases on the work of [Ben Hanson](http://www.benhanson.net/)

%package lib
Summary: lib components for the php-parle package.
Group: Libraries

%description lib
lib components for the php-parle package.


%prep
%setup -q -n parle-0.8.3
cd %{_builddir}/parle-0.8.3

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/parle.so
