help:
	@echo 'Help on this program'
	@echo
	@echo ' * html: Build the HTML page in the `build/` directory'
	@echo ' * clean: Remove the contents of the `build/` directory'

html:
	GIT_VERSION=`git describe --tags` VERSION=`git describe --tags --abbrev=0` tox

clean:
	rm -f build/*


.PHONY: build clean
