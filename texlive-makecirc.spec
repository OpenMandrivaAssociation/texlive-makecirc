Name:		texlive-makecirc
Version:	15878
Release:	2
Summary:	A MetaPost library for drawing electrical circuit diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/makecirc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecirc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecirc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MakeCirc is a MetaPost library that contains diverse symbols
for use in circuit diagrams. MakeCirc offers a high quality
tool, with a simple syntax. MakeCirc is completely integrated
with LaTeX documents and with other MetaPost drawing/graphic.
Its output is a PostScript file. MakeCirc only requires (La)TeX
and MetaPost to work.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/makecirc/ejemplos.mp
%{_texmfdistdir}/metapost/makecirc/latex.mp
%{_texmfdistdir}/metapost/makecirc/makecirc.mp
%doc %{_texmfdistdir}/doc/metapost/makecirc/MakeCirc-en.pdf
%doc %{_texmfdistdir}/doc/metapost/makecirc/MakeCirc.pdf
%doc %{_texmfdistdir}/doc/metapost/makecirc/README
%doc %{_texmfdistdir}/doc/metapost/makecirc/ejemplos.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
