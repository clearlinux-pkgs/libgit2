#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgit2
Version  : 0.27.7
Release  : 19
URL      : https://github.com/libgit2/libgit2/archive/v0.27.7.tar.gz
Source0  : https://github.com/libgit2/libgit2/archive/v0.27.7.tar.gz
Summary  : The git library, take 2
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 MIT
Requires: libgit2-lib = %{version}-%{release}
Requires: libgit2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libssh2-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libcurl)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
hey

%package dev
Summary: dev components for the libgit2 package.
Group: Development
Requires: libgit2-lib = %{version}-%{release}
Provides: libgit2-devel = %{version}-%{release}

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
%setup -q -n libgit2-0.27.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540563911
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1540563911
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgit2
cp COPYING %{buildroot}/usr/share/package-licenses/libgit2/COPYING
cp deps/http-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/libgit2/deps_http-parser_LICENSE-MIT
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
/usr/lib64/libgit2.so.0.27.7
/usr/lib64/libgit2.so.27

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgit2/COPYING
/usr/share/package-licenses/libgit2/deps_http-parser_LICENSE-MIT
/usr/share/package-licenses/libgit2/examples_COPYING
