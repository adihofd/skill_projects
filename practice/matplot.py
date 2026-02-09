# import matplotlib.pyplot as plt

# def plot_sales(x,y):
    
#     plt.plot(x,y)
    
#     plt.title("Sales")

#     plt.xlabel("Person")
#     plt.ylabel("Number of Sales")

#     plt.show()


# def input_data():
#     a=[]
#     b=[]
#     inp=int(input("Enter the no of Salespersons:"))
#     for i in range(1,inp+1):
#         a.append(input(f"Enter Salesperson {i} name:"))
#         b.append(int(input(f"Enter Salesperson {i} no of sales:")))
#         print(f"\n")
    
#     plot_sales(a,b)


# input_data()



# import matplotlib.pyplot as plt

# def plot_product_sales(x,y):
    
#     plt.bar(x,y)
    
#     plt.title("Product Sales")

#     plt.xlabel("Products")
#     plt.ylabel("Number of Sales")

#     plt.show()


# def input_data():
#     a=[]
#     b=[]
#     inp=int(input("Enter the no of Products:"))
#     for i in range(1,inp+1):
#         a.append(input(f"Enter Product {i} name:"))
#         b.append(int(input(f"Enter no of sales:")))
#         print(f"\n")
    
#     plot_product_sales(a,b)


# input_data()


# import matplotlib.pyplot as plt

# x = [2,3,4,2,5,6,3,2,8,9,10,7,6,5,4,3,2,12,15,9]
# plt.hist(x,bins=6,rwidth=0.9)   
# plt.title("Call Durations")
# plt.xlabel("Minutes")
# plt.ylabel("Frequency")
# plt.show()

# import matplotlib.pyplot as plt

# x = [10,20,30,40,50,60,70,80]
# y = [1,3,4,6,7,9,11,14]

# plt.scatter(x,y)   
# plt.title("Call Durations")
# plt.xlabel("calls")
# plt.ylabel("conversions")
# plt.show()

# import matplotlib.pyplot as plt

# days = [1,2,3,4,5]
# calls = [50,65,70,60,80]

# products = ["Laptop","Phone","Tablet","Watch"]
# sales = [120,200,90,150]

# fig,ax=plt.subplots(2,2)

# ax[0,0].plot(days,calls)    
# ax[0,0].set_title("call frquency")
# ax[0,0].set_xlabel("days")
# ax[0,0].set_ylabel("calls")

# ax[0,1].bar(products,sales)    
# ax[0,1].set_title("sales")
# ax[0,1].set_xlabel("product")
# ax[0,1].set_ylabel("sale")

# ax[1,0].hist(calls)    
# ax[1,0].set_title("call frquency")
# ax[1,0].set_xlabel("days")
# ax[1,0].set_ylabel("calls")

# ax[1,1].scatter(days,calls)    
# ax[1,1].set_title("sales")
# ax[1,1].set_xlabel("product")
# ax[1,1].set_ylabel("sale")



# plt.show()


# import matplotlib.pyplot as plt

# call_duration = [2,3,4,2,5,6,3,2,8,9,10,7,6,5,4,3,2,12,15,9,30]

# plt.boxplot(call_duration)
# plt.title("Box Plot")
# plt.ylabel("Minutes")
# plt.show()



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df=pd.DataFrame({
#     "calls": [50,60,70,80,90],
#     "duration": [3,4,5,6,7],
#     "revenue": [5000,6000,7500,9000,11000],
#     "conversions": [5,6,8,9,12]
# })

# corr=df.corr()

# sns.heatmap(corr, annot=True)
# plt.title("Correlation Heatmap")
# plt.show()

# df=pd.DataFrame({
#     "agent": ["A","A","A","B","B","B","C","C","C"],
#     "call_duration": [3,5,7,2,4,6,8,9,10]
# })

# sns.boxplot(data=df,x="agent",y="call_duration")

# plt.title("Call Duration by Agent")
# plt.show()

