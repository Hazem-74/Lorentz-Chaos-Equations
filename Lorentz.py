import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# Lorenz equations
def lorenz(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# Initial parameters
sigma_init = 10
rho_init = 28
beta_init = 8 / 3

# Initial condition
xyz0 = [0, 1, 1.05]

# Time span
t_span = [0, 50]
t_eval = np.linspace(*t_span, 5000)

# Solve initial system
sol = solve_ivp(lorenz, t_span, xyz0, args=(sigma_init, rho_init, beta_init), t_eval=t_eval)
x, y, z = sol.y
t = sol.t

# Set up figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot(x, y, z, lw=0.8, color='blue')
ax.set_title("Lorenz Attractor - Interactive Slider Control")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Adjust layout for sliders
plt.subplots_adjust(left=0.1, bottom=0.25)

# Define sliders
ax_sigma = plt.axes([0.1, 0.15, 0.65, 0.03])
ax_rho = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_beta = plt.axes([0.1, 0.05, 0.65, 0.03])

slider_sigma = Slider(ax_sigma, 'Sigma', 0.1, 50, valinit=sigma_init)
slider_rho = Slider(ax_rho, 'Rho', 0.1, 100, valinit=rho_init)
slider_beta = Slider(ax_beta, 'Beta', 0.1, 20, valinit=beta_init)


# Update function
def update(val):
    sigma = slider_sigma.val
    rho = slider_rho.val
    beta = slider_beta.val

    sol = solve_ivp(lorenz, t_span, xyz0, args=(sigma, rho, beta), t_eval=t_eval)
    line.set_data(sol.y[0], sol.y[1])
    line.set_3d_properties(sol.y[2])

    ax.set_title(f"Lorenz Attractor\nσ={sigma:.2f}, ρ={rho:.2f}, β={beta:.2f}")
    fig.canvas.draw_idle()


# Register update
slider_sigma.on_changed(update)
slider_rho.on_changed(update)
slider_beta.on_changed(update)

# Show plot
plt.show()