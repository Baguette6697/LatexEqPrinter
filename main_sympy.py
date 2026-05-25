from sympy import preview

# We wrap the cases environment inside \[ and \] to put LaTeX into math mode
my_equation = r"""\[
\begin{cases} 
M_A = F \times \frac{L}{4} \\ 
M_B = F \times \frac{3L}{4} \\ 
M_C = 2 \times L^2 \times q \\ 
M_D = 2 \cdot L^2 \cdot q 
\end{cases}
\]"""

preview(
    my_equation,
    output="system.png",
    viewer="file",
    filename="system.png",
    dviwrapper="dvipng",
)
print("Saved successfully via SymPy!")