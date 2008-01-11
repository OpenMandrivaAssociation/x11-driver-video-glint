%define debug_package	%{nil}

Name: x11-driver-video-glint
Version: 1.1.1
Release: %mkrel 4
Summary: The X.org driver for 3DLabs Permedia
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-glint  xorg/drivers/xf86-video-glint
# cd xorg/drivers/xf86-video/glint
# git-archive --format=tar --prefix=xf86-video-glint-1.1.1/ xf86-video-glint-1.1.1@mandriva | bzip2 -9 > xf86-video-glint-1.1.1.tar.bz2
########################################################################
Source0: xf86-video-glint-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-glint-1.1.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros >= 1.1.5-4mdk
#BuildRequires: gcc-4.2.2-2mdv2008.1
#BuildRequires: glibc-devel-2.7-1mdv2008.1
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.4


BuildRequires: GL-devel
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for 3DLabs Permedia

%prep
%setup -q -n xf86-video-glint-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.*
