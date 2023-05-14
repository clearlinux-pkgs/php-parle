#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
#
Name     : php-parle
Version  : 0.8.4
Release  : 34
URL      : https://pecl.php.net/get/parle-0.8.4.tgz
Source0  : https://pecl.php.net/get/parle-0.8.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSL-1.0
Requires: php-parle-lib = %{version}-%{release}
Requires: php-parle-license = %{version}-%{release}
BuildRequires : buildreq-php
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Parle provides lexing and parsing facilities for PHP
=============================================
Lexing and parsing is used widely in the PHP core and extensions. Usually such a functionality is packed into a piece of C/C++ and depends on tools like [flex](http://flex.sourceforge.net/), [re2c](http://re2c.org/), [Bison](http://www.gnu.org/software/bison/), [LEMON](http://www.hwaci.com/sw/lemon/) or similar. With Parle, it is possible to implement lexing and parsing in PHP while relying on features and principles of the parser/lexer generator tools for C/C++. The Lexer and Parser classes are there in the Parle namespace.
The implementation bases on the work of [Ben Hanson](http://www.benhanson.net/)

%package lib
Summary: lib components for the php-parle package.
Group: Libraries
Requires: php-parle-license = %{version}-%{release}

%description lib
lib components for the php-parle package.


%package license
Summary: license components for the php-parle package.
Group: Default

%description license
license components for the php-parle package.


%prep
%setup -q -n parle-0.8.4
cd %{_builddir}/parle-0.8.4
pushd ..
cp -a parle-0.8.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-parle
cp %{_builddir}/parle-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-parle/22b3561bb56bcb40fbae8dd7c009662590efbee4 || :
cp %{_builddir}/parle-%{version}/lib/lexertl14/include/lexertl/licence_1_0.txt %{buildroot}/usr/share/package-licenses/php-parle/a1fa5197b92b58a4360f7c0e209b59ac0c132b81 || :
cp %{_builddir}/parle-%{version}/lib/parsertl14/include/parsertl/licence_1_0.txt %{buildroot}/usr/share/package-licenses/php-parle/a1fa5197b92b58a4360f7c0e209b59ac0c132b81 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/parle.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-parle/22b3561bb56bcb40fbae8dd7c009662590efbee4
/usr/share/package-licenses/php-parle/a1fa5197b92b58a4360f7c0e209b59ac0c132b81
