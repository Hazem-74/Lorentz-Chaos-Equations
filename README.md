# Lorentz Chaos Equations

This repository, authored by Hazem-74, contains Jupyter notebooks dedicated to exploring and visualizing the fascinating **Lorentz chaos equations**. These equations are a classic example of a system exhibiting chaotic behavior, renowned for illustrating concepts like the "butterfly effect" and the existence of strange attractors.

## Project Purpose

The primary purpose of this project is to provide a clear, computational demonstration of the Lorenz system. It aims to:
*   Define the Lorenz ordinary differential equations (ODEs) and their key parameters.
*   Numerically solve these equations over time.
*   Visualize the resulting trajectories in 3D space, revealing the iconic Lorenz attractor.
*   Illustrate the fundamental concepts of chaos theory, such as nonlinearity and sensitivity to initial conditions.

---

## Files Overview

### `Lorentz Eq.ipynb`

This Jupyter notebook is the core of the project. It systematically presents, solves, and visualizes the Lorenz system.

**Purpose:** To define the Lorenz equations, set standard chaotic parameters, numerically integrate the system, and plot the resulting 3D Lorenz attractor.

**Methods and Main Logic:**
1.  **Introduction to Lorenz Equations:** Provides a detailed explanation of the Lorenz system, its historical context (Edward Lorenz, 1963, atmospheric convection), the mathematical formulation of the three coupled nonlinear ODEs, and the physical meaning of its state variables (`x`, `y`, `z`) and parameters (`sigma`, `rho`, `beta`).
2.  **Classic Chaotic Parameters:** Specifies the widely recognized parameter values (`sigma=10`, `rho=28`, `beta=8/3`) that lead to chaotic behavior and the formation of the Lorenz attractor.
3.  **Key Features Discussion:** Highlights important characteristics of the Lorenz system, including nonlinearity, dissipation, the strange attractor, and its sensitivity to initial conditions.
4.  **Numerical Integration:**
    *   Utilizes `numpy` for numerical operations.
    *   Defines the Lorenz ODEs as a Python function `lorenz(t, xyz, sigma, rho, beta)`.
    *   Employs `scipy.integrate.solve_ivp` to numerically solve the system of differential equations over a specified time span (e.g., `t_span = [0, 50]`) with a chosen initial condition (e.g., `xyz0 = [0, 1, 1.05]`).
5.  **3D Visualization:**
    *   Uses `matplotlib.pyplot` to create a 3D plot of the computed `x`, `y`, and `z` trajectories.
    *   The plot clearly visualizes the "Lorenz Attractor," showcasing its distinctive butterfly-like shape, which is a hallmark of chaotic systems.

---

## Project Requirements

To run the notebooks in this repository, you will need:
*   Python 3.7+
*   Jupyter Notebook or Jupyter Lab
*   The following Python libraries:
    *   `numpy`
    *   `scipy`
    *   `matplotlib`

A `requirements.txt` file is provided for easy installation of these dependencies.

## Installation

Follow these steps to set up the project on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Hazem-74/Lorentz-Chaos-Equations.git
    ```

2.  **Navigate to the Project Directory:**
    ```bash
    cd Lorentz-Chaos-Equations
    ```
    
3.  **Install Dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## How to Run the Notebooks

1.  **Start Jupyter Notebook/Lab:**
    ```bash
    jupyter notebook
    # OR
    jupyter lab
    ```
    This command will open a browser window displaying the Jupyter interface.

2.  **Open and Run the Notebook:**
    *   In the Jupyter interface, navigate to the `Lorentz Eq.ipynb` file and click on it to open.
    *   To execute the code, you can run cells individually by selecting a cell and pressing `Shift + Enter`, or run all cells by going to `Kernel -> Restart & Run All`.

You will see the 3D plot of the Lorenz Attractor generated within the notebook.

---

## Author

*   **Hazem-74** - [GitHub Profile](https://github.com/Hazem-74)