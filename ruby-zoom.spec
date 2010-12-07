%define rbname zoom
%define version 0.2.2
%define release %mkrel 8

Summary: Ruby binding to the Z39.50 Object-Orientation Model
Name: ruby-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: LGPL
URL: http://ruby-zoom.rubyforge.org/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel 
BuildRequires: yaz-devel tcp_wrappers-devel

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model
(ZOOM), an abstract object-oriented programming interface to a subset of the
services specified by the Z39.50 standard, also known as the international
standard ISO 23950.

This software is based (and therefore depends) on YAZ, a free-software
implementation of the Z39.50/SRW/SRU standards, but could be easily ported
to any ZOOM compliant implementation.

%prep
%setup -q
rm -f doc/rd/Ruby%2FLibburn doc/.cvsignore doc/gendoc.sh

%build
ruby extconf.rb
%make CFLAGS="%{__common_cflags} -fPIC"

%install
make install DESTDIR=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ChangeLog README doc sample
%{ruby_sitearchdir}/%{rbname}.so
%{ruby_sitelibdir}/marc.rb

