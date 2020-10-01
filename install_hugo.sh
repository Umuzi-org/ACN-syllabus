#!/bin/sh

VERSION_HUGO="0.51"  # this version matches the one on AWS amplify

wget "https://github.com/gohugoio/hugo/releases/download/v${VERSION_HUGO}/hugo_${VERSION_HUGO}_Linux-64bit.tar.gz" && \
tar -xf hugo_${VERSION_HUGO}_Linux-64bit.tar.gz hugo -C / && \
sudo mv hugo /usr/bin/hugo && \
rm -rf hugo_${VERSION_HUGO}_Linux-64bit.tar.gz

hugo