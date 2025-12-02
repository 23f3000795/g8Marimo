import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Dataset creation: Generating a simple synthetic dataset with some random variables
np.random.seed(42)
data_size = 100
data = pd.DataFrame({
    'x': np.linspace(0, 10, data_size),
    'y': np.random.normal(size=data_size)
})

# Email as a comment (for personal reference)
# Contact: 23f3000795@ds.study.iitm.ac.in

# Create an interactive slider widget to control a variable (e.g., scale of y-axis)
slider = widgets.FloatSlider(
    value=1.0,
    min=0.1,
    max=5.0,
    step=0.1,
    description='Scale Y:',
    continuous_update=True
)

# Function to update the plot dynamically based on the slider value
def update_graph(scale):
    # Here, scale is dependent on the slider value
    scaled_data = data.copy()
    scaled_data['y'] *= scale  # Scaling the y-values based on the slider
    
    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(scaled_data['x'], scaled_data['y'], label=f'Scaled by {scale:.2f}', color='tab:blue')
    plt.title(f'Scatter Plot: y values scaled by {scale:.2f}')
    plt.xlabel('X')
    plt.ylabel('Scaled Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Link slider with update_graph function
widgets.interactive(update_graph, scale=slider)

# The slider widget updates the graph dynamically as you adjust it.
display(slider)

# Define a function that updates markdown based on slider value
def update_markdown(scale):
    markdown = f"""
    # Data Analysis - Dynamic Markdown Output

    The data is currently displayed with the y-values scaled by a factor of **{scale:.2f}**.

    As you adjust the slider, the graph above will change in response, illustrating the effect of scaling the y-values.

    ## Observations:
    - The x-values remain constant as they are independent of the scaling factor.
    - The y-values are scaled proportionally, showing the relationship between **scale** and the **y-variable**.

    ### Next Steps:
    - You may experiment with different scaling factors to see how it affects the data distribution.
    """
    display(Markdown(markdown))

# Use an interactive widget to dynamically update markdown text
widgets.interactive(update_markdown, scale=slider)

# Create another widget that is dependent on the previous slider value
slider2 = widgets.FloatSlider(
    value=1.0,
    min=0.1,
    max=10.0,
    step=0.1,
    description='Factor X:',
    continuous_update=True
)

# Another dependent analysis that combines both the scale and factor values
def update_transformed_data(scale, factor):
    transformed_data = data.copy()
    transformed_data['y'] *= scale  # Apply scaling to y
    transformed_data['x'] *= factor  # Apply a separate transformation to x

    # Plot the transformed data
    plt.figure(figsize=(8, 6))
    plt.scatter(transformed_data['x'], transformed_data['y'], color='tab:orange')
    plt.title(f'Scatter Plot: Scaled and Transformed Data')
    plt.xlabel('Transformed X')
    plt.ylabel('Scaled Y')
    plt.grid(True)
    plt.show()

# Link the new widget to update function
widgets.interactive(update_transformed_data, scale=slider, factor=slider2)

# Display the new slider widget for transformation of X
display(slider2)
