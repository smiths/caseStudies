PY = py -3
PYTST = pytest
PYFLAGS = --cov
DOXY = doxygen
DOXYCFG = doxConfig

PYDOC = $(PY) -m pydoc
PYDOCFLAGS = -w

RMDIR = rm -rf

.PHONY: test doc clean

test:
	$(PYTST) $(PYFLAGS)

doc:
	$(DOXY) $(DOXYCFG)
	cd latex && $(MAKE) 
	@echo The generated files can be viewed \
	in the new directories /html and /latex
  
clean:
	@- $(RMDIR) html
	@- $(RMDIR) latex