%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/XML-DOM-%{version}/find-perl-requires
Summary:	XML-DOM perl module
Summary(pl):	Modu³ perla XML-DOM
Name:		perl-XML-DOM
Version:	1.25
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-DOM-%{version}.tar.gz
Patch:		perl-XML-DOM-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-XML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XML-DOM - module for building DOM Level 1 compliant document structures.

%description -l pl
XML-DOM - modu³ do tworzenia struktur dokumentów zgodnych z DOM Level 1.

%prep
%setup -q -n XML-DOM-%{version}
%patch -p1

chmod +x find-perl-requires

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XML/DOM
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz samples/*

%{perl_sitelib}/XML/DOM.pm
%{perl_sitearch}/auto/XML/DOM

%{_mandir}/man3/*
