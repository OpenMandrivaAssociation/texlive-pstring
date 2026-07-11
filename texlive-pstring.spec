%global tl_name pstring
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset sequences with justification pointers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pstring
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstring.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstring.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you typeset justified sequences, also called pointing
strings. It's used for instance, in research papers about Game Semantics
to represent sequence of game moves with their associated justification
pointers. Depending on wether using LaTeX or pdfLaTeX, the package uses
PSTricks and pst-node respectively pgf/TikZ.

