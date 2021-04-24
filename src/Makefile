# Project IVS 2
# Author: Patrik Sehnoutek, xsehno01
# Date: 2021-04-16

SHELL = /bin/bash

.PNONY: all depend pack clean test doc run profile installer

all: run

depend:
	bash dependencies.sh

pack: doc installer
	rm -rf ../../xkrali20_xsehno01_xcecha06
	mkdir -p ../../xkrali20_xsehno01_xcecha06/repo
	mkdir ../../xkrali20_xsehno01_xcecha06/doc
	mkdir ../../xkrali20_xsehno01_xcecha06/install
	cp -a ../../IVS-calculator/. ../../xkrali20_xsehno01_xcecha06/repo
	cp -a ../doc/. ../../xkrali20_xsehno01_xcecha06/doc
	cp -a ../installer/. ../../xkrali20_xsehno01_xcecha06/install
	rm -rf  ../../xkrali20_xsehno01_xcecha06/install/mathcalc-1.0
	rm -rf ../../xkrali20_xsehno01_xcecha06/repo/doc
	cd ../.. && zip -r xkrali20_xsehno01_xcecha06.zip xkrali20_xsehno01_xcecha06
	 
clean:
	rm -rf ../../xkrali20_xsehno01_xcecha06

test: mathlibcalc_tests.py depend
	python3 $<

doc: Doxyfile
	sudo apt install -y doxygen
	sudo apt install -y graphviz
	cd .. && rm -rf doc
	mkdir ../doc && cd ../doc && doxygen ../src/$<

run: main.py depend
	python3 $<

profile: profiling.py depend
	python3 $<

installer: main.py mathlibcalc.py gui.py calculator.py
	bash install.sh
