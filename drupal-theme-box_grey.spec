%define		themename box_grey
Summary:	Drupal Theme Box_grey
Name:		drupal-theme-%{themename}
Version:	4.6.0
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{themename}-%{version}.tar.gz
# Source0-md5:	26ba07cd642dcf917eca0bbfe331ea7d
URL:		http://drupal.org/node/11624
Requires:	drupal >= 4.6.0
Requires:	drupal-themeengine-phptemplate >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir		%{_datadir}/drupal/themes
%define		_themehtmldir	%{_datadir}/drupal/htdocs/themes

%description
Box_grey is intended to be relatively easy to modify for those that
aren't competent in css positioning, but can manage css colours,
backgrounds and borders (or are at least willing to try). It's
designed to be fairly robust with different sizes of content and
lastly has a neutral grey colour scheme which will hopefully encourage
people to change it.

%prep
%setup -q -n %{themename}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_themehtmldir},%{_themedir}}/%{themename}

# box_grey
install *.{css,png}  $RPM_BUILD_ROOT%{_themehtmldir}/%{themename}
install *.tpl.php $RPM_BUILD_ROOT%{_themedir}/%{themename}
ln -s ../../htdocs/themes/%{themename}/screenshot.png $RPM_BUILD_ROOT%{_themedir}/%{themename}

# theme style box_cleanslate
install -d $RPM_BUILD_ROOT{%{_themehtmldir}/%{themename}/box_cleanslate,%{_themedir}}/%{themename}}
install box_cleanslate/*.{css,png} $RPM_BUILD_ROOT%{_themehtmldir}/%{themename}/box_cleanslate
ln -s ../../htdocs/themes/%{themename}/box_cleanslate $RPM_BUILD_ROOT%{_themedir}/%{themename}/box_cleanslate

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_themedir}/%{themename}
%{_themehtmldir}/%{themename}