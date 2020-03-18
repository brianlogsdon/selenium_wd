import unittest
from unitTestPackage.test_class1 import TestClass1
from unitTestPackage.test_class2 import TestClass2


# get all tests from testclass1 and test class2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)


# create test suite combining the 2

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)