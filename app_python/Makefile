PROJECT ?= .
VENVDIR ?= $(PROJECT)/venv

PYLINT := $(VENVDIR)/bin/pylint
PYLINTFLAGS := -rn
PYTHONFILES := $(wildcard $(PROJECT)/*.py) $(wildcard $(PROJECT)/*/*.py)

PYCODESTYLE := $(VENVDIR)/bin/pycodestyle
PYCODESTYLEFLAGS := --first

PYTEST := $(VENVDIR)/bin/pytest
PYTESTFLAGS := -rP

venv: $(VENVDIR)/touchfile

# Install dependencies and create touchfile to track venv changes
$(VENVDIR)/touchfile: $(PROJECT)/requirements.txt
	test -d $(VENVDIR) || python3 -m venv $(VENVDIR)
	. $(VENVDIR)/bin/activate; pip3 install -Ur $(PROJECT)/requirements.txt
	touch $(VENVDIR)/touchfile

clean:
	rm -rf $(VENVDIR) $(PROJECT)/__pycache__

# Lint all python files with pylint
pylint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

# Lint a specific file with pylint
%.pylint: $(VENVDIR)/touchfile
	$(PYLINT) $(PYLINTFLAGS) $*.py

# Check all python files for PEP compliance
pep8: $(patsubst %.py,%.pep8,$(PYTHONFILES))

# Check a specific file for PEP compliance
%.pep8: $(VENVDIR)/touchfile
	$(PYCODESTYLE) $(PYCODESTYLEFLAGS) $*.py

# Run pylint and PEP checks for all python files
lint: pep8 pylint

test: $(VENVDIR)/touchfile
	PYTHONPATH=$(PROJECT)/.. $(PYTEST) $(PYTESTLAGS) $(PROJECT)/tests
