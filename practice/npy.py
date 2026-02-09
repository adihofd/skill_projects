import numpy as np
# oda=np.array([1,2,3,4])
# tda=np.array([[1,2,3,4],[1,2,3,4]])
# rda=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
# print(f"{oda}\n{tda}\n{rda}")
# o=np.zeros(3)
# two=np.zeros((3,3))
# full=np.full((3,3),0)
# arar=np.arange(0,10,2)
# ls=np.linspace(0,0.1,3)
# iden=np.eye(3)
# randoom=np.random.randint(1,10,size=(3,3))
# print(f"{o}\n{two}\n{full}\n{arar}\n{ls}\n{iden}\n{randoom}")
# import numpy as np

# a = np.array([[1,2,3],[4,5,6]])

# print("Array:\n", a)
# print("Shape:", a.shape)
# print("Dimensions:", a.ndim)
# print("Data type:", a.dtype)
# print("Total elements:", a.size)
# print("Bytes per element:", a.itemsize)
# print("Total bytes:", a.nbytes)

# import numpy as np

# # m = np.array([[11, 22, 33, 44],
# #               [55, 66, 77, 88],
# #               [99, 111, 122, 133]])

# # print(f"{m.shape}\n\n{m[1,2]}\n\n{m[1]}\n\n{m[:,2]}\n\n{m[0:2,1:3]}\n\n{m[1:2]}\n\n{m[m>60]}\n\n{m[[0,1,2],[1,2,3]]}\n\n{m[1:,2:]}")

# a = np.array([2,4,6,8])
# # Add 3 to every element.
# print(f"{a+3}\n\n")

# b = np.array([1,2,3])
# c = np.array([4,5,6])
# # Multiply them elementwise.

# print(f"{b*c}\n\n")

# x = np.array([10,20,30,40])

# print(f"{np.mean(x)}\n\n")


# m = np.array([[1,2,3],
#               [4,5,6]])

# v = np.array([10,20,30])

# print(m+v)

# m = np.array([[10, 20, 30],
#               [40, 50, 60],
#               [70, 80, 90]])
# x = np.array([1.2, 2.7, 3.49, 4.51])

# print(f"{np.sqrt(m)}\n\n{np.sum(m,axis=0)}\n\n{np.sum(m,axis=1)}\n\n{np.argmax(m)}\n\n{np.round(x)}")



# m = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])

# flat=m.flatten()

# print(f"{np.reshape(m,(1,9))}\n\n{flat}\n\n{m.T}\n\n{np.vstack([m,m])}\n\n{np.hstack([m,m])}\n\n{np.hsplit(m,3)}")
# import numpy as np
# a=np.random.randint(1,10,size=(3,3))
# b=np.random.rand(2,4)
# c=np.random.randn(3,3)
# d=np.random.choice([10,20,30,40],size=5)
# f=np.random.normal(loc=100,scale=10,size=5)
# np.random.seed(44)
# e=np.random.rand(2,3)

# print(f"{a}\n\n{b}\n\n{c}\n\n{d}\n\n{e}\n\n{f}")

# a = np.array([10, 3, 5, 2, 9])
# m = np.array([[4,2,3],
#               [9,1,8]])
# x = np.array([1,2,2,3,3,3,4])
# print(f"{np.sort(a)}\n\n{np.argsort(a)}\n\n{np.sort(m,axis=1)}\n\n{np.sort(m,axis=0)}\n\n{np.unique(x,return_counts=True)}\n\n{np.searchsorted(np.sort(a),6)}")

# a = np.array([5,10,15])
# np.save("file.npy",a)

# a_load=np.load("file.npy")
# print(f"{a_load}\n\n")

# x=np.array([1,2,3])
# y=np.array([[4,5],[6,7]])
# np.savez("file_1.npz",first=x,second=y)
# x_y=np.load("file_1.npz")
# print(f"{x_y['first']}\n{x_y['second']}")

# t=np.loadtxt("num.txt")
# print(f"{t}\n\n")

# m=np.genfromtxt("mess.csv",delimiter=',')
# print(m)

# from io import StringIO
# text="1,2,3\n4,5,6\n7,8,9"
# t=np.loadtxt(StringIO(text),delimiter=',')
# print(f"{t}\n\n")
# text1="1,,3\n4,5,6\n,8,9"
# m=np.genfromtxt(StringIO(text1),delimiter=",")
# print(m)

# a = np.array([1,2,3,4,5,6])
# m = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# b=a[1:4]
# print(b)
# b[0]=200
# print(f"\n\n{a}\n\n{b}\n\n")
# m_d=m.flatten()
# m_d[[0]]=20
# print(m_d)
# print(f"\n\n{m}\n\n{m.strides}")