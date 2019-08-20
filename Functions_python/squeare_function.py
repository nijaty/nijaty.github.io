# def square_function(x):
#     return x*x

# print(square_function(5))

# main_list = []
# a = list(map(int,input().split()))
# for ele in range(a[0]):
#     main_list.append([])
# for cox in range(len(main_list)):
#     z = int(input())
#     main_list[cox].append(z)
# print(main_list)
#print(int(1000/a[1]))
d = 0
main_list = []
ilk_iki_verilenler = list(map(int,input().split()))
for ele in range(ilk_iki_verilenler[0]):
    main_list.append([])
for z in range(ilk_iki_verilenler[0]):
    for mirt in range(int(input())):    
       main_list[z].append(int(input()))
    d += max(main_list[z]) * max(main_list[z])
print(d)
print(main_list)

