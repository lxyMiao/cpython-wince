#!/bin/bash

rm pyconfig.tmp pyconfig.pre.tmp
rm zip.list
rm -rf wince_build
rm make.log

if test -e Makefile; then
    make distclean;
fi

echo "Clean up finished."
