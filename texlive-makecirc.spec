%global tl_name makecirc
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A MetaPost library for drawing electrical circuit diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/makecirc
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecirc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecirc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MakeCirc is a MetaPost library that contains diverse symbols for use in
circuit diagrams. MakeCirc offers a high quality tool, with a simple
syntax. MakeCirc is completely integrated with LaTeX documents and with
other MetaPost drawing/graphic. Its output is a PostScript file.
MakeCirc only requires (La)TeX and MetaPost to work.

