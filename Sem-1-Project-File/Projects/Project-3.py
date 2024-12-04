# Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
data = {'Product Category': ['Electronics', 'Clothing', 'Home Decor', 'Books', 'Toys'],'Average Sales': np.random.randint(1000, 5000, 5)}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
plt.bar(df['Product Category'], df['Average Sales'], color='skyblue')
plt.title('Average Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Sales ($)')
plt.show()