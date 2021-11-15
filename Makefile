.PHONY = build install

build:
	@python setup.py build

install:
	@python setup.py install --user
	@./scripts/install.sh

uninstall:
	@./scripts/uninstall.sh
	@pip uninstall wallpapr

clean:
	@rm -rf dist build wallpapr.egg-info
