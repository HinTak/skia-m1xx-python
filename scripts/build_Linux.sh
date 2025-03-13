#!/usr/bin/env bash

export PATH=${PWD}/depot_tools:$PATH

EXTRA_CFLAGS=""

if [[ $(uname -m) == "aarch64" ]]; then
    # Install ninja for aarch64
    yum -y install epel-release && \
        yum repolist && \
        yum install -y ninja-build && \
        mv depot_tools/ninja depot_tools/ninja.bak
fi

# Install system dependencies
yum install -y \
    python3 \
    fontconfig-devel \
    mesa-libGL-devel \
    xorg-x11-server-Xvfb \
    mesa-dri-drivers && \
    yum clean all && \
    rm -rf /var/cache/yum

if [[ $(uname -m) == "aarch64" ]] && [[ $CI_SKIP_BUILD == "true" ]]; then
    # gn and skia already built in a previous job
    exit 0
fi

# Build gn
export CC=gcc
export CXX=g++
export AR=ar
export CFLAGS="-Wno-deprecated-copy"
export LDFLAGS="-lrt"
git clone https://gn.googlesource.com/gn && \
    cd gn && \
    git checkout fe330c0ae1ec29db30b6f830e50771a335e071fb && \
    python3 build/gen.py && \
    ninja -C out gn && \
    cd ..

# Build skia
cd skia && \
    python3 tools/git-sync-deps && \
    patch -p1 < ../patch/make_data_assembly.patch && \
    patch -p1 < ../patch/libjpeg-arm.patch && \
    cp -f ../gn/out/gn bin/gn && \
    bin/gn gen out/Release --args="
is_official_build=true
skia_enable_tools=true
skia_use_system_libjpeg_turbo=false
skia_use_system_libwebp=false
skia_use_system_libpng=false
skia_use_system_icu=false
skia_use_system_harfbuzz=false
extra_cflags_cc=[\"-frtti\"]
extra_ldflags=[\"-lrt\"]
" && \
    ninja -C out/Release skia skia.h experimental_svg_model && \
    cd ..
