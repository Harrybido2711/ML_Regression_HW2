# Mini-project (5 points)

## Goals of the project

This project is meant to be a chance to explore beyond the scope of
easily-specified assignment instructions. As such, earning full points on this
will require you to demonstrate effort and creativity, but we won't give you an
explicit rubric. We'll suggest some things we expect you to explore, but you
can choose what you want to focus on. We reserve the right to give you zero
points on this project if you turn in something that does not demonstrate
sufficient effort. If you earn zero points on your first attempt, we will give
you a chance to meet with the course staff and discuss your submission, after
which we may give you partial credit or a chance to redo the assignment.

Your project should involve training models on the provided dataset (see
below), but you can use any models you want (not just polynomial regression). 
Your written report should describe what you tried, and should explain your
work in terms of hypotheses, experiments, and results. Try to decide what you
want to do by proposing a hypothesis and then design experiments to test it.

You can but are absolutely not required to implement any machine learning
models that you use for the project. If you just want to use implementations
from your HW1 or HW2 code, or published libraries like `scikit-learn` or Pytorch,
that's fine.

We will include a pseudonymous "leaderboard" showing the performance of all
students' submitted models (see below). Your grade will not be determined by
your position on the leaderboard, but we may give out extra credit to the
student(s) with the best-performing model. Your report should at least discuss
how you trained and validated your models on the provided dataset and how that
performance aligned with or differed from the leaderboard performance.

## Possible project ideas for inspiration

While the point of this project is for you to do something you're excited about,
here are a few possible ideas that would be interesting:
- Compare your polynomial regression model against `scikit-learn` regression
  models. Explore which hyperparameters are most influential and implement two
  of them to extend your HW2 implementation.
- Extend your HW1 decision tree model to work with regression tasks, analogous
  to the DecisionTreeRegressor class in `scikit-learn`. Explore how your
  implementation compare against the published one on this dataset.

## What to turn in

For the project, you should create a single PDF named `report.pdf`, which you
will upload to the "HW2 Mini-project" assignment on Canvas.

Your report should contain the following:
- One (and **only one**) page of text describing everything you want us to
  evaluate. This needs to be legible: a minimum of 12pt font with at least 1cm
  margins.
- As many pages as you want of citations, figures, and/or plots. Your text can
  and should reference the contents of these additional pages, but we should be
  able to read the text alone and understand the scope of what you
  accomplished. Don't say "I built Figure 1"; say "When I tried varying the
  model's learning rate, I saw that accuracy increased up to a learning rate of
  0.3 and then began decreasing (Figure 1)."

Your report should not contain:
- Your name or Net ID; we will grade this anonymously.
- Any code that you wrote; that belongs in your GitHub repo.

## The dataset

We have uploaded a `hw2_project.csv` dataset in the [Homework Handouts
folder](https://canvas.northwestern.edu/courses/252410/files/folder/Homework%20Handouts)
on Canvas. The goal of this project is to train regression models to predict
the `class` variable from the 23 feature (`X1` through `X23`). We are keeping
the origin of the dataset a secret, but it has been widely used as a benchmark
for evaluating machine learning methods in a biochemical domain. A recent
published paper using a version of this dataset achieved a root mean squared
error (RMSE) of 0.722.

After the assignment is due, I will share a link to the original dataset and
its documentation. Please do not try to figure out the origin of the dataset
before then.

## Leaderboard and trained models

While we will not directly grade your code or any models you train, you will
need to push trained models to GitHub to have them evaluated on the test set.
The provided `hw2_project.csv` dataset is the train set; we have the test
set available only on the autograder. Your written report must discuss the
performance of the your trained models on both the train and test sets.

To submit a model to be evaluated on the test set, you must push a python
script to the `models/` folder. If you upload a file named `my_model.py`,
we will run it from the root of your repository with:

`python project/my_model.py hw1_test_set.csv predictions.csv`

The `hw2_test_set.csv` will be a local path to the test set, which will be in
the same format as the provided `hw2_project.csv` train set. Make sure you
upload any supporting model files to your repository and that they are
accessible when we try to evaluate your model. Each individual file should be
less than 5MB in size -- if you want to do something that requires a larger
model file, ask for help on Piazza.

The `predictions.csv` argument will be a local path to which your script must
output its predictions as a `.csv` file. The file should have a single column
with a header of "PREDICTION". See `project/example.py` for an example of the
expected behavior.

We will run the model evaluation script at most once every hour, and you may
upload at most one model per hour. Your model script must take at most one
minute to produce its test set predictions. The test set is roughly one third
the size of the training set.

Every time the autograder evaluates models, it will create a new csv file of
the results of all students' models. These results will be public to all
students in the class, but your identity is hidden behind a pseudonym, using
the `password` string from Homework 1. For example, if the autograder evaluated
a commit of yours with hash `abcd1234`, running the python script you pushed to
`project/my_model.py`, and if your HW1 "password" was `ffeeddbbcc`, then
everyone in the class would be able to see that hash, script name, and password
alongside that model's performance. You'll be able to see your own results by
looking for your password, and you'll be able to see everyone else's results,
but no one should be able to connect your results back to your name or Net ID.

Your grade will not be determined by your position on the leaderboard, but we
may give out extra credit to the student(s) with the best-performing model.
Your report should at least discuss how you trained and validated your models
on the provided dataset and how that performance aligned with or differed from
the leaderboard performance.

## Allowed packages

You can use whatever packages you want locally, but your submitted model file
must run on the autograder, which will have a limited number of packages
installed. You may request that we install a new package on the autograder,
but we cannot guarantee our ability to do so. At the time of releasing the
assignment, the autograder has the following packages installed:

- `numpy>=2.3.3`
- `pandas>=2.3.3`
- `scikit-learn>=1.7.2`
- `scipy>=1.16.2`
- `torch>=2.8.0`

## Questions?

Please ask on Piazza. We will pin a post with clarifications or corrections
about the assignment.
