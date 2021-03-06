%global _hardened_build 1
%global majorver 0.7
%global gen_name calculator
%global _default_patch_fuzz 2

Name:		xfce4-calculator-plugin
Version:	0.7.0
Release:	6%{?dist}
Summary:	A calculator plugin for the Xfce4 panel

License:	GPLv2+
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{majorver}/%{name}-%{version}.tar.bz2

Patch0:		https://raw.githubusercontent.com/birdie-github/OpenRGB/master/xfce4-calculator-plugin.do-not-move-cursor.diff

BuildRequires:  gcc-c++
BuildRequires:	automake
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-panel-devel
BuildRequires:	gtk2-devel
BuildRequires:	intltool
BuildRequires:  autoconf automake autogen xfce4-dev-tools libtool
Requires:	xfce4-panel

%description
xfce4-calculator-plugin is a calculator plugin for the Xfce4 panel.

Place the plugin in your panel, enter your calculation into the text field 
and press Enter to calculate the result.

The plugin supports common mathematical operators (+, -, *, /, ^) with usual 
precedence rules and some basic functions (e.g., trigonometric functions) 
and constants.


%prep
%autosetup -p1
# remove empty file
rm -f NEWS

%build
env NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc TODO AUTHORS
%{_libdir}/xfce4/panel/plugins/libcalculator.so
%{_libdir}/xfce4/panel/plugins/libcalculator.la
%{_datadir}/xfce4/panel/plugins/%{gen_name}.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog

* Tue Sep 29 2020 Artem S. Tashkinov <aros gmx com> - 0.7.0-6
- Fix for https://gitlab.xfce.org/panel-plugins/xfce4-calculator-plugin/-/issues/3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 MukundanRagavan <nonamedotc@fedoraproject.org> - 0.7.0-2
- Add translation files and libs

* Sun Mar 10 2019 MukundanRagavan <nonamedotc@fedoraproject.org> - 0.7.0-2
- Fix install of .desktop file

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.6.0-1
- Spec cleanup / modernization
- Bump to 0.6.0 upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-2
- Remove bad config option that got left over by mistake

* Mon Apr 11 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-1
- Initial package
