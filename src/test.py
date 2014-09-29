import unittest

from kao_factory.Test.suite import suite as kao_factory_suite

# Collect all the test suites
suites = [kao_factory_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
