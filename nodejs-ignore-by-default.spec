%{?scl:%scl_package nodejs-ignore-by-default}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name ignore-by-default

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.0.1
Release:    3%{?dist}
Summary:    A list of directories you should ignore by default
License:    ISC
URL:        https://github.com/novemberborn/ignore-by-default#readme
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
A list of directories you should ignore by default

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- rh-nodejs8 rebuild

* Tue Nov 01 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-2
- Initial build

