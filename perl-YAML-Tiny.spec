%define module   YAML-Tiny
%define version    1.30
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Read/Write YAML files with as little code as possible
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/YAML/%{module}-%{version}.tar.gz
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/YAML

