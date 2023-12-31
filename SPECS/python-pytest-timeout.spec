%global pypi_name pytest-timeout

Name:           python-%{pypi_name}
Version:        1.4.2
Release:        7%{?dist}
Summary:        py.test plugin to abort hanging tests

License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout
Source0:        %{pypi_source}

# This patch skips 3 tests out of 38 because of missing dependency
# python-pexpect in RHEL 9
Patch1:         0001-Remove-test-only-dependency-pexpect.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest} >= 3.6.0
BuildRequires:  %{py3_dist setuptools}

%global _description %{expand:
This is a plugin which will terminate tests after a certain timeout. When doing
so it will show a stack dump of all threads running at the time. This is useful
when running tests under a continuous integration server or simply if you don’t
know why the test suite hangs.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -k "not test_cov"


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/pytest_timeout*
%{python3_sitelib}/__pycache__/pytest_timeout*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.2-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 15 2021 Tomas Orsava <torsava@redhat.com> - 1.4.2-6
- Remove test-dependency on python-pexpect

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.2-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 30 2021 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-4
- Don't BuildRequire python3-pytest-cov
Resolves: rhbz#1945252

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Scott Talbert <swt@techie.net> - 1.4.2-1
- Update to new upstream release 1.4.2 (#1857421)

* Fri Jun 26 2020 Scott Talbert <swt@techie.net> - 1.4.1-2
- Add missing BR for setuptools

* Tue Jun 16 2020 Scott Talbert <swt@techie.net> - 1.4.1-1
- Update to new upstream release 1.4.1 (#1846923)
- Modernize packaging

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Scott Talbert <swt@techie.net> - 1.3.4-1
- Update to new upstream release (#1788278)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-6
- Rebuilt for Python 3.8

* Thu Aug 08 2019 Scott Talbert <swt@techie.net> - 1.3.3-5
- Remove Python 2 subpackages (#1737398)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-3
- Add upstream patch for pytest 4 compatibility

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Scott Talbert <swt@techie.net> - 1.3.3-1
- New upstream release 1.3.3

* Tue Oct 23 2018 Scott Talbert <swt@techie.net> - 1.3.2-1
- New upstream release 1.3.2

* Fri Sep 14 2018 Scott Talbert <swt@techie.net> - 1.3.1-2
- Disable writing bytecode when running tests to avoid packaging pycache files

* Tue Jul 24 2018 Scott Talbert <swt@techie.net> - 1.3.1-1
- New upstream release 1.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Scott Talbert <swt@techie.net> - 1.3.0-1
- New upstream release 1.3.0

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Scott Talbert <swt@techie.net> - 1.2.1-1
- New upstream release 1.2.1 (fixes FTBFS #1590256)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Scott Talbert <swt@techie.net> - 1.2.0-3
- Updated to use versioned dependency name

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Scott Talbert <swt@techie.net> - 1.2.0-1
- New upstream release 1.2.0
- Enable tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Thu Aug 11 2016 Scott Talbert <swt@techie.net> - 1.0.0-1
- Initial package.
