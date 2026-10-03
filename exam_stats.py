import pandas as pd
import numpy as np
from scipy import stats

# Store the scores of 10 students.
scores = pd.Series(
    [72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69]
)

# Display count, mean, standard deviation, and quartiles.
print("Descriptive statistics:")
print(scores.describe())

# Remove missing values only for the shape calculations.
valid_scores = scores.dropna()

print("\nSkewness:", round(stats.skew(valid_scores), 4))
print("Kurtosis:", round(stats.kurtosis(valid_scores), 4))
print("\nMissing values:", scores.isnull().sum())
mean_score = scores.mean()
filled_scores = scores.fillna(mean_score)

print("\nMean used for filling:", mean_score)
print("\nFilled scores:")
print(filled_scores)