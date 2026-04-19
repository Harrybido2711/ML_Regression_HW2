# HW 2: Polynomial Regression, Logistic Regression, and Perceptron

There are 25 points possible for this assignment. 2 points are for the setup,
10 points for the code, 8 points for the free-response questions, and 5 points
for the mini-project. The setup portion is due earlier than the other pieces --
all deadlines are on Canvas. Please carefully read this entire README before
starting the assignment.

## What's changed since HW1?

- There is no `password` file for this homework.
- If you used a conda environment for HW1, please reuse that. If you used `uv`,
  we've provided the same `uv.lock` and `pyproject.toml` files as in HW1.
- There are several functions that make it trivially easy to implement linear
  regression. Please do not use those. You should be computing at least one
  matrix inverse in your implementation.

## Academic integrity

Your work must be your own. You may not work with others. Do not submit other
people's work as your own, and do not allow others to submit your work as
theirs. 

If you need help debugging your code, make a *private* post on Piazza or come
to office hours. You may not show your code (including pseudocode) to other
students under any circumstances.

You are required to completely understand any homework solution that you
submit, and, in case of any doubt, you must be prepared to orally explain your
solution. If you have submitted a solution that you cannot verbally explain,
then you have violated this policy.

Please see [the academic integrity
policy](https://canvas.northwestern.edu/courses/252410/pages/academic-integrity)
for more detail.  By pushing your code to GitHub, you agree to these rules, and
understand that there may be severe consequences for violating them.

## Important instructions

Your work will be graded and aggregated using an autograder that will download
the code and free response questions from each student's repository. If you
don't follow the instructions, you run the risk of getting *zero points*. The
`test_setup` test cases gives you points for following these instructions 
and will make it possible to grade your work easily.

The essential instructions:
- Your code must be *pushed* to GitHub for us to grade it!
  We will only grade the latest version of your code that was pushed to GitHub
  before the deadline (accounting for late days; see below).
- Your NetID must be in the `netid` file; replace `NETID_GOES_HERE` with your
  netid.
- Your answer to each free response question should be upload to Canvas in *its
  own PDF* with the filename `qYYY.pdf`, where `YYY` is the question number. So
  your answer to free response question 2 should be in a PDF file with the
  filename `q2.pdf`.
- Do not include your name or Net ID in the content of your free response PDFs
  -- we will grade these anonymously. 

## Late Work

In general, unexcused late work is worth zero points. The autograder will only
download work from your repository that was pushed to GitHub before the
deadline. However:

- Each student gets four late days to use across the entire quarter. If you
  want to use late days, use the [late day assignment
  ](https://canvas.northwestern.edu/courses/252410/assignments/1757666) on
  Canvas.
- You can use at most two late days per assignment. Late days cannot be used
  for setup, and apply equally to coding, free-response, and projects.
- If you have a personal emergency, please ask for help. You do not have to
  share any personal information with me, but I will ask you to get in touch
  with the dean who oversees your student services to coordinate
  accommodations.

## Clone this repository and environment setup

You can just use the same environment for this assignment that you used for
HW1. For more detailed versions of these instructions, refer to the HW1 README.

## What to do for this assignment

The detailed instructions for the work you need to do are in `problems.md`.

For the coding portion of the assignment, you will:
- Implement mean squared error loss
- Implement two fairness metrics
- Generate polynomial data on which to fit your models 
- Implement a polynomial regression model
- Implement a logistic regression model
- Implement a perceptron model

The details on the free-response questions and mini-project are available in
`problems.md` and `project.md` respectively.

In every function where you need to write code, there is a `raise
NotImplementedError` in the code. You will replace that line with code that
completes what the function docstring asks you to do.  The test cases will
guide you through the work you need to do and tell you how many points you've
earned. The test cases can be run from the root directory of this repository
with:

``python -m pytest -s``

To run a single test, you can specify it with `-k`, e.g., `python -m pytest -s
-k test_setup`.  To run a group of tests, you can use `-k` with a prefix, e.g.,
`python -m pytest -s -k test_knn` will run all tests that begin with
`test_knn`.  The `-s` means that any print statements you include will in
fact be printed; the default behavior (`python -m pytest`) will suppress
everything but the pytest output.

We will use these test cases to grade your work! Even if you change the test
cases such that you pass the tests on your computer, we're still going to use
the original test cases to grade your assignment.

## Questions? Problems? Issues?

Ask a question on Piazza, and we'll help you there.

## Helpful Material

See the `logistic_regression.pdf` file provided in this repo. The lectures on
(linear and polynomial) regression and on classification will also be helpful.
