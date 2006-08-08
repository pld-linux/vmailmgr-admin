Summary:	Simple administration tools for vmailmgr
Summary(pl):	Proste narzêdzie administracyjne do vmailmgr
Name:		vmailmgr-admin
Version:	0.97
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.xmedia.net/software/%{name}-%{version}.tar.gz
# Source0-md5:	4b48a49ed6faaa4656de662d1dfa69b2
Patch0:		%{name}.restartqmail.patch
URL:		http://em.ca/~bruceg/vmailmgr/
Requires:	php
Requires:	qmail
Requires:	vmailmgrd
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		appdir		/home/services/httpd/html/vmailmgr-admin
%define		cgidir		/home/services/httpd/cgi-bin

%description
This is very simple interface for administering vmailmgr (virtualizing
POP3 password interface).

%description -l pl
Prosty interfejs do administrowania vmailmgr (wirtualizuj±cym
interfejsem hase³ POP3).

%prep
%setup -q
%patch0 -p0

%build
cd c
%{__cc} %{rpmcflags} adduser.c utils.c -oadduser
%{__cc} %{rpmcflags} deluser.c utils.c -odeluser
%{__cc} %{rpmcflags} domainsetup.c utils.c -odomainsetup
%{__cc} %{rpmcflags} maildirmake.c utils.c -omaildirmake
%{__cc} %{rpmcflags} restartqmail.c -orestartqmail
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{appdir},%{cgidir}}

install php/* $RPM_BUILD_ROOT%{appdir}
install c/{adduser,deluser,domainsetup,maildirmake,restartqmail} $RPM_BUILD_ROOT%{cgidir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo -n "In cgi-bin you will find new files: adduser,deluser,domainsetup,maildirmake,restartqmail"
echo "you have to suidroot them to be able to use this software. You have been warned."

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(755,root,root) %{cgidir}/*
%dir %{appdir}
%attr(755,http,http) %{appdir}/*
