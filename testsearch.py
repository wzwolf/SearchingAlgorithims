#!/usr/bin/env python3

import search
import sort
import extractdata
import unittest

# test file extraction 
class TestExtractData(unittest.TestCase):
    """test file extraction. 
    if pass means file extracts each line of data into an array"""
    # setup()
    def setUp(self):
        pass # do something before each test are run
    # teardown
    def tearDown(self):
        pass # do something after each test are run
    # Test 1 - normal 
    def test_basic(self):
        testcase = "data1"
        expected = [66, 2, 74, 30, 68, 13, 58, 35, 10, 85, 80, 74, 15, 34, 82, 9, 72, 56]
        # Test passes if function(testcase) == expected
        self.assertEqual(extractdata.file_to_array(testcase), expected)


# test insertion sort
class TestInsertionSort(unittest.TestCase):
    """test insertion sort. 
    if pass means file managed to sort data correctly"""
    # setup()
    def setUp(self):
        pass # do something before each test are run
    # teardown
    def tearDown(self):
        pass # do something after each test are run
    # Test 1 - normal 
    def test_basic(self):
        testcase = extractdata.file_to_array("data1")
        expected = extractdata.file_to_array("sorteddata1")
        # Test passes if function(testcase) == expected
        self.assertEqual(sort.insertionsort(testcase), expected)
    # test 2 - data set 2 
    def test_data2(self):
        testcase = extractdata.file_to_array("data2")
        expected = extractdata.file_to_array("sorteddata2")
        # Test passes if function(testcase) == expected
        self.assertEqual(sort.insertionsort(testcase), expected)
    # test 3 - data set 3
    def test_data3(self):
        testcase = extractdata.file_to_array("data3")
        expected = extractdata.file_to_array("sorteddata3")
        # Test passes if function(testcase) == expected
        self.assertEqual(sort.insertionsort(testcase), expected)

# runs all the test
if __name__ == '__main__':
    unittest.main()

