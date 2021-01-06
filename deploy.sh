#!/bin/sh

hugo
gsutil rsync -R public gs://syllabus.africacode.net
