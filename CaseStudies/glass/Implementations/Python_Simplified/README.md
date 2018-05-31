Case Studies Using Drasil

Files related to glass breaking project.


-------System Requirements-------

Python version: python3.4+ 
    
    NOTE: Different versions round floating points in different ways. Using prior versions might lead to failing in tests. Makefile currently set PY to python3.4. You might need to explicitly declare the version you use in order to run the code and tests.(e.g. python3.5 -m Implementation.mainfun "defaultInput.txt")

Numpy: A Python extension numpy needs to be installed in order to run the code and tests. You can find download location and build instructions here https://www.scipy.org/scipylib/download.html .
    
    NOTE: Numpy supports Python 2.x series as well as Python 3.2 and newer. The first release of Numpy to support Python 3 was Numpy 1.5.0..


-------How to run the code and tests-------

To run the code: Go to /Python_Simplified and type "make" at the prompt. This way "defaultInput.txt" is set as the input file that mainfun consumes. If you want to change the input file, type "python3.x -m Implementation.mainfun filename" instead.
                           
To run the tests: Go to /Python_Simplified and type "make test" at the prompt. 

    If you want to run the tests individually, type "python3.x -m unittest Test.test*.test*" instead. (The first "test*" is the name of the folders in /Python_Simplified/Test, e.g. testCalculations. The second "test*" is  the name 
        of the test file inside that folder. NOTE: don't include ".py").

    If you want to run the tests for a specific module, type "python3.x -m Test.test*.*Tests". ("test*" is the name of the folder that contains tests for this specific module and "*Tests" is the name of the python file that summarizes tests for this module, e.g. calcTests. NOTE: don't include "unittest" in the command line here)

To generate the documents: Go to /Python_Simplified and type "make doc" at the prompt.

To remove all the generated files and directories: Go to /Python_Simplified and type "make clean" at the prompt.

To do all of the above in one step: Go to /Python_Simplified and type "make all" at the prompt.

-------Purpose of files and subfolders-------

/Python_Simplified/Documentation: Contains the Software Requirements Specification (SRS) , Module Guide (MG) for Glass-BR.

/Python_Simplified/Implementation: Contains the code for each module of Glass-BR.

/Python_Simplified/Test: Contains the code for testing.

/Python_Simplified/Test/allTests.py: Test summary for all tests.

/Python_Simplified/Test/test*: Contains tests for the corresponding module.

/Python_Simplified/Test/test*/*Tests.py: Test summary for all tests of the corresponding module.

/Python_Simplified/Test/Inputfiles: Contains files needed for testing.

/Python_Simplified/Test/Inputfiles/testInput*.txt: These files contain valid input values for this program and are used as input files for tests.

/Python_Simplified/Test/Inputfiles/testInvalidInput*.txt: These files contain invalid input values for this program and are used as input files for tests (testCheckConstraints*.py mainly).

/Python_Simplified/Test/Inputfiles/output*.txt: These files contain the expected output of mainfun.py and are compared with the actual output of mainfun.py in testMainfun*.py.  

/Python_Simplified/Test/Inputfiles/testTable*.txt: These files contain data used in testReadTable*.py.

/Python_Simplified/OldTests: The same as /Test, but for old tests.

/Python_Simplified/TestDocumentation: Contains the documentation for the tests.

/Python_Simplified/SDF.txt TSD.txt: Contain data for interpolation.

/Python_Simplified/defaultInput.txt: The default input file that mainfun.py consumes.

/Python_Simplified/Makefile: Contains the build instructions for running 'make'.
