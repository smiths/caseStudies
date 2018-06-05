import os
import unittest
from Implementation import readTable
import numpy as np

class TestReadTable(unittest.TestCase):
   
   def setUp(self):
        # reads readTable.txt input file and saves it as input
        with open(os.path.join("Test/Inputfiles", "readTable.txt"), 'r') as f:
            input = f.readlines()

        # input is split based on ";" delimiter
        input = list(map(lambda x: x.split(";"), input))
 
        self.numTests = len(input)
        self.inputFileName    = [row[0]          for row in input] 
        self.num_colShouldBe  = [row[1]          for row in input]
        self.array1Expctd     = [row[2]          for row in input]
        self.array2Expctd     = [row[3].rstrip() for row in input]

        self.num_col = []
        self.array1  = []
        self.array2  = []

        for i in range(self.numTests):
            self.num_col += [readTable.read_z_array(os.path.join("Test/Inputfiles", self.inputFileName[i]))]
            self.array1 += [readTable.read_x_array(os.path.join("Test/Inputfiles", self.inputFileName[i]), self.num_col[i])]
            self.array2 += [readTable.read_y_array(os.path.join("Test/Inputfiles", self.inputFileName[i]), self.num_col[i])]

   # checks if returned weight charges from the first line of the input files are as expected
   def test_read_z_array(self):
       for i in range(self.numTests):
        with self.subTest(i=i):
          z = (self.num_colShouldBe[i]).split(",") #e.g. --> '4.5,9.1,14.,18.' becomes ['4.5','9.1','14.','18.']
          z = [float(temp) for temp in z]         #e.g. --> [4.5,9.1,14.,18.]
          self.assertTrue(self.num_col[i] == z)

  #fixme: determine semantics of using these particular numbers
   def test_read_x_array(self):
       self.assertTrue((self.array1[0] == np.array([[6.143397364345, 6.128184215473, 6.344639409554, 7.199850837298],
                                                    [6.158648279689, 6.158648279689, 6.344639409554, 7.21772438659],
                                                    [6.189263785047, 6.189263785047, 6.376179502933, 7.253604707984],
                                                    [6.189263785047, 6.189263785047, 6.407876386546, 7.271611700659],
                                                    [6.204628563268, 6.22003148438, 6.407876386546, 7.289663395493]])).all())
       self.assertTrue((self.array1[1] == np.array([[7.970252894984, 9.112111846077, 9.815736636723, 10.67908230799, 11.70510612844],
                                                    [8.009874141258, 9.157409433529, 9.864532041808, 10.73216952563, 11.73416392368],
                                                    [8.009874141258, 9.20293220165 , 9.864532041808, 10.78552064729, 11.79249610018],
                                                    [8.049692350311, 9.20293220165 , 9.924500405864, 10.83913698486, 11.85111825412],
                                                    [8.089708501272, 9.248681269843, 9.980983057161, 10.89301985678, 11.85111825412],
                                                    [8.089708501272, 9.294657763077, 9.987584432489, 10.89301985678, 11.92316345312]])).all())
       #for i in range(self.numTests):
       # with self.subTest(i=i):
          #x = (self.array1Expctd[i]).split(",") 
          #x = [float(temp) for temp in z]
          #self.assertTrue(self.array1[i] == x)
          #self.assertTrue(...)

   #fixme: determine semantics of using these particular numbers
   def test_read_y_array(self):
       self.assertTrue((self.array2[0] == np.array([[4.411877630513, 7.62703125734, 9.952136903603, 9.992650492472],
                                                    [4.388319475839, 7.575020192327, 10.00554408521, 9.924527029632],
                                                    [4.364878545185, 7.494339327108, 9.898975926537, 9.871513535251],
                                                    [4.341579876052, 7.534556975369, 9.793542815831, 9.833410793036],
                                                    [4.318397091121, 7.434385814135, 9.846098917578, 9.766372924029]])).all())
       self.assertTrue((self.array2[1] == np.array([[9.923747652747, 9.922695591037, 9.975357211856, 9.974691344625, 9.988805920683],
                                                    [9.806380585608, 9.869691879586, 9.869110570885, 9.894895413212, 9.920708667661],
                                                    [9.870738321536, 9.764570670656, 9.922072199691, 9.815737836455, 9.867715569689],
                                                    [9.765605967045, 9.816971296184, 9.816384526916, 9.763305457453, 9.762615410259],
                                                    [9.661593367897, 9.71241160949 , 9.774400184513, 9.659317360827, 9.81500554307 ],
                                                    [9.713441375674, 9.608965578705, 9.726269624499, 9.711153154632, 9.710458320146]])).all())
       #for i in range(self.numTests):
       # with self.subTest(i=i):
       #   self.assertTrue(...)
   
if __name__ == "__main__":
    unittest.main()