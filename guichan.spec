%define	name	guichan
%define	version	0.7.1
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Portable C++ GUI library for games using Allegro, SDL and OpenGL

Group:          Development/Libraries
License:        BSD
URL:            http://guichan.sourceforge.net
Source0:        http://guichan.googlecode.com/files/guichan-%{version}.tar.gz
Patch0:         guichan-0.7.1-soname.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  allegro-devel, SDL-devel, SDL_image-devel, GL-devel

%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different objects for 
displaying graphics and grabbing user input.

%package devel
Summary:        Header and libraries for guichan development
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package includes header and libraries files for development using
guichan, a small and efficient C++ GUI library designed for games. This
package is needed to build programs written using guichan.

%prep
%setup -q -n %{name}-%{version}
for i in src/Makefile.am src/*/Makefile.am ; do
    touch -r $i $i.stamp
done
%patch0 -p1
for i in src/Makefile.am src/*/Makefile.am ; do
    touch -r $i.stamp $i
done


%build
libtoolize --copy --force
aclocal
autoconf
%configure
%make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Removing Libtool archives and static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif


%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libguichan-%{version}.so
%{_libdir}/libguichan_allegro-%{version}.so
%{_libdir}/libguichan_opengl-%{version}.so
%{_libdir}/libguichan_sdl-%{version}.so

%files devel
%{_includedir}/guichan.hpp
%{_includedir}/guichan/
%{_libdir}/libguichan.so
%{_libdir}/libguichan_allegro.so
%{_libdir}/libguichan_opengl.so
%{_libdir}/libguichan_sdl.so
