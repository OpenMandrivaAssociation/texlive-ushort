Name:		texlive-ushort
Version:	32261
Release:	2
Summary:	Shorter (and longer) underlines and underbars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ushort
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ushort.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
