import pytest
from FunctADT import *
from SeqServices import *
from Input import *
from GlassTypeADT import GlassTypeT

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

    # test Input.py

    @staticmethod
    def test_load_params():
        s = "NewImplementation\\TestFiles\\defaultInputFile.txt"
        assert (load_params(s) == 4.0, 2.0, GlassTypeT("AN"), 0.008,  
                                  0.0, 1.5, 11.0, 2.5, 1.0, 10,
                                  7, 2.86e-53, 7.17e7, 3, 1, 
                                  0.26965, 2.16, 1, 11.1018, 2.0)
        with pytest.raises(FileNotFoundError):
            f = load_params("nonExistantDirectory.txt")

    @staticmethod
    def test_verify_params():
        path = "NewImplementation\\TestFiles\\"
        with pytest.raises(ValueError):
            v = load_params(path+"aNegative.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"aSmallerThanB.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"aTooLarge.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"aTooSmall.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"arMaxExceeded.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"bNegative.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"bTooLarge.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"bTooSmall.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"pbTolAboveOne.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"pbTolBelowZero.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"wNegative.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"wTooLarge.txt")
        with pytest.raises(ValueError):
            v= load_params(path+"wTooSmall.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"tntNegative.txt")
        with pytest.raises(ValueError):
            v = load_params(path+"sdTooLarge.txt")
        with pytest.raises(ValueError):
            v= load_params(path+"sdTooSmall.txt")


