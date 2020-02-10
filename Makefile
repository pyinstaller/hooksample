# You can set these variables from the command line.
VENVDIR       = _venv
SPHINXOPTS    =
SPHINXBUILD   = "$(VENVDIR)"/bin/sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

PLATFORM:=$(shell uname)
ifeq ($(PLATFORM),Linux)
    OPEN?=xdg-open
else ifeq ($(PLATFORM),Darwin)
    OPEN?=open
endif

# Put it first so that "make" without argument is like "make help".
help: _venv
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean dist-clean venv

clean:
	rm -rf "$(BUILDDIR)"

dist-clean: clean
	rm -rf "$(VENVDIR)"

_venv:
	python3 -m venv "$(VENVDIR)"
	"$(VENVDIR)"/bin/pip install --upgrade pip
	"$(VENVDIR)"/bin/pip install -r docs-requirements.txt
	@echo
	@echo "Now run 'make html'"

# Open the built website, works on macOS and Linux
.PHONY: open
open:
	"$(OPEN)" _build/html/index.html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile _venv
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
