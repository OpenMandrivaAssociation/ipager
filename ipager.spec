%define name    ipager
%define version 1.1.0
%define release %mkrel 3
%define Summary IPager : a pager for *WM

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        MIT
Group:          Graphical desktop/Other
URL:            http://www.useperl.ru/ipager
Source0:        http://www.useperl.ru/ipager/src/%name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
Patch0:         ipager-1.1.0-sconstruct.diff
BuildRequires:	scons
BuildRequires:  imlib2-devel
BuildRequires:  X11-devel

%description
IPager is a pager!
Originally it was developed for Fluxbox but can also be used with other WMs.

features

    * Zoom! When the mouse pointer is over it, desktop image enlarges.
    * Various image zoom effects.

A flexible set of config options makes IPager an integral part of your desktop.

    * Main window transparency.
    * Transparent workspaces icons.
    * Main window background color.
    * Workspace icon: a defined color or transparent.
    * Borders: can be applied to main window and to workspace icons.
    * Switch workspaces: any mouse button upon your choice.
    * You can send a window from one workspace to another
    * Application icons are also supported

A range of various color themes allows you to easily integrate IPager into your
desktop.

%prep
%{__rm} -rf $RPM_BUILD_ROOT
%setup -q
%patch -p0
%build
scons

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
scons PREFIX=$RPM_BUILD_ROOT/usr install

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%defattr(0644,root,root,0755)
%doc README ToDo ChangeLog LICENSE themes/*


