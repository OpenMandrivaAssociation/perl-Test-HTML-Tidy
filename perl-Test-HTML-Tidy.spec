%define upstream_name    Test-HTML-Tidy
%define upstream_version 1.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9

Summary:	Test::More-style wrapper around HTML::Tidy 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Tidy)

BuildArch:	noarch

%description 
Handy way to check that HTML is valid, according to HTML::Tidy. It is built
with Test::Builder and plays happily with Test::More and friends.

If you are not already familiar with Test::More now would be the time to go
take a look.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-6mdv2010.1
+ Revision: 505273
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.00-5mdv2010.0
+ Revision: 430597
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2009.0
+ Revision: 258513
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.00-3mdv2009.0
+ Revision: 246534
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.00-1mdv2008.1
+ Revision: 131615
- kill re-definition of %%buildroot on Pixel's request


* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2007.1
+ Revision: 143563
- Imported perl-Test-HTML-Tidy-1.00-1mdv2007.1 into SVN repository.

* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2007.1
- first mdv release

