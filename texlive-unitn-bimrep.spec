Name:		texlive-unitn-bimrep
Version:	45581
Release:	2
Summary:	A bimonthly report class for the PhD School of Materials, Mechatronics and System Engineering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unitn-bimrep
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitn-bimrep.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitn-bimrep.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to rapidly write the bimonthly report for
The Ph.D. School in Materials, Mechatronics and System
Engineering. It allows to define the research activities, the
participation to school and congress, and the publication
performed by a student.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/unitn-bimrep
%doc %{_texmfdistdir}/doc/latex/unitn-bimrep

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
