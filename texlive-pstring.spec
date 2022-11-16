Name:		texlive-pstring
Version:	42857
Release:	1
Summary:	Typeset sequences with justification pointers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pstring
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstring.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstring.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you typeset justified sequences, also called
pointing strings. It's used for instance, in research papers
about Game Semantics to represent sequence of game moves with
their associated justification pointers. Depending on wether
using LaTeX or pdfLaTeX, the package uses PSTricks and pst-node
respectively pgf/TikZ.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pstring
%doc %{_texmfdistdir}/doc/latex/pstring

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
