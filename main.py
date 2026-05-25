import matplotlib.pyplot as plt


def latex_to_image(latex_str, output_filename="equation.png", dpi=300):
    """Converts a LaTeX equation string to a transparent PNG image.

    Parameters:
    - latex_str: The LaTeX equation (e.g., r'$e^{i\pi} + 1 = 0$')
    - output_filename: The name of the saved file
    - dpi: Dots per inch (higher means higher resolution/larger image)
    """
    # 1. Create a figure. We start small; bbox_inches='tight' will crop it perfectly.
    fig = plt.figure(figsize=(3, 1))

    # 2. Add the LaTeX text in the middle of the figure
    # we use 're' for the font to give it that classic TeX look
    plt.text(
        0.5,
        0.5,
        latex_str,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=16,
        usetex=False,  # Uses matplotlib's built-in mathtext
        math_fontfamily="cm",  # Computer Modern font (classic LaTeX look)
    )

    # 3. Hide the axes completely
    plt.axis("off")

    # 4. Save the image with a transparent background
    # bbox_inches='tight' removes all unnecessary white space around the equation
    # pad_inches adds a tiny bit of breathing room so edges aren't cut off
    plt.savefig(
        output_filename,
        dpi=dpi,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0.1,
    )
    plt.close(fig)
    print(f"Saved: {output_filename}")


# --- Example Usage ---
if __name__ == "__main__":
    # Note the 'r' before the string. This treats backslashes as raw text.
    my_equation = r"$\int_{a}^{b} f(x) \,dx = F(b) - F(a)$"

    latex_to_image(my_equation, "calculus.png", dpi=300)
