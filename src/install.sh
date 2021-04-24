#!/bin/bash
# -*- coding: utf8 -*-

FOLDER="mathcalc-1.0"

# dependencies to create debian file
sudo apt-get install build-essential autoconf automake autotools-dev dh-make debhelper devscripts fakeroot cdbs lintian pbuilder

cp cal.png main.py gui.py calculator.py mathlibcalc.py ../installer/$FOLDER
mkdir /opt/mathcalc

# create debian package
cd ../installer/$FOLDER && dh_make -e xkrali20@stud.fit.vutbr.cz -c gpl3 -n -s -f ../$FOLDER
cp ./config/install ./debian
cp ./config/control ./debian

# build debian
dpkg-buildpackage -rfakeroot -uc -b

# remove files (v pripade, ze nechcete zmazat zakomentovat)
rm *.py
rm cal.png
rm -rf debian
