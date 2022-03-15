#Dclaring and defining nested dictionary
people ={1:{'name': 'Hagi', 'age':23,'Gender':'Female'},
          2:{'name': 'Dadi', 'age':57,'Gender':'male'},
         }
print(people)
         #accessing dictioary
new_var = print("Hello",people[1]['name'],"you are ",people[1]['age'],"Years old Young Lady")
print(people[2]['name'])
print(people[2]['age'])
print(people[2]['Gender'])

people[3] = {}

#Adding elements to a dictionary
people[3]['name'] = 'Asnat'
people[3]['nickname'] = 'Yohi'
people[3]['Job'] = 'Student'
people[3]['Sex'] = 'Female'
print(people[3])
print()
print()
print("all People lists ",people)
print()
print()
##Adding a dictionary to a nested dictionary
people[4] = {'name':"Kine","age":'32', 'married':'Yes'}
print(people[4]['name'],people[4])
print()
print(people)

#deleting nested dictionary 
del people[3]['Job']
print()
print(people[3]['name'],people[3])
print()
##Iteratig through nested dictionary
print(people.items())

for p_id,p_info in people.items():
    #gives us an id eachtime iterating
    print("\n Person ID: ",p_id)
#will print us name,age sex as key and their values as p_info[key]
    for key in p_info:
        print(key + ':',p_info[key])