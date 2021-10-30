import json
bal = 

with open('record.json','r') as file:
        data = json.load(file)
        data['Cash_in_account'] = bal
        
with open('record.json','w') as file:
    json.dump(data,file,indent=4)



