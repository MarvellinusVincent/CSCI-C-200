# Assignment 4

- Username: mvincen
- Commit hash used for grading: f1233df17c5a793e3f769e5788333b3e100f1c86

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 97.93/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (48.93/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `a`, `b`, `c`, `day`: 9.0/9
    - TA Comments: All good!


- Problem 2:
    - `q`: 8.0/8
    - TA Comments:  All good!


- Problem 3:
    - `inner_prod`, `mag`, `angle`, `match`, `best_match`: 8.9/10
    - TA Comments:  Line 71 should have been `new = [i,j,angle(i,j)]`.


- Problem 4:
    - `intersect`: 6.0/6
    - TA Comments:  All good!


- Problem 5:
    - `mean`, `variance`, `std`, `mean_centered`: 10.0/10
    - TA Comments:  All good!


- Problem 6:
    - `equi`: 7.0/7
    - TA Comments:  All good!



## Code Review & style (49/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `a`, `b`, `c`, `day`: 9/9
    - TA Comments: Good job!


- Problem 2:
    - `q`: 8/8
    - TA Comments: Good job!


- Problem 3:
    - `inner_prod`, `mag`, `angle`, `match`, `best_match`: 9.5/10
    - TA Comments: I am docking 1/2 point as you used the `min` builtin. We expect you to write all this code explicitly not use builtins.


- Problem 4:
    - `intersect`: 6/6
    - TA Comments: Good job!


- Problem 5:
    - `mean`, `variance`, `std`, `mean_centered`: 9.5/10
    - TA Comments: Docking another 1/2 point for using the `sum` builtin. Please don't use utility functions unless explicitly allowed.


- Problem 6:
    - `equi`: 7/7
    - TA Comments: Good job!


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_bestmatch_4_end_to_end
ERROR: Input: [[1], [1]]
ERROR: min() arg is an empty sequence
ERROR: ----------------------------------------------------------------------------
ERROR: min() arg is an empty sequence
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment4/mvincen/a4_hidden_test.py", line 148, in test_bestmatch_4_end_to_end
    return_value = a4.best_match(a4.match(input))
  File "/home/sara/Spring-2022/Gradingdata/Assignment4/mvincen/a4.py", line 79, in best_match
    raw = scores[list.index(min(list))]
ValueError: min() arg is an empty sequence
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_bestmatch_4_end_to_end
ERROR: Input: [[1, 1], [0, 1], [1, 1]]
ERROR: 45.0 != 0 within 2 places (45.0 difference)
ERROR: ----------------------------------------------------------------------------
ERROR: 45.0 != 0 within 2 places (45.0 difference)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment4/mvincen/a4_hidden_test.py", line 155, in test_bestmatch_4_end_to_end
    self.assertAlmostEqual(angle(return_value[0], return_value[1]), output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 883, in assertAlmostEqual
    raise self.failureException(msg)
AssertionError: 45.0 != 0 within 2 places (45.0 difference)
ERROR: ============================================================================
```
```
