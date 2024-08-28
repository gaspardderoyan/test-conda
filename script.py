import numpy as np
import pandas as pd

# Create a random DataFrame
data = {
    'A': np.random.randint(0, 100, 10),
    'B': np.random.randint(0, 100, 10)
}
df = pd.DataFrame(data)

# Calculate the mean of column A
mean_a = df['A'].mean()

print(f"The mean of column A is: {mean_a}")
