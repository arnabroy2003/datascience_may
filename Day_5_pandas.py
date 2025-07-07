import pandas as pd

# Series: One-D Labeled array
# s = pd.Series([1,2,3,4])
# print(s)

# s = pd.Series([10,55,89,75], index=['a','b','c','d'])

# print(s['d'])
# print(s.mean())
# print(s.sum())
# print(s + 5)


# DataFrame: 2D table
# data = {
#     'Name': ['Tarun', 'Attadeep', 'Sathiyapriya','Jyoshna'],
#     'age': [19, 20, 18, 21],
#     'Marks': [85,92,78, 57],
#     'address': [266,511,80, 47]
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.head()) # First 5 rows
# print(df.tail(2)) # Last 2 rows
# print(df.shape) # (rows, columns)
# print(df.columns) # Column Names
# print(df['Name']) #Accesss Column
# print(df.iloc[2]) # Row by Index
# print(df.loc[0, 'Marks']) #Specific Cell
# print(df.loc[3, 'age'])


#Load CSV Data
df = pd.read_csv('data.csv')
# print(df.head())
# print(df.describe()) # summary stats
# print(df.info()) # Data type + Nulls

# Filtering Rows

# fil = df[df['Age']>30]
# print(fil)

# fil = df[(df['Age'] > 30) & (df['Salary'] > 90000)]
# print(fil)

# Adding New Columns
# df['Status'] = "Old"
# df.loc[df['Age'] < 30, 'Status'] = "Young"
# print(df)

#Sorting
# sort = df.sort_values(by='Age', ascending=False)
# print(sort)
# sort = df.sort_values(by='Name', ascending=True)
# print(sort)

# Handling Missing Value
# print(df.isnull()) #Where null?
# print(df.isnull().sum()) #column-wise count
# print(df.dropna()) # Remove null rows
# print(df.dropna(axis=1)) #Remove column with nulls
# print(df.fillna(1)) # Replace with Values
