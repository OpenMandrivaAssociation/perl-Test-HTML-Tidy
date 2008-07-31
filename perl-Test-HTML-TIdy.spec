%define module  Test-HTML-Tidy
%define name    perl-%{module}
%define version 1.00
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Test::More-style wrapper around HTML::Tidy 
License:        GPL or Artistic
Group:          Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(HTML::Tidy)

%description 
Handy way to check that HTML is valid, according to HTML::Tidy. It is built
with Test::Builder and plays happily with Test::More and friends.

If you are not already familiar with Test::More now would be the time to go
take a look.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*


