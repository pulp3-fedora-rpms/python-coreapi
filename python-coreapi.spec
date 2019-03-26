# Created by pyp2rpm-3.3.2
%global pypi_name coreapi

Name:           python-%{pypi_name}
Version:        2.3.3
Release:        1%{?dist}
Summary:        Python client library for Core API

License:        BSD
URL:            https://github.com/core-api/python-client
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(coreschema)
Requires:       python3dist(itypes)
Requires:       python3dist(requests)
Requires:       python3dist(setuptools)
Requires:       python3dist(uritemplate)
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/coreapi/codecs
%{python3_sitelib}/coreapi/transports
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Feb 27 2019 Mike DePaulo <mikedep333@gmail.com> - 2.3.3-1
- Initial package.
