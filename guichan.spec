%define major   1
%define api     0.8.1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Name:		guichan
Version:	0.8.2
Release:	4
Summary:	Portable C++ GUI library for games using Allegro, SDL and OpenGL

Group:		System/Libraries
License:	BSD
URL:		http://guichan.sourceforge.net
Source0:	http://guichan.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		guichan-0.8.2-mdv-fix-linkage.patch

BuildRequires:  allegro-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(gl)
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
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib%{name}*-%{api}.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{staticdevelname}
%{_libdir}/*.a

