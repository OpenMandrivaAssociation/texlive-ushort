# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ushort
# catalog-date 2008-02-29 19:54:55 +0100
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-ushort
Version:	2.2
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Some engineers need underlined or twice underlined variables
for which the usual \underline is too long. This package
provides a generic command for creating underlines of various
sizes and types.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
