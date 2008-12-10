Summary: DBD-Oracle module for perl
Name: perl-DBD-Oracle
Version: 1.22
Release: 2%{?dist}
License:  GPL+ or Artistic
Group: Development/Libraries
Source0: %{name}-%{version}.tar.gz
Url: http://www.cpan.org
BuildRoot: %{_tmppath}/perl-DBD-Oracle-buildroot/
BuildRequires: perl >= 0:5.6.1, perl(DBI)
BuildRequires: oracle-instantclient-devel
BuildRequires: oracle-instantclient-sqlplus
Requires: perl >= 0:5.6.1

%description
DBD-Oracle module for perl

%package explain
Summary: Oora_explain script from DBD-Oracle module for perl
Group: Development/Libraries

%description explain
ora_explain script

%prep
%define modname %(echo %{name}| sed 's/perl-//')
%setup -q -n %{modname}-%{version} 

%build
eval $(perl -V:sitearch)
eval $(perl -V:vendorarch)

MKFILE=$(rpm -ql oracle-instantclient-devel | grep demo.mk)

perl Makefile.PL -m $MKFILE INSTALLDIRS="vendor" PREFIX=%{_prefix}
make  %{?_smp_mflags} OPTIMIZE="%{optflags}"

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} pure_install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | 
    sed "s@^$RPM_BUILD_ROOT@@g" | 
    grep -E -v 'perllocal.pod|\.packlist|ora_explain' \
    > %{modname}-%{version}-filelist
if [ "$(cat %{modname}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi
rm -f `find $RPM_BUILD_ROOT -type f -name perllocal.pod -o -name .packlist`

%files -f %{modname}-%{version}-filelist
%defattr(-,root,root)

%files explain
%defattr(-,root,root)
%{_bindir}/ora_explain
%{_mandir}/man1/ora_explain.1.gz

%changelog
* Tue Nov 25 2008 Miroslav Suchy <msuchy@redhat.com> 1.22-2
- added buildrequires for oracle-lib-compat
- rebased to DBD::Oracle 1.22
- removed DBD-Oracle-1.14-blobsyn.patch

* Thu Oct 16 2008 Milan Zazrivec 1.21-4
- bumped release for minor release tagging
- added %{?dist} to release

* Tue Aug 26 2008 Mike McCune 1.21-3
- Cleanup spec file to work in fedora and our new Makefile structure

* Wed Jul  2 2008 Michael Mraka <michael.mraka@redhat.com> 1.21-2
- rebased to DBD::Oracle 1.21, Oracle Instantclient 10.2.0.4
- ora_explain moved into subpackage

* Wed May 21 2008 Jan Pazdziora - 1.19-8
- rebuild on RHEL 4 as well.

* Fri Dec 05 2007 Michael Mraka <michael.mraka@redhat.com>
- update to DBD::Oracle 1.19 to support oracle-instantclient

* Fri Jun 20 2003 Mihai Ibanescu <misa@redhat.com>
- Linking against Oracle 9i Release 2 client libraries. 

* Sun Nov 11 2001 Chip Turner <cturner@redhat.com>
- update to DBD::Oracle 1.12 to fix LOB bug

* Mon Jul 23 2001 Cristian Gafton <gafton@redhat.com>
- compile against oracle libraries using -rpath setting
- disable as many checks as we can from the default Makefile.PL

* Mon Apr 30 2001 Chip Turner <cturner@redhat.com>
- Spec file was autogenerated. 
