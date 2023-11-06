#!/bin/sh

hugo
gsutil rsync -R public gs://content.africacode.net
