import re

def name_rank(year, male,female, data):
    
    var_year = re.findall(year,data, re.IGNORECASE)         # Findall returns all the occurance on the other side, search returns... 
    var_male = re.findall(male, data, re.IGNORECASE)        # ... only the first occurence.
    var_female = re.findall(female, data, re.IGNORECASE)

    if(var_male and var_female):
        print(var_year[0])                                  # Printing year
        return var_male, var_female                         # returning tuple of lists
    else:
        print('Name does not exist in this file')


def sorter(s):
    return s[-1]


filename= 'C:\\Users\\My PC\\Desktop\\2.html'
f = open(filename, 'r')
names = f.read()
f.close()


year = r'<b>popularity in\s+(\d\d\d\d)'                     # () is used to extract only the data we care about given the other...
m_name = '<td>(\d+)</td>\s+<td>(\w\w\w+)</td>'              # ... matching characters, rather than fetching all the junk.
f_name = '<td>(\d+)</td>\s+<td>\w\w\w+</td>\s+<td>(\w\w\w+)</td>'
raw_data = name_rank(year, m_name, f_name, names)


male = raw_data[0]                                          # Extracting the returned tuple values
female = raw_data[1]

male_and_female = []
male_n_female = sorted(male+female)
sorted_m_and_f = sorted(male_n_female, key =sorter)

for i in sorted_m_and_f:
    print(i[0],i[1])    
