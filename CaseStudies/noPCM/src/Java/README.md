This implementation requires Apache Commons Math. It can be downloaded from https://commons.apache.org/proper/commons-math/download_math.cgi. After downloading, create a lib/ directory here and add to it the commons-math3-3.6.1.jar file (version number might be different depending on when you downloaded Apache).

With the set-up completed, the following command will compile the program (from a Unix-style terminal):

`javac -cp lib/commons-math3-3.6.1.jar:. SWHS/Control.java SWHS/InputParameters.java SWHS/NoPCMODE.java SWHS/Calculations.java SWHS/OutputFormat.java`

Then to run the program on the test input provided here:

`java -cp lib/commons-math3-3.6.1.jar:. SWHS/Control test.in`