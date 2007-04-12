Name: x11-driver-video-glint
Version: 1.1.1
Release: %mkrel 2
Summary: The X.org driver for 3DLabs Permedia
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glint-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

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

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/glint_drv.la
%{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.4.bz2

