Name:		tuxnes
Summary:	tuxnes - Linux Nintendo Entertainment System emulator
Summary(pl):	tuxnes - Linuksowy emulator systemu Nintendo
Version:	0.75
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://telia.dl.sourceforge.net/sourceforge/tuxnes/%{name}-%{version}.tar.gz
URL:		http://tuxnes.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define			_prefix		/usr/X11R6/

%description
TuxNES is an emulator for the 8-bit Nintendo Entertainment System.

%description -l pl
TuxNES jest emulatorem 8-bitowego systemu rozrywki Nintendo.

%prep
%setup -q

%build
%configure2_13

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf README AUTHORS BUGS CHANGES COPYING NEWS THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*