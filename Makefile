# makefile for Abstrys CLI Demos
#

build:
	./setup.py build

install:
	./setup.py install --user

uninstall:
	pip3 uninstall -y abstrys-cli-demos

docs:
	sphinx-build -b html docsrc doc_build

clean:
	rm -rf doc_build

spotless:
	rm -rf doc_build
	rm -rf build
	rm -rf dist
	rm -rf abstrys_cli_demos.egg-info

