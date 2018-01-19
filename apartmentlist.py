
def find_group_sizes(left, results):
    #assign group size to variable
    group5 = 5
    group4  = 4
    group3 = 3
    #if we've reached zero, exit returning anything passed through results
    if left == 0:
        print "zero left"
        return results
    #if exactly 5 are left, make a group of 5 and return results with last group appended
    elif left == 5:
        results.append(group5)
        return results
    #if we have 4 left, make a grouop of 4 and append that to the list of results
    elif left == 4:
        print "four left"
        left = left - 4
        results.append(group4)
        return results
    #if we have three left, make a group of three and add to results, return
    elif left == 3:
        left = left - 3
        print "three left"
        results.append(group3)
        return results
    #if we have 2 left, start stealing from the last group size
    elif left == 2:
        last_group = results.pop()
        results.append(group4)
        results.append(group3)
        return results
    #if we have one left, steal from the last group size
    elif left == 1:
        last_group = results.pop()
        results.append(group3)
        results.append(group3)
        return results
    #if we have more than 5, keep filling up groups of 5
    results.append(group5)
    find_group_sizes(left - group5, results)
    

def create_groups(num_employees):
    #set results to a list
    results = []
    #call function to find group sizes favoring 5s
    find_group_sizes(left=num_employees, results=results)
    return results

group_sizes = create_groups(26)






def create_group(group_sizes, employees):
    #create groups with the names, set list of final groups to variable
    result_group = []
    #go through each group size
    for num in group_sizes:
        #create group
        group = []
        for person in range(num -1):
            #pop off an employee to add to group, this is also where you could use random sample of group size to randomize
            group.append(employees.pop())
        result_group.append(group)
    return result_group

employees= ['Pa Rigsby',
'Mellissa Tse',
'Josephina Juarbe',
'Irena Biddy',
'Yolonda Schurr',
'Georgina Schroeder',
'Maddie Nee',
'Jc Eades',
'Jeromy Lafave',
'Tomi Rodden',
'Lavern Rine',
'Jeannette Tyler',
'Keshia Besse',
'Jacquelin Pizer',
'Julian Hardage',
'Raylene Rudy',
'Audie Taulbee',
'Jenna Mukai',
'Nicole Berlin',
'Marge Appleberry']

print create_group(group_sizes, employees)
    








   

