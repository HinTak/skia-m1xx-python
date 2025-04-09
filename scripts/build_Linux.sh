#!/usr/bin/env bash

export PATH=${PWD}/depot_tools:$PATH

EXTRA_CFLAGS=""

# Install system dependencies
yum -y install epel-release && \
yum install -y \
    ninja-build gn \
    fontconfig-devel \
    mesa-libGL-devel \
    xorg-x11-server-Xvfb \
    mesa-dri-drivers && \
    yum clean all && \
    mv depot_tools/ninja depot_tools/ninja.bak && \
    mv depot_tools/gn depot_tools/gn.bak && \
    rm -rf /var/cache/yum

# EL8 anomaly: EL7 is python 2 and EL9 is python 3
[[ -f /usr/bin/python ]] || ln -s /usr/bin/python3 /usr/bin/python

# Build skia
cd skia && \
    patch -p1 < ../patch/git-sync-deps.patch && \
    python tools/git-sync-deps && \
    patch -p1 < ../patch/make_data_assembly.patch && \
    patch -p1 < ../patch/libjpeg-arm.patch && \
    patch -p1 < ../patch/skia-m87-c++-code.diff && \
    patch -p1 < ../patch/8d921a16f835aa6da69bac16f77ac0305e478954.patch && \
    patch -p1 < ../patch/ed435953dfd6e277549f07bb2fa977130f0e29fc.patch && \
    patch -p1 < ../patch/4f4c064d5b749f139eb69d6e7f3852cb0fd53d4f.patch && \
    gn gen out/Release --args="
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
