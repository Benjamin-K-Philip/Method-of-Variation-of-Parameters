# Method of Variation of Parameters


## Description 
The concept Method of Variation of Parameters is implemented using Python code by using SymPy library, which performs symbolic calculation of the Wronskian Method as well as symbolic integration in order to calculate the particular solution and general solution. The program then shifts to numerical plotting using Matplotlib.

---

<br>

---

## Description of the selected problems
Following are the Problems selected:- <br>
Q.) Find the Particular Solution and General Solution:

**Problem 1: (*x*<sup>2</sup> - 1)*y''* - 2*xy'* + 2*y* = (*x*<sup>2</sup> - 1)<sup>2</sup>**

**Problem 2: *y''* + *y* = sec *x* cosec *x***

**Problem 3: (*x*<sup>2</sup> + *x*)*y''* + (2 - *x*<sup>2</sup>)*y'* - (2 + *x*)*y* = *x*(*x* + 1)<sup>2</sup>**
<br>

The above selected problems are from the **textbook Differential Equations With Applications and Historical Notes, from Chapter 3: Second Order Linear Equations, Section 19**. These problems deals with Second-Order Linear Non-Homogeneous Differential Equations and their study of the mathematical connection between the system's inherent characteristics and its behavior when subjected to external influences. The following gives the description of the above problems:

➤ **Distinguishing and Classification of Problems:** The selected problems involves the classification of constant co-efficients (Problem 2) and variable co-efficients (Problems 1 and 3). In the latter case, a component of the Complementary Function is identified first by intuition such as <br> **_y = x or y = e<sup>x</sup>_** before Reduction of Order Method can be applied.

➤ **Use of Variation of Parameters Method:** Problems involve use of Variation of Parameters method to obtain Particular Solution. The method is crucial because "forcing functions" (the expressions on the right-hand side) are non-standard; otherwise, undetermined co-efficient method would be inapplicable.

---

<br>

---

## Procedure/Method used
The following are the procedures that describes the Method of Variation of Parameters: 

**1. Finding the Complementary Function (*y*<sub>*c*</sub>):** <br>
The first step involves solving the homogeneous version of the equation (setting the right side to zero). <br>
  - For constant coefficients (Problem 2), we use the characteristic equation.
  - For variable coefficients (Problems 1 and 3), we identify two linearly independent solutions, ***y*<sub>1</sub>(*x*)** and ***y*<sub>2</sub>(*x*)**, often found by inspection or by reduction of order.
  - **Result: *y*<sub>*c*</sub> = *C*<sub>1</sub>*y*<sub>1</sub>(*x*) + *C*<sub>2</sub>*y*<sub>2</sub>(*x*)**
<br>

**2. Variation of Parameters for the Particular Integral (*y*<sub>*p*</sub>):** <br>
Instead of constants *C*<sub>1</sub> and *C*<sub>2</sub>, we assume the particular solution takes the form: <br>
<div align="center">

***y*<sub>*p*</sub> = *u*<sub>1</sub>(*x*)*y*<sub>1</sub>(*x*) + *u*<sub>2</sub>(*x*)*y*<sub>2</sub>(*x*)**

</div>

To find *u*<sub>1</sub> and *u*<sub>2</sub>, we solve the following system of equations:

**1. *u*<sub>1</sub>'*y*<sub>1</sub> + *u*<sub>2</sub>'*y*<sub>2</sub> = 0**

**2. *u*<sub>1</sub>'*y*<sub>1</sub>' + *u*<sub>2</sub>'*y*<sub>2</sub>' = $\boldsymbol{\frac{f(x)}{a(x)}}$**

**Where *f*(*x*) is the non-homogeneous term and *a*(*x*) is the coefficient of *y*'**

<br>

**3. Calculating the Wronskian:**
The code relies on the Wronskian Method (***W***), which ensures the solutions are linearly independent:
<div align="center">
 
***W* (*y*<sub>1</sub>, *y*<sub>2</sub>) = *y*<sub>1</sub>*y*<sub>2</sub>' - *y*<sub>2</sub>*y*<sub>1</sub>'**

</div>

The functions ***u*<sub>1</sub>** and ***u*<sub>2</sub>** are then found by integration:
  - **$u_1 = \int \frac{-y_2 f(x)}{W \cdot a(x)} \, dx$**
  - **$u_2 = \int \frac{y_1 f(x)}{W \cdot a(x)} \, dx$**

<br>

**4. Constructing the General Solution:** <br>
Finally, the code combines the two parts to form the general solution:
<div align="center">
 
***y* = *y*<sub>*c*</sub> + *y*<sub>*p*</sub>**

</div>

---

<br>

---

## Algorithm/Coding Approach <br>
The following are the Algorithm/Coding Approach: <br>

➤ **Symbolic Definition:** The code uses the SymPy module for the definition of mathematical variables (**_x_**) and functions (**_y_**) as symbols. Therefore, it enables the interpretation of complicated math expressions as textual inputs and not as numerical values.

➤ **String Normalization:** For better usability purposes, the program normalizes string input. It removes any whitespaces and converts all characters to lowercase.

➤ **Mathematical Expression to Code:** The python code utilizes a method called lambdify (sp.lambdify), which translates an abstract symbolic expression into an executable code capable of generating numerical data.

➤ **Graph Solution:** It uses Matplotlib library for graph of the solution. For each input problem, the code selects particular intervals of x-axis to provide accurate graph without mathematical exceptions (division by zero).

---

<br>

---

## Output Results


