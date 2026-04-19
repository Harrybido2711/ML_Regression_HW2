## Instructions

There are 25 points possible for this assignment. 2 points are for the setup,
10 points for the code, 8 points for the free-response questions, and 5 points
are for the mini-project. The setup portion is due earlier than the other
pieces -- all deadlines are on Canvas.

### Setup (2 points)

To pass `test_setup_netid`, all you need to do is put your Net ID in the
`netid` file. There is no `password` component in the setup for this
assignment. Your final coding submission should also pass the `test_setup`
tests. If you delete your Net ID or if your code has syntax errors, the
autograder may give you a zero. If you think the autograder has unfairly given
you fewer points than you should have earned, it is your responsibility to let
us know. If mistakes on your end require us to manually grade your code, we
will deduct points.

### Coding (10 points)

You need to write code in every function in `src/` that raises a
`NotImplementedError` exception. Your code is graded automatically using the
test cases in `tests/`.  To see what your grade is going to be, you can run
`python -m pytest`; make sure you have installed the packages from
`requirements.txt` first. If the autograder says you get 100/100, it means you
get all the points.

The tests build on and sometimes depend on each other. We suggest that you
implement them in the order they appear in `tests/rubric.json`. That file also
allows you to see how many (relative) points each test is worth and which other
tests it may depend on. 

You may not use `fairlearn`, `sklearn`, or `scipy` to implement the functions
in this assignment.  However, you are welcome to look at the relevant
documentation; for example, for the [PolynomialFeatures](
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
and [LinearRegression](
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
classes.  Do not use the numpy functions `lstsq`, `polynomial`, `polyfit` or
`polyval` for any of your solutions. Please do not use the python internal
modules or functions `importlib`, `getattr`, or `globals`. The `test_imports`
case will try to alert you if you use this disallowed packages or functions;
please do not try to circumvent these checks. The `test_imports` case is
written rather pedantically; it just checks for string matches. So if you use
the word "polynomial" in a comment, it will give you a zero for the coding
portion until you change that. You can just replace that with "poly-nomial" or
something to pass the test.

The grade given to you by the autograder on Canvas is the grade you should
expect to receive. If something goes wrong (your code times out, you import a
disallowed package, you accidentally push a syntax error, etc.) and your final
autograder grade is a 0, we will manually grade your code but subtract a 2
point penalty. Please be careful and read the feedback that the autograder is
giving you.

**Note**: `test_custom_transform` may require significant trial and error and
is only worth about 0.5 points towards your final grade. *Please don't spend
several hours on it.* After you've given it an initial try, please take a look
at FRQ5; you can get 1 point for describing your methodology, even if you
didn't pass the test case.

Hints:
  - For all questions in this assignment, you can use any numpy function. A
    helpful numpy function is `np.sign`: it returns the sign of each element in
    an array. That is, -1 if the element is less than 0, 1 if the element is
    greater than 0, and 0 if the element is 0.

  - For the `test_custom_transform`, you are similarly allowed to use any numpy
    functions – e.g., `np.sin`, `np.cos`, and related functions. The output of
    your `custom_transform` function should be a matrix of shape (N, 3) or (N,
    2), but each of those columns should be new features you have created.
    That is, you don't need to copy the original (N, 2) input and only create
    one new feature – you should create 2 or 3 new features. Your choice of
    these features can and should rely on your knowledge that this function is
    a spiral. The only thing that's off limits is hardcoding the labels from
    `spiral.csv` into your feature transform. E.g., a trivial solution is to load
    the dataset and do a manual lookup for the label; don't do that. You may
    find it helpful to read [this article on spirals](
    https://en.wikipedia.org/wiki/Spiral).

### Mini-project (5 points)

See [`project.md`](project.md).

### Free response (8 points)

There are five free response questions, detailed below. Your answer to each
should be in its own PDF file, titled `qYYY.pdf` where `YYY` is the number of
the question. So your answer to question 1 should be in a file named `q1.pdf`.
For questions with multiple parts, put all parts in the single PDF and just
clearly label where each part begins. Please *do not put your name in these
PDFs* -- we will grade your work anonymously.

### Citations (required)

All sources (including LLMs or generative AI) must be referenced and disclosed,
regardless of whether you used them for the coding or free-response portions.
You should disclose those sources in a single `citations.pdf` file that you
upload to the same Canvas assignment as you upload your free-response PDFs.

This citations PDF should include:
- if you discussed the homework with other students in any way (except via
  Piazza), which students did you talk to? About which questions?
- if any online resources may have influenced your approach to solving these
  questions (e.g., you saw a helpful guide to the ID3 algorithm, or you copied
  a line of code from a StackOverflow post), where can we find those resources?
- if you used an LLM such as ChatGPT in any way, what did you do? Please
  include prompts or chat logs as possible.

If you do not include a citations PDF, we will assume you did not speak to any
other students about the class and online resources or LLMs did not influence
your answers in any meaningful way. If we later discover that is false, you may
be reported for an academic integrity violation.

When in doubt, please err on the side of disclosing more than you think is
necessary or relevant.

## Free response questions

### 1. Polynomial Regression model complexity (1 point)

You should not need to write any code for this question. For this question, you
will need to run some experiments using the code in `free_response/q1.py`. Note
that this file relies on your `PolynomialRegression` code as well as some
functions from `sklearn`. The code will create several plots, some of which you
will include in your answers to the parts below. 

If you run `python -m free_response.q1` from your repository's root directory
(i.e., the same place where you run `python -m pytest`), it should fill your
`free_response/plots/` folder with 16 individual plots and add one "meta-plot"
to `free_response/`. Please *do not* push these plots to GitHub!

- a. Look at the "meta-plot" created by `free_response/q1.py` in
  `free_response/q1_regression.png`. Include
  the meta-plot (but not all 16 individual plots!) in your PDF for this
  question. Then, read the code in `q1.py` and figure out how it works.

  For this plot, provide a 2-3 sentence description of the plot.
  What does it show? What are the X-axis and the Y-axes? Where does this plot
  show that models are overfitting or underfitting? Does this match up with
  what we discussed in lecture? What, if anything, surprises you?

- b. Look through the 16 plots created by the `*_regression_experiment()`
  functions in `free_response/q1.py`, that will be saved to
  `free_response/plots/`. Find one plot where the model is clearly
  overfitting, and add it to your PDF. How can you tell that the model is
  overfitting? Then, find one plot where the model is clearly underfitting, and
  do the same. For each plot, include at least a one-sentence explanation.

Your answer should include three plots: one meta-plots showing broader trends
across many experiments in part a, and two individual plots showing the results
of individual experiments that either overfit or underfit in part b.

### 2. Fairness on a toy dataset (3 points)

For this question, look at the code provided in `free_response/q2.py`.  You
shouldn't need to write any code specifically for this question. Once you've
implemented the fairness metrics in `src/metrics.py`, you can run this script
with `python -m free_response.q2`. It will train some models, print out some
important metrics about those models, and visualize them in
`free_response/q2_fairness.png`.

The data for this problem (in `data/frq.fairness.csv`) has four columns:
Income, Credit, Group, and Loan. Suppose that we want to predict whether an
applicant will receive a loan based on their income and credit. Loan is a
binary variable, and Income and Credit are continuous.  Group is some
demographic category (e.g. star-bellied or plain-bellied) which is binary in
this data.  We want our classifier to be fair -- it should not perform
differently overall for individuals with G=0 or G=1. The provided code will
train several LogisticRegression models on this data, and you will analyze
these models' behavior.

- a.  Look at the LogisticRegression model trained in `part_a()` and shown in
  the top left plot. In `free_response/q2_fairness.png`, the area shaded grey
  shows positive predictions; the area shaded red shows negative predictions.
  * To what extent does the classifier treat individuals in Group 0 differently
    from those in Group 1? Answer in terms of the boundary and/or the metrics.
  * If you were applying for a loan and this classifier were making the
    decision and all you cared about was receiving a loan, would you rather be
    a member of Group 0 or Group 1? Why? 

- b.  Consider the LogisticRegression model trained in `part_b()` and shown in
  the top right plot of `free_response/q2_fairness.png`. Look at the code for
  `part_a` and `part_b`.
  * What's different about how this model was trained compared to the model
    from part __a.__?
  * How does this model's decision boundary and metrics differ from those of
    the model in part __a.__? Does this surprise you? Why or why not?

- c.  Look at the code for both LogisticRegression models trained in
  `part_c()` and visualized in the bottom two plots of
  `free_response/q2_fairness.png`.
  * What is different about how each of these two models were trained?
  * If you were applying for a loan and were a member of Group 0 and all you
    cared about was receiving a loan, would you rather be classified by the
    part __c.__ "G=0" classifier or the classifier from part __b.__? Why?
  * What do you find interesting or surprising about the comparison between
    the model from part __b__. and the models from part __c.__? Why?

### 3. Compare LogisticRegression and Perceptron (2 points)

Run `python -m free_response.q3` to compare your LogisticRegression and
Perceptron implementations against the
`sklearn.linear_model.LogisticRegression`.  The code fits each model to the
`polynomial.csv` dataset, using a polynomial feature transform of varying
degrees.

(a) What general trends do you notice in the
`free_response/q3_polynomial_compare.png` plot produced by this code? What
surprises you?

(b) There should be some settings in which the `sklearn` implementation achieve
better accuracy than your Logistic Regression implementation. To understand
why, look at [the documentation](
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
for `sklearn.linear_model.LogisticRegression`. The model has more than 10
different arguments in its constructor, most of which you didn't use in your
code. Pick the two arguments that you think have the most impact on the
`sklearn` model's performance -- why do you think they help that
implementation to outperform your own?

For example, `fit_intercept` is an argument that you didn't use (though it
defaults to `True,` which matches the behavior of your implementation, so don't
choose this in your answer). If you hadn't implemented your LogisticRegression
to fit an intercept, you could say that this argument was important because it
allows the model to learn decision boundaries that aren't centered at the
origin.

### 4. Cross-validation for LogisticRegression (1 point)

Run `python -m free_response.q4` to explore how a LogisticRegression model
behaves as you vary the number of folds of cross-validation. The code fits
the model using `k`-fold cross-validation for a `k` of 3, 6, and 9. It then
plots the decision boundary on each of the `k` test sets along with the
corresponding precision and recall. You do not need to add these plots to your
PDF.

For questions (a-c), please answer the question once for each of the three
values of `k`.

(a) For each value of `k`: across all test sets created by this cross
validation, what is the largest number of examples that any **training** set
contains? Express this as an integer.

(b) For each value of `k`: do you see any `NaN` values in the precision and
recall numbers? Why or why not?

(c) For each value of `k`: What are the mean and standard deviation of the
precision values across each of the `k` test sets? In your calculation, ignore
`NaN` values and don't use the `ddof` parameter. Then, answer this question
again for recall instead of precision.

(d) Summarize the trends you notice in parts (a-c) above as you vary `k`.  Give
a brief explanation of a benefit and drawback for both a larger value of `k`
and a smaller value of `k`. If you were looking at a new dataset, what factors
would help you pick a good value for `k`?

### 5. Custom transform and the spiral dataset (1 point)

Were you able to pass the `test_custom_transform` case? If so, explain what you
did. If not, explain what you tried to do and why.  Provide as much detail as
you can! 
