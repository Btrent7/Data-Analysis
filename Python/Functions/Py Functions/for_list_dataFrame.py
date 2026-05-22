stu_list = ["Bob", "Ron", "Shelly", "Freddy", "Tammy"]

print(stu_list[0])
print(stu_list[:3])

for stu in stu_list:
    print(stu)

for i in range(len(stu_list)):
    print(i, stu_list[i])



stu_grade_dict = {"Bob":90, 
                  "Ron":87, 
                  "Shelly":73, 
                  "Freddy":67, 
                  "Tammy":88
                }

print(stu_grade_dict["Bob"])

for stu in stu_grade_dict:
    print(stu, stu_grade_dict[stu], sep=', ')

import pandas as pd
student = { "name": ["Bob", "Ron", "Shelly", "Freddy", "Tammy"],
            "grade": [70, 55,  89, 92, 76],
            "classroom": ['506B', '400A', '236A', None, '400A']
        }

student = pd.DataFrame(student)

print(student)