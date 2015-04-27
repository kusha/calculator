# ReadHead calculator makefile
# Authors: Mark Birger, Daniil Khudiakov, Martin Knotek
# Date: 26 Apr 2015

all:
	python3 setup.py build

install:
	python3 setup.py install

uninstall:
	python3 setup.py install --record files.txt ; tr '\n' '\0' < files.txt | xargs -0 rm -f -- ; rm -f ./files.txt ;

doc:
	doxygen Doxyfile

clean:
	rm -rf ./build ./dist ./docs redhead_calculator.egg-info
