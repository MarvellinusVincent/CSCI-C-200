# Assignment 5

- Username: mvincen
- Commit hash used for grading: d7fde38e14673d019c377ed4a4ed702f31285571

- Graded by: Sara Zomorodi

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 84.4/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (40.9/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `makeProbability`:3.0/3
    - `entropy`: 3.0/3
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `L`: 5.2/7
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `div9`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `p`:3.0/3
    - `c`:1.5/3
    - `d`: 3.0/3
    - TA Comments: Your c_g has issues. 


- Problem 5:
    - `potato`: 2.2/7
    - TA Comments: There is on logical error with this fucntion. 


- Problem 6:
    - `msi`: 6.0/7
    - TA Comments: You are just missing one single test case. 


- Problem 7:
    - `dollars`: 7.0/7
    - TA Comments: TA did not add any comments.

## Code Review & style (43.5/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `makeProbability`: 3/3
    - `entropy`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `L`: 5/7
    - TA Comments: You have to look for the biggest series of 1. But you are comparing them to the first element. But what about `x[0]` itself? 


- Problem 3:
    - `div9`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `p`: 3/3
    - `c`: 2/3
    - `d`: 3/3
    - TA Comments: You are forgetting the second variable in `c_g`. 


- Problem 5:
    - `potato`: 4/7
    - TA Comments: Your while loop only runs once. Because you didn;t need indent it. So it'll just run once for `size=2`.


- Problem 6:
    - `msi`: 6.5/7
    - TA Comments: You never check the last item in the list itself. Look at line 218 in your code. You are starting from i+1. 


- Problem 7:
    - `dollars`: 7/7
    - TA Comments: TA did not add any comments.

## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_L_2_hard
ERROR: Test case for function: L
ERROR: Input: ([1, 1, 1, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 0
ERROR: Expected output: 4
ERROR: 4 != 0
ERROR: ----------------------------------------------------------------------------
ERROR: 4 != 0
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 4 != 0
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_L_5_sample
ERROR: Test case for function: L
ERROR: Input: ([1, 1, 1, 1, 1, 0, 1, 0, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 4
ERROR: Expected output: 5
ERROR: 5 != 4
ERROR: ----------------------------------------------------------------------------
ERROR: 5 != 4
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 5 != 4
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 1
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 9
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 2
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 82
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 3
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 756
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 4
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 7048
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 5
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 66384
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 6
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 631072
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 7
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 6048576
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 8
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 58388608
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 9
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 567108864
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 10
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 5536870912
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_msi_7_simple
ERROR: Test case for function: msi
ERROR: Input: ([-7, -7, -7, 7],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [0, 1, 0]
ERROR: Expected output: [3, 4, 7]
ERROR: Lists differ: [3, 4, 7] != [0, 1, 0]

First differing element 0:
3
0

- [3, 4, 7]
+ [0, 1, 0]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [3, 4, 7] != [0, 1, 0]

First differing element 0:
3
0

- [3, 4, 7]
+ [0, 1, 0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [3, 4, 7] != [0, 1, 0]

First differing element 0:
3
0

- [3, 4, 7]
+ [0, 1, 0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([1, 2],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: None
ERROR: Expected output: [1, 2]
ERROR: [1, 2] != None
ERROR: ----------------------------------------------------------------------------
ERROR: [1, 2] != None
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: [1, 2] != None
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([-1, -2, -3, -4, 0, 1, 2],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [-1, -1, -1, -1, 0, 1, 2]
ERROR: Expected output: [-4, -3, -2, -1, 0, 1, 2]
ERROR: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-1, -1, -1, -1, 0, 1, 2]

First differing element 0:
-4
-1

- [-4, -3, -2, -1, 0, 1, 2]
+ [-1, -1, -1, -1, 0, 1, 2]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-1, -1, -1, -1, 0, 1, 2]

First differing element 0:
-4
-1

- [-4, -3, -2, -1, 0, 1, 2]
+ [-1, -1, -1, -1, 0, 1, 2]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-1, -1, -1, -1, 0, 1, 2]

First differing element 0:
-4
-1

- [-4, -3, -2, -1, 0, 1, 2]
+ [-1, -1, -1, -1, 0, 1, 2]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([-1, -1, -1, -2.0],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [-1, -1, -1, -1]
ERROR: Expected output: [-2.0, -1, -1, -1]
ERROR: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -1]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -1]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -1]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -1]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -1]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -1]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([9, 8, 7, 6, 5, 4, 3, 2, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [9, 9, 9, 9, 9, 9, 9, 9, 9]
ERROR: Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
ERROR: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [9, 9, 9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [9, 9, 9, 9, 9, 9, 9, 9, 9]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [9, 9, 9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [9, 9, 9, 9, 9, 9, 9, 9, 9]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [9, 9, 9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [9, 9, 9, 9, 9, 9, 9, 9, 9]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([6, 5, 4, 3, 2, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [6, 6, 6, 6, 6, 6]
ERROR: Expected output: [1, 2, 3, 4, 5, 6]
ERROR: Lists differ: [1, 2, 3, 4, 5, 6] != [6, 6, 6, 6, 6, 6]

First differing element 0:
1
6

- [1, 2, 3, 4, 5, 6]
+ [6, 6, 6, 6, 6, 6]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5, 6] != [6, 6, 6, 6, 6, 6]

First differing element 0:
1
6

- [1, 2, 3, 4, 5, 6]
+ [6, 6, 6, 6, 6, 6]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5, 6] != [6, 6, 6, 6, 6, 6]

First differing element 0:
1
6

- [1, 2, 3, 4, 5, 6]
+ [6, 6, 6, 6, 6, 6]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([5, 4, 3, 2, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [5, 5, 5, 5, 5]
ERROR: Expected output: [1, 2, 3, 4, 5]
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([5, 4, 3, 2, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [5, 5, 5, 5, 5]
ERROR: Expected output: [1, 2, 3, 4, 5]
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([2, 1, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]

First differing element 0:
1
2

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?  ---         ---        ----              ^

+ [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
?     +++         +++          ++++         ^

ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]

First differing element 0:
1
2

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?  ---         ---        ----              ^

+ [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
?     +++         +++          ++++         ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]

First differing element 0:
1
2

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?  ---         ---        ----              ^

+ [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
?     +++         +++          ++++         ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([9, 2, 1, 4, 5, 7, 6],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [9, 9, 9, 9, 9, 9, 9]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 9]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9]
+ [9, 9, 9, 9, 9, 9, 9]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9]
+ [9, 9, 9, 9, 9, 9, 9]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9]
+ [9, 9, 9, 9, 9, 9, 9]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([9, 2, 1, 4, 12, 5, 7, 6],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [9, 9, 9, 9, 12, 12, 12, 12]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 9, 12]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [9, 9, 9, 9, 12, 12, 12, 12]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [9, 9, 9, 9, 12, 12, 12, 12]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [9, 9, 9, 9, 12, 12, 12, 12]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [9, 9, 9, 9, 12, 12, 12, 12]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [9, 9, 9, 9, 12, 12, 12, 12]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [9, 9, 9, 9, 12, 12, 12, 12]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([-1, -1, -1, -1, 0, 1, 2],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [-1, -1, -1, -1, 0, 1, 2]
ERROR: Expected output: [-4, -3, -2, -1, 0, 1, 2]
ERROR: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-1, -1, -1, -1, 0, 1, 2]

First differing element 0:
-4
-1

- [-4, -3, -2, -1, 0, 1, 2]
+ [-1, -1, -1, -1, 0, 1, 2]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-1, -1, -1, -1, 0, 1, 2]

First differing element 0:
-4
-1

- [-4, -3, -2, -1, 0, 1, 2]
+ [-1, -1, -1, -1, 0, 1, 2]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-1, -1, -1, -1, 0, 1, 2]

First differing element 0:
-4
-1

- [-4, -3, -2, -1, 0, 1, 2]
+ [-1, -1, -1, -1, 0, 1, 2]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([-1, -1, -1, -1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [-1, -1, -1, -1]
ERROR: Expected output: [-2.0, -1, -1, -1]
ERROR: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -1]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -1]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -1]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -1]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -1]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -1]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([9, 9, 9, 9, 9, 9, 9, 9, 9],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [9, 9, 9, 9, 9, 9, 9, 9, 9]
ERROR: Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
ERROR: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [9, 9, 9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [9, 9, 9, 9, 9, 9, 9, 9, 9]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [9, 9, 9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [9, 9, 9, 9, 9, 9, 9, 9, 9]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [9, 9, 9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [9, 9, 9, 9, 9, 9, 9, 9, 9]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([6, 6, 6, 6, 6, 6],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [6, 6, 6, 6, 6, 6]
ERROR: Expected output: [1, 2, 3, 4, 5, 6]
ERROR: Lists differ: [1, 2, 3, 4, 5, 6] != [6, 6, 6, 6, 6, 6]

First differing element 0:
1
6

- [1, 2, 3, 4, 5, 6]
+ [6, 6, 6, 6, 6, 6]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5, 6] != [6, 6, 6, 6, 6, 6]

First differing element 0:
1
6

- [1, 2, 3, 4, 5, 6]
+ [6, 6, 6, 6, 6, 6]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5, 6] != [6, 6, 6, 6, 6, 6]

First differing element 0:
1
6

- [1, 2, 3, 4, 5, 6]
+ [6, 6, 6, 6, 6, 6]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([5, 5, 5, 5, 5],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [5, 5, 5, 5, 5]
ERROR: Expected output: [1, 2, 3, 4, 5]
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([5, 5, 5, 5, 5],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [5, 5, 5, 5, 5]
ERROR: Expected output: [1, 2, 3, 4, 5]
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5] != [5, 5, 5, 5, 5]

First differing element 0:
1
5

- [1, 2, 3, 4, 5]
+ [5, 5, 5, 5, 5]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]

First differing element 0:
1
2

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?  ---         ---        ----              ^

+ [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
?     +++         +++          ++++         ^

ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]

First differing element 0:
1
2

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?  ---         ---        ----              ^

+ [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
?     +++         +++          ++++         ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]

First differing element 0:
1
2

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?  ---         ---        ----              ^

+ [2, 2, 4, 5, 7, 7, 8, 9, 11, 11, 12, 13, 15, 15]
?     +++         +++          ++++         ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([9, 9, 9, 9, 9, 9, 9],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [9, 9, 9, 9, 9, 9, 9]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 9]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9]
+ [9, 9, 9, 9, 9, 9, 9]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9]
+ [9, 9, 9, 9, 9, 9, 9]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [9, 9, 9, 9, 9, 9, 9]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9]
+ [9, 9, 9, 9, 9, 9, 9]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: insertion
ERROR: Input: ([9, 9, 9, 9, 12, 12, 12, 12],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [9, 9, 9, 9, 12, 12, 12, 12]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 9, 12]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [9, 9, 9, 9, 12, 12, 12, 12]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [9, 9, 9, 9, 12, 12, 12, 12]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [9, 9, 9, 9, 12, 12, 12, 12]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [9, 9, 9, 9, 12, 12, 12, 12]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/mvincen/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [9, 9, 9, 9, 12, 12, 12, 12]

First differing element 0:
1
9

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [9, 9, 9, 9, 12, 12, 12, 12]
ERROR: ============================================================================
```
```
