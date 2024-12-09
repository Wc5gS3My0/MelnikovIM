import unittest
import tests_12_3
import modul12_1
my_test_suite = unittest.TestSuite()

my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(modul12_1.RunnerTest))
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_test_suite)