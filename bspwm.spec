Summary:	A tiling window manager based on binary space partitioning
Name:		bspwm
Version:	0.9.12
Release:	1
Group:		Development/X11
License:	BSD
URL:		https://github.com/baskerville/bspwm
Source0:	https://github.com/baskerville/bspwm/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(xcb-ewmh)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-util)

%description
bspwm is a tiling window manager that represents windows as the leaves of a
full binary tree.

It only responds to X events, and the messages it receives on a dedicated
socket.

bspc is a program that writes messages on bspwm's socket.

bspwm doesn't handle any keyboard or pointer inputs: a third party program
(e.g. sxhkd) is needed in order to translate keyboard and pointer events to
bspc invocations.

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/bspc
%{_datadir}/bash-completion/completions/bspc
%{_datadir}/zsh/site-functions/_bspc
%{_datadir}/fish/vendor_completions.d/bspc.fish
%{_datadir}/xsessions/%{name}.desktop
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/bspc.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%before_configure
%make_build

%install
%make_install PREFIX="%{_prefix}"

