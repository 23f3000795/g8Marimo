import marimo as mo
from drawdata import BarWidget

a = 10
b = 1

def multiply(x, y):
    return x * y

# Email as a comment (for personal reference)
# Contact: 23f3000795@ds.study.iitm.ac.in

widget = mo.ui.anywidget(BarWidget(height=200, width=700, n_bins=24, collection_names=["usage", "sunshine"]))

# INPUTS:
# - var_a (from cell above)
# - var_b (created in this notebook)

# OUTPUTS:
# - cleaned_df: used by visualization and model cells

name = mo.ui.text(label="Enter your name")
name

mo.md(f"""
# Hello, **{name.value or "Stranger"}**! 👋  
This heading updates instantly as you type.
""")

 
