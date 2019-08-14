import re

def male_name_rank(year, male, data):
    var = re.findall(male, data, re.IGNORECASE)
    var2 = re.findall(year,data,re.IGNORECASE)
    
    if var:
        print(var2[0]) #printing year here. this might not be the best practice, but at the moment that is enough wrt the exercise requirements
        return var
    else:
        print('Name does not exist in this file')


def female_name_rank(female, data):
    var = re.findall(female,data,re.IGNORECASE)
    
    if var:
        return var
    else:
        print('Name does not exist in this file')


def tuple_sort(string):     # This function is to sort tuples from it's second value
    return string[-1]


filename= 'C:\\Users\\Muhammad Idrees\\Desktop\\4.html'
f = open(filename, 'r')     # 'r' is for reading only. 'w' for writing.
names = f.read()
f.close()

male_raw_data = male_name_rank(r'<b>popularity in\s+(\d\d\d\d)','<td>(\d+)</td>\s+<td>(\w\w\w+)</td>',names)
female_raw_data= female_name_rank(r'<td>(\d+)</td>\s+<td>\w\w\w+</td>\s+<td>(\w\w\w+)</td>',names)

raw_data=male_raw_data+female_raw_data
sorted_data = sorted(raw_data, key=tuple_sort)          # "key" helps us determine which value we want to take for sorting purposes. 

counter = 1
for i in sorted_data:
    print(counter,i[1],i[0])
    counter +=1

    
