PY = py -3
PYTST = pytest
PYFLAGS = --cov
DOXY = doxygen
DOXYCFG = doxConfig

PYDOC = $(PY) -m pydoc
PYDOCFLAGS = -w

RMDIR = rm -rf

DOCDIR = doc

.PHONY: test doc clean

test:
	$(PYTST) $(PYFLAGS)

doc:
	mkdir -p $(DOCDIR)
	$(DOXY) $(DOXYCFG)
	cd html && mv *.html ../$(DOCDIR)
	cd latex && $(MAKE) 
	cd latex && mv *.tex ../$(DOCDIR)
	cd latex && mv *.pdf ../$(DOCDIR)
	@echo The generated files have been moved \
	to a new directory /$(DOCDIR)
  
clean:
	@- $(RMDIR) html
	@- $(RMDIR) latex