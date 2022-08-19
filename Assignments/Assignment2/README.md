# Assignment 2

- Username: mvincen
- Commit hash used for grading: 3fc8d4cb37e546d314b3c614ac525fe407563764

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 97.5/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (48/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `g`: 6/10
    - TA Comments: Please make it a habit of checking In-Scribe. It is the main way the TAs communicate with the students. Here's a post about changes to this problem. https://inscribe.education/main/indianau/6754110229501759/conversations/6749461749700541?topicSlug=assignment2&searchText=g&backToListTab=search

- Problem 2:
    - `f`: 1010
    - TA Comments: Good job!

- Problem 3:
    - `h_0`: 3/3
    - `h_1`: 3/3
    - `h`: 4/4
    - TA Comments: Good job!

- Problem 4:
    - `q`: 15/15
    - TA Comments: Good job!


- Problem 5:
    - `eq`: 20/20
    - TA Comments: Good job!


- Problem 6:
    - `path`: 20/20
    - TA Comments: Good job!


- Problem 7:
    - `max2d`: 7/7
    - `max3d`: 8/8
    - TA Comments: Good job!



## Code Review & style (49.5/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

Global Comments:
1. You have an unused import statement on line 3. You should never have unused import statements in your file. It might seem minor but you can introduce a lot of problems this way.
2. You have 'pass' statements at the end of all of your functions (except eq(lst): and m(x,y):). You should not have any code after your return statements. This is because no code will execute if it is after a return statement.

 Problem 1:
    - `g`: 10/10
    - TA Comments: See "Global Comments" above.

- Problem 2:
    - `f`: 10/10
    - TA Comments: See "Global Comments" above.

- Problem 3:
    - `h_0`: 3/3
    - `h_1`: 3/3
    - `h`: 4/4
    - TA Comments: See "Global Comments" above.

- Problem 4:
    - `q`: 14/15
    - TA Comments: See "Global Comments" above. Additionally, you have import math on line 57 in this function. All import statements should be at the top of your file. You are not using this import statement. 


- Problem 5:
    - `eq`: 20/20
    - TA Comments: See "Global Comments" above.


- Problem 6:
    - `path`: 20/20
    - TA Comments: See "Global Comments" above.


- Problem 7:
    - `max2d`: 7/7
    - `max3d`: 8/8
    - TA Comments: See "Global Comments" above.



## Unittest Results
```
-------------------------------------
test_g_4_one failed.

Traceback (most recent call last):
  File "d:\Projects\IU-C200-AI\CSCI-C200-Spring-2022-StudentSupport\Gradingdata\Assignment2\mvincen\a2_hidden_test.py", line 16, in test_g_4_one
    self.assertAlmostEqual(a2.g(0), 2, 2)
AssertionError: 1 != 2 within 2 places (1 difference)

======================================

Code tests: 48.0/50.0
g: 6/10    
f: 10/10   
h0: 3/3    
h1: 3/3    
h: 4/4     
q: 15/15   
eq: 20/20  
path: 20/20
max2d: 7/7 
max3d: 8/8
```