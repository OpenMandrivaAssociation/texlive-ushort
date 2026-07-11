%global tl_name ushort
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Shorter (and longer) underlines and underbars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ushort
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Some engineers need underlined or twice underlined variables for which
the usual \underline is too long. This package provides a generic
command for creating underlines of various sizes and types.

