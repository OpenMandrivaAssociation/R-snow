%global packname  snow
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3_7
Release:          1
Summary:          Simple Network of Workstations
Group:            Sciences/Mathematics
License:          GPL
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/snow/snow_0.3-7.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-utils 
Requires:         R-Rmpi R-rpvm R-rlecuyer R-rsprng R-nws 
BuildRequires:    R-devel texlive-collection-latex R-utils
BuildRequires:    R-Rmpi R-rpvm R-rlecuyer R-rsprng R-nws 

%description
Support for simple parallel computing in R.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R*
%{rlibdir}/%{packname}/help
