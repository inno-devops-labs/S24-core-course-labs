PROJECT := app_python
VENVDIR ?= $(PROJECT)/venv

include app_python/Makefile

run: $(VENVDIR)/touchfile
	. $(VENVDIR)/bin/activate; python3 -m $(PROJECT)
