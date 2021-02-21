import operator
grades = [[86,55,45],[70,75,65],[99,95,90],[46,78,97],[15,47,84]]
name =["Mehmet Burhan Görmeli","Fehmi Ongün","Okay Er","Sertel Çayan","Akay Durgut"]
average_grades = []




for i in range(0,len(grades)):
    average=0
    for j in range(len(grades[i])):
             average =average+ grades[i][j]
    average_grades.append(average/3)




dic = {name[i]: average_grades[i] for i in range(len(average_grades))}
maxgrade = max(dic, key=dic.get)
print(dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True)))
print("en yuksek notu alan "+maxgrade+" i kutlariz")
