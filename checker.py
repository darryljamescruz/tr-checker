import pandas as pd

df = pd.read_csv('techrental.csv', encoding='latin-1')

# Combine both conditions with & (and)
filtered = df[(df['Available'] == 'Yes') & (df['State'] == 'In service')]
result = filtered[['Parent resource', 'Barcode']]

print(result)