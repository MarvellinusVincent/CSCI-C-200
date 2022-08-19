# Assignment 6

- Username: mvincen
- Commit hash used for grading: 509a4b6c8454648571f43c79768d022141ee8df0

- Graded by: Ankush Pathak

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 69.5/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (33.0/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `C`:4.0/4
    - `B`: 6.0/6
    - TA Comments: All good!


- Problem 2:
    - `get_data`: 0.0/4
    - `pop`: 3.0/3
    - `error`: 0.0/3
    - TA Comments: 
      - `get_data`: You are opening the file incorrectly. You were supposed to use the `path` and `name` parameters.
      - `error`: Each element in `data` is a tuple, you were supposed to unpack the tuple to get the year and population value for that year out from the tuple. Also not sure why you multiplied `i` by 10.


- Problem 3:
    - `isogram`: 10.0/10
    - TA Comments: All good!


- Problem 4:
    - `Hex`:0/10
    - TA Comments: The problem explicitly states you cannot use Python built-ins.


- Problem 5:
    - `div_11`: 10.0/10
    - TA Comments: All good!


## Code Review & style (36.5/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `C`:4.0/4
    - `B`: 6.0/6
    - TA Comments: Good job!


- Problem 2:
    - `get_data`: 2/4
    - `pop`: 3.0/3
    - `error`: 1.5/3
    - TA Comments: Please work on understanding how to read data from files.


- Problem 3:
    - `isogram`: 10.0/10
    - TA Comments: Good job!


- Problem 4:
    - `Hex`:0/10
    - TA Comments: The problem explicitly states you cannot use Python built-ins.


- Problem 5:
    - `div_11`: 10.0/10
    - TA Comments: Good job!

## Unittest Results
```
WARNING: Could not reliably determine column separator assuming it to be space.
INFO: Guessed " " as the file separator expected by the get_data function
ERROR: ============================================================================
ERROR: Failed test case: test_d_getdata_2_data_test
ERROR: Test case for function: getdata
ERROR: Input: 0 1650
10 1750
20 1860
30 2070
40 2300
50 2560
60 3040
70 3710
80 4450
90 5280
100 6080
110 6870

ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: [(0, 1650), (10, 1750), (20, 1860), (30, 2070), (40, 2300), (50, 2560), (60, 3040), (70, 3710), (80, 4450), (90, 5280), (100, 6080), (110, 6870)]
ERROR: not enough values to unpack (expected 2, got 0)
ERROR: ----------------------------------------------------------------------------
ERROR: not enough values to unpack (expected 2, got 0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6_hidden_test.py", line 203, in test_d_getdata_2_data_test
    actual_output = a6.get_data("some_path", "some_file")
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6.py", line 52, in get_data
    year,pop = i.split()
ValueError: not enough values to unpack (expected 2, got 0)
ERROR: ============================================================================
```
```
WARNING: Could not reliably determine column separator assuming it to be space.
INFO: Guessed " " as the file separator expected by the get_data function
ERROR: ============================================================================
ERROR: Failed test case: test_d_getdata_2_data_test
ERROR: Test case for function: getdata
ERROR: Input: 0 100

ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: [(0, 100)]
ERROR: not enough values to unpack (expected 2, got 0)
ERROR: ----------------------------------------------------------------------------
ERROR: not enough values to unpack (expected 2, got 0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6_hidden_test.py", line 203, in test_d_getdata_2_data_test
    actual_output = a6.get_data("some_path", "some_file")
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6.py", line 52, in get_data
    year,pop = i.split()
ValueError: not enough values to unpack (expected 2, got 0)
ERROR: ============================================================================
```
```
WARNING: Could not reliably determine column separator assuming it to be space.
INFO: Guessed " " as the file separator expected by the get_data function
ERROR: ============================================================================
ERROR: Failed test case: test_d_getdata_2_data_test
ERROR: Test case for function: getdata
ERROR: Input: 0 100
10 200

ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: [(0, 100), (10, 200)]
ERROR: not enough values to unpack (expected 2, got 0)
ERROR: ----------------------------------------------------------------------------
ERROR: not enough values to unpack (expected 2, got 0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6_hidden_test.py", line 203, in test_d_getdata_2_data_test
    actual_output = a6.get_data("some_path", "some_file")
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6.py", line 52, in get_data
    year,pop = i.split()
ValueError: not enough values to unpack (expected 2, got 0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_getdata_2_filename_test
ERROR: Test case for function: get_data
ERROR: Input: ('SomeFolder', 'some_file')
ERROR: Actual output: pop.txt
ERROR: Expected output: Correctly constructed file path
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_getdata_2_filename_test
ERROR: Test case for function: get_data
ERROR: Input: ('Assignment6', 'pop.txt')
ERROR: Actual output: pop.txt
ERROR: Expected output: Correctly constructed file path
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_error_3_sample
ERROR: Test case for function: error
ERROR: Input: [(0, 1650), (10, 1750), (20, 1860), (30, 2070), (40, 2300), (50, 2560), (60, 3040), (70, 3710), (80, 4450), (90, 5280), (100, 6080), (110, 6870)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: [6.196115261019245, 2300.210770763446]
ERROR: unsupported operand type(s) for ** or pow(): 'float' and 'tuple'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for ** or pow(): 'float' and 'tuple'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6_hidden_test.py", line 269, in test_g_error_3_sample
    actual_ouput = a6.error(filedata)
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6.py", line 71, in error
    a = (i * 10) - pop(i * 10)
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/mvincen/a6.py", line 63, in pop
    return 1436.53*(1.01395)**year
TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'tuple'
ERROR: ============================================================================
```
```
