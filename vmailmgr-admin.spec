Summary:	Simple aministration tools for vmailmgr (virtualizing POP3 password interface)
Name:		vmailmgr-admin
Version:	0.97
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
SOURCE:		http://www.xmedia.net/software/vmailmgr-admin-%{version}.tar.gz
Patch:		vmailmgr-admin.restartqmail.patch
#URL:		http://em.ca/~bruceg/vmailmgr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	php
Requires:	webserver
Requires:	qmail
Requires:	vmailmgrd



%description
This is very simple interface for administering vmailmgr.

%prep
%setup -q
%patch -p0
%build
cd c
%{__cc} -O2 adduser.c utils.c -oadduser
%{__cc} -O2 deluser.c utils.c -odeluser
%{__cc} -O2 domainsetup.c utils.c -odomainsetup
%{__cc} -O2 maildirmake.c utils.c -omaildirmake
%{__cc} -O2 restartqmail.c -orestartqmail
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{home/httpd/{cgi-bin,html/vmailmgr-admin}}
install -d $RPM_BUILD_ROOT/usr/share/doc/%{name}
install php/* $RPM_BUILD_ROOT/home/httpd/html/vmailmgr-admin/
install c/{adduser,deluser,domainsetup,maildirmake,restartqmail} $RPM_BUILD_ROOT/home/httpd/cgi-bin/

gzip -9nf {INSTALL,README,COPYING}
%post
echo -n "In cgi-bin you will find new files: adduser,deluser,domainsetup,maildirmake,restartqmail "
echo "you have to suidroot them to be able to use this software. You have been warned.  "

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,httpd,httpd) /home/httpd/cgi-bin/*
%attr(755,httpd,httpd) /home/httpd/html/%{name}/*
