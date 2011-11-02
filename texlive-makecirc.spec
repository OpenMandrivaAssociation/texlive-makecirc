Name:		texlive-makecirc
Version:	20061119
Release:	1
Summary:	A MetaPost library for drawing electrical circuit diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/makecirc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecirc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecirc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
MakeCirc is a MetaPost library that contains diverse symbols
for use in circuit diagrams. MakeCirc offers a high quality
tool, with a simple syntax. MakeCirc is completely integrated
with LaTeX documents and with other MetaPost drawing/graphic.
Its output is a PostScript file. MakeCirc only requires (La)TeX
and MetaPost to work.

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
%{_texmfdistdir}/metapost/makecirc/ejemplos.mp
%{_texmfdistdir}/metapost/makecirc/latex.mp
%{_texmfdistdir}/metapost/makecirc/makecirc.mp
%doc %{_texmfdistdir}/doc/metapost/makecirc/MakeCirc-en.pdf
%doc %{_texmfdistdir}/doc/metapost/makecirc/MakeCirc.pdf
%doc %{_texmfdistdir}/doc/metapost/makecirc/README
%doc %{_texmfdistdir}/doc/metapost/makecirc/ejemplos.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
