#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests fail -- buggy perl?
%define		pdir	XML
%define		pnam	DOM
Summary:	XML::DOM - build DOM Level 1 compliant document structures
Summary(pl.UTF-8):	XML::DOM - budowanie struktur dokumentów zgodnych z DOM Level 1
Name:		perl-XML-DOM
Version:	1.44
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ec2032a06e5762984f7a332c199c205
URL:		http://search.cpan.org/dist/XML-DOM/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-RegExp
BuildRequires:	perl-libwww
BuildRequires:	perl-libxml >= 0.07
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'Dom', that allows XML::Parser to build an Object
Oriented datastructure with a DOM Level 1 compliant interface.
However, there is a new DOM module, XML::GDOME which is under active
development and significantly faster than XML::DOM, since it is based
on the libgdome C library.

%description -l pl.UTF-8
To jest rozszerzenie Perla do XML::Parser. Dodaje do XML::Parser nowy
styl o nazwie "Dom", pozwalając modułowi budować obiektowo
zorientowane struktury danych z interfejsem zgodnym z DOM Level 1.
Aczkolwiek jest nowy moduł DOM, XML::GDOME - aktualnie aktywnie
rozwijany i znacznie szybszy niż XML::DOM, ponieważ jest oparty na
bibliotece C libgdome.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/XML/DOM
%{perl_vendorlib}/XML/DOM.pm
%{perl_vendorlib}/XML/DOM/*.pm
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man3/*
