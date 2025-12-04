import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    # Email: 23f3000795@ds.study.iitm.ac.in
    # Cell 1: Import libraries and create sample dataset
    # This cell generates the base data that will be used throughout the notebook
    
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Generate sample dataset: relationship between study hours and test scores
    np.random.seed(42)
    study_hours = np.linspace(0, 10, 100)
    # Base relationship: linear with some noise
    base_scores = 50 + 4 * study_hours + np.random.normal(0, 5, 100)
    test_scores = np.clip(base_scores, 0, 100)
    
    # Create DataFrame
    df = pd.DataFrame({
        'study_hours': study_hours,
        'test_scores': test_scores
    })
    
    return df, mo, np, pd, plt, study_hours, test_scores
    

@app.cell
def __(mo):
    # Cell 2: Create interactive slider widget
    # This slider allows users to filter data by minimum study hours
    # The slider value will be used in subsequent cells for dynamic filtering
    
    hours_slider = mo.ui.slider(
        start=0,
        stop=10,
        step=0.5,
        value=0,
        label="Minimum Study Hours Filter:"
    )
    
    return hours_slider,


@app.cell
def __(df, hours_slider):
    # Cell 3: Filter data based on slider value
    # This cell depends on: df (from Cell 1) and hours_slider (from Cell 2)
    # The filtered data will be used for visualization and statistics
    
    min_hours = hours_slider.value
    filtered_df = df[df['study_hours'] >= min_hours]
    
    # Calculate statistics on filtered data
    mean_score = filtered_df['test_scores'].mean()
    count = len(filtered_df)
    correlation = filtered_df['study_hours'].corr(filtered_df['test_scores'])
    
    return correlation, count, filtered_df, mean_score, min_hours


@app.cell
def __(count, correlation, filtered_df, mean_score, min_hours, mo, np, plt):
    # Cell 4: Create visualization and dynamic markdown output
    # This cell depends on: filtered_df, mean_score, count, correlation (from Cell 3)
    # Generates a scatter plot and dynamic statistics based on the slider value
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_df['study_hours'], filtered_df['test_scores'], 
               alpha=0.6, s=50, c='steelblue', edgecolors='black', linewidth=0.5)
    
    # Add trend line
    z = np.polyfit(filtered_df['study_hours'], filtered_df['test_scores'], 1)
    p = np.poly1d(z)
    ax.plot(filtered_df['study_hours'], p(filtered_df['study_hours']), 
            "r--", alpha=0.8, linewidth=2, label=f'Trend line')
    
    ax.set_xlabel('Study Hours', fontsize=12)
    ax.set_ylabel('Test Scores', fontsize=12)
    ax.set_title(f'Study Hours vs Test Scores (Filtered: ≥{min_hours:.1f} hours)', 
                 fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Dynamic markdown output that changes based on slider state
    dynamic_output = mo.md(f"""
    ## Data Analysis Results
    
    **Filter Applied:** Showing students with ≥ **{min_hours:.1f}** study hours
    
    ### Key Statistics:
    - **Sample Size:** {count} students
    - **Average Test Score:** {mean_score:.2f}
    - **Correlation Coefficient:** {correlation:.3f}
    
    ### Interpretation:
    {f"The positive correlation of {correlation:.3f} suggests a {'strong' if correlation > 0.7 else 'moderate' if correlation > 0.4 else 'weak'} relationship between study hours and test scores." if count > 0 else "No data available for this filter."}
    
    {"💡 **Insight:** Students who study more tend to achieve higher test scores!" if correlation > 0.5 and count > 0 else ""}
    """)
    
    visualization = mo.as_html(fig)
    plt.close()
    
    return ax, dynamic_output, fig, p, visualization, z


@app.cell
def __(dynamic_output, hours_slider, mo, visualization):
    # Cell 5: Display the interactive interface
    # This cell depends on: hours_slider (Cell 2), visualization and dynamic_output (Cell 4)
    # Presents the complete interactive analysis to the user
    
    mo.vstack([
        mo.md("# Interactive Study Hours Analysis"),
        mo.md("*Demonstrating variable dependencies and reactive computation in Marimo*"),
        mo.md("---"),
        hours_slider,
        mo.md("---"),
        visualization,
        dynamic_output
    ])
    
    return


if __name__ == "__main__":
    app.run()
