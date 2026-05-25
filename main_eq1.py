import matplotlib.pyplot as plt

# 1. Configure Matplotlib to use LaTeX AND include the amsmath package
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('font', family='serif', size=24)

# 2. Define your LaTeX equation
# Keep it as a single-line Python string so Matplotlib doesn't break it apart.
# We still use \\ for the LaTeX line breaks inside the system.
equation = r"$\begin{cases} M_A = F \cdot \frac{L}{4} \\ M_B = -F \cdot \frac{3L}{4} \\ M_C = Q \cdot L = 2 \cdot L^2 \cdot q \\ M_D = -Q \cdot L = -2 \cdot L^2 \cdot q \end{cases}$"

# 3. Create a figure without axes
fig = plt.figure(figsize=(6, 3))
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

# 4. Draw the text onto the figure
ax.text(0.5, 0.5, equation,
        horizontalalignment='center',
        verticalalignment='center',
        color='black')

# 5. Save the image with a transparent background
output_filename = "system_equation.png"
plt.savefig(output_filename,
            transparent=True,
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.05)

print(f"Success! Your equation has been saved as '{output_filename}'")