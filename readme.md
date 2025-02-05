# T-Test P-Value Calculator 🧮

A Python-based graphical application for calculating p-values from t-scores and degrees of freedom (df). This tool supports both one-tailed and two-tailed t-tests and provides statistical significance interpretation.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.x
- SciPy library

## Installation

1. Clone or download the repository to your local machine
2. Install the required dependency (SciPy) recommended to use virtual environments using conda:
   ```bash
   pip install scipy
   ```

## Usage

1. Run the program:
   ```bash
   python GUI.py
   ```

2. Enter your values:
   - T-score: Enter your calculated t-statistic
   - Degrees of Freedom: Enter the degrees of freedom for your test

3. Select test type:
   - Two-tailed: Use when testing for differences in either direction
   - One-tailed: Use when testing for differences in only one direction

4. Click "Calculate" to get your results

## Understanding the Results

The program provides:
- The calculated p-value to 4 decimal places
- Interpretation of statistical significance:
  * p < 0.001: Highly statistically significant
  * p < 0.01: Very statistically significant
  * p < 0.05: Statistically significant
  * p ≥ 0.05: Not statistically significant

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Version History

- 1.0.0 (2025-02-05)
  * Initial release
  * Basic GUI implementation
  * One-tailed and two-tailed test support