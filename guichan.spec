%define	name	guichan
%define	version	0.8.2
%define	release	%mkrel 1
%define major   1
%define api     0.8.1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Portable C++ GUI library for games using Allegro, SDL and OpenGL

Group:          System/Libraries
License:        BSD
URL:            http://guichan.sourceforge.net
Source0:        http://guichan.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         guichan-0.8.2-mdv-fix-linkage.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  allegro-devel
Buildrequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	GL-devel
BuildRequires:	nas-devel

%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different objects for 
displaying graphics and grabbing user input.

%package -n %{libname}
Summary:        Shared library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n %{staticdevelname}
Summary:        Static libraries for programs which will use %{name}
Group:          Development/C++
Requires:       %{develname} = %{version}
Provides:       %{name}-static-devel = %{version}-%{release}

%description -n %{staticdevelname}
This package contains the static libraries necessary for developing
programs which will use %{name}.

%prep
%setup -q
%patch0 -p1 -b .linkage

%build
autoreconf -f -i
%configure2_5x  --enable-sdl \
                --enable-sdlimage \
                --enable-opengl \
                --enable-allegro
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib%{name}*-%{api}.so.*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{staticdevelname}
%defattr(-,root,root,-)
%{_libdir}/*.a
%{_libdir}/*.la
