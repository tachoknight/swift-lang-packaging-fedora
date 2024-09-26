# 6/27/24 - temporary disable __brp_add_determinism
# as it prevents the package from successfully building
%if 0%{?fedora} >= 41
# on Fedora 41/Rawhide
%undefine __brp_add_determinism
%endif
%global debug_package %{nil}
%undefine _auto_set_build_flags

%global linux_version fedora

#################################################
# Make sure these are changed for every release!
#################################################
%global swift_version 6.0.1-RELEASE
%global package_version 6.0.1
%global fedora_release 1

%global swift_source_location swift-source

# Set to the right version per the json file
%global icu_version 69
%global yams_version 5.0.6
%global swift_argument_parser_version 1.2.3
%global swift_crypto_version 3.0.0
%global ninja_version 1.11.1
%global cmake_version 3.24.2
%global swift_atomics_version 1.2.0
%global swift_collections_version 1.1.2
%global swift_numerics_version 1.0.2
%global swift_system_version 1.3.0
%global swift_nio_version 2.31.2
%global swift_nio_ssl_version 2.15.0
%global swift_certificates_version 1.0.1
%global swift_asn1_version 1.0.0
%global wasmkit_version 0.0.3
%global wasi_version 20
%global swift_format_version 6.0
%global swift_llvm_bindings_version 6.0
%global swift_foundation_icu_version 6.0
%global swift_foundation_version 6.0
%global zlib_version 1.3


Name:           swift-lang
Version:        %{package_version}
Release:        %{fedora_release}%{?dist}
Summary:        The Swift programming language
License:        Apache-2.0
URL:            https://www.swift.org

Source0:        https://github.com/apple/swift/archive/refs/tags/swift-%{swift_version}.tar.gz#/swift.tar.gz
Source1:        https://github.com/apple/swift-corelibs-libdispatch/archive/swift-%{swift_version}.tar.gz#/corelibs-libdispatch.tar.gz
Source2:        https://github.com/apple/swift-corelibs-foundation/archive/swift-%{swift_version}.tar.gz#/corelibs-foundation.tar.gz
Source3:        https://github.com/apple/swift-integration-tests/archive/swift-%{swift_version}.tar.gz#/swift-integration-tests.tar.gz
Source4:        https://github.com/apple/swift-corelibs-xctest/archive/swift-%{swift_version}.tar.gz#/corelibs-xctest.tar.gz
Source5:        https://github.com/apple/swift-package-manager/archive/swift-%{swift_version}.tar.gz#/package-manager.tar.gz
Source6:        https://github.com/apple/swift-llbuild/archive/swift-%{swift_version}.tar.gz#/llbuild.tar.gz
Source7:        https://github.com/apple/swift-cmark/archive/swift-%{swift_version}.tar.gz#/cmark.tar.gz
Source8:        https://github.com/apple/swift-xcode-playground-support/archive/swift-%{swift_version}.tar.gz#/swift-xcode-playground-support.tar.gz
Source9:        https://github.com/apple/sourcekit-lsp/archive/swift-%{swift_version}.tar.gz#/sourcekit-lsp.tar.gz
Source10:       https://github.com/apple/indexstore-db/archive/swift-%{swift_version}.tar.gz#/indexstore-db.tar.gz
Source11:       https://github.com/apple/llvm-project/archive/swift-%{swift_version}.tar.gz#/llvm-project.tar.gz
Source12:       https://github.com/apple/swift-tools-support-core/archive/swift-%{swift_version}.tar.gz#/swift-tools-support-core.tar.gz
Source13:       https://github.com/apple/swift-argument-parser/archive/%{swift_argument_parser_version}.tar.gz#/swift-argument-parser.tar.gz
Source14:       https://github.com/apple/swift-driver/archive/swift-%{swift_version}.tar.gz#/swift-driver.tar.gz
Source15:       https://github.com/apple/swift-syntax/archive/swift-%{swift_version}.zip#/swift-syntax.tar.gz
Source16:       https://github.com/jpsim/Yams/archive/%{yams_version}.tar.gz#/yams.tar.gz
Source17:       https://github.com/apple/swift-crypto/archive/refs/tags/%{swift_crypto_version}.tar.gz#/swift-crypto.tar.gz
Source18:       https://github.com/ninja-build/ninja/archive/refs/tags/v%{ninja_version}.tar.gz#/ninja.tar.gz
Source19:       https://github.com/KitWare/CMake/archive/refs/tags/v%{cmake_version}.tar.gz#/cmake.tar.gz
Source20:       https://github.com/apple/swift-atomics/archive/%{swift_atomics_version}.tar.gz#/swift-atomics.tar.gz
Source21:       https://github.com/apple/swift-stress-tester/archive/swift-%{swift_version}.tar.gz#/swift-stress-tester.tar.gz
Source22:       https://github.com/apple/swift-docc/archive/swift-%{swift_version}.tar.gz#/swift-docc.tar.gz
Source23:       https://github.com/apple/swift-docc-render-artifact/archive/swift-%{swift_version}.tar.gz#/swift-docc-render-artifact.tar.gz
Source24:       https://github.com/apple/swift-docc-symbolkit/archive/swift-%{swift_version}.tar.gz#/swift-docc-symbolkit.tar.gz
Source25:       https://github.com/apple/swift-collections/archive/%{swift_collections_version}.tar.gz#/swift-collections.tar.gz
Source26:       https://github.com/apple/swift-numerics/archive/%{swift_numerics_version}.tar.gz#/swift-numerics.tar.gz
Source27:       https://github.com/apple/swift-system/archive/%{swift_system_version}.tar.gz#/swift-system.tar.gz
Source28:       https://github.com/apple/swift-nio/archive/%{swift_nio_version}.tar.gz#/swift-nio.tar.gz
Source29:       https://github.com/apple/swift-nio-ssl/archive/%{swift_nio_ssl_version}.tar.gz#/swift-nio-ssl.tar.gz
Source30:       https://github.com/apple/swift-format/archive/refs/heads/release/%{swift_format_version}.zip#/swift-format.zip
Source31:       https://github.com/apple/swift-lmdb/archive/swift-%{swift_version}.tar.gz#/swift-lmdb.tar.gz
Source32:       https://github.com/apple/swift-markdown/archive/swift-%{swift_version}.tar.gz#/swift-markdown.tar.gz
Source33:       https://github.com/apple/swift-experimental-string-processing/archive/swift-%{swift_version}.tar.gz#/swift-experimental-string-processing.tar.gz
Source34:       https://github.com/apple/swift-certificates/archive/%{swift_certificates_version}.tar.gz#/swift-certificates.tar.gz
Source35:       https://github.com/apple/swift-asn1/archive/%{swift_asn1_version}.tar.gz#/swift-asn1.tar.gz
Source36:       https://github.com/unicode-org/icu/archive/refs/heads/maint/maint-%{icu_version}.zip#/icu.zip
Source37:       https://github.com/swiftwasm/WasmKit/archive/refs/tags/%{wasmkit_version}.tar.gz#/wasm.tar.gz
Source38:       https://github.com/WebAssembly/wasi-libc/archive/refs/tags/wasi-sdk-%{wasi_version}.tar.gz#/wasi-sdk.tar.gz
Source39:       https://github.com/apple/swift-llvm-bindings/archive/refs/heads/swift/release/%{swift_llvm_bindings_version}.zip#/swift-llvm-bindings.zip
Source40:       https://github.com/apple/swift-foundation-icu/archive/refs/heads/release/%{swift_foundation_icu_version}.zip#/swift-foundation-icu.zip
Source41:       https://github.com/apple/swift-foundation/archive/refs/heads/release/%{swift_foundation_version}.zip#/swift-foundation.zip
Source42:       https://github.com/apple/swift-testing/archive/refs/tags/swift-%{swift_version}.tar.gz#/swift-testing.tar.gz
Source43:       https://github.com/madler/zlib/releases/download/v%{zlib_version}/zlib13.zip
Source44:       swiftlang.conf

Patch1:         need_pic.patch
Patch2:         no_pipes.patch
Patch3:         enable_lzma.patch
Patch4:         resource_dir.patch
Patch5:         have_strcat.patch
Patch6:         latest_python.patch

BuildRequires:  clang
BuildRequires:  swig
BuildRequires:  rsync
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libxml2-devel
BuildRequires:  sqlite-devel
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libedit-devel
BuildRequires:  perl-podlators
BuildRequires:  swiftlang
BuildRequires:  lld

Requires:       glibc-devel
Requires:       binutils-gold
Requires:       gcc

ExclusiveArch:  x86_64 aarch64 

Provides:       swiftlang = %{version}-%{release}


%description
Swift is a general-purpose programming language built using 
a modern approach to safety, performance, and software design 
patterns.

The goal of the Swift project is to create the best available 
language for uses ranging from systems programming, to mobile 
and desktop apps, scaling up to cloud services. Most 
importantly, Swift is designed to make writing and maintaining 
correct programs easier for the developer. 


%prep
%setup -q -c -n %{swift_source_location} -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24 -a 25 -a 26 -a 27 -a 28 -a 29 -a 30 -a 31 -a 32 -a 33 -a 34 -a 35 -a 36 -a 37 -a 38 -a 39 -a 40 -a 41 -a 42 -a 43
# The Swift build script requires directories to be named
# in a specific way so renaming the source directories is
# necessary
mv swift-cmark-swift-%{swift_version} cmark
mv swift-testing-swift-%{swift_version} swift-testing
mv swift-corelibs-foundation-swift-%{swift_version} swift-corelibs-foundation
mv swift-corelibs-libdispatch-swift-%{swift_version} swift-corelibs-libdispatch
mv swift-corelibs-xctest-swift-%{swift_version} swift-corelibs-xctest
mv swift-integration-tests-swift-%{swift_version} swift-integration-tests
mv swift-llbuild-swift-%{swift_version} llbuild
mv swift-package-manager-swift-%{swift_version} swiftpm
mv swift-swift-%{swift_version} swift
mv swift-xcode-playground-support-swift-%{swift_version} swift-xcode-playground-support
mv sourcekit-lsp-swift-%{swift_version} sourcekit-lsp
mv indexstore-db-swift-%{swift_version} indexstore-db
mv llvm-project-swift-%{swift_version} llvm-project
mv swift-syntax-swift-%{swift_version} swift-syntax
mv swift-tools-support-core-swift-%{swift_version} swift-tools-support-core
mv swift-argument-parser-%{swift_argument_parser_version} swift-argument-parser
mv swift-driver-swift-%{swift_version} swift-driver
mv swift-crypto-%{swift_crypto_version} swift-crypto
mv CMake-%{cmake_version} cmake
mv swift-atomics-%{swift_atomics_version} swift-atomics
mv swift-docc-swift-%{swift_version} swift-docc
mv swift-docc-render-artifact-swift-%{swift_version} swift-docc-render-artifact
mv swift-docc-symbolkit-swift-%{swift_version} swift-docc-symbolkit
mv swift-collections-%{swift_collections_version} swift-collections
mv swift-numerics-%{swift_numerics_version} swift-numerics
mv swift-system-%{swift_system_version} swift-system
mv swift-nio-%{swift_nio_version} swift-nio
mv swift-nio-ssl-%{swift_nio_ssl_version} swift-nio-ssl
mv swift-format-release-%{swift_format_version} swift-format
mv swift-lmdb-swift-%{swift_version} swift-lmdb
mv swift-markdown-swift-%{swift_version} swift-markdown
mv swift-stress-tester-swift-%{swift_version} swift-stress-tester
mv swift-experimental-string-processing-swift-%{swift_version} swift-experimental-string-processing
mv swift-certificates-%{swift_certificates_version} swift-certificates
mv swift-asn1-%{swift_asn1_version} swift-asn1
mv swift-llvm-bindings-swift-release-%{swift_llvm_bindings_version} swift-llvm-bindings
mv swift-foundation-icu-release-%{swift_foundation_icu_version} swift-foundation-icu
mv swift-foundation-release-%{swift_foundation_version} swift-foundation

# ICU 
mv icu-maint-maint-%{icu_version} icu

# Yams
mv Yams-%{yams_version} yams

# Ninja
mv ninja-%{ninja_version} ninja

# WasmKit
mv WasmKit-%{wasmkit_version} wasmkit

# zlib
mv zlib-%{zlib_version} zlib

# Fix python to python3 
%py3_shebang_fix swift/utils/api_checker/swift-api-checker.py
%py3_shebang_fix llvm-project/compiler-rt/lib/hwasan/scripts/hwasan_symbolize

# Enable PIC for cmark
%patch -P1 -p0

# Pipes has been removed in Python
%patch -P2 -p0

# Enable LZMA
%patch -P3 -p0

# https://github.com/swiftlang/swift/pull/74814
pushd swift
%patch -P4 -p1
popd

# Weird (hopefully temp) situation of strlcpy and strncat
# not being found at the system level
# This does not work for EPEL9, so we need to make sure
# that this patch is _not_ applied when building for EPEL9
%if ! 0%{?el9}
%patch -P5 -p0
%endif

# After Python 3.12 certain functions have been removed, 
# which is in Fedora 41
%if 0%{?fedora} >= 41
%patch -P6 -p0
%endif

%build
export VERBOSE=1

# Here we go!
swift/utils/build-script --preset=buildbot_linux,no_test install_destdir=%{_builddir} installable_package=%{_builddir}/swift-%{version}-%{linux_version}.tar.gz


%install
mkdir -p %{buildroot}%{_libexecdir}/swift/%{package_version}
cp -r %{_builddir}/usr/* %{buildroot}%{_libexecdir}/swift/%{package_version}
mkdir -p %{buildroot}%{_bindir}
ln -fs %{_libexecdir}/swift/%{package_version}/bin/swift %{buildroot}%{_bindir}/swift
ln -fs %{_libexecdir}/swift/%{package_version}/bin/swiftc %{buildroot}%{_bindir}/swiftc
ln -fs %{_libexecdir}/swift/%{package_version}/bin/sourcekit-lsp %{buildroot}%{_bindir}/sourcekit-lsp
mkdir -p %{buildroot}%{_mandir}/man1
cp %{_builddir}/usr/share/man/man1/swift.1 %{buildroot}%{_mandir}/man1/swift.1
mkdir -p %{buildroot}/usr/lib
ln -fs %{_libexecdir}/swift/%{package_version}/lib/swift %{buildroot}/usr/lib/swift
mkdir -p %{buildroot}%{_libdir}
ln -fs %{_libexecdir}/swift/%{package_version}/lib/lib{IndexStore,sourcekitdInProc,swiftDemangle}.so* %{buildroot}%{_libdir}/
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d/
install -m 0644 %{SOURCE44} %{buildroot}/%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


# This is to fix an issue with check-rpaths complaining about
# how the Swift binaries use RPATH
export QA_SKIP_RPATHS=1


%files
%license swift/LICENSE.txt
%{_bindir}/swift
%{_bindir}/swiftc
%{_bindir}/sourcekit-lsp
%{_mandir}/man1/swift.1.gz
%{_libexecdir}/swift/
%{_usr}/lib/swift
%{_libdir}/libIndexStore.so*
%{_libdir}/libsourcekitdInProc.so*
%{_libdir}/libswiftDemangle.so*
%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Wed Sep 25 2024 Ron Olson <tachoknight@gmail.com> - 6.0.1-1
- Updated to Swift 6.0.1-RELEASE
  Resolves: rhbz#2313366
* Mon Sep 16 2024 Ron Olson <tachoknight@gmail.com> - 6.0-1
- Updated to Swift 6.0-RELEASE
* Mon Aug 26 2024 Zephyr Lykos <fedora@mochaa.ws> - 6.0-1
- Export Swift development tool libraries to libdir
* Mon Jul 22 2024 Byoungchan Lee <byoungchan.lee@gmx.com> - 6.0-1
- Minimize runtime/compile time dependencies
* Fri Jul 19 2024 Ron Olson <tachoknight@gmail.com> - 6.0-1
- Added file to add the Swift libraries to the ld.so.conf.d directory
* Sun Jun 30 2024 Ron Olson <tachoknight@gmail.com> - 6.0-1
- Patch from finagolfin
  https://github.com/swiftlang/swift/pull/74814
* Tue Apr 23 2024 Ron Olson <tachoknight@gmail.com> - 6.0-1
- First attempt at getting 6.0 working
* Mon Sep 18 2023 Ron Olson <tachoknight@gmail.com> - 5.9-1
- Updated to Swift 5.9-RELEASE
  Resolves: rhbz#2239543
* Fri Sep 15 2023 Ron Olson <tachoknight@gmail.com> - 5.10-1
- First working version of Swift 5.10
* Wed Mar 29 2023 Ron Olson <tachoknight@gmail.com> - 5.9-1
- Cleanup and first attempt at getting 5.9 going though
  5.8 hasn't been released yet
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
* Tue Dec 27 2022 Ron Olson <tachoknight@gmail.com> - 5.8-1
- Cleanup and first attempt at getting 5.8 going
* Fri Dec 16 2022 Ron Olson <tachoknight@gmail.com> - 5.7.2-2
- SPDX migration
* Wed Dec 14 2022 Ron Olson <tachoknight@gmail.com> - 5.7.2-1
- Updated to Swift 5.7.2-RELEASE
  Resolves: rhbz#2153189
* Wed Nov 02 2022 Ron Olson <tachoknight@gmail.com> - 5.7.1-1
- Updated to Swift 5.7.1-RELEASE
  Resolves: rhbz#2139320
* Tue Nov 01 2022 Ron Olson <tachoknight@gmail.com> - 5.7-4
- Merged fix from Lumír Balhar to replace the pathfix.py tool
  with the new way for Python 3.12
* Tue Sep 27 2022 Ron Olson <tachoknight@gmail.com> - 5.7-3
- Resolves: rhbz#2130233
* Tue Sep 27 2022 Ron Olson <tachoknight@gmail.com> - 5.7-2
- Added patch to handle an initialized variable but not
  used
* Tue Sep 13 2022 Ron Olson <tachoknight@gmail.com> - 5.7-1
- Updated to Swift 5.7-RELEASE
* Thu May 05 2022 Ron Olson <tachoknight@gmail.com> - 5.7-1
- First working version of Swift 5.7
* Mon Apr 25 2022 Ron Olson <tachoknight@gmail.com> - 5.7-1
- First attempt to build swift-5.7
* Thu Apr 21 2022 Ron Olson <tachoknight@gmail.com> - 5.6.1-2
- Removed ncurses-compat-libs as a runtime dependency as it 
  has been removed from Fedora Rawhide
* Mon Apr 11 2022 Ron Olson <tachoknight@gmail.com> - 5.6.1-1
- Updated to Swift 5.6.1-RELEASE
* Wed Mar 30 2022 Ron Olson <tachoknight@gmail.com> - 5.6-1
- Updated to Swift 5.6-RELEASE
* Tue Feb 15 2022 Ron Olson <tachoknight@gmail.com> - 5.5.3-1
- Updated to Swift 5.5.3-RELEASE
* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
* Wed Jan 12 2022 Ron Olson <tachoknight@gmail.com> - 5.6-1
- First build of Swift-5.6
* Tue Dec 14 2021 Ron Olson <tachoknight@gmail.com> - 5.5.2-1
- Updated to Swift 5.5.2-RELEASE
* Wed Oct 27 2021 Ron Olson <tachoknight@gmail.com> - 5.5.1-1
- Updated to Swift 5.5.1-RELEASE
* Tue Sep 21 2021 Ron Olson <tachoknight@gmail.com> - 5.5-1
- Updated to Swift 5.5-RELEASE
* Fri Sep 17 2021 Ron Olson <tachoknight@gmail.com> - 5.4.3-2
- Added patch to allow building using Clang 13
* Wed Sep 15 2021 Ron Olson <tachoknight@gmail.com> - 5.4.3-1
- Updated to swift-5.4.3-RELEASE
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
* Thu Jul 15 2021 Ron Olson <tachoknight@gmail.com> - 5.4.2-2
- Discovered that EPEL-8 doesn't have binutils-gold
* Mon Jul 05 2021 Ron Olson <tachoknight@gmail.com> - 5.4.2-1
- Updated to swift-5.4.2-RELEASE
* Mon Jun 21 2021 Ron Olson <tachoknight@gmail.com> - 5.4.1-2
- Changes for EPEL-8
* Thu Jun 10 2021 Ron Olson <tachoknight@gmail.com> - 5.4.1-1
- Added fix for RPATH problems
* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.4-2
- Rebuilt for Python 3.10
* Thu Jun 03 2021 Ron Olson <tachoknight@gmail.com> 5.5-1
- Removed special CMake stuff for EPEL 8
* Tue Jun 01 2021 Ron Olson <tachoknight@gmail.com> 5.5-1
- Added patch to remove Cyclades from LLVM
* Fri May 28 2021 Jesús Abelardo Saldívar Aguilar <jasaldivara@gmail.com> 5.5-1
- Added patches to fix circular dependency on PkgConfig
* Fri May 21 2021 Ron Olson <tachoknight@gmail.com> 5.5-1
- First version of Swift 5.5 - 5.5-DEVELOPMENT-SNAPSHOT-2021-05-18-a
* Tue Apr 27 2021 Ron Olson <tachoknight@gmail.com> 5.4-1
- Updated to swift-5.4-RELEASE
* Tue Apr 06 2021 Ron Olson <tachoknight@gmail.com> 5.4-1
- Updated to swift-5.4-DEVELOPMENT-SNAPSHOT-2021-03-25-a
* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 5.3.3-2
- Rebuilt for removed libstdc++ symbol (#1937698)
* Thu Jan 28 2021 Ron Olson <tachoknight@gmail.com> 5.3.3-1
- Updated to swift-5.3.3-RELEASE
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
* Thu Jan 21 2021 Ron Olson <tachoknight@gmail.com> 5.4-1
- First working version of Swift 5.4
* Tue Dec 22 2020 Ron Olson <tachoknight@gmail.com> 5.3.2-1
- Updated to swift-5.3.2-RELEASE
* Fri Dec 04 2020 Jeff Law <law@redhat.com> 5.3.1-2
- Fix missing #include for gcc-11

* Fri Nov 13 2020 Ron Olson <tachoknight@gmail.com> 5.3.1-1
- Updated to swift-5.3.1-RELEASE
* Thu Sep 17 2020 Ron Olson <tachoknight@gmail.com> 5.3-1
- Updated to swift-5.3-RELEASE
* Mon Aug 10 2020 Ron Olson <tachoknight@gmail.com> 5.2.5-1
- Updated to swift-5.2.5-RELEASE
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.4-2
- Rebuilt for Python 3.9

* Wed May 20 2020 Ron Olson <tachoknight@gmail.com> 5.2.4-1
- Updated to swift-5.2.4-RELEASE
* Wed Apr 29 2020 Ron Olson <tachoknight@gmail.com> 5.2.3-1
- Updated to swift-5.2.3-RELEASE
* Fri Apr 17 2020 Ron Olson <tachoknight@gmail.com> 5.2.2-2
- Added patch to remove use of sys/sysctl.h as it was removed
  in Rawhide (future F33)
* Wed Apr 15 2020 Ron Olson <tachoknight@gmail.com> 5.2.2-1
- Updated to swift-5.2.2-RELEASE
* Sun Apr 12 2020 Ron Olson <tachoknight@gmail.com> 5.2.1-3
- Put CMake back as a build step because the version in EPEL 8 is too
  old
* Sun Apr 12 2020 Ron Olson <tachoknight@gmail.com> 5.2.1-2
- Added s390x architecture and F30-specific requires
* Mon Apr 06 2020 Ron Olson <tachoknight@gmail.com> 5.2.1-1
- Reorganized the package to place everything in a single location,
  changed the versioning scheme, and removed a number of obsolete patches
* Wed Apr 01 2020 Ron Olson <tachoknight@gmail.com> 5.2.1-0.1.20200331git2e3b1b3
- Updated to swift-5.2.1-RELEASE
* Wed Mar 25 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.10.20200324git443e9a4
- Updated to swift-5.2-RELEASE
* Thu Mar 12 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.9.20200311git33150e3
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-03-11-a and switched to
  using patched version of cmake to get around issues building 5.2 with
  3.17
* Fri Feb 28 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.8.20200227git33150e3
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-02-27-a
* Sun Feb 02 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.7.20200201git66c06ab
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-02-01-a
* Sat Feb 01 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.6.20200131gitfab20c6
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-01-31-a
* Thu Jan 30 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.5.20200129gita0c1677
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-01-29-a
* Tue Jan 28 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.4.20200127git7c02102
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-01-27-a
* Mon Jan 20 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.3.20200117git3194881
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-01-17-a
* Fri Jan 10 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.2.20200109git880e9e6
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-01-09-a
* Tue Jan 07 2020 Ron Olson <tachoknight@gmail.com> 5.2-0.1.20200106git74df113
- Updated to swift-5.2-DEVELOPMENT-SNAPSHOT-2020-01-06-a
* Sat Dec 21 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.6.20191220git04833a6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-20-a
* Fri Dec 20 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.5.20191219git04833a6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-19-a
* Thu Dec 19 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.4.20191218git04833a6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-18-a
* Wed Dec 18 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.3.20191217git04833a6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-17-a
* Tue Dec 17 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.2.20191216git04833a6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-16-a
* Fri Dec 13 2019 Ron Olson <tachoknight@gmail.com> 5.1.3-0.1.20191213git005fc1f
- Updated to swift-5.1.3-RELEASE
* Fri Dec 13 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.20.20191212gita22eb08
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-12-a
* Wed Dec 11 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.19.20191210git4a1b378
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-10-a
* Tue Dec 10 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.18.20191209git4a1b378
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-09-a
* Mon Dec 09 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.17.20191130gited9117a
- Release of 5.1.2 with sourcekit-lsp enabled. The user still needs to build
  and install the plugin for vscode; if they do this version will support
  code-completion, also works with neovim too
* Sat Dec 07 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.16.20191206git4b8db65
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-06-a
* Fri Dec 06 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.15.20191205git4b8db65
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-05-a
* Thu Dec 05 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.14.20191204git4b8db65
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-04-a
* Wed Dec 04 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.13.20191203git4b8db65
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-12-03-a
* Sat Nov 30 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.12.20191129git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-29-a
* Fri Nov 29 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.11.20191128git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-28-a
* Thu Nov 28 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.10.20191127git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-27-a
* Wed Nov 27 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.9.20191126git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-26-a
* Tue Nov 26 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.8.20191125git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-25-a
* Mon Nov 25 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.7.20191124git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-24-a
* Sat Nov 23 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.6.20191122git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-22-a
* Fri Nov 22 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.5.20191121git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-21-a
* Tue Nov 19 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.4.20191118git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-18-a
* Mon Nov 18 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.3.20191117git60f3082
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-17-a
* Sat Nov 16 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.2.20191115git51fe191
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-15-a
* Fri Nov 15 2019 Ron Olson <tachoknight@gmail.com> 5.1.3-0.1.20191114gite74feb6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-14-a
* Thu Nov 07 2019 Ron Olson <tachoknight@gmail.com> 5.1.2-0.1.20191107git71def56
- Updated to swift-5.1.2-RELEASE
* Wed Nov 06 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.7.20191105gitb368b0d
- Added icu, also updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-05-a
* Mon Nov 04 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.6.20191101git74328cd
- Added unpackaged files, switched to new llvm-project-based subproject
* Sun Nov 03 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.5.20191101git74328cd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-11-01-a
* Thu Oct 31 2019 Ron Olson <tachoknight@gmail.com> 5.1.1-0.4.20191004git4242edd
- Added sourcekit-lsp
* Wed Oct 30 2019 Ron Olson <tachoknight@gmail.com> 5.1.1-0.3.20191004git4242edd
- Clang 9 was causing compiler-rt to not build properly due to a macro.
* Thu Oct 17 2019 Ron Olson <tachoknight@gmail.com> 5.1.1-0.2.20191004git4242edd
- Fixed issue with installing swift-lang only gave the option for
  swift-lang-runtime
* Fri Oct 04 2019 Ron Olson <tachoknight@gmail.com> 5.1.1-0.1.20191004git4242edd
- Updated to swift-5.1.1-RELEASE
* Thu Sep 19 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.57.20190919gitfa33242
- Updated to swift-5.1-RELEASE and removed FrameworkABIBaseline as apparently
  it disappeared
* Thu Sep 19 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.56.20190918gite05f800
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-18-a
* Wed Sep 18 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.55.20190917git1f49050
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-17-a
* Tue Sep 17 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.54.20190916git279ca88
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-16-a
* Mon Sep 16 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.53.20190915git279ca88
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-15-a
* Sun Sep 15 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.52.20190914git279ca88
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-14-a
* Sat Sep 14 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.51.20190913git11b9972
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-13-a
* Fri Sep 13 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.50.20190912gitb9d082f
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-12-a
* Thu Sep 12 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.49.20190911gitb8f4481
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-11-a
* Tue Sep 10 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.48.20190909git28a0436
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-09-a
* Mon Sep 09 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.47.20190908git28a0436
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-08-a also added test for
  Red Hat Enterprise Linux and CentOS (when it is updated to match RHEL 8)
  Also packaged some new files
* Fri Sep 06 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.46.20190905git1880eb0
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-05-a
* Thu Sep 05 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.45.20190904git1880eb0
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-04-a
* Wed Sep 04 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.44.20190903gitfcc37cd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-03-a
* Tue Sep 03 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.43.20190902gitfcc37cd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-02-a
* Mon Sep 02 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.42.20190901gitfcc37cd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-09-01-a
* Sun Sep 01 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.41.20190831gitfcc37cd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-31-a
* Fri Aug 30 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.40.20190829gitfcc37cd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-29-a
* Thu Aug 29 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.39.20190828gite90298c
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-28-a and added explicit
  requirement for python3-distro
* Wed Aug 28 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.38.20190827gite90298c
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-27-a and added a patch
  to allow LLDB to be built using Python 3.8 (currently in F32/Rawhide)
* Tue Aug 27 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.37.20190826git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-26-a
* Mon Aug 26 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.36.20190825git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-25-a
* Sun Aug 25 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.35.20190824git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-24-a
* Sat Aug 24 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.34.20190823git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-23-a
* Fri Aug 23 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.33.20190822git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-22-a
* Wed Aug 21 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.32.20190820git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-20-a
* Mon Aug 19 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.31.20190817git3b0cf9e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-17-a
* Sat Aug 17 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.30.20190816git1329017
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-16-a
* Fri Aug 16 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.29.20190815git1329017
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-15-a
* Wed Aug 14 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.28.20190813git425a146
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-13-a
* Tue Aug 13 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.27.20190812git425a146
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-08-12-a and added another
  directory
* Fri Jul 26 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.26.20190725git0450b7d
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-25-a
* Thu Jul 25 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.25.20190724gite9b6385
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-24-a
* Wed Jul 24 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.24.20190723git3e8f631
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-23-a 
* Tue Jul 23 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.23.20190719gitf883175
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-19-a and first version
  that relies on Python 3 for building
* Mon Jul 15 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.22.20190714git7b90512
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-14-a
* Sun Jul 14 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.21.20190713git26c2dbe
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-13-a
* Sat Jul 13 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.20.20190712gita062b3c
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-12-a
* Fri Jul 12 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.19.20190711gitacd767e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-11-a
* Thu Jul 11 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.18.20190710gitd7f811d
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-10-a
* Wed Jul 10 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.17.20190709gitf67864b
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-09-a
* Thu Jul 04 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.16.20190703gitd2c038e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-03-a
* Wed Jul 03 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.15.20190702git2efadfd
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-02-a
* Tue Jul 02 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.14.20190701git6761ba4
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-07-01-a and removed 
  dependency on python-sphinx as a problem with a pygments lexer was being
  treated as an error and causing the builds to fail
* Sun Jun 30 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.13.20190629gitdcde8ac
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-29-a
* Sat Jun 29 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.12.20190628gitca3c825
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-28-a
* Fri Jun 28 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.11.20190627git993b248
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-27-a
* Thu Jun 27 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.10.20190626git16859f1
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-26-a and added patch
  to remove reference to depreciated header file
* Wed Jun 26 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.9.20190624git4e7bcdb
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-24-a and got the REPL
  to work
* Sun Jun 23 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.8.20190621git9729868
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-21-a
* Fri Jun 21 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.7.20190620gita5aa0c6
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-20-a
* Thu Jun 20 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.6.20190619git500333c
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-19-a
* Thu Jun 20 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.5.20190619git500333c
- Cleaned up the spec file to remove 4.2 to 5 migration code and some
  old patches
* Mon Jun 17 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.4.20190616gitcbfbc8e
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-06-16-a
* Sun Jun 02 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.3.20190529git37f230a
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-05-29-a
* Fri Apr 26 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.2.20190425git6d89fc9
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-04-25-a
* Thu Apr 18 2019 Ron Olson <tachoknight@gmail.com> 5.1-0.1.20190416git85a776d
- Updated to swift-5.1-DEVELOPMENT-SNAPSHOT-2019-04-16-a
* Thu Mar 28 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.53.20190325gitba33f9e
- Modified spec file to handle upgrades from 4.2 to 5.0.
* Mon Mar 25 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.52.20190325gitba33f9e
- Updated to swift-5.0-RELEASE
* Mon Mar 25 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.51.20190324git130a414
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-03-24-a, removed _gettid
  patch as the changed were merged upstream
* Fri Mar 22 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.50.20190310git4d6e741
- The swift-corelibs-xctest library was being zeroed out due to issue with
  CMake 3.14 where it was being copied into the same directory. A bug
  report has been filed with CMake but until it is resolved, the cmake file
  has been patched to not perform the copy.
* Fri Mar 15 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.50.20190310git4d6e741
- Modules did not work properly in the REPL due to additional lib path; 
  fixed with symlinks to the lower directory structures
* Fri Mar 15 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.50.20190310git4d6e741
- python2-sphinx was removed from Fedora after 30 so it will use the python3
  version
* Thu Mar 14 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.50.20190310git4d6e741
- Fixed issues introduced by upstream changes
* Mon Mar 11 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.50.20190310git4d6e741
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-03-10-a
* Thu Mar 07 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.49.20190306git5834830
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-03-06-a
* Wed Mar 06 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.48.20190305git5834830
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-03-05-a
* Tue Mar 05 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.47.20190304gitad10379
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-03-04-a
* Fri Mar 01 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.46.20190228gitfeacc3f
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-28-a
* Wed Feb 27 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.45.20190226gitfa5d493
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-26-a
* Tue Feb 26 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.44.20190225gita8126fb
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-25-a
* Mon Feb 25 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.43.20190224gita8126fb
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-24-a
* Sun Feb 24 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.42.20190223gita8126fb
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-23-a
* Sat Feb 23 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.41.20190222gita24adaf
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-22-a
* Fri Feb 22 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.40.20190221git86a39df
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-21-a
* Thu Feb 21 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.39.20190220git817dff3
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-20-a
* Wed Feb 20 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.38.20190219git817dff3
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-19-a
* Mon Feb 18 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.37.20190217git15be364
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-17-a
* Sun Feb 17 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.36.20190216git15be364
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-16-a
* Sat Feb 16 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.35.20190215git15be364
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-15-a
* Fri Feb 15 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.34.20190214git8d88441
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2019-02-14-a
* Wed Feb 13 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.33.20190206gitd07c25a
- Added patch to fix an issue with compiler-rt using std::thread in a vector
* Fri Feb 08 2019 Ron Olson <tachoknight@gmail.com> 5.0-0.32.20190206gitd07c25a
- Added patch to allow the Swift REPL to work properly, also removed patch
  for aarch64 because the changes were merged upstream
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.31.20181214gitee39236
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Sat Dec 15 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.31.20181212gite231ae1
- First version that supports aarch64
* Thu Dec 13 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.31.20181212gite231ae1
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-12-a
* Thu Dec 13 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.30.20181212gite231ae1
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-12-a
* Thu Dec 13 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.29.20181212gite231ae1
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-12-a
* Tue Dec 11 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.28.20181210gitf83ec0c
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-10-a
* Mon Dec 10 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.26.20181209gitc14e1a3
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-09-a
* Sun Dec 09 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.25.20181208git3945260
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-08-a
* Sat Dec 08 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.24.20181207git0a73e15
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-07-a
* Fri Dec 07 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.23.20181206git565e767
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-06-a
* Wed Dec 05 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.22.20181204gitb74d54a
- Updated to swift-5.0-DEVELOPMENT-SNAPSHOT-2018-12-04-a
* Wed Dec 05 2018 Egor Zhdan <egor.zhdan@gmail.com>            
- Include dependencies to ncurses which are required by SourceKit and 
  included in Apple installation guide
* Wed Dec 05 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.21.20181204gitfacaad1
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-12-04-a
* Tue Dec 04 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.20.20181203git3376f9f
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-12-03-a
* Mon Dec 03 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.19.20181202gita8a8bdc
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-12-02-a
* Sun Dec 02 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.18.20181201gitb01ee72
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-12-01-a
* Sat Dec 01 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.17.20181130gitd8f12cb
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-30-a
* Thu Nov 29 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.16.20181128git806cf57
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-28-a
* Tue Nov 27 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.15.20181126gita820992
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-26-a
* Mon Nov 26 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.14.20181125gita820992
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-25-a
* Sat Nov 24 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.13.20181123gita820992
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-23-a
* Fri Nov 23 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.12.20181122gitfb52a2e
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-22-a
* Mon Nov 19 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.11.20181116git201dcba
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-16-a
* Fri Nov 16 2018 Ron Olson <tachoknight@gmail.com> 5.0-0.10.20181115git739169d
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-11-15-a
* Wed Oct 31 2018 Ron Olson <tachoknight@gmail.com> 4.2.1-0.101.20181030git02a6ca9
- Updated to swift-4.2.1-RELEASE
* Tue Oct 30 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.100.20181029gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-29-a
* Sat Oct 27 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.99.20181026gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-26-a
* Fri Oct 26 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.98.20181025gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-25-a
* Wed Oct 24 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.97.20181023gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-23-a
* Tue Oct 23 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.96.20181022gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-22-a
* Mon Oct 22 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.95.20181021gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-21-a
* Sun Oct 21 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.94.20181020gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-20-a
* Fri Oct 19 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.93.20181018gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-18-a
* Thu Oct 18 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.92.20181017gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-17-a
* Wed Oct 17 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.91.20181016gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-16-a
* Tue Oct 16 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.90.20181015gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-15-a
* Mon Oct 15 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.89.20181014gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-14-a
* Sun Oct 14 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.88.20181013gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-13-a
* Sat Oct 13 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.87.20181012gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-12-a
* Fri Oct 12 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.86.20181011gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-11-a
* Thu Oct 11 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.85.20181010gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-10-a
* Wed Oct 10 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.84.20181009gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-09-a
* Tue Oct 09 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.83.20181008gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-08-a
* Mon Oct 08 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.82.20181007gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-07-a
* Sun Oct 07 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.81.20181006gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-06-a
* Sat Oct 06 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.80.20181005gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-05-a
* Thu Oct 04 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.79.20181003gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-03-a
* Wed Oct 03 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.78.20181002gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-02-a
* Tue Oct 02 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.77.20181001gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-10-01-a
* Sat Sep 29 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.76.20180928gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-28-a
* Fri Sep 28 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.75.20180927gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-27-a
* Thu Sep 27 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.74.20180926gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-26-a
* Wed Sep 26 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.73.20180925gitf4134eb
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-25-a
* Tue Sep 25 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.72.20180924git01644d5
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-24-a
* Mon Sep 24 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.71.20180922gitac7c511
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-22-a
* Sat Sep 15 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.70.20180914git2dfdbf2
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-14-a
* Fri Sep 14 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.69.20180913git2dfdbf2
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-13-a
* Thu Sep 13 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.68.20180912git2c6399a
- Updated to swift-4.2-RELEASE
* Wed Sep 12 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.67.20180911gitbe88499
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-11-a
* Sun Sep 09 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.66.20180908gitbe88499
- Added patch for clang 7.0
* Sun Sep 09 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.65.20180908gitbe88499
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-08-a
* Sat Sep 08 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.64.20180907gitc922f68
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-09-07-a
* Sun Aug 26 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.63.20180825git7d204ce
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-25-a
* Sat Aug 25 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.62.20180824git7d204ce
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-24-a
* Fri Aug 24 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.61.20180823git7d204ce
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-23-a
* Thu Aug 23 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.60.20180822git7d204ce
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-22-a
* Wed Aug 22 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.59.20180821git7d204ce
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-21-a
* Tue Aug 21 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.58.20180820gitde88335
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-20-a
* Sun Aug 19 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.57.20180818gitde88335
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-18-a
* Sat Aug 18 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.56.20180817gitde88335
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-17-a
* Fri Aug 17 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.55.20180816gitde88335
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-16-a
* Thu Aug 16 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.54.20180815gitefbe78e
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-15-a
* Wed Aug 15 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.53.20180814git3146921
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-14-a
* Sat Aug 11 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.52.20180810gita710c2f
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-10-a
* Thu Aug 09 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.51.20180808git1c8f885
- Updated to swift-4.2-CONVERGENCE
* Wed Aug 08 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.50.20180807gitab5ce2e
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-07-a
* Tue Aug 07 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.49.20180806gitab5ce2e
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-06-a
* Sat Aug 04 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.48.20180803git68f32fc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-03-a
* Fri Aug 03 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.47.20180802git44a88d4
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-02-a
* Thu Aug 02 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.46.20180801git3f7d681
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-08-01-a
* Wed Aug 01 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.45.20180731git00acd41
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-31-a
* Tue Jul 31 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.44.20180730gitfe1f442
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-30-a
* Sun Jul 29 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.43.20180728gitfe1f442
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-28-a
* Sat Jul 28 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.42.20180727git9d01b59
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-27-a
* Wed Jul 25 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.41.20180724git18650bc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-24-a and removed
  lldb patches as they were merged upstream into the 4.2 branch
* Tue Jul 24 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.40.20180723git18650bc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-23-a
* Mon Jul 23 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.39.20180722git18650bc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-22-a
* Sun Jul 22 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.38.20180721git18650bc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-21-a
* Sat Jul 21 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.37.20180720git18650bc
- Added patches for lldb to fix relative path issue (see URL by patches) until
  it's merged into the 4.2 branch
* Sat Jul 21 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.37.20180720git18650bc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-20-a
* Fri Jul 20 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.36.20180719git9277281
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-19-a
* Thu Jul 19 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.35.20180718gite325e32
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-18-a
* Tue Jul 17 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.34.20180716gitaaf545a
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-16-a 
* Sun Jul 15 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.33.20180703git107e307
- Switched from __provides_exclude_from to __provides_exclude to inhibit
  lldb being included as a dependency
* Thu Jul 12 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.32.20180703git107e307
- Reverted to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-03-a as loading modules
  in the REPL seems to have been broken as of the 2018-07-04 builds.
  2018-07-03 is currently the best version until the issue is resolved.
* Thu Jul 12 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.31.20180711git104c96a
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-11-a 
* Wed Jul 11 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.30.20180709gitd9561d9
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-09-a and added a check to
  include python-unversioned-command for verisons greated than 28 while
  working on making patches/pull requests upstream to be explicit about
  which version of Python to use. Also removed patch for time struct issue
  as the fix has been handled upstream. Also switched to ExclusiveArch
  instead of ExcludeArch per suggestion from Dan Horák.
* Thu Jul 05 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.29.20180705git1e2dc99
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-05-a
* Thu Jul 05 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.28.20180704gitf56a941
- Removed explicit requirement on libatomic and libbsd, modifed files section
  of the runtime package so it can own the directory
* Thu Jul 05 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.27.20180704gitf56a941
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-04-a
* Tue Jul 03 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.26.20180703git107e307
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-03-a, added a
  filter for excluding lldb libraries from public view, and broke out the
  runtime libraries into their own -runtime package. 
* Mon Jul 02 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.25.20180702gitc2e1567
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-02-a 
* Mon Jul 02 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.24.20180701git6079032
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-01-a, removed unnecessary
  lldb headers
* Sat Jun 30 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.23.20180630gitb3408e8
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-30-a 
* Fri Jun 29 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.22.20180629gitdab0d8e
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-29-a, removed unnecessary
  files and links
* Fri Jun 29 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.21.20180628git9f8f2a1
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-28-a 
* Thu Jun 28 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.20.20180626gitbe3b9a7
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-26-a 
* Wed Jun 13 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.19.20180612gitbb9532c
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-12-a and removed
  gcc-c++ as a build requirement
* Tue Jun 12 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.18.20180611gitd99cd32
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-10-a and removed
  separate ninja build (will now use the repo-based one)
* Mon Jun 11 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.17.20180610git7a35ad0
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-10-a 
* Fri Jun 08 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.16.20180607git78e9497
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-07-a 
* Thu Jun 07 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.15.20180606git4e2064e
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-06-a 
* Tue Jun 05 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.14.20180604git9e274fc
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-04-a 
* Sun Jun 03 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.13.20180602gitadad0f5
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-02-a 
* Wed May 30 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.12.20180529git4160301
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-05-29-a 
* Wed May 23 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.11.20180522git58f7399
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-05-22-a 
* Mon May 21 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.10.20180520gitbb77484
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-05-20-a and added
  patch for removing sys/ustat.h references
* Tue May 15 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.9.20180514gitf58f528
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-05-14-a
* Wed May 09 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.8.20180508git0e6d867
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-05-08-a
* Wed May 02 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.7.20180502gitb08fb12
- Updated to swift-4.2-DEVELOPMENT-SNAPSHOT-2018-05-02-a
* Mon Apr 23 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.6.20180422git5030d38
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-04-22-a
* Thu Apr 19 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.5.20180418gitac06163
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-04-18-a
* Mon Apr 16 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.4.20180415git22530b9
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-04-15-a
* Thu Apr 12 2018 Ron Olson <tachoknight@gmail.com> 4.2-0.3.20180411git537a846
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-04-11-a
* Wed Feb 28 2018 Ron Olson <tachoknight@gmail.com> 4.1-0.2.20180227git5f2f440
- Updated to swift-DEVELOPMENT-SNAPSHOT-2018-02-27-a
* Wed Feb 14 2018 Ron Olson <tachoknight@gmail.com> 4.1-0.1.20180214git5a1a34b
- Initial package for Fedora
