print("Hello World")

type(3)



my_list=(['Arapahoe', 'Denver','Jefferson'])

countries = my_list

#Add El Paso to the second position in the list. 

countries.insert(3,"El Paso")

#'Remove Arapahoe from the list. 

countries.pop(0)

#'Make Denver the third item in the list, but keep Jefferson the second item in the list.  

countries[0]="El Paso"

countries[2]="Denver"

#'Add Arapahoe to the list. 

countries.append("Arapahoe")



print(countries)

countries_dict={}

countries_dict["Aropahoe"]=422829

countries_dict["Denver"]=463353

countries_dict["Jefferson"]=432438

len(countries_dict)

countries_dict.items()


print(countries_dict)

voting_data=[]

voting_data.append({"county":"Aropahoe","registered_voters" : 422829})

voting_data.append({"county":"Denver","registered_voters": 463353})

voting_data.append({"county":"Jefferson","registered_voters": 432438})

len(voting_data)

voting_data.pop(0)

voting_data.insert(0, ({"county":"El Paso","registered_voters": 461149}))

voting_data.pop(1)

voting_data.insert(2,({"county":"Denver","registered_voters": 463353}))

voting_data.append({"county":"Aropohe","registered_voters": 422829})

print(voting_data)