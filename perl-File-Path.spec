%define upstream_name    File-Path
%define upstream_version 2.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.09
Release:	1

Summary:	File path and name utilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-Path-2.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildArch:	noarch

%description
This module provide a convenient way to create directories of arbitrary
depth and to delete an entire directory subtree from the filesystem.

The following functions are provided:

* make_path( $dir1, $dir2, .... )

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2.80.0-2mdv2011.0
+ Revision: 654962
- rebuild for updated spec-helper

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 2.80.0-1mdv2011.0
+ Revision: 462466
- update to 2.08

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.70.0-1mdv2010.0
+ Revision: 395223
- import perl-File-Path


* Sun Jul 12 2009 cpan2dist 2.07-1mdv
- initial mdv release, generated with cpan2dist

