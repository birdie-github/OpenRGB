%global _name OpenRGB
%global _lto_cflags %nil

Name:           openrgb
Version:        0.7
Release:        1%{?dist}
Summary:        Open source RGB lighting control that doesn't depend on manufacturer software

License:        GPLv2
URL:            https://gitlab.com/CalcProgrammer1/%{_name}
Source0:        https://gitlab.com/CalcProgrammer1/%{_name}/-/archive/release_%{version}/OpenRGB-release_%{version}.tar.bz2
Source1:        %{_name}.desktop

BuildRequires:  gcc-c++ libusb-devel libstdc++-devel qt5-qtbase-devel desktop-file-utils hidapi-devel mbedtls-devel systemd-rpm-macros
Requires:       hicolor-icon-theme

%description
Open source RGB lighting control that doesn't depend on manufacturer software. Supports Windows and Linux.

ASUS, ASRock, Corsair, G.Skill, Gigabyte, HyperX, MSI, Razer, ThermalTake, and more supported

%prep
%autosetup -p1 -n %{_name}-release_%{version}

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

#icon
install -Dpm 644 qt/%{_name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{_name}.png

#desktop
desktop-file-install %{SOURCE1}

%post -n %{name}
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{_name}.png
%{_datadir}/applications/%{_name}.desktop
%{_metainfodir}/org.%{name}.%{_name}.metainfo.xml
%{_udevrulesdir}/60-%{name}.rules
%license LICENSE
%doc README.md

%changelog
* Thu Apr 18 2022 Artem S. Tashkinov <aros gmx com> - 0.7-1
- Disabled -flto because it makes the app crash when when parsing a config file

* Thu Dec 30 2021 Artem S. Tashkinov <aros gmx com> - 0.7-0
- Updated to 0.7

* Sat Jul 24 2021 Artem S. Tashkinov <aros gmx com> - 0.6-0
- Updated to 0.6

* Mon Dec 07 2020 Artem S. Tashkinov <aros gmx com> - 0.5-0
- Updated to 0.5

* Mon Sep 28 2020 Artem S. Tashkinov <aros gmx com> - 0.4-0
- Updated to 0.4

* Sat May 16 2020 Carlos Mogas da Silva <r3pek@r3pek.org> - 0.2-2
- Applied review changes in https://bugzilla.redhat.com/show_bug.cgi?id=1835958#c1

* Thu May 14 2020 Carlos Mogas da Silva <r3pek@r3pek.org> - 0.2-1
- Initial import
