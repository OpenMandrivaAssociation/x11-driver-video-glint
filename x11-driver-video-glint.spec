Name: x11-driver-video-glint
Version: 1.2.8
Release: 2
Summary: X.org driver for 3DLabs Permedia
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glint-%{version}.tar.bz2

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(gl)

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-glint is the X.org driver for 3DLabs Permedia.

%prep
%setup -qn xf86-video-glint-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.8-1
+ Revision: 810712
- version update 1.2.8

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.7-2
+ Revision: 787225
- Rebuild for x11-server 1.12

* Thu Feb 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.7-1
+ Revision: 775107
- version update 1.2.7

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.6-3
+ Revision: 748402
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.6-2
+ Revision: 703746
- rebuild for new x11-server

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.6-1
+ Revision: 699287
- update to new version 1.2.6

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.5-5
+ Revision: 683574
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-4
+ Revision: 671148
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.5-3mdv2011.0
+ Revision: 595741
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.5-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Sun Sep 12 2010 Thierry Vignaud <tv@mandriva.org> 1.2.5-1mdv2011.0
+ Revision: 577826
- new release

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.4-1mdv2010.0
+ Revision: 407745
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.3-1mdv2010.0
+ Revision: 391863
- update to version 1.2.3

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.2-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.2-1mdv2009.1
+ Revision: 317847
- New version 1.2.2

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 308167
- rebuild for new X server
- new release 1.2.1

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265920
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194207
- Update to version 1.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-7mdv2008.1
+ Revision: 165554
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-6mdv2008.1
+ Revision: 156605
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-5mdv2008.1
+ Revision: 154859
- Updated BuildRequires and resubmit package.
- Modify glint driver to match pattern used in all other xorg driver modules.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-4mdv2008.1
+ Revision: 98692
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2008.0
+ Revision: 75759
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

