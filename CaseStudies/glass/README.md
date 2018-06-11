Case Studies Using Drasil

Files related to glass breaking project.


-------System Requirements-------

Python version: python3.4+ 
    
    NOTE: Different versions round floating points in different ways. Using prior versions might lead to failing in tests. Makefile currently set PY to python3.4. You might need to explicitly declare the version you use in order to run the code and tests.(e.g. python3.5 -m Implementation.mainfun "defaultInput.txt")

Numpy: A Python extension numpy needs to be installed in order to run the code and tests. You can find download location and build instructions here https://www.scipy.org/scipylib/download.html .
    
    NOTE: Numpy supports Python 2.x series as well as Python 3.2 and newer. The first release of Numpy to support Python 3 was Numpy 1.5.0..


-------Purpose of files and subfolders-------

/glass/docs: Contains the Software Requirements Specification (SRS), Module Guide (MG) for Glass-BR.

/glass/refs: Contains references.

/glass/src: Contains the code and testing for each module of Glass-BR, in C and Python.

/glass/test: Will contain testing in the future.

/glass/misc/latex.pdf: A general overview of the project.