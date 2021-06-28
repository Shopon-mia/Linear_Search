def linear_search(list, search_number):
    found = False
    for i in range(0, len(list)):
        if list[i] == search_number:
            found = True
            break
    
    if found == True:
        print("Number is found at ",i, "index")
    else:
        print("Number is not found")



list =[10, 30, 20, 5, 40]
search_number = 20
linear_search(list,search_number)