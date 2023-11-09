patient_number = int(input())
patient_list = []

for i in range (patient_number):
    name, insurance, danger_lvl = input().split()
    danger_lvl = int(danger_lvl)
    if insurance == "premium":
        insurance = 5
    if insurance == "ouro":
        insurance = 4
    if insurance == "prata":
        insurance = 3
    if insurance == "bronze":
        insurance = 2 
    if insurance == "resto":
        insurance = 1
    
    patient_list.append((name, insurance, danger_lvl))
    
def list_order(list):
    for i in range(len(list)):
     for j in range(len(list) - i - 1):
            if list[j][1] == list[j + 1][1]:
                if list[j][2] == list[j + 1][2]:
                    if list[j][0] > list[j + 1][0]:
                        list[j], list[j + 1] = list[j + 1], list[j]
                else:
                    if list[j][2
                                ] < list[j + 1][2]:
                        list[j], list[j + 1] = list[j + 1], list[j]
            else:
                if list[j][1] < list[j + 1][1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
    return list

result = list_order(patient_list)
for i in result:
  print(i[0])