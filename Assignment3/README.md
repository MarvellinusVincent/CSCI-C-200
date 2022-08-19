# Assignment 3

- Username: mvincen
- Commit hash used for grading: ccec11d55999d54d50d14d9342f55e9ab90a384f

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



OVERALL: Amazing job man!! You have very clear, readable code, and your variables have relevant and applicable names. Keep up the great work.

## Total Score: 98/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (49.0/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `N`: 3.0/3
    - `N_t`: 3.0/3
    - `W`: 3.0/3
    - `L`: 2.0/2
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `q`: 3.0/4
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `amt`: 6.0/6
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `f`: 5.0/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmetic_mean`, `geo_mean`, `har_mean`, `RMS_mean`: 8.0/8
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `F`, `V`, `C`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `Mortgage`, `total_paid`: 4.0/4
    - TA Comments: TA did not add any comments.


- Problem 8:
    - `is_geo`: 5.0/5
    - TA Comments: TA did not add any comments.



## Code Review & style (49/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `N`: 3/3
    - `N_t`: 3/3
    - `W`: 3/3
    - `L`: 3/2
    - TA Comments: Amazing job. Great variable naming

- Problem 2:
    - `q`: 3/4
    - TA Comments: If the discrimitate is 0, the solution dosn't require an imaginary component because sqrt(0) = 0. So the condition should be "if (b**2)-(4*a*c) >= 0:"

    Also, in the case that this evaluates true, just type 'return True' rather than re-computing the condition for no reason.

- Problem 3:
    - `amt`: 6/6
    - TA Comments: Perfect

- Problem 4:
    - `f`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmetic_mean`, `geo_mean`, `har_mean`, `RMS_mean`: _/8
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `F`, `V`, `C`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `Mortgage`, `total_paid`: 4/4
    - TA Comments: TA did not add any comments.


- Problem 8:
    - `is_geo`: 5/5
    - TA Comments: TA did not add any comments.


## Unittest Results
ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/mvincen/a3_hidden_test.py", line 137, in test_q_1_dis_zero
    check_assertion(result, self.assertEqual, None, True, a3.q, (4,4,1))

ERROR: Input: ((4, 4, 1),) -- ignore the outermost () and the trailing ,
ERROR: True != False
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/mvincen/a3_hidden_test.py", line 138, in test_q_1_dis_zero
    check_assertion(result, self.assertEqual, None, True, a3.q, (5,5,5/4))

ERROR: Input: ((5, 5, 1.25),) -- ignore the outermost () and the trailing ,
ERROR: True != False
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/mvincen/a3_hidden_test.py", line 139, in test_q_1_dis_zero
    check_assertion(result, self.assertEqual, None, True, a3.q, (1/4,5,25))

ERROR: Input: ((0.25, 5, 25),) -- ignore the outermost () and the trailing ,
ERROR: True != False
ERROR: ======================================

