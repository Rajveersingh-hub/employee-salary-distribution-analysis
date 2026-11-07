import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = pd.read_csv("employee_salary.csv")

salary = data["Salary"]

# Mean
mean = salary.mean()

# Variance
variance = salary.var()

# Standard Deviation
std = salary.std()

# Skewness
skewness = salary.skew()

# Kurtosis
kurtosis = salary.kurt()

# Display results
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

# Fit Normal Distribution
x = np.linspace(salary.min(), salary.max(), 100)
normal_curve = norm.pdf(x, mean, std)

# Histogram and Normal Curve
plt.hist(salary, bins=10, density=True, alpha=0.6)
plt.plot(x, normal_curve, linewidth=2)

plt.xlabel("Salary")
plt.ylabel("Density")
plt.title("Employee Salary Distribution with Normal Curve")
plt.show()