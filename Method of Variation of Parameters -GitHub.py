import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
y = sp.Function('y')(x)
C1, C2 = sp.symbols('C1 C2')

def plot_solution(expr, x_vals, title):
    f = sp.lambdify(x, expr, modules=["numpy"])
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, color="blue", linewidth=2, label="Particular solution")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.6)
    plt.axvline(0, color="black", linewidth=0.6)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

def solve_problem(user_input):
    clean_input = user_input.replace(" ", "").lower()
    
    if "(x^2-1)y''-2xy'+2y=(x^2-1)^2" in clean_input:
        general = sp.Eq(y, C1*x + C2*(x**2 + 1) + sp.Rational(1, 6)*x**4 - sp.Rational(1, 2)*x**2)
        particular = sp.Rational(1, 6)*x**4 - sp.Rational(1, 2)*x**2
        title = "(x^2 - 1)y'' - 2xy' + 2y = (x^2 - 1)^2"
        x_vals = np.linspace(-0.9, 0.9, 400)

    elif "y''+y=secxcosecx" in clean_input:
        particular = -sp.sin(x) * sp.log(sp.csc(x) + sp.cot(x)) - sp.cos(x) * sp.log(sp.sec(x) + sp.tan(x))
        general = sp.Eq(y, C1*sp.cos(x) + C2*sp.sin(x) + particular)
        title = "y'' + y = sec x cosec x"
        x_vals = np.linspace(0.2, 1.2, 400)

    elif "(x^2+x)y''+(2-x^2)y'-(2+x)y=x(x+1)^2" in clean_input:
        # Your exact solution: y = c1*e^x + c2/x - x - 1 - (1/3)x^2
        general = sp.Eq(y, C1*sp.exp(x) + C2/x - x - 1 - sp.Rational(1, 3)*x**2)
        particular = -x - 1 - sp.Rational(1, 3)*x**2
        title = "(x^2 + x)y'' + (2 - x^2)y' - (2 + x)y = x(x + 1)^2"
        x_vals = np.linspace(0.2, 2.0, 400)

    else:
        print("\n[Error] Problem not recognized. Please enter one of the exact equations shown.")
        return

    print("\n--- General Solution ---")
    print(general)

    print("\n--- Particular Solution ---")
    print(f"y(x) = {sp.simplify(particular)}")

    plot_solution(particular, x_vals, title)

while True:
    print("\n" + "=" * 50)
    print("                PROBLEM SELECTION")
    print("=" * 50)
    print("Please select and type one of the following problems to find the Particular Solution and General Solution:")
    print("1. (x^2 - 1)y'' - 2xy' + 2y = (x^2 - 1)^2")
    print("2. y'' + y = sec x cosec x")
    print("3. (x^2 + x)y'' + (2 - x^2)y' - (2 + x)y = x(x + 1)^2")
    print("-" * 50)

    user_text = input("Please enter a problem: ").strip()
    solve_problem(user_text)

    cont = input("\nDo you want to continue (Yes/No)? ").strip().lower()
    if cont != "yes":
        print("Thank you. Terminating program.")
        break