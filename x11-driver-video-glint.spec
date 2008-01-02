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
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.*
