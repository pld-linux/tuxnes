Summary:	tuxnes - Linux Nintendo Entertainment System emulator
Summary(pl):	tuxnes - Linuksowy emulator systemu Nintendo
Name:		tuxnes
Version:	0.75
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://telia.dl.sourceforge.net/sourceforge/tuxnes/%{name}-%{version}.tar.gz
URL:		http://tuxnes.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
TuxNES is an emulator for the 8-bit Nintendo Entertainment System.

%description -l pl
TuxNES jest emulatorem 8-bitowego systemu rozrywki Nintendo.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS BUGS CHANGES NEWS THANKS
%attr(755,root,root) %{_bindir}/*
