import pytest
from FunctADT import *
from SeqServices import *
from Input import Input
from GlassTypeADT import *
from ThicknessADT import ThicknessT
from ContoursADT import ContoursT

from math import isclose

class TestAll:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
    
    def setup_method(self):
        X = [1, 2, 10]
        Y = [1, 2, 10]
        o = 1
        self.c1 = FuncT(X, Y, o)

        X = [0, 5, 9, 13]
        Y = [0, 3, 30, 27]
        o = 2
        self.c2 = FuncT(X, Y, o)

    def teardown_method(self, method):
        self.c1 = None
        self.c2 = None

    # test SeqServices.py

    @staticmethod
    def test_isAscending():
        assert (isAscending([1, 2, 3, 4, 5.5]))
        assert (not (isAscending([1, 2, 3, 4, 0])))
        assert (not (isAscending([1, 2, 0, 4, 5])))

    @staticmethod
    def test_isInBounds():
        A = [1, 2, 3, 4, 5.5]
        assert (isInBounds(A, 3.4))
        assert (not(isInBounds(A, 100)))
        assert (not(isInBounds(A, 0)))
    
    @staticmethod
    def test_interpLin():
        assert (interpLin(3 , 6 , 4.5 , 5.67 , 4) == 5.78)
        
    @staticmethod
    def test_interpQuad():
        assert (interpQuad(0, 0, 3 , 6 , 4.5 , 5.67 , 4) == (5.8533333333333335))

    @staticmethod
    def test_index():
        A = [1, 2, 3, 4, 5.5]
        assert (index(A, 1) == 0) # x is present in list, checks "=" req
        assert (index(A, 5.5) == 3) # ensures that x < A[i+1]
        assert (index([1, 2, 3, 4, 5.5], 3.12345678) == 2) # i can be found easily

    # test FuncTADT.py
    
    # Testing exceptions of FuncT and associated methods
    @staticmethod
    def test_FuncT_ssmErr():
        with pytest.raises(SeqSizeMismatch):
            c = FuncT([0,1,2], [0], 1)
            c = FuncT([0], [0,1,2], 2)

    @staticmethod
    def test_FuncT_notAscendingErr():
        with pytest.raises(IndepVarNotAscending):
            c = FuncT([0,0,0], [0, 1, 3], 1) # x values are equal
            c = FuncT([5,4,6], [0, 1, 3], 2)

    @staticmethod
    def test_FuncT_InvalidInterpErr():
        with pytest.raises(InvalidInterpOrder):
            c = FuncT([1, 2, 3], [0, 1, 3], 0)
            c = FuncT([1, 2, 3], [0, 1, 3], 3)

    def test_FuncT_oodErr(self):
        with pytest.raises(OutOfDomain):
            e = self.c1.eval(100)

    # Testing to ensure that the methods of FuncT functions as intended
    def test_minD(self):
        assert (self.c1.minD() == 1)

    def test_maxD(self):
        assert (self.c1.maxD() == 10)

    def test_order(self):
        assert (self.c1.order() == 1)

    def test_eval(self):
        assert (self.c1.eval(3) == 3) # order 1 tested
        assert (self.c2.eval(6) == 7.083333333333334) # order 2 tested

# test GlassTypeADT.py

class TestGlassTypeADT:

    # Testing initialization of GlassTypeT and exceptions
    def test_constructor_GlassTypeT(self):
        assert (GlassTypeT("AN").g == gtf.AN)
        assert (GlassTypeT("FT").g == gtf.FT)
        assert (GlassTypeT("HS").g == gtf.HS)
        with pytest.raises(ValueError):
            gt = GlassTypeT("GT").g
        with pytest.raises(ValueError):
            gt = GlassTypeT("an").g
        with pytest.raises(ValueError):
            gt = GlassTypeT("").g
        with pytest.raises(ValueError):
            gt = GlassTypeT(2).g

    #Testing conversion from glass type to GTF
    def test_GTF(self):
        assert (GlassTypeT("AN").GTF() == 1.0)
        assert (GlassTypeT("FT").GTF() == 4.0)
        assert (GlassTypeT("HS").GTF() == 2.0)

    #Testing getting string
    def test_toString(self):
        assert (GlassTypeT("AN").toString() == "AN")
        assert (GlassTypeT("FT").toString() == "FT")
        assert (GlassTypeT("HS").toString() == "HS")

# test ThicknessADT.py

class TestThicknessT:

    # Testing initialization of ThicknessT and exceptions
    def test_constructor_ThicknessT(self):
        assert (ThicknessT(2.5).t == 2.5)
        assert (ThicknessT(2.7).t == 2.7)
        assert (ThicknessT(3.0).t == 3.0)
        assert (ThicknessT(22.0).t == 22.0)
        with pytest.raises(ValueError):
            th = ThicknessT(1.0).t
        with pytest.raises(ValueError):
            th = ThicknessT("2.5").t

    # Testing conversion from t to h

    def test_toMinThick(self):
        assert (ThicknessT(2.5).toMinThick() == 2.16)
        assert (ThicknessT(2.7).toMinThick() == 2.59)
        assert (ThicknessT(3.0).toMinThick() == 2.92)
        assert (ThicknessT(4.0).toMinThick() == 3.78)
        assert (ThicknessT(5.0).toMinThick() == 4.57)
        assert (ThicknessT(6.0).toMinThick() == 5.56)
        assert (ThicknessT(8.0).toMinThick() == 7.42)
        assert (ThicknessT(10.0).toMinThick() == 9.02)
        assert (ThicknessT(12.0).toMinThick() == 11.91)
        assert (ThicknessT(16.0).toMinThick() == 15.09)
        assert (ThicknessT(19.0).toMinThick() == 18.26)
        assert (ThicknessT(22.0).toMinThick() == 21.44)

    # Testing getting t (float)

    def test_toFloat(self):
        assert (ThicknessT(2.5).toFloat() == 2.5)
        assert (ThicknessT(8.0).toFloat() == 8.0)
        assert (ThicknessT(22.0).toFloat() == 22.0)

# test Input.py

class TestInput:
    # Testing initialization of Input
    def test_constructor_Input(self):
        init = Input()
        assert init.a == 0.0
        assert init.b == 0.0
        assert init.g == "AN"
        assert init.Pbtol == 0.0
        assert init.SDx == 0.0
        assert init.SDy == 0.0
        assert init.SDz == 0.0
        assert init.t == 2.5
        assert init.TNT == 0.0
        assert init.w == 0.0
        
        assert init.m == 0.0
        assert init.k == 0.0
        assert init.E == 0.0
        assert init.td == 0.0
        assert init.LSF == 0.0

        assert init.LDF == 0.0
        assert init.h == 0.0
        assert init.GTF == 0.0
        assert init.SD == 0.0
        assert init.AR == 0.0

    # Testing loading from file and FileNotFoundError exception
    def test_load_params_default(self):
        s = "NewImplementation\\TestFiles\\defaultInputFile.txt"
        default = Input()
        default.load_params(s)
        assert default.a == 4.0
        assert default.b == 2.0
        assert default.g.toString() == "AN"
        assert default.Pbtol == 0.008
        assert default.SDx == 0.0
        assert default.SDy == 1.5
        assert default.SDz == 11.0
        assert default.t.toFloat() == 2.5
        assert default.TNT == 1.0
        assert default.w == 10
        
        assert default.m == 7
        assert default.k == 2.86e-53
        assert default.E == 7.17e7
        assert default.td == 3
        assert default.LSF == 1

        assert isclose(default.LDF, 0.2696, abs_tol=0.0001)
        assert default.h == 2.16
        assert default.GTF == 1
        assert isclose(default.SD, 11.1018, abs_tol=0.0001)
        assert default.AR == 2.0

        fail = Input()
        with pytest.raises(FileNotFoundError):
            fail.load_params("nonExistantDirectory.txt")

    # Testing exceptions of verify_params()
    def test_verify_params(self):
        path = "NewImplementation\\TestFiles\\"
        init = Input()
        with pytest.raises(ValueError):
            init.load_params(path+"aNegative.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"aSmallerThanB.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"aTooLarge.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"aTooSmall.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"arMaxExceeded.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"bNegative.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"bTooLarge.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"bTooSmall.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"pbTolAboveOne.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"pbTolBelowZero.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"wNegative.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"wTooLarge.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"wTooSmall.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"tntNegative.txt")
        # Cannot create a test case for SD < 0, since it is calculated from
        # positive numbers and will always be positive.
        with pytest.raises(ValueError):
            init.load_params(path+"sdTooLarge.txt")
        with pytest.raises(ValueError):
            init.load_params(path+"sdTooSmall.txt")

# test ContoursADT.py

class TestContoursT:
    # Testing initialization of ContoursT and exceptions
    def test_constructor_ContoursT(self):
        assert(ContoursT(1).S == [])
        assert(ContoursT(1).Z == [])
        assert(ContoursT(2).o == 2)
        with pytest.raises(InvalidInterpOrder):
            ct = ContoursT(3).o
        with pytest.raises(InvalidInterpOrder):
            ct = ContoursT(0).o

    # Testing adding of elements to state variables
    def test_add(self):
        init = ContoursT(1)
        init.add(1, 1)
        assert(init.S == [1])
        assert(init.Z == [1])
        init.add(3.5, 2)
        assert(init.S == [1, 3.5])
        assert(init.Z == [1, 2])
        with pytest.raises(IndepVarNotAscending):
            init.add(5, 0)
        with pytest.raises(IndepVarNotAscending):
            init.add(5, 2)

    # Testing getting an element from S
    def test_getC(self):
        init = ContoursT(1)
        init.add(1, 1)
        init.add(3.5, 2)
        assert(init.getC(0) == 1)
        assert(init.getC(1) == 3.5)
        with pytest.raises(InvalidIndex):
            init.getC(2)

    # Testing generating a FuncT class
    def test_slice(self):
        init = ContoursT(1)
        with pytest.raises(OutOfDomain):
            init.slice(0, False)