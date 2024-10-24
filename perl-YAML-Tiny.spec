%define modname	YAML-Tiny

Summary:	Read/Write YAML files with as little code as possible
Name:		perl-%{modname}
Version:	1.74
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/YAML::Tiny
Source0:	http://www.cpan.org/modules/by-module/YAML/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
*YAML::Tiny* is a perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and memory
overhead.

Most of the time it is accepted that Perl applications use a lot of memory
and modules. The *::Tiny* family of modules is specifically intended to
provide an ultralight and zero-dependency alternative to many more-thorough
standard modules.

This module is primarily for reading human-written files (like simple
config files) and generating very simple human-readable files. Note that I
said *human-readable* and not *geek-readable*. The sort of files that your
average manager or secretary should be able to look at and make sense of.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc LICENSE README Changes
%{perl_vendorlib}/YAML
%{_mandir}/man3/*
