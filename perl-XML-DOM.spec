%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/XML-DOM-%{version}/find-perl-requires
Summary:	XML-DOM perl module
Summary(pl):	Modu³ perla XML-DOM
Name:		perl-XML-DOM
Version:	1.25
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-DOM-%{version}.tar.gz
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-DOM - module for building DOM Level 1 compliant document
structures.

%description -l pl
XML-DOM - modu³ do tworzenia struktur dokumentów zgodnych z DOM Level
1.

%prep
%setup -q -n XML-DOM-%{version}
%patch -p1

chmod +x find-perl-requires

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz samples/*
%{perl_sitelib}/XML/DOM.pm
%{_mandir}/man3/*
