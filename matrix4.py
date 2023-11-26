dic = {1:{"name":"John", "age":27,"sex":"Male"},
       2:{"name":"Marie","age":22,"sex":"Female"},
       3:{"name":"Sali","age":23,"sex":"Female"}}

for key in dic:
    x=dic[key]['age']
#for name,age in dic:
    if(x>22):
        print(dic[key]['name'])
        