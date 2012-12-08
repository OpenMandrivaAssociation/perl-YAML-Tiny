%define upstream_name    YAML-Tiny
%define upstream_version 1.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Read/Write YAML files with as little code as possible
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/YAML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch: noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/YAML


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.500.0-3mdv2012.0
+ Revision: 765903
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.500.0-2
+ Revision: 764399
- rebuilt for perl-5.14.x

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.500.0-1
+ Revision: 687008
- update to new version 1.50

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.480.0-3
+ Revision: 676642
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.480.0-2
+ Revision: 676479
- rebuild

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.480.0-1
+ Revision: 635804
- update to new version 1.48

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.460.0-1mdv2011.0
+ Revision: 622930
- update to new version 1.46

* Wed Aug 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.440.0-1mdv2011.0
+ Revision: 569160
- new version

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.430.0-1mdv2011.0
+ Revision: 551210
- update to 1.43

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.410.0-1mdv2010.1
+ Revision: 477632
- update to 1.41

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.0
+ Revision: 408862
- update to 1.40

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.390.0-1mdv2010.0
+ Revision: 401808
- rebuild using %%perl_convert_version
- fixed license field

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.39-1mdv2010.0
+ Revision: 378240
- update to new version 1.39

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2010.0
+ Revision: 376725
- update to new version 1.38

* Wed Jan 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2009.1
+ Revision: 326624
- update to new version 1.36

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-1mdv2009.1
+ Revision: 320445
- update to new version 1.35

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.32-3mdv2009.0
+ Revision: 268885
- rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 Thierry Vignaud <tv@mandriva.org> 1.32-2mdv2009.0
+ Revision: 208941
- fix spacing at top of description

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2009.0
+ Revision: 208377
- update to new version 1.32

* Sat May 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdv2009.0
+ Revision: 205400
- update to new version 1.31

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2009.0
+ Revision: 201899
- update to new version 1.30

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2009.0
+ Revision: 195162
- import perl-YAML-Tiny


* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2009.0
- first mdv release
