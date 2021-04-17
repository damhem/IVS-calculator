#!/bin/bash
# -*- coding: utf8 -*-

FOLDER="mathcalc-1.0"

sudo apt-get install build-essential autoconf automake autotools-dev dh-make debhelper devscripts fakeroot cdbs lintian pbuilder

cp main.py gui.py calculator.py mathlibcalc.py ../installer/$FOLDER

# vytvorenie debian balicku
cd ../installer/$FOLDER && dh_make -e xkrali20@stud.fit.vutbr.cz -c gpl3 -n -s -f ../$FOLDER
cp ./config/install ./debian
cp ./config/control ./debian

# build debian
dpkg-buildpackage -rfakeroot -uc -b

# remove files (v pripade, ze nechcete zmazat zakomentovat)
rm *.py
rm -rf debian
