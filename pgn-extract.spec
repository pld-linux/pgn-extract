Summary:	Utility to extract and manipulate chess games in PGN format
Summary(pl):	narzêdzie do ekstrakcji partii szachowych z plików w formacie PGN i manipulowania nimi
Name:		pgn-extract
Version:	15.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.cs.kent.ac.uk/pub/djb/Extract/%{name}.tgz
# Source0-md5:	ae83686650900af4d027e17b6e34f361
Patch0:		%{name}-makefile.patch
#Patch1:	extract-moves.patch
#Patch2:	extract-egcs.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small utility can extract and manipulate chess game files in PGN
format.

%description -l pl
Jest to niewielki program s³u¿±cy do ekstrakcji partii szachowych z
plików w formacie PGN i do manipulowania nimi.

%prep
%setup -q -c
%patch0 -p1
#%patch1
#%patch2

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/bin,%{_prefix}/lib/games/pgn-extract}
cp pgn-extract $RPM_BUILD_ROOT%{_prefix}/bin/
install -d $RPM_BUILD_ROOT%{_prefix}/lib/games/pgn-extract
cp eco.pgn $RPM_BUILD_ROOT%{_prefix}/lib/games/pgn-extract

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README help.html
%attr(755,root,root) %{_prefix}/bin/*
%{_prefix}/lib/games/pgn-extract
