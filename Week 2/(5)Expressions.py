#Code by Infiltrat8r

str1 = 'anachronistically'
str2 = 'counterintuitive'
print(str1,'has',len(str1)-len(str2),'more character(s) than:',str2) 

lst = ['misrepresentation','misinterpretation']
lst.sort()
print('The word',lst[0],'appears before the word',lst[1],'in the dictionary.')

str3 = 'floccinaucinihilipilification'

if 'e' not in str3 :
    print('The letter e not is in',str3)

str3 = 'counterrevolution'
str4 = 'counter'
str5 = 'resolution'

print('The number of charachters in',str3,'is',len(str3))
print('The number of charachters in',str4,'and',str5,'is also',(len(str4)+len(str5)))
