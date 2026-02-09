import pandas as pd
"""
df=pd.Series([5,12,18,25,40],index=['x','y','z','p','q'])
print(df)
print(df.mean())
"""
"""
df=pd.DataFrame({
    'product':['Apple','Banana','Grapes'],
    'Price':[120,40,90],
    'Quantity':[10,25,15]
},index=['x','y','z'])
print(df)
print(df['Price'])
print(df['Price'].mean())
print(df.info())
print("\n")
print(df.iloc[1])
print("\n")
print(df.loc['x'])
"""
"""
import pandas as pd

data = {
    'Name': ['Adi', 'Rahul', 'Kiran'],
    'Age': [18, 21, 22],
    'Marks': [90, 85, 95]
}

df = pd.DataFrame(data)
print(df)
df.to_csv("students.csv",index=False)
"""
"""

df = pd.DataFrame({
    'Name': ['Adi', 'Rahul', 'Kiran', 'John'],
    'Age': [18, None, 22, None],
    'Marks': [90, 85, None, 70]
})

print(df)

print("\nMisiing")
print(df.isnull().sum())
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Marks']=df['Marks'].fillna(df['Marks'].median())
print(df)
"""
"""

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Adi', 'Rahul', 'Kiran', 'John']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 5],
    'Marks': [90, 85, 70]
})

result = pd.merge(df1,df2,how='inner',on='ID')
print(result)
"""
"""
df = pd.DataFrame({
    'Product': ['Apple', 'Apple', 'Banana', 'Banana', 'Grapes'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
    'Sales': [120, 150, 80, 60, 200]
})
print(df)
print(df.describe())
print(df.groupby('Product')['Sales'].agg(['sum','mean','max']))
print(df.groupby(['Product','City'])['Sales'].sum())
"""
"""
df = pd.DataFrame({
    'Product': ['Apple', 'Apple', 'Banana', 'Banana', 'Grapes'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
    'Sales': [120, 150, 80, 60, 200]
})
print(f"{df.sort_values(by='Sales',ascending=False)}\n{df.sort_values(by=['Product','Sales'],ascending=[True,False])}")


df['Rank'] = df['Sales'].rank(ascending=False)
print(df)
"""
"""
df = pd.DataFrame({
    'Product': ['Apple', 'Apple', 'Banana', 'Banana', 'Grapes'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
    'Sales': [120, 150, 80, 60, 200]
})
df['Bonus']=df['Sales'].apply(lambda x:x*0.10)
df['Category']=df['Sales'].apply(lambda x:'Premium' if x>100 else 'Regular')

print(df)
"""
"""
df = pd.DataFrame({
    'Product': ['Apple', 'Apple', 'Banana', 'Banana', 'Grapes'],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
    'Sales': [120, 150, 80, 60, 200]
})
product_sales = df.groupby('Product')['Sales'].sum()

product_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

city_sales = df.groupby('City')['Sales'].sum()


city_sales.plot(kind='bar')
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()co
"""
import pandas as pd
# ser=pd.Series([91, 85, 72, 88],index=['math', 'eng', 'sci', 'hist'])
# print(f"{ser}\n\n{ser['eng']}\n\n{ser+5}")

# ser=ser.apply(lambda x:"A" if x>90 else("B" if 90>=x>=80 else "C"))
# print(f"\n\n{ser}\n\n")
# df=pd.DataFrame({
#     'Name':['A','B','C'],
#     'Age':[20,25,22],
#     'City':['Delhi','Mumbai','Chennai']
# })

# print(f"{df}\n\n{df[df['Age']>20]}\n\n")

# df['Salary']=[50000, 60000, 55000]

# print(f"{df}\n\n")

# df['Salary']+=10000

# print(f"{df}\n\n")

# df.drop('City',axis=1,inplace=True)

# print(f"{df}\n\n")

# import pandas as pd

# df = pd.DataFrame({
#     'Name'   : ['A','B','C','D','E'],
#     'Age'    : [20, 25, 22, 28, 30],
#     'City'   : ['Delhi','Mumbai','Chennai','Delhi','Hyderabad'],
#     'Salary' : [50000, 60000, 55000, 70000, 80000]
# })


# print(f"\n\n{df.loc[0:2]}\n\n{df.iloc[0:3]}\n\n{df[(df['Age'] >= 25) & (df['Salary'] > 70000)]}")

# df['Bonus']=(df['Salary'])/10
# df['Salary']+=df['Bonus']

# print(f"\n\n{df}")

# df.drop('City',axis=1,inplace=True)
# df.rename(columns={"Name":"EmpName"})

# print(f"\n\n{df}\n\n")
# print(f"{df.iloc[[0, 2, 4]][['Name', 'Salary']]}")
# df = pd.DataFrame({
#     'Name'   : ['A','B','C','D','E'],
#     'Age'    : [20, 25, 22, 28, 30],
#     'City'   : ['Delhi','Mumbai','Chennai','Delhi','Hyderabad'],
#     'Salary' : [50000, 60000, 55000, 70000, 80000]
# })

# print(f"""{df.loc[[1,3,4],['Name','City']]}\n\n{df.iloc[[0,2,4]][['Salary','Age']]}\n\n{df.query("City != 'Delhi' and 22<Age<30")}\n\n""")


# print(f"{df.apply(lambda row: row['Salary'] + 5000 if row['City'] in ['Delhi', 'Mumbai'] else row['Salary'], axis=1)}")

# df=df.set_index('Name')
# print(f"{df.loc[['D']]}")

# df = pd.DataFrame({
#     'Name'   : ['A','B','C','D','E'],
#     'Age'    : [20, 25, 22, 28, 30],
#     'City'   : ['Delhi','Mumbai','Chennai','Delhi','Hyderabad'],
#     'Salary' : [50000, 60000, 55000, 70000, 80000]
# })

# a=df.groupby('City')['Salary'].sum()
# b=df.groupby('City').agg(
#     avg_age=('Age','mean'),
#     max_sal=('Salary','max'),
#     min_sal=('Salary','min')

# )
# c=df.groupby('Age').size()

# df['City_Avg_Salary']=df.groupby('City')['Salary'].transform('mean')

# d=df
# e=df.groupby('City')['Salary'].sum()

# print(f"{a}\n\n{b}\n\n {c}\n\n {d}\n\n {e[e>100000]}\n\n")


# import pandas as pd

# df = pd.DataFrame({
#     'Name':['A','B','C','D'],
#     'Age':[20, None, 25, None],
#     'City':['Delhi','Mumbai', None, 'Chennai']
# })



# print(f"{df.isnull().sum()}\n\n")
# df.dropna(how='all',inplace=True)
# print(f"{df}\n\n")
# df['Age']=df['Age'].fillna(df['Age'].median())
# print(f"{df}\n\n")
# df['City']=df['City'].fillna('Unknown')

# print(f"{df}\n\n")

df = pd.DataFrame({
    'City': ['Delhi','Delhi','Mumbai','Mumbai','Chennai'],
    'Product': ['A','B','A','B','A'],
    'Sales': [120, 150, 100, 200, 80]
})


# a=df.pivot_table(values='Sales',index='City',aggfunc='sum')
# b=df.pivot_table(
#  values='Sales',
#  index='City',
#  columns='Product',
#  aggfunc=['sum','mean'],fill_value=0)
# c=pd.crosstab(df['City'], df['Product'])
# d="\n"
# e="\n"

# print(f"{a}\n\n{b}\n\n {c}\n\n {d}\n\n {e}\n\n")

# df = pd.DataFrame({
#     'Date': ['2023-01-01','2023-01-05','2023-02-10','2023-03-01'],
#     'Sales': [100, 150, 200, 250]
# })
# df['Date']=pd.to_datetime(df['Date'])

# df['Day']=df['Date'].dt.day
# df['Month']=df['Date'].dt.month
# df['Year']=df['Date'].dt.year

# print(f"{df}\n\n{df[df['Date']>'2023-01-31']}\n\n{df.sort_values('Date')}\n\n")
# df.set_index('Date',inplace=True)
# print(f"{df.resample('ME').sum()}")

# df = pd.DataFrame({
#     'City': ['Delhi','Delhi','Mumbai','Mumbai'],
#     'Product': ['A','B','A','B'],
#     'Sales': [100, 150, 200, 250]
# })


# df_D =df.set_index(['City','Product'])
# print(f"{df_D}\n\n{df_D.loc[[('Delhi','A')]]}\n\n{df_D.loc[[('Mumbai')]]}")
# df_D=df_D.unstack(['Product'])
# print(f"\n\n{df_D}")

# import pandas as pd

# df = pd.DataFrame({
#     'Day': [1,2,3,4,5,6],
#     'Sales': [10, 20, 30, 40, 50, 60]
# })
# df['MA_3'] = df['Sales'].rolling(window=3).mean()

# print(f"\n\n{df}")
# df['Roll_Sum_3'] =df['Sales'].rolling(3).mean()
# print(f"\n\n{df}")
# df['Exp_Mean'] = df['Sales'].expanding().mean()
# print(f"\n\n{df}")
# df['EWM_0.3'] = df['Sales'].ewm(alpha=0.3).mean()
# print(f"\n\n{df}")

# df=pd.DataFrame({
#     ' Customer Name ': ['  John', 'Alice ', 'Bob', 'Alice ', None],
#     'Age': [25, -1, 40, None, 30],
#     'City ': ['delhi ', '  mumbai', None, 'Delhi', 'HYDERABAD '],
#     'Amount$': ['100', '200', 'invalid', '300', None]
# })
# df.columns=(df.columns
#                 .str.strip()
#                 .str.lower()
#                 .str.replace(' ', '_')
#                 .str.replace('$', '', regex=False)
# )
# print(f"\n\n{df}")
# df['age'].replace(-1,None,inplace=True)

# print(f"\n\n{df}")

# df['age'].fillna(df['age'].median(),inplace=True)

# print(f"\n\n{df}")

# df.fillna({'city':'Unknown'},inplace=True)
# df.drop_duplicates(inplace=True)
# df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
# df.fillna({'amount':0}, inplace=True)


# print(f"\n\n{df}")


