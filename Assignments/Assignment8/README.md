# Assignment 8

- Username: mvincen
- Commit hash used for grading: 7c9a3cd466f80603950a0ad1fdaef80fdcae7069

- Graded by: Pradeep Reddy Rokkam

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 88.6/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (42.6/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `step`:9.0/10
    - TA Comments: Line 22 of your code is redundant( you already have this in line 20) and is causing a syntax error. Because of this your function failed all the test cases. I am giving you marks as I think this is a simple mistake. But please be careful


- Problem 2:
    - `distance`: 5.0/5
    - `brute`: 3.6/5
    - TA Comments: Your code  works for all scenarios except for one scenario where the points with minimum distance are the points in position 1 and 2.
    Thiis beaces you initialzed your 
    first = 0
    second = 0

    instead it should be 
    first = 0
    second = 1

    Othewise you did a good job!



- Problem 3:
    - `productivity`: 10.0/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `permutation`:10.0/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `Vector`:5.0/10
    - TA Comments: You should vectors instead of list for addition, Subtraction, Scalar multiplication. Code not submitted for __eq__ and __repr__ methods.



## Code Review & style (46/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `step`:9/10
    - TA Comments: Please be careful about Redundant lines


- Problem 2:
    - `distance`: 5/5
    - `brute`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `productivity`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `permutation`:10/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `Vector`:7/10
    - TA Comments: Logic is correct for most functions but please be careful about the format of how values should be returned


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 1
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (1, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 2 direction: 2
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 3 direction: 3
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 1)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 4 direction: 4
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 1
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (1, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 9 direction: 2
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (-1, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 6 direction: 3
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 1)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 1
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (1, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 2
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (-1, 0)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 3
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 1)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 4
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, -1)
ERROR: module 'random' has no attribute 'randit'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'random' has no attribute 'randit'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 125, in test_a_step_10
    a8.step(x, y, i)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 22, in step
    direction = rn.randit(1,4)
AttributeError: module 'random' has no attribute 'randit'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_brute_5
ERROR: Test case for function: brute
ERROR: Input: [(1, 1), (4, 5)]
ERROR: Actual output: [(1, 1), (1, 1), 5.0]
ERROR: Expected output: [(1, 1), (4, 5), 5]
ERROR: (4, 5) not found in [(1, 1), (1, 1), 5.0]
ERROR: ----------------------------------------------------------------------------
ERROR: (4, 5) not found in [(1, 1), (1, 1), 5.0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 188, in test_c_brute_5
    self.assertIn(expected_output[i], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1096, in assertIn
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: (4, 5) not found in [(1, 1), (1, 1), 5.0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_brute_5
ERROR: Test case for function: brute
ERROR: Input: [(0, 0), (4, 3), (100, 200)]
ERROR: Actual output: [(0, 0), (0, 0), 5.0]
ERROR: Expected output: [(0, 0), (4, 3), 5]
ERROR: (4, 3) not found in [(0, 0), (0, 0), 5.0]
ERROR: ----------------------------------------------------------------------------
ERROR: (4, 3) not found in [(0, 0), (0, 0), 5.0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 188, in test_c_brute_5
    self.assertIn(expected_output[i], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1096, in assertIn
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: (4, 3) not found in [(0, 0), (0, 0), 5.0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_Vector_1_add
ERROR: Test case for function: Vector_add
ERROR: Input: [(1, 2, 3), (-1, -2, -3)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 0, 0)
ERROR: 'NoneType' object has no attribute 'get_tuple'
ERROR: ----------------------------------------------------------------------------
ERROR: 'NoneType' object has no attribute 'get_tuple'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 321, in test_f_Vector_1_add
    actual_output = result_vector.get_tuple()
AttributeError: 'NoneType' object has no attribute 'get_tuple'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_Vector_1_add
ERROR: Test case for function: Vector_add
ERROR: Input: [(-1, -2, -3), (-1, -2, -3)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (-2, -4, -6)
ERROR: 'NoneType' object has no attribute 'get_tuple'
ERROR: ----------------------------------------------------------------------------
ERROR: 'NoneType' object has no attribute 'get_tuple'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 321, in test_f_Vector_1_add
    actual_output = result_vector.get_tuple()
AttributeError: 'NoneType' object has no attribute 'get_tuple'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_Vector_1_sub
ERROR: Test case for function: Vector_sub
ERROR: Input: [(1, 2, 3), (-1, -2, -3)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (2, 4, 6)
ERROR: 'NoneType' object has no attribute 'get_tuple'
ERROR: ----------------------------------------------------------------------------
ERROR: 'NoneType' object has no attribute 'get_tuple'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 347, in test_g_Vector_1_sub
    actual_output = result_vector.get_tuple()
AttributeError: 'NoneType' object has no attribute 'get_tuple'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_Vector_1_sub
ERROR: Test case for function: Vector_sub
ERROR: Input: [(-1, -2, -3), (-1, -2, -3)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (0, 0, 0)
ERROR: 'NoneType' object has no attribute 'get_tuple'
ERROR: ----------------------------------------------------------------------------
ERROR: 'NoneType' object has no attribute 'get_tuple'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 347, in test_g_Vector_1_sub
    actual_output = result_vector.get_tuple()
AttributeError: 'NoneType' object has no attribute 'get_tuple'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_h_Vector_1_rmul
ERROR: Test case for function: Vector_rmul
ERROR: Input: [5, (-1, -2, -3)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (-5, -10, -15)
ERROR: 'int' object has no attribute '_Vector__v'
ERROR: ----------------------------------------------------------------------------
ERROR: 'int' object has no attribute '_Vector__v'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 371, in test_h_Vector_1_rmul
    result_vector = input_data[0] * vector_1
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 170, in __rmul__
    return self.__mul__(other)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 176, in __mul__
    for j in range(len(other.__v)):
AttributeError: 'int' object has no attribute '_Vector__v'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_h_Vector_1_rmul
ERROR: Test case for function: Vector_rmul
ERROR: Input: [-3, (-1, -2, -3)]
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (3, 6, 9)
ERROR: 'int' object has no attribute '_Vector__v'
ERROR: ----------------------------------------------------------------------------
ERROR: 'int' object has no attribute '_Vector__v'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 371, in test_h_Vector_1_rmul
    result_vector = input_data[0] * vector_1
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 170, in __rmul__
    return self.__mul__(other)
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 176, in __mul__
    for j in range(len(other.__v)):
AttributeError: 'int' object has no attribute '_Vector__v'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_i_Vector_1_mul
ERROR: Test case for function: Vector_mul
ERROR: Input: [(0, 5, 6), (1, 10, -1)]
ERROR: Actual output: [44]
ERROR: Expected output: 44
ERROR: 44 != [44]
ERROR: ----------------------------------------------------------------------------
ERROR: 44 != [44]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 398, in test_i_Vector_1_mul
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 44 != [44]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_i_Vector_1_mul
ERROR: Test case for function: Vector_mul
ERROR: Input: [(-1, 0, 1), (10, 10, 10)]
ERROR: Actual output: [0]
ERROR: Expected output: 0
ERROR: 0 != [0]
ERROR: ----------------------------------------------------------------------------
ERROR: 0 != [0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 398, in test_i_Vector_1_mul
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 0 != [0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_k_Vector_1_neg
ERROR: Test case for function: Vector_neg
ERROR: Input: (3, -3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (-3, 3)
ERROR: local variable 'i' referenced before assignment
ERROR: ----------------------------------------------------------------------------
ERROR: local variable 'i' referenced before assignment
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 445, in test_k_Vector_1_neg
    actual_output = (-vector).get_tuple()
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 191, in __neg__
    for i in range(len(self.__v[i])):
UnboundLocalError: local variable 'i' referenced before assignment
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_k_Vector_1_neg
ERROR: Test case for function: Vector_neg
ERROR: Input: (-6, 0, 6)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: (6, 0, -6)
ERROR: local variable 'i' referenced before assignment
ERROR: ----------------------------------------------------------------------------
ERROR: local variable 'i' referenced before assignment
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 445, in test_k_Vector_1_neg
    actual_output = (-vector).get_tuple()
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 191, in __neg__
    for i in range(len(self.__v[i])):
UnboundLocalError: local variable 'i' referenced before assignment
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_l_Vector_1_eq
ERROR: Test case for function: Vector_eq
ERROR: Input: [(1, 2, 3), (1, 2, 3)]
ERROR: Actual output: None
ERROR: Expected output: True
ERROR: True != None
ERROR: ----------------------------------------------------------------------------
ERROR: True != None
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 471, in test_l_Vector_1_eq
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: True != None
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_l_Vector_1_eq
ERROR: Test case for function: Vector_eq
ERROR: Input: [(-1, -2, -3), (-1, 2, -3)]
ERROR: Actual output: None
ERROR: Expected output: False
ERROR: False != None
ERROR: ----------------------------------------------------------------------------
ERROR: False != None
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 471, in test_l_Vector_1_eq
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: False != None
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Vector_1_repr
ERROR: Test case for function: Vector_repr
ERROR: Input: (1, 2, 3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <1, 2, 3>
ERROR: __repr__ returned non-string (type NoneType)
ERROR: ----------------------------------------------------------------------------
ERROR: __repr__ returned non-string (type NoneType)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 494, in test_m_Vector_1_repr
    self.assertEqual(expected_output, repr(vector_1))
TypeError: __repr__ returned non-string (type NoneType)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Vector_1_repr
ERROR: Test case for function: Vector_repr
ERROR: Input: (-1, 0, -3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <-1, 0, -3>
ERROR: __repr__ returned non-string (type NoneType)
ERROR: ----------------------------------------------------------------------------
ERROR: __repr__ returned non-string (type NoneType)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 494, in test_m_Vector_1_repr
    self.assertEqual(expected_output, repr(vector_1))
TypeError: __repr__ returned non-string (type NoneType)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Vector_1_repr
ERROR: Test case for function: Vector_repr
ERROR: Input: (1, 2, 3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <1, 2, 3>
ERROR: __repr__ returned non-string (type NoneType)
ERROR: ----------------------------------------------------------------------------
ERROR: __repr__ returned non-string (type NoneType)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 504, in test_m_Vector_1_repr
    self.assertEqual(expected_output.replace(" ", ""), repr(vector_1).replace(" ", ""))
TypeError: __repr__ returned non-string (type NoneType)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Vector_1_repr
ERROR: Test case for function: Vector_repr
ERROR: Input: (-1, 0, -3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <-1, 0, -3>
ERROR: __repr__ returned non-string (type NoneType)
ERROR: ----------------------------------------------------------------------------
ERROR: __repr__ returned non-string (type NoneType)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 504, in test_m_Vector_1_repr
    self.assertEqual(expected_output.replace(" ", ""), repr(vector_1).replace(" ", ""))
TypeError: __repr__ returned non-string (type NoneType)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Vector_2_all
ERROR: Test case for function: Vector_all
ERROR: Input: Multiple operations on vectors
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <0, 0, 0>
ERROR: local variable 'i' referenced before assignment
ERROR: ----------------------------------------------------------------------------
ERROR: local variable 'i' referenced before assignment
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8_hidden_test.py", line 519, in test_n_Vector_2_all
    result_vector = (-vector_1) + (-1 * vector_2) + vector_3 - vector_3
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/mvincen/a8.py", line 191, in __neg__
    for i in range(len(self.__v[i])):
UnboundLocalError: local variable 'i' referenced before assignment
ERROR: ============================================================================
```
```
