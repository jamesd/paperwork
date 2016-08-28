# paperwork is a python2-only app; unstable has been converted to python3
Name:           paperwork
Version:        0.3.2
Release:        1%{?dist}
Summary:        A personal document manager for scanned documents

License:        gplv3+
URL:            https://github.com/jflesch/paperwork/wiki
Source0:        https://github.com/jflesch/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  enchant-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  python-devel
BuildRequires:  python-pillow-devel
BuildRequires:  python-setuptools
BuildRequires:  zlib-devel
Requires:  gtk3
Requires:  poppler-glib
Requires:  pycairo
Requires:  pygobject3
Requires:  python-Levenshtein
Requires:  python-enchant
Requires:  python-pycountry
Requires:  python-pyocr
Requires:  python-simplebayes
Requires:  python-termcolor
Requires:  python-whoosh
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
%{__python2} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


# %check
# %{__python2} setup.py test


%files
%license COPYING
%doc AUTHORS README.markdown example-paperwork.conf ChangeLog
%{python2_sitelib}/*
%{_datadir}/applications/paperwork.desktop
%{_datadir}/%{name}
%{_datadir}/locale
%{_datadir}/icons
%{_bindir}/%{name}
%{_bindir}/paperwork-chkdeps

%changelog
* Tue Aug 23 2016 James Davidson <james@greycastle.net>
- Initial packaging
