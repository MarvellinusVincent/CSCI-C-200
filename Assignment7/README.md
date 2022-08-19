# Assignment 7

- Username: mvincen
- Commit hash used for grading: bacd32f9cd97241a8618e61aaa253a774a4fbc6d

- Graded by: Jungmin Lee

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 65.6/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (28.6/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `Fraction`:7.5/11
    - TA Comments: Your formatting is incorrrect, however other than that, it looks great!. I added some points back since several autograder failed due to your __repr__.


- Problem 2:
    - `encrypt`: 2.0/2
    - `decrypt`: 1.1/2
    - `encryptsentence`: 3.0/5
    - `decryptsentence`: 3.0/4
    - TA Comments: Cannot pass the case for input ('a', 0) -> shift 0, in your decrypt function. Your encryptsentence and decrpytsentence couldn't pass the test case since your encrypt and decrypt is incorrect. By themselves (encryptsentence, decryptsentence, looks correct) Added points +1, for each of them.


- Problem 3:
    - `getaminoacids`: 0.0/5
    - `getDNA`: 0.0/5
    - `translate`: 0.0/3
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `Function`:12.0/13
    - TA Comments: repr should return f"f(x) = {self.Function}"



## Code Review & style (37/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `Fraction`:11/11
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `encrypt`: 2/2
    - `decrypt`: 2/2
    - `encryptsentence`: 5/5
    - `decryptsentence`: 4/4
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `getaminoacids`: 0/5
    - `getDNA`: 0/5
    - `translate`: 0/3
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `Function`:13/13
    - TA Comments: TA did not add any comments.


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (5, 7)
ERROR: Actual output: frac(5,7)
ERROR: Expected output: frac(5/7)
ERROR: 'frac(5/7)' != 'frac(5,7)'
- frac(5/7)
?       ^
+ frac(5,7)
?       ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(5/7)' != 'frac(5,7)'
- frac(5/7)
?       ^
+ frac(5,7)
?       ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(5/7)' != 'frac(5,7)'
- frac(5/7)
?       ^
+ frac(5,7)
?       ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (1, 2)
ERROR: Actual output: frac(1,2)
ERROR: Expected output: frac(1/2)
ERROR: 'frac(1/2)' != 'frac(1,2)'
- frac(1/2)
?       ^
+ frac(1,2)
?       ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(1/2)' != 'frac(1,2)'
- frac(1/2)
?       ^
+ frac(1,2)
?       ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(1/2)' != 'frac(1,2)'
- frac(1/2)
?       ^
+ frac(1,2)
?       ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (4, 5)
ERROR: Actual output: frac(4,5)
ERROR: Expected output: frac(4/5)
ERROR: 'frac(4/5)' != 'frac(4,5)'
- frac(4/5)
?       ^
+ frac(4,5)
?       ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(4/5)' != 'frac(4,5)'
- frac(4/5)
?       ^
+ frac(4,5)
?       ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(4/5)' != 'frac(4,5)'
- frac(4/5)
?       ^
+ frac(4,5)
?       ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((6, 7), (1, 2))
ERROR: Actual output: frac(3,7)
ERROR: Expected output: ((3, 7), 'frac(3/7)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((4, 3), (1, 2))
ERROR: Actual output: frac(2,3)
ERROR: Expected output: ((2, 3), 'frac(2/3)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_decrypt_2
ERROR: Test case for function: decrypt
ERROR: Input: ('a', 0) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: {
ERROR: Expected output: a
ERROR: 'a' != '{'
- a
+ {

ERROR: ----------------------------------------------------------------------------
ERROR: 'a' != '{'
- a
+ {
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'a' != '{'
- a
+ {

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_decrypt_2
ERROR: Test case for function: decrypt
ERROR: Input: ('a', 27) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: {
ERROR: Expected output: a
ERROR: 'a' != '{'
- a
+ {

ERROR: ----------------------------------------------------------------------------
ERROR: 'a' != '{'
- a
+ {
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'a' != '{'
- a
+ {

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_decrypt_2
ERROR: Test case for function: decrypt
ERROR: Input: ('a', 2) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: {
ERROR: Expected output: z
ERROR: 'z' != '{'
- z
+ {

ERROR: ----------------------------------------------------------------------------
ERROR: 'z' != '{'
- z
+ {
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'z' != '{'
- z
+ {

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('this is a secret message used for testing', 0) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: thisaisaaasecretamessageausedaforatesting
ERROR: Expected output: this{is{a{secret{message{used{for{testing
ERROR: 'this{is{a{secret{message{used{for{testing' != 'thisaisaaasecretamessageausedaforatesting'
- this{is{a{secret{message{used{for{testing
?     ^  - ^      ^       ^    ^   ^
+ thisaisaaasecretamessageausedaforatesting
?     ^   ^^      ^       ^    ^   ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'this{is{a{secret{message{used{for{testing' != 'thisaisaaasecretamessageausedaforatesting'
- this{is{a{secret{message{used{for{testing
?     ^  - ^      ^       ^    ^   ^
+ thisaisaaasecretamessageausedaforatesting
?     ^   ^^      ^       ^    ^   ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'this{is{a{secret{message{used{for{testing' != 'thisaisaaasecretamessageausedaforatesting'
- this{is{a{secret{message{used{for{testing
?     ^  - ^      ^       ^    ^   ^
+ thisaisaaasecretamessageausedaforatesting
?     ^   ^^      ^       ^    ^   ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('this is a secret message about the class', 5) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx
ERROR: Expected output: ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
ERROR: 'ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx' != 'ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx'
- ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
?     ^  ^ ^      ^       ^     ^   ^
+ ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx
?     ^  ^ ^      ^       ^     ^   ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx' != 'ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx'
- ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
?     ^  ^ ^      ^       ^     ^   ^
+ ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx
?     ^  ^ ^      ^       ^     ^   ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx' != 'ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx'
- ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
?     ^  ^ ^      ^       ^     ^   ^
+ ymnxanxafaxjhwjyarjxxfljafgtzyaymjahqfxx
?     ^  ^ ^      ^       ^     ^   ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('aaaaa zzzzzzzz', 81) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: aaaaaazzzzzzzz
ERROR: Expected output: aaaaa{zzzzzzzz
ERROR: 'aaaaa{zzzzzzzz' != 'aaaaaazzzzzzzz'
- aaaaa{zzzzzzzz
?      ^
+ aaaaaazzzzzzzz
?      ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaa{zzzzzzzz' != 'aaaaaazzzzzzzz'
- aaaaa{zzzzzzzz
?      ^
+ aaaaaazzzzzzzz
?      ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaa{zzzzzzzz' != 'aaaaaazzzzzzzz'
- aaaaa{zzzzzzzz
?      ^
+ aaaaaazzzzzzzz
?      ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_decryptsentence_4
ERROR: Test case for function: decrypt_sentence
ERROR: Input: ('this{is{a{secret{message{used{for{testing', 0) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: this is   secret mess ge used for testing
ERROR: Expected output: this is a secret message used for testing
ERROR: 'this is a secret message used for testing' != 'this is   secret mess ge used for testing'
- this is a secret message used for testing
?         ^            ^
+ this is   secret mess ge used for testing
?         ^            ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'this is a secret message used for testing' != 'this is   secret mess ge used for testing'
- this is a secret message used for testing
?         ^            ^
+ this is   secret mess ge used for testing
?         ^            ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'this is a secret message used for testing' != 'this is   secret mess ge used for testing'
- this is a secret message used for testing
?         ^            ^
+ this is   secret mess ge used for testing
?         ^            ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_decryptsentence_4
ERROR: Test case for function: decrypt_sentence
ERROR: Input: ('aaaaa{zzzzzzzz', 81) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output:       zzzzzzzz
ERROR: Expected output: aaaaa zzzzzzzz
ERROR: 'aaaaa zzzzzzzz' != '      zzzzzzzz'
- aaaaa zzzzzzzz
+       zzzzzzzz

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaa zzzzzzzz' != '      zzzzzzzz'
- aaaaa zzzzzzzz
+       zzzzzzzz
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaa zzzzzzzz' != '      zzzzzzzz'
- aaaaa zzzzzzzz
+       zzzzzzzz

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_h_getaminoacids_3
ERROR: Test case for function: get_amino_acids
ERROR: Input: Isoleucine, I, ATT, ATC, ATA
Leucine, L, CTT, CTC, CTA, CTG, TTA, TTG
Valine, V, GTT, GTC, GTA, GTG
Phenylalanine, F, TTT, TTC
Methionine, M, ATG
CYSteine, C, TGT, TGC
Alanine, A, GCT, GCC, GCA, GCG
Glycine, G, GGT, GGC, GGA, GGG
Proline, P, CCT, CCC, CCA, CCG
Threonine, T, ACT, ACC, ACA, ACG
Serine, S, TCT, TCC, TCA, TCG, AGT, AGC
Tyrosine, Y, TAT, TAC
Tryptophan, W, TGG
Glutamine, Q, CAA, CAG
Asparagine, N, AAT, AAC
Histidine, H, CAT, CAC
Glutamic_acid, E, GAA, GAG
AsparTic acid, D, GAT, GAC
Lysine, K, AAA, AAG
Arginine, R, CGT, CGC, CGA, CGG, AGA, AGG
Stop_codons, -, TAA, TAG, TGA
ERROR: Actual output: None
ERROR: Expected output: {('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I'], ('CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'): ['Leucine', 'L'], ('GTT', 'GTC', 'GTA', 'GTG'): ['Valine', 'V'], ('TTT', 'TTC'): ['Phenylalanine', 'F'], ('ATG',): ['Methionine', 'M'], ('TGT', 'TGC'): ['CYSteine', 'C'], ('GCT', 'GCC', 'GCA', 'GCG'): ['Alanine', 'A'], ('GGT', 'GGC', 'GGA', 'GGG'): ['Glycine', 'G'], ('CCT', 'CCC', 'CCA', 'CCG'): ['Proline', 'P'], ('ACT', 'ACC', 'ACA', 'ACG'): ['Threonine', 'T'], ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'): ['Serine', 'S'], ('TAT', 'TAC'): ['Tyrosine', 'Y'], ('TGG',): ['Tryptophan', 'W'], ('CAA', 'CAG'): ['Glutamine', 'Q'], ('AAT', 'AAC'): ['Asparagine', 'N'], ('CAT', 'CAC'): ['Histidine', 'H'], ('GAA', 'GAG'): ['Glutamic_acid', 'E'], ('GAT', 'GAC'): ['AsparTic acid', 'D'], ('AAA', 'AAG'): ['Lysine', 'K'], ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'): ['Arginine', 'R'], ('TAA', 'TAG', 'TGA'): ['Stop_codons', '-']}
ERROR: None != {('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I[864 chars]'-']}
ERROR: ----------------------------------------------------------------------------
ERROR: None != {('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I[864 chars]'-']}
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 414, in test_h_getaminoacids_3
    self.assertEqual(actual_output, amino_acid_dict)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != {('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I[864 chars]'-']}
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_h_getaminoacids_3
ERROR: Test case for function: get_amino_acids
ERROR: Input: Stop_codons, -, TAA, TAG, TGA
Arginine, A, CGG
ERROR: Actual output: None
ERROR: Expected output: {('TAA', 'TAG', 'TGA'): ['Stop_codons', '-'], ('CGG',): ['Arginine', 'A']}
ERROR: None != {('TAA', 'TAG', 'TGA'): ['Stop_codons', '-'], ('CGG',): ['Arginine', 'A']}
ERROR: ----------------------------------------------------------------------------
ERROR: None != {('TAA', 'TAG', 'TGA'): ['Stop_codons', '-'], ('CGG',): ['Arginine', 'A']}
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 414, in test_h_getaminoacids_3
    self.assertEqual(actual_output, amino_acid_dict)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != {('TAA', 'TAG', 'TGA'): ['Stop_codons', '-'], ('CGG',): ['Arginine', 'A']}
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_j_getDNA_3
ERROR: Test case for function: get_DNA
ERROR: Input: >HSGLTH1 Human theta 1-globin gene
CCACTGCACTCACCGCACCCGGCCAATTTTTGTGTTTTTAGTAGAGACTAAATACCATATAGTGAACACCTAAGA
CGGGGGGCCTTGGATCCAGGGCGATTCAGAGGGCCCCGGTCGGAGCTGTCGGAGATTGAGCGCGCGCGGTCCCGG
GATCTCCGACGAGGCCCTGGACCCCCGGGCGGCGAAGCTGCGGCGCGGCGCCCCCTGGAGGCCGCGGGACCCCTG
GCCGGTCCGCGCAGGCGCAGCGGGGTCGCAGGGCGCGGCGGGTTCCAGCGCGGGGATGGCGCTGTCCGCGGAGGA
CCGGGCGCTGGTGCGCGCCCTGTGGAAGAAGCTGGGCAGCAACGTCGGCGTCTACACGACAGAGGCCCTGGAAAG
GTGCGGCAGGCTGGGCGCCCCCGCCCCCAGGGGCCCTCCCTCCCCAAGCCCCCCGGACGCGCCTCACCCACGTTC
CTCTCGCAGGACCTTCCTGGCTTTCCCCGCCACGAAGACCTACTTCTCCCACCTGGACCTGAGCCCCGGCTCCTC
ACAAGTCAGAGCCCACGGCCAGAAGGTGGCGGACGCGCTGAGCCTCGCCGTGGAGCGCCTGGACGACCTACCCCA
CGCGCTGTCCGCGCTGAGCCACCTGCACGCGTGCCAGCTGCGAGTGGACCCGGCCAGCTTCCAGGTGAGCGGCTG
CCGTGCTGGGCCCCTGTCCCCGGGAGGGCCCCGGCGGGGTGGGTGCGGGGGGCGTGCGGGGCGGGTGCAGGCGAG
TGAGCCTTGAGCGCTCGCCGCAGCTCCTGGGCCACTGCCTGCTGGTAACCCTCGCCCGGCACTACCCCGGAGACT
TCAGCCCCGCGCTGCAGGCGTCGCTGGACAAGTTCCTGAGCCACGTTATCTCGGCGCTGGTTTCCGAGTACCGCT
GAACTGTGGGTGGGTGGCCGCGGGATCCCCAGGCGACCTTCCCCGTGTTTGAGTAAAGCCTCTCCCAGGAGCAGC
CTTCTTGCCGTGCTCTCTCGAGGTCAGGACGCGAGAGGAAGGCGC
ERROR: Actual output: None
ERROR: Expected output: ['>HSGLTH1 Human theta 1-globin gene', 'CCACTGCACTCACCGCACCCGGCCAATTTTTGTGTTTTTAGTAGAGACTAAATACCATATAGTGAACACCTAAGACGGGGGGCCTTGGATCCAGGGCGATTCAGAGGGCCCCGGTCGGAGCTGTCGGAGATTGAGCGCGCGCGGTCCCGGGATCTCCGACGAGGCCCTGGACCCCCGGGCGGCGAAGCTGCGGCGCGGCGCCCCCTGGAGGCCGCGGGACCCCTGGCCGGTCCGCGCAGGCGCAGCGGGGTCGCAGGGCGCGGCGGGTTCCAGCGCGGGGATGGCGCTGTCCGCGGAGGACCGGGCGCTGGTGCGCGCCCTGTGGAAGAAGCTGGGCAGCAACGTCGGCGTCTACACGACAGAGGCCCTGGAAAGGTGCGGCAGGCTGGGCGCCCCCGCCCCCAGGGGCCCTCCCTCCCCAAGCCCCCCGGACGCGCCTCACCCACGTTCCTCTCGCAGGACCTTCCTGGCTTTCCCCGCCACGAAGACCTACTTCTCCCACCTGGACCTGAGCCCCGGCTCCTCACAAGTCAGAGCCCACGGCCAGAAGGTGGCGGACGCGCTGAGCCTCGCCGTGGAGCGCCTGGACGACCTACCCCACGCGCTGTCCGCGCTGAGCCACCTGCACGCGTGCCAGCTGCGAGTGGACCCGGCCAGCTTCCAGGTGAGCGGCTGCCGTGCTGGGCCCCTGTCCCCGGGAGGGCCCCGGCGGGGTGGGTGCGGGGGGCGTGCGGGGCGGGTGCAGGCGAGTGAGCCTTGAGCGCTCGCCGCAGCTCCTGGGCCACTGCCTGCTGGTAACCCTCGCCCGGCACTACCCCGGAGACTTCAGCCCCGCGCTGCAGGCGTCGCTGGACAAGTTCCTGAGCCACGTTATCTCGGCGCTGGTTTCCGAGTACCGCTGAACTGTGGGTGGGTGGCCGCGGGATCCCCAGGCGACCTTCCCCGTGTTTGAGTAAAGCCTCTCCCAGGAGCAGCCTTCTTGCCGTGCTCTCTCGAGGTCAGGACGCGAGAGGAAGGCGC']
ERROR: None != ['>HSGLTH1 Human theta 1-globin gene', 'C[1016 chars]CGC']
ERROR: ----------------------------------------------------------------------------
ERROR: None != ['>HSGLTH1 Human theta 1-globin gene', 'C[1016 chars]CGC']
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 455, in test_j_getDNA_3
    self.assertEqual(actual_output, list_on_read)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != ['>HSGLTH1 Human theta 1-globin gene', 'C[1016 chars]CGC']
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_j_getDNA_3
ERROR: Test case for function: get_DNA
ERROR: Input: >C200 IU Bloomington 2022-python-expert gene
TAATAGTGACGGCGGCGGTAATAGTGAAA
ERROR: Actual output: None
ERROR: Expected output: ['>C200 IU Bloomington 2022-python-expert gene', 'TAATAGTGACGGCGGCGGTAATAGTGAAA']
ERROR: None != ['>C200 IU Bloomington 2022-python-expert[35 chars]AAA']
ERROR: ----------------------------------------------------------------------------
ERROR: None != ['>C200 IU Bloomington 2022-python-expert[35 chars]AAA']
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 455, in test_j_getDNA_3
    self.assertEqual(actual_output, list_on_read)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != ['>C200 IU Bloomington 2022-python-expert[35 chars]AAA']
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_l_translate_3
ERROR: Test case for function: translate
ERROR: Input: ({('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I'], ('CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'): ['Leucine', 'L'], ('GTT', 'GTC', 'GTA', 'GTG'): ['Valine', 'V'], ('TTT', 'TTC'): ['Phenylalanine', 'F'], ('ATG',): ['Methionine', 'M'], ('TGT', 'TGC'): ['CYSteine', 'C'], ('GCT', 'GCC', 'GCA', 'GCG'): ['Alanine', 'A'], ('GGT', 'GGC', 'GGA', 'GGG'): ['Glycine', 'G'], ('CCT', 'CCC', 'CCA', 'CCG'): ['Proline', 'P'], ('ACT', 'ACC', 'ACA', 'ACG'): ['Threonine', 'T'], ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'): ['Serine', 'S'], ('TAT', 'TAC'): ['Tyrosine', 'Y'], ('TGG',): ['Tryptophan', 'W'], ('CAA', 'CAG'): ['Glutamine', 'Q'], ('AAT', 'AAC'): ['Asparagine', 'N'], ('CAT', 'CAC'): ['Histidine', 'H'], ('GAA', 'GAG'): ['Glutamic_acid', 'E'], ('GAT', 'GAC'): ['AsparTic acid', 'D'], ('AAA', 'AAG'): ['Lysine', 'K'], ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'): ['Arginine', 'R'], ('TAA', 'TAG', 'TGA'): ['Stop_codons', '-']}, ['>HSGLTH1 Human theta 1-globin gene', 'CCACTGCACTCACCGCACCCGGCCAATTTTTGTGTTTTTAGTAGAGACTAAATACCATATAGTGAACACCTAAGACGGGGGGCCTTGGATCCAGGGCGATTCAGAGGGCCCCGGTCGGAGCTGTCGGAGATTGAGCGCGCGCGGTCCCGGGATCTCCGACGAGGCCCTGGACCCCCGGGCGGCGAAGCTGCGGCGCGGCGCCCCCTGGAGGCCGCGGGACCCCTGGCCGGTCCGCGCAGGCGCAGCGGGGTCGCAGGGCGCGGCGGGTTCCAGCGCGGGGATGGCGCTGTCCGCGGAGGACCGGGCGCTGGTGCGCGCCCTGTGGAAGAAGCTGGGCAGCAACGTCGGCGTCTACACGACAGAGGCCCTGGAAAGGTGCGGCAGGCTGGGCGCCCCCGCCCCCAGGGGCCCTCCCTCCCCAAGCCCCCCGGACGCGCCTCACCCACGTTCCTCTCGCAGGACCTTCCTGGCTTTCCCCGCCACGAAGACCTACTTCTCCCACCTGGACCTGAGCCCCGGCTCCTCACAAGTCAGAGCCCACGGCCAGAAGGTGGCGGACGCGCTGAGCCTCGCCGTGGAGCGCCTGGACGACCTACCCCACGCGCTGTCCGCGCTGAGCCACCTGCACGCGTGCCAGCTGCGAGTGGACCCGGCCAGCTTCCAGGTGAGCGGCTGCCGTGCTGGGCCCCTGTCCCCGGGAGGGCCCCGGCGGGGTGGGTGCGGGGGGCGTGCGGGGCGGGTGCAGGCGAGTGAGCCTTGAGCGCTCGCCGCAGCTCCTGGGCCACTGCCTGCTGGTAACCCTCGCCCGGCACTACCCCGGAGACTTCAGCCCCGCGCTGCAGGCGTCGCTGGACAAGTTCCTGAGCCACGTTATCTCGGCGCTGGTTTCCGAGTACCGCTGAACTGTGGGTGGGTGGCCGCGGGATCCCCAGGCGACCTTCCCCGTGTTTGAGTAAAGCCTCTCCCAGGAGCAGCCTTCTTGCCGTGCTCTCTCGAGGTCAGGACGCGAGAGGAAGGCGC'])
ERROR: Actual output: None
ERROR: Expected output: PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR
ERROR: None != 'PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSE[296 chars]RGRR'
ERROR: ----------------------------------------------------------------------------
ERROR: None != 'PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSE[296 chars]RGRR'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 497, in test_l_translate_3
    self.assertEqual(actual_output, translation)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != 'PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSE[296 chars]RGRR'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_l_translate_3
ERROR: Test case for function: translate
ERROR: Input: ({('TAA', 'TAG', 'TGA'): ['Stop_codons', '-'], ('CGG',): ['Arginine', 'A']}, ['>C200 IU Bloomington 2022-python-expert gene', 'TAATAGTGACGGCGGCGGTAATAGTGAAA'])
ERROR: Actual output: None
ERROR: Expected output: ---AAA---
ERROR: None != '---AAA---'
ERROR: ----------------------------------------------------------------------------
ERROR: None != '---AAA---'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/mvincen/Assignment7/a7_hidden_test.py", line 497, in test_l_translate_3
    self.assertEqual(actual_output, translation)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != '---AAA---'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_1_repr
