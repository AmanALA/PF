#Code by Infiltrat8r

def lst_fuctions(lst):

    if len(lst)%2 == 0 :    #for lists with even number of elements

        mid_index = (int((len(lst)/2)))   #expression for middle element index
        print('\nIndex of middle element of list is:',mid_index)
        
        mid_ele = lst[mid_index]    #expression for middle element
        print('Middle element of the list is :',mid_ele)
        
        lst.sort(reverse = True )   #expression for reverse sorting
        print('The list sorted in Descending order is:',lst)
        
        lst.sort()   #expressions for removing first element and placing to the last 
        first_ele = lst[0]
        lst.remove(first_ele)
        lst.append(first_ele)
        print('The list with first element placed at last:',lst)
        
        
    else :  #for lists with odd number of elements

        mid_index = (int(((len(lst)-1)/2)))   #expression for middle element index
        print('\nIndex of middle element of list is:',mid_index)
        
        mid_ele = lst[mid_index]   #expression for middle element
        print('Middle element of the list is :',mid_ele)
        
        lst.sort(reverse = True )   #expression for reverse sorting
        print('The list sorted in Descending order is:',lst)
        
        lst.sort()   #expressions for removing first element and placing to the last 
        first_ele = lst[0]
        lst.remove(first_ele)
        lst.append(first_ele)
        print('The list with first element placed at last:',lst)


Test_lst1 = [1,2,3,4,5,6]
Test_lst2 = [1,2,3,4,5,6,7]

lst_fuctions(Test_lst1)
lst_fuctions(Test_lst2)

