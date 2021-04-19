# Project IVS 2
# Author: Patrik Sehnoutek, xsehno01
# Date: 2021-04-16

SHELL = /bin/bash

.PNONY: all pack clean test doc run profile

all: run

depend:
	sudo apt install -y python3-pip
	pip3 install PyQt5

pack: doc
	mkdir -p ../../xkrali20_xsehno01_xcecha06/repo
	mkdir ../../xkrali20_xsehno01_xcecha06/doc
	mkdir ../../xkrali20_xsehno01_xcecha06/install
	cp -a ../../IVS-calculator/. ../../xkrali20_xsehno01_xcecha06/repo
	cp -a ../doc/. ../../xkrali20_xsehno01_xcecha06/doc
	cp -a ../install/. ../../xkrali20_xsehno01_xcecha06/install
	rm -rf ../../xkrali20_xsehno01_xcecha06/repo/doc
	rm -rf ../../xkrali20_xsehno01_xcecha06/repo/install
	cd ../.. && zip -r xkrali20_xsehno01_xcecha06.zip xkrali20_xsehno01_xcecha06
	 
clean:
	rm -rf ../../xkrali20_xsehno01_xcecha06

test: mathlibcalc_tests.py depend
	python3 mathlibcalc_tests.py

doc: Doxyfile
	sudo apt install -y doxygen
	sudo apt install -y graphviz
	cd .. && rm -rf doc
	mkdir ../doc && cd ../doc && doxygen ../src/$<

run: main.py depend
	python3 main.py

profile: profiling.py depend
	python3 profiling.py

installer: main.py mathlibcalc.py gui.py calculator.py
	bash install.sh
