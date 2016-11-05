help:
	@echo 'Help on this program'
	@echo
	@echo ' * build: Build the HTML page in the `build/` directory'

build:
	GIT_VERSION=`git describe --tags` VERSION=`git describe --tags --abbrev=0` tox

clean:
	rm -f build/*


.PHONY: build clean
