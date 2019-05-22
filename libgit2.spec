#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgit2
Version  : 0.28.2
Release  : 26
URL      : https://github.com/libgit2/libgit2/archive/v0.28.2/libgit2-0.28.2.tar.gz
Source0  : https://github.com/libgit2/libgit2/archive/v0.28.2/libgit2-0.28.2.tar.gz
Summary  : A linkable library for Git
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT Zlib
Requires: libgit2-lib = %{version}-%{release}
Requires: libgit2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libssh2-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
libgit2 examples
================
These examples are a mixture of basic emulation of core Git command line
functions and simple snippets demonstrating libgit2 API usage (for use
with Docurium).  As a whole, they are not vetted carefully for bugs, error
handling, and cross-platform compatibility in the same manner as the rest
of the code in libgit2, so copy with caution.

%package dev
Summary: dev components for the libgit2 package.
Group: Development
Requires: libgit2-lib = %{version}-%{release}
Provides: libgit2-devel = %{version}-%{release}
Requires: libgit2 = %{version}-%{release}
Requires: libgit2 = %{version}-%{release}

%description dev
dev components for the libgit2 package.


%package lib
Summary: lib components for the libgit2 package.
Group: Libraries
Requires: libgit2-license = %{version}-%{release}

%description lib
lib components for the libgit2 package.


%package license
Summary: license components for the libgit2 package.
Group: Default

%description license
license components for the libgit2 package.


%prep
%setup -q -n libgit2-0.28.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558516130
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1558516130
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgit2
cp COPYING %{buildroot}/usr/share/package-licenses/libgit2/COPYING
cp deps/http-parser/COPYING %{buildroot}/usr/share/package-licenses/libgit2/deps_http-parser_COPYING
cp deps/regex/COPYING %{buildroot}/usr/share/package-licenses/libgit2/deps_regex_COPYING
cp deps/winhttp/COPYING.GPL %{buildroot}/usr/share/package-licenses/libgit2/deps_winhttp_COPYING.GPL
cp deps/winhttp/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libgit2/deps_winhttp_COPYING.LGPL
cp deps/zlib/COPYING %{buildroot}/usr/share/package-licenses/libgit2/deps_zlib_COPYING
cp examples/COPYING %{buildroot}/usr/share/package-licenses/libgit2/examples_COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/git2/annotated_commit.h
/usr/include/git2/apply.h
/usr/include/git2/attr.h
/usr/include/git2/blame.h
/usr/include/git2/blob.h
/usr/include/git2/branch.h
/usr/include/git2/buffer.h
/usr/include/git2/checkout.h
/usr/include/git2/cherrypick.h
/usr/include/git2/clone.h
/usr/include/git2/commit.h
/usr/include/git2/common.h
/usr/include/git2/config.h
/usr/include/git2/cred_helpers.h
/usr/include/git2/deprecated.h
/usr/include/git2/describe.h
/usr/include/git2/diff.h
/usr/include/git2/errors.h
/usr/include/git2/filter.h
/usr/include/git2/global.h
/usr/include/git2/graph.h
/usr/include/git2/ignore.h
/usr/include/git2/index.h
/usr/include/git2/indexer.h
/usr/include/git2/inttypes.h
/usr/include/git2/mailmap.h
/usr/include/git2/merge.h
/usr/include/git2/message.h
/usr/include/git2/net.h
/usr/include/git2/notes.h
/usr/include/git2/object.h
/usr/include/git2/odb.h
/usr/include/git2/odb_backend.h
/usr/include/git2/oid.h
/usr/include/git2/oidarray.h
/usr/include/git2/pack.h
/usr/include/git2/patch.h
/usr/include/git2/pathspec.h
/usr/include/git2/proxy.h
/usr/include/git2/rebase.h
/usr/include/git2/refdb.h
/usr/include/git2/reflog.h
/usr/include/git2/refs.h
/usr/include/git2/refspec.h
/usr/include/git2/remote.h
/usr/include/git2/repository.h
/usr/include/git2/reset.h
/usr/include/git2/revert.h
/usr/include/git2/revparse.h
/usr/include/git2/revwalk.h
/usr/include/git2/signature.h
/usr/include/git2/stash.h
/usr/include/git2/status.h
/usr/include/git2/stdint.h
/usr/include/git2/strarray.h
/usr/include/git2/submodule.h
/usr/include/git2/sys/alloc.h
/usr/include/git2/sys/commit.h
/usr/include/git2/sys/config.h
/usr/include/git2/sys/diff.h
/usr/include/git2/sys/filter.h
/usr/include/git2/sys/hashsig.h
/usr/include/git2/sys/index.h
/usr/include/git2/sys/mempack.h
/usr/include/git2/sys/merge.h
/usr/include/git2/sys/odb_backend.h
/usr/include/git2/sys/openssl.h
/usr/include/git2/sys/path.h
/usr/include/git2/sys/refdb_backend.h
/usr/include/git2/sys/reflog.h
/usr/include/git2/sys/refs.h
/usr/include/git2/sys/repository.h
/usr/include/git2/sys/stream.h
/usr/include/git2/sys/time.h
/usr/include/git2/sys/transport.h
/usr/include/git2/tag.h
/usr/include/git2/trace.h
/usr/include/git2/transaction.h
/usr/include/git2/transport.h
/usr/include/git2/tree.h
/usr/include/git2/types.h
/usr/include/git2/version.h
/usr/include/git2/worktree.h
/usr/lib64/libgit2.so
/usr/lib64/pkgconfig/libgit2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgit2.so.0.28.2
/usr/lib64/libgit2.so.28

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgit2/COPYING
/usr/share/package-licenses/libgit2/deps_http-parser_COPYING
/usr/share/package-licenses/libgit2/deps_regex_COPYING
/usr/share/package-licenses/libgit2/deps_winhttp_COPYING.GPL
/usr/share/package-licenses/libgit2/deps_winhttp_COPYING.LGPL
/usr/share/package-licenses/libgit2/deps_zlib_COPYING
/usr/share/package-licenses/libgit2/examples_COPYING
