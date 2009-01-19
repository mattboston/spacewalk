Summary: RHN support for yum
Name: yum-rhn-plugin
Source: %{name}-%{version}.tar.gz
Source1: version
Version: %(echo `awk '{ print $1 }' %{SOURCE1}`)
#Release: %(echo `awk '{ print $2 }' %{SOURCE1}`)%{?dist}
Release: %{expand: %(awk '{ print $2 }' %{SOURCE1})}
License: GPLv2
Group: System Environment/Base
Url: http://rhn.redhat.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python
BuildRequires: rhpl
BuildRequires: intltool
BuildRequires: gettext

Requires: yum >= 3.0-5.3
Requires: rhn-client-tools >= 0.4.19

# Not really, but for upgrades we need these
Requires: rhn-setup
Obsoletes: up2date

%description
This yum plugin provides support for yum to access a Red Hat Network server for
software updates.

%prep
%setup -q

%build
make -f Makefile.yum-rhn-plugin

%install
rm -rf $RPM_BUILD_ROOT
make -f Makefile.yum-rhn-plugin install VERSION=%{version}-%{release} PREFIX=$RPM_BUILD_ROOT MANPATH=%{_mandir} 

%find_lang %{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/rhnplugin.conf

%dir /var/lib/up2date

%{_mandir}/man5/rhnplugin.conf.5*
%{_mandir}/man8/rhnplugin.8*
%{_mandir}/man8/yum-rhn-plugin.8*

/usr/lib/yum-plugins/rhnplugin.py
/usr/lib/yum-plugins/rhnplugin.pyc
/usr/lib/yum-plugins/rhnplugin.pyo

/usr/share/rhn/actions/packages.py
/usr/share/rhn/actions/packages.pyc
/usr/share/rhn/actions/packages.pyo


%changelog
* Tue Nov 11 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-30%{?dist}
- Resolves: #470988

* Fri Oct 24 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-28%{?dist}
- Resolves: #467043

* Tue Oct 21 2008 John Matthews <jmatthews@redhat.com> - 0.5.3-27%{?dist}
- Updated rhn-client-tools requires to 0.4.19 or greater

* Thu Sep 18 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-26%{?dist}
- Resolves: #431082 #436043 #436804 #441265 #448012 #448044 #449726
- Resolves: #450241 #453690 #455759 #455760 #456540 #457191  #462499

* Wed Aug  6 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-20%{?dist}
- new build

* Tue Aug  5 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-12%{?dist}
- Resolves: #457190

* Tue May 20 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-12%{?dist}-
- new build

* Mon May 19 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-6
- Resolves: #447402

* Tue Mar 11 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-6
- Resolves: #438175

* Tue Mar 11 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-5
- Resolves: #435840

* Tue Mar 11 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-4
- Resolves: #433781

* Wed Jan 16 2008 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.3-3
- Resolves: #222327, #226151, #245013, #248385, #251915, #324141 
- Resolves: #331001, #332011, #378911

* Fri Aug 17 2007 Pradeep Kilambi <pkilambi@redhat.com>  - 0.5.2-3
- Resolves: #232567

* Tue Jul 17 2007 Pradeep Kilambi <pkilambi@redhat.com> - 0.5.2-2
- Resolves: #250638

* Tue Jul 17 2007 James Slagle <jslagle@redhat.com> - 0.5.2-1
- Patch from katzj@redhat.com for yum 3.2.x compatibility
- Resolves: #243769

* Thu Jun 26 2007 Shannon Hughes <shughes@redhat.com> - 0.5.1-2
- Resolves: #232567, #234880, #237300

* Thu Dec 14 2006 John Wregglesworth <wregglej@redhat.com> - 0.3.1-1
- Updated translations.
- Related: #216835

* Wed Dec 13 2006 James Bowes <jbowes@redhat.com> - 0.3.0-2
- Add requires for rhn-setup.
- Related: #218617

* Mon Dec 11 2006 James Bowes <jbowes@redhat.com> - 0.3.0-1
- Updated translations.
- Related: #216835

* Tue Dec 05 2006 James Bowes <jbowes@redhat.com> - 0.2.9-1
- Updated translations.

* Fri Dec 01 2006 James Bowes <jbowes@redhat.com> - 0.2.8-1
- Updated translations.

* Thu Nov 30 2006 James Bowes <jbowes@redhat.com> - 0.2.7-1
- New and updated translations.

* Tue Nov 28 2006 James Bowes <jbowes@redhat.com> - 0.2.6-1
- Reauthenticate with RHN if the session expires.
- Resolves: #217706

* Tue Nov 28 2006 James Bowes <jbowes@redhat.com> - 0.2.5-1
- New and updated translations.

* Mon Nov 20 2006 James Bowes <jbowes@redhat.com> - 0.2.4-1
- Fix for #215602

* Mon Nov 13 2006 James Bowes <jbowes@redhat.com> - 0.2.3-1
- Add man pages.

* Fri Nov 03 2006 James Bowes <jbowes@redhat.com> - 0.2.2-1
- Fix for #213793

* Mon Oct 30 2006 James Bowes <jbowes@redhat.com> - 0.2.1-1
- New translations.
- Fixes for #212255, #213031, #211568

* Tue Oct 25 2006 James Bowes <jbowes@redhat.com> - 0.2.0-1
- Use sslCACert rather than sslCACert[0]. Related to #212212.

* Tue Oct 24 2006 James Bowes <jbowes@redhat.com> - 0.1.9-3
- add BuildRequires: gettext

* Tue Oct 24 2006 James Bowes <jbowes@redhat.com> - 0.1.9-2
- add BuildRequires: intltool

* Tue Oct 24 2006 James Bowes <jbowes@redhat.com> - 0.1.9-1
- fixes for #181830, #208852, #206941

* Tue Oct 24 2006 James Bowes <jbowes@redhat.com> - 0.1.8-1
- Require a version of rhn-client-tools that doesn't provide up2date.
- package the translation files.

* Fri Oct 13 2006 James Bowes <jbowes@redhat.com> - 0.1.7-2
- Obsolete up2date

* Wed Oct 11 2006 James Bowes <jbowes@redhat.com> - 0.1.7-1
- New version.
- Don't always assume we have an optparser.

* Thu Oct 05 2006 James Bowes <jbowes@redhat.com> - 0.1.6-1
- New version.

* Fri Sep 15 2006 James Bowes <jbowes@redhat.com> - 0.1.5-1
- Require rhpl for translation.

* Thu Sep 14 2006 James Bowes <jbowes@redhat.com> - 0.1.0-1
- New version.
- Require rhn-client-tools >= 0.1.4.
- Stop ghosting pyo files.

* Thu Aug 10 2006 James Bowes <jbowes@redhat.com> - 0.0.9-1
- New version.
- Fix for bz #202091 pirut crashes after installing package

* Mon Aug 07 2006 James Bowes <jbowes@redhat.com> - 0.0.8-2
- Set gpg checking from the plugin's config.

* Thu Aug 03 2006 James Bowes <jbowes@redhat.com> - 0.0.8-1
- New version.

* Mon Jul 31 2006 James Bowes <jbowes@redhat.com> - 0.0.7-1
- New version.

* Mon Jul 31 2006 James Bowes <jbowes@redhat.com> - 0.0.6-1
- Fix for bz #200697 – yum-rhn-plugin causes yum to fail
  under rhel5-server

* Thu Jul 27 2006 James Bowes <jbowes@redhat.com> - 0.0.5-1
- New version.

* Thu Jul 20 2006 James Bowes <jbowes@redhat.com> - 0.0.4-1
- New version.

* Wed Jul 19 2006 James Bowes <jbowes@redhat.com> - 0.0.3-3
- Correct buildroot location.

* Wed Jul 19 2006 James Bowes <jbowes@redhat.com> - 0.0.3-2
- Spec file cleanups.

* Wed Jul 12 2006 James Bowes <jbowes@redhat.com> - 0.0.3-1
- Install the packages action.

* Thu May 18 2006 James Bowes <jbowes@redhat.com> - 0.0.2-1
- Make Evr checking on rhn packages more exact.

* Mon Apr 17 2006 James Bowes <jbowes@redhat.com> - 0.0.1-2
- Update requirements for yum >= 2.9.0

* Tue Feb 28 2006 James Bowes <jbowes@redhat.com> - 0.0.1-1
- Initial version.
