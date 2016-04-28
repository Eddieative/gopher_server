server:
	python2.7.10 ./server.py

client:
	python2.7.10 ./client.py

compile:
	-python2.7.10 setup.py clean --all
	-rm -f `find . -name "*~"`
	-rm -f `find . -name "*.pyc"`
	-rm -f `find . -name "*.pygc"`
	-rm -f `find . -name "*.class"`
	-rm -f `find . -name "*.bak"`
	-rm -f `find . -name ".cache*"`
	-rm -f `find . -name "*.pyc"`
	-rm -rf build
	python2.7.10 setup.py install