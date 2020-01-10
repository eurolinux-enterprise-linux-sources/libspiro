Name:           libspiro
Version:        20071029
Release:        10%{?dist}
Summary:        Library to simplify the drawing of beautiful curves

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://libspiro.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_src-%{version}.tar.bz2
# Patch to add aarch64 support
Patch0:         http://ausil.fedorapeople.org/aarch64/libspiro/libspiro-aarch64.patch

%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libspiro-20071029

%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README gpl.txt README-RaphLevien
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sat Mar 23 2013 Kevin Fenzi <kevin@scrye.com> 20071029-10
- Add patch to add aarch64 support. Fixes bug #925890

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Parag <paragn AT fedoraproject DOT org> - 20071029-8
- Resolves:rh#879153 - spec cleanup for recent packaging guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 20071029-6
- rebuild for gcc 4.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 15 2009 Parag <paragn AT fedoraproject.org> - 20071029-4
- Fix rpmlint error "libspiro.src:53: E: files-attr-not-set"

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Kevin Fenzi <kevin@tummy.com> - 20071029-1
- Initial version for Fedora
