Summary:	tuxnes - Linux Nintendo Entertainment System emulator
Summary(pl):	tuxnes - linuksowy emulator systemu Nintendo
Name:		tuxnes
Version:	0.75
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/tuxnes/%{name}-%{version}.tar.gz
# Source0-md5:	5db0cd42dfdff3e681805e93b4867c43
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
%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS BUGS ChangeLog CHANGES NEWS THANKS
%attr(755,root,root) %{_bindir}/*
