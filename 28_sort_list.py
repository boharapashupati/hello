first_list =[0,5,2,45,6,7,82,676,5, -50,-80]
# first_list.sort()
# print(first_list)


temp =0
sort_list =[]
for num in first_list:
    if num>temp:
        sort_list.append(num)
        temp=num
    else:
        sort_list.insert(0,num)
sort_list.sort()
print(sort_list)


#assignment to short given list [1,5,9,6,89,1203,4,23]

# list_a = [1,5,9,6,89,1203,4,23]
# list_a.sort()
# print(list_a)



# name = "pashupati"
# moth_name = ["junuory", "feb","mar", "apr","may", "june","july","aug"]
# print(moth_name [:7])






































