Summary:	Utility to extract and manipulate chess games in PGN format.
Name:		extract
Version:	1.0
Release:	4
License:	GPL
Group:		Applications/Games
Source0:	ftp://mango.ukc.ac.uk/djb/Extract/%{name}.tar.gz
# Source0-md5:	10eb7480f285b1f738a5c9593d7855ec
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-moves.patch
Patch2:		%{name}-egcs.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small utility can extract and manipulate chess game files in PGN
format.

%prep
%setup -q -c
%patch -p1
%patch1
%patch2

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/bin,%{_prefix}/lib/games/extract}
cp extract $RPM_BUILD_ROOT%{_prefix}/bin/
install -d $RPM_BUILD_ROOT%{_prefix}/lib/games/extract
cp eco.pgn $RPM_BUILD_ROOT%{_prefix}/lib/games/extract

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_prefix}/bin/*
%{_prefix}/lib/games/extract
