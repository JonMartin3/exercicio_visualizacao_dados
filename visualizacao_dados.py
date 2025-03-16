import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())
print(df.info())

