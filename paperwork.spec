Name:           paperwork
Version:        1.2.1
Release:        1%{?dist}
Summary:        A personal document manager for scanned documents

License:        gplv3+
URL:            https://github.com/jflesch/paperwork/wiki
Source0:        https://github.com/jflesch/%{name}/archive/%{version}/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  enchant-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pillow-devel
BuildRequires:  python3-setuptools
BuildRequires:  zlib-devel
Requires:  gtk3
Requires:  libpillowfight
Requires:  paperwork-backend = %{version}
Requires:  poppler-glib
Requires:  pycairo
Requires:  pygobject3
Requires:  python-termcolor
Requires:  python3-Levenshtein
Requires:  python3-enchant
Requires:  python3-pillowfight
Requires:  python3-pycountry
Requires:  python3-pyinsane
Requires:  python3-pyocr
Requires:  python3-simplebayes
Requires:  python3-whoosh
Requires:  tesseract


%description
Paperwork is a personal document manager for scanned documents (and
PDFs).

It's designed to be easy and fast to use. The idea behind Paperwork is
"scan & forget": You should be able to just scan a new document and
forget about it until the day you need it again.

In other words, let the machine do most of the work for you.


%prep
%autosetup


%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


# %check
# %{__python3} setup.py test


%files
%license COPYING
%doc AUTHORS README.markdown example-paperwork.conf ChangeLog
%{python3_sitelib}/*
%{_bindir}/%{name}


%changelog
* Thu Sep 21 2017 James Davidson <james@greycastle.net> - 1.2.1-1
- Update to 1.2.1

* Tue Nov 22 2016 James Davidson <james@greycastle.net> - 1.0.5-1
- Update on 1.0.5

* Sat Nov 19 2016 James Davidson <james@greycastle.net> - 1.0.4-1
- Update to 1.0.4

* Fri Nov 18 2016 James Davidson <james@greycastle.net> - 1.0.3-1
- Update to 1.0.3

* Tue Aug 23 2016 James Davidson <james@greycastle.net>
- Initial packaging
