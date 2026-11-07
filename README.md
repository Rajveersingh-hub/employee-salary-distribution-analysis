# Employee Salary Distribution Analysis

## Project Overview

This project analyzes a sample of employee salary data using statistical methods.

The analysis focuses on:

- Mean
- Variance
- Skewness
- Kurtosis
- Normal Distribution

## Project Flow

```text
Sample Salary Data
        ↓
Load Dataset
        ↓
Calculate Mean
        ↓
Calculate Variance
        ↓
Calculate Standard Deviation
        ↓
Calculate Skewness
        ↓
Calculate Kurtosis
        ↓
Fit Normal Distribution
        ↓
Histogram + Normal Curve
        ↓
Interpret Results
```

## Dataset

The sample salary data is stored in:

`employee_salary.csv`

The dataset contains:

- Employee_ID
- Salary

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy

## Analysis

### Mean

Calculates the average salary of the employees.

### Variance

Measures the spread of salary values around the mean.

### Standard Deviation

Measures the variation in salaries and is used for fitting the normal distribution.

### Skewness

Shows whether the salary distribution is symmetric or tilted toward one side.

### Kurtosis

Shows the tail behavior of the salary distribution compared with a normal distribution.

### Normal Distribution

A normal distribution is fitted using the calculated mean and standard deviation.

The actual salary data is shown using a histogram, and the fitted normal distribution is shown as a curve over the histogram.

## Output

The project produces:

- Mean
- Variance
- Standard Deviation
- Skewness
- Kurtosis
- Histogram with fitted Normal Distribution curve

## Project Structure

```text
employee-salary-distribution-analysis/
│
├── employee_salary.csv
├── salary_analysis.py
└── README.md
```