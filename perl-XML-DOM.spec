
# Conditional build:
%bcond_without tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	DOM
Summary:	Build DOM Level 1 compliant document structures
Name:		perl-XML-DOM
Version:	1.43
Release:	1
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4c3fdd46e7ada0f9db326b493058d4d
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-RegExp
BuildRequires:	perl-libxml >= 0.07
BuildRequires:	perl-libwww
BuildRequires:	perl-XML-Parser >= 2.30
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(XML::DOM)' 'perl-(

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'Dom', that allows XML::Parser to build an Object
Oriented datastructure with a DOM Level 1 compliant interface.
However, there is a new DOM module, XML::GDOME which is under active
development and significantly faster than XML::DOM, since it is based
on the libgdome C library.

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
