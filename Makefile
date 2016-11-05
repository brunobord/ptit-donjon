help:
	@echo 'Help on this program'
	@echo
	@echo ' * html: Build the HTML page in the `docs/` directory'
	@echo ' * clean: Remove the contents of the `docs/` directory'

html:
	GIT_VERSION=`git describe --tags` VERSION=`git describe --tags --abbrev=0` tox

clean:
	rm -f docs/*


.PHONY: build clean
