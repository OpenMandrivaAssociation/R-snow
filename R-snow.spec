%global packname  snow
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3_10
Release:          1
Summary:          Simple Network of Workstations
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-10.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-utils 
Requires:         R-Rmpi R-rpvm R-rlecuyer R-rsprng R-nws 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils
BuildRequires:    R-Rmpi R-rpvm R-rlecuyer R-rsprng R-nws 

%description
Support for simple parallel computing in R.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R*
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_8-1
+ Revision: 774987
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_7-1
+ Revision: 774661
- Import R-snow
- Import R-snow

