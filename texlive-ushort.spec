# revision 32261
# category Package
# catalog-ctan /macros/latex/contrib/ushort
# catalog-date 2012-04-09 09:24:18 +0200
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-ushort
Version:	2.2
Release:	3
Summary:	Shorter (and longer) underlines and underbars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ushort
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Some engineers need underlined or twice underlined variables
for which the usual \underline is too long. This package
provides a generic command for creating underlines of various
sizes and types.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ushort/ushort.sty
%doc %{_texmfdistdir}/doc/latex/ushort/README
%doc %{_texmfdistdir}/doc/latex/ushort/ushort.pdf
%doc %{_texmfdistdir}/doc/latex/ushort/ushort.tex
%doc %{_texmfdistdir}/doc/latex/ushort/ushort.txt
#- source
%doc %{_texmfdistdir}/source/latex/ushort/ushort.dtx
%doc %{_texmfdistdir}/source/latex/ushort/ushort.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
