%define _disable_ld_no_undefined 1

Summary:  	X.org driver for 3DLabs Permedia
Name:		x11-driver-video-glint
Version:	1.2.9
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glint-%{version}.tar.bz2

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-glint is the X.org driver for 3DLabs Permedia.

%prep
%setup -qn xf86-video-glint-%{version}
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.*

