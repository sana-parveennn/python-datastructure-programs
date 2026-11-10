# d = {1,2,3,4}
# print(type(d))

# d = {"hello":100,"broo":200,"sunday":300}
# print(d["hello"])    #accesing values

# d['hello'] = 1000   #changing the values

# d = {10:100,20:200,30:300,40:400}
# print(d[10])



# d = dict([("name" , "sanaa"),("age" , 20)])
# print(d)

# traversing
# a = {10:100,20:200,30:300,40:400}
# for i in a.values():
#     print(i)

# dictionary methods


# a = {10:100,20:200,30:300,40:400}

# a.setdefault(12)
# print(a)

# a = {10:100,20:200,30:300}
# b = {40:400,50:500,60:600}

# a.update(b)
# print(a)

# count frequency of array elements
# a = [1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d.keys())


# s1 = "aabbcc"
# s2 = "bacckab"

# if len(s1) == len(s2):
#     d = {}
#     for i in s1 :
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1

#     for i in s2:
#         if i in d.keys():
#             d[i] -= 1
#         else:
#             print("an extra element was found")

#     for i in d:
#         if d[i] != 0:
#             print("sorry your elements are not same ")
#             break
#     else:
#         print("your strings are same")

# else:
#     print("not same")


a = [1,1,1,1,2,2,2,2,2,3,3,4,4,5,5,5,6,6,6,7,8,9,0]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1


for i in d:
    if d[i] > 1:
        print(i)


































