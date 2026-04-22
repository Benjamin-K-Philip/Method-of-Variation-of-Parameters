# Method of Variation of Parameters


## Description 
The concept Method of Variation of Parameters is implemented using Python code by using SymPy library, which performs symbolic calculation of the Wronskian Method as well as symbolic integration in order to calculate the particular solution and general solution. The program then shifts to numerical plotting using Matplotlib.

---


## Description of the selected problems
Following are the Problems selected:- <br>
Q.) Find the Particular Solution and General Solution:

**Problem 1: (x<sup>2</sup> - 1)y'' - 2xy' + 2y = (x<sup>2</sup>-1)<sup>2</sup>**

**Problem 2: y'' + y = sec x cosec x**

**Problem 3: (x <sup>2</sup> + x)y'' + (2 - x<sup>2</sup>)y' - (2 + x)y = x(x + 1)<sup>2</sup>**
<br>

The above selected problems are from the textbook Differential Equations With Applications and Historical Notes, from Chapter 3: Second Order Linear Equations, Section 19. These problems deals with Second-Order Linear Non-Homogeneous Differential Equations and their study of the mathematical connection between the system's inherent characteristics and its behavior when subjected to external influences. The following gives the description of the above problems:

 ➤ **Distinguishing and Classification of Problems:** The selected problems involves the classification of constant co-efficients (Problem 2) and variable co-efficients (Problems 1 and 3). In the latter case, a component of the Complementary Function is identified first by intuition such as <br> **y = x or y = e<sup>x</sup>** before Reduction of Order Method can be applied.

➤ **Use of Variation of Parameters Method:** Problems involve use of Variation of Parameters method to obtain Particular Solution. The method is crucial because "forcing functions" (the expressions on the right-hand side) are non-standard; otherwise, undetermined co-efficient method would be inapplicable.

---

## Procedure/Method used

The following are the procedures that describes the Method of Variation of Parameters: 

**1. Finding the Complementary Function (y<sub>c</sub>):** <br>
The first step involves solving the homogeneous version of the equation (setting the right side to zero). <br>
  - For constant coefficients (Problem 2), we use the characteristic equation.
  - For variable coefficients (Problems 1 and 3), we identify two linearly independent solutions, **y<sub>1</sub>(x)** and **y<sub>2</sub>(x)**, often found by inspection or by reduction of order.
  - **Result: yc = C<sub>1</sub>y<sub>1</sub>(x) + C<sub>2</sub>y<sub>2</sub>(x)**
<br>

**2. Variation of Parameters for the Particular Integral (y<sub>p</sub>):** <br>
Instead of constants C<sub>1</sub> and C<sub>2</sub>, we assume the particular solution takes the form: <br>
<div align="center">

**y<sub>p</sub> = u<sub>1</sub>(x)y<sub>1</sub>(x) + u<sub>2</sub>(x)y<sub>2</sub>(x)**

</div>

To find *u*<sub>1</sub> and *u*<sub>2</sub>, we solve the following system of equations:

**1. *u*<sub>1</sub>'*y*<sub>1</sub> + *u*<sub>2</sub>'*y*<sub>2</sub> = 0**

**2. *u*<sub>1</sub>'*y*<sub>1</sub>' + *u*<sub>2</sub>'*y*<sub>2</sub>' = *f(x)* / *a(x)***
