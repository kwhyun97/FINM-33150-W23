# FINM-33150-W23

Contact (Professor/TAs/Graders): <a href = "ta33150-2023@lists.uchicago.edu">ta33150-2023@lists.uchicago.edu</a>

HW Questions: On <a href = "https://edstem.org/us/courses/32282/discussion/">Ed Discussion</a> except in special cases

Zoom: <a href = "https://uchicago.zoom.us/j/97298244621?pwd=dGp6SEZIanQwTWtNdXRFc0wwNnpsQT09">weekly class</a>.

## Overview
Quantitative trading strategies, employing investment decisions based on model output, are a major component of business operations in the finance industry worldwide. We will present the vital features of these strategies as found in several asset classes (equities, futures, credit, FX, interest rates, energy and, to a lesser extent, cryptotokens). Particular topics of concentration include spread trades, carry trades, parameter reversion, model prediction/evaluation, and market making.

 

A large proportion of the models involved in quantitative strategies are expressible in terms of regressions. We will cover most of the ways they are used, including practical tricks and considerations, concentrating particularly on achieving trustworthy performance. Mathematically, we will learn the computation of linear regressions with and without weights, in univariate and multivariate cases, having least squares or other objective functions.

 

Of the major computation technologies actively used by the finance industry (C/C++, Matlab, kdb, Java, R, VB/Excel, C#, Julia, SQL, Python) we have chosen R and Python for numerical computation, with data coming from Quandl and some proprietary sources.

## Partial Flipped Instruction
This class will contain a mix of in-person and online instruction.  Our first meeting is, naturally, entirely in person and I look forward to seeing you there.

Five of the ten class sessions will be "flipped", in the sense that the required lecture material will consist of videos posted in Canvas Panopto, and the corresponding in-class time will be devoted to questions, help and discussion.  Of these five flipped sessions, two will be entirely remote -- we will not meet in the classroom on those weeks.

Another five of our ten class sessions will be traditional, in which the instructor presents lecture material live.  Zoom will still be active for those.

At the end of the quarter, we will have a Canvas quiz (for credit) asking about your experience with flipped versus traditional instruction, to be used in future versions of the class.

 

## Technology and Obstacles
Most of the effort in quantitative research is devoted to expressing our ideas in computational terms. This involves writing and debugging code, and it can be a frustrating struggle. All of you will grapple at times with our data sources, with R and Python, with equation formatting software and so on. Your frustration is part of the learning process and will ultimately make you a stronger quant.

 

To ease your use of R and Python, I recommend Anaconda Links to an external site., a copy of Posit RStudio Links to an external site., plus a copy of PyCharm Links to an external site.(free academic license Links to an external site.).   Another great environment is available in the form of Visual Studio Code Links to an external site..  

Online, a highly complete R environment is available at the Posit/RStudio Cloud Links to an external site.and a Jupyter environment is at CoCalc Links to an external site..  

 

Some technologies I strongly encourage you to learn, but are not treated in this class, include

SQL database querying and table design in fifth normal form
Writing C/C++ code to be used as a library by R or Python (FINM 32000, 32600)
Parallel CPU processing, GPU processing (FINM 32950)
 

### A.I. Tools
Since your homework and projects require both computer code and prose, you may find A.I. tools such as ChatGPT helpful.  We encourage you to try them out.  If you employ A.I. to help with your homework, please indicate the prompts involved.

These tools have some well-known pitfalls, so we are unsure whether they are actually useful for quantitative finance or not.  We will likely have a survey asking your opinion on that matter near the end of the quarter.

 

## Coursework
<h3> <b> Homework </b> </h3>
Our homework assignments will consist mainly of exercises (computer programs and analysis documents) resembling finance industry uses for regression, or simple components of trading strategies. Homework will be due at 23:00:00 on Thursday evenings, and must always be submitted in a single file to the class website. Use a zip archive if you have more than one file. You must make your own name and student number part of the file name. In addition, any Jupyter notebooks, particularly your "main" analysis notebook, must have your name and student number as part of the file name, and in the notebook itself near the top.

All homework must be submitted as Jupyter notebooks capable of running on Python version 3.10 or R version 4.2 without unexpected package dependencies.  Please see the R and Python Canvas Pages for commands that help Anaconda to install standard packages.  (This packages listed there may have additions through the quarter as need arises.)

While students may communicate with each other on homework sets, each problem set must be an individual creation. No copying of code or prose from other people is permitted. Students submitting homework with substantially similar code or analyses will fail the assignment and, at instructor's discretion, the course.

The same rules apply for electronic resources including old homework sets from this class; you are welcome to examine them and derive inspiration from their code, but your work must be your own.

When you need help doing your homework, your first resource should be the class forums. Any issue you encounter is liable to be found manifold among your colleagues in this class, and I want everyone to have the opportunity to help each other out.

 

Late homework will be treated as follows:

* No HW accepted more than 1 week past due date
* HW submitted after an assignment has been completely graded: 50% penalty
* HW submitted 1 second or more after 23:00:00 CDT: 25% penalty
 
<h3> <b> Final Project </b> </h3>
The final project will be for 2-4 person groups to create a quantitative trading strategy with short pitchbooks and accompanying Jupyter notebooks (nicely formatted 5-30 page presentation of the strategy's major properties). You or your group will be graded mostly on the clarity of the pitch book and notebook along with the correctness and completeness of the strategy implementation/analysis, not on the strategy's (simulated) returns.

The final project will be completed in two phases:

* Draft phase:
  - Group established
  - Strategy chosen and explained in pitchbook and in notebook
  - Some data downloaded, cleaned, and graphed nicely
  - No implementation or analysis necessary
* Final submission
 

### Grading
Class participation: 5%
Homework: 45%
Project Draft: 15%
Final Project: 35%
 

### Teaching Staff
  Instructor:  Brian K. Boonstra

  TAs: Satyajit Sarangdhar and Max Anderson
