# 🔢 Gaussian Elimination Solver

## 📖 Description

This is a simple Python program that solves a system of three linear equations using **Gaussian Elimination**. The goal of this task, assigned during the **KAITECH training**, is to manually implement the algorithm without relying on external libraries like NumPy — to better understand the underlying mathematical logic.

The program operates on an **augmented matrix** representing the system of equations, applies Gaussian Elimination to convert it to upper triangular form, and then performs **Back Substitution** to find the values of the unknowns.

---

## 🧮 Problem Statement

We are solving the following system of equations:

2x + 3y + z = 1
4x + y + 2z = 2
3x + 2y + 3z = 3


---

## 🚀 How It Works

- `step1()`:
  - Normalizes the pivot elements to 1.
  - Eliminates the elements below the main diagonal to achieve row echelon form.
  
- `solve()`:
  - Performs back substitution to find the values of `x`, `y`, and `z`.

- `display()`:
  - Prints the matrix at its current state.

---

## 📦 Output Example


[1.0, 1.5, 0.5, 0.5] 
[0.0, -5.0, 0.0, 0.0]
[0.0, 0.0, 2.0, 2.0]
x = 0.0 y = -0.0 z = 1.0

🧑‍💻 Author
Developed as part of a training task at KAITECH.
The purpose is to reinforce understanding of linear algebra and algorithm implementation in Python.

