# a = [1,1.3,"hello",True]

# print(type(a))


# #list is a hetrogeneous nature you can store anything init
# #list can store duplicate values too

# b = [2,3,3,2,4,4]
# #its mutable that means you can store dupliate value



# c = [1,2,3,4.5,6,7]
# #you can change values even after once you assign it


# s = "NATURE"
# print(s[2])


# l = [10,20,30,40,50]

# print(l[0], l[-5])
# print(l[:3])


# a = [10,20,30,40,54,60]
# a[4] = 50
# print(a)         #mutable


# #refrence copy
# a = [10,20,30,40,50]

# b = a
# b[0] = 100

# print(a)
# print(b)

# #shello copy
# a =[10,20,30,40,50]
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)

# #deep copy
# import copy
# a =[10,20,30,40,50]
# b =copy.deepcopy(a)
# b[0] = 100

# print(a)
# print(b)

# import copy
# a = [[10,20],[30,40]]

# b1 = a.copy()
# b2 = copy.deepcopy(a)

# b1[0] [0] = 999
# b2[1] [0] = 888

# print("original:", a)
# print("shellow:", b1)
# print("deep:",b2)


# #reversing method1
# a = [10,20,30,40,50]
# for i in a:
#     print(i)
 
#  #transversing method2 (index)
# a = [10,20,30,40,50,60]
# for i in range(len(a)):
#     print(i)



# a = [10,20,30,40]
# a.append(50)
# print(a)

# a = [1,23,43,54,45,90,36,78,89]
# max = a[0]
# index = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"your max elemnet is {max} at {index}")

# a = [1,23,43,54,45,90,36,78,89]
# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = a[i]
#         index2 = index
#         index = i
#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i

# print(f"max {max} at {index} and max 2 is {max2} at {index2}")

# a = [11,12,13,14,15,16,17,18,23,34,35,56,78,90]
# for i in range (len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break

# else:
#     print("your list is sorted")


# a = [10,20,30,40,50]

# for i in range(len(a)-1):
#     a[i],a[i+1] = a[i+1],a[i]

# print(a)


# k = int(input("how many times you wanna rotate "))
# a = [10,20,30,40,50]


# for i in range(k):
#     for i in range(len(a)-1):
#         a[i],a[i+1] = a[i+1],a[i]

# print(a)

# a = [10,20,30,40,50]
# b = []

# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])

# print(b)



# a = [10,20,30,40,50]
# b = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[b] = a[b],a[i]
#     b = b-1
# print(a)


# a = [54,68,4,5,3,78,9,87,55,43]
# search = 3

# for i in range(len(a)):
#     if a[i] == search:
#         print(f"element found at index {i}")
#         break
# else:
#     print(f"no such element exist")


# a = [11,12,13,15,16,26,47,68,78,90]

# search = 68

# start = 0
# last = len(a)-1
# mid = (start + last)//2

# while start <= last:
#     if a[mid] == search:
#         print(f"element found at index {mid}")
#         break
#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start + last)//2

#     elif a[mid] > search:
#         last = mid - 1
#         mid = (start + last)//2


# else:
#     print(F"soory no such element exist")



# 
# a = [56,34,67,976,43,6,8,2234,7,89,68,34]

# for j in range(len(a)-1):

#     for i in range(len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]

# print(a)




# a = [56,34,67,976,43,6,8,2234,7,89,68,34]

# for i in range(len(a)-1):
#     j = i+1
#     min = i
#     for k in range(j,len(a)):
#         if a[k] < a[min]:
#             min = k

#     a[i],a[min] = a[min],a[i]

# print(a)














































































