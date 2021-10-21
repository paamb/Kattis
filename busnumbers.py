n = int(input())
stops = [(x.strip()) for x in input().split()]
# print(stops)
stops = sorted(stops,key = lambda x: int(x))
# print(stops)
liste = []
string = ""
for stop in stops:
    if len(liste) == 0:
        liste.append(stop)
        continue
    if len(liste) > 2 and int(liste[-1]) != (int(stop)-1):
        string += str(liste[0]) + "-" + str(liste[-1]) + " "
        liste.clear()
        liste.append(stop)
    elif int(liste[-1]) == (int(stop)-1):
        liste.append(stop)
    elif int(liste[-1]) != (int(stop)-1):
        string += " ".join(liste) + " "
        liste.clear()
        liste.append(stop)

if len(liste) > 2:
    string += str(liste[0]) + "-" + str(liste[-1])
else:
    string += " ".join(liste) 

print(string)
    # else:
    #     print("2", stop)
    #     if len(liste) > 2:
    #         string += str(liste[0]) + "-" + str(liste[-1]) + " "
    #         liste.clear()
    #     else:
    #         string += str(liste[0])
    #     liste.append(stop)
# print(string)





    #  if len(liste) == 0:
    #     liste.append(stop)
    #     continue
    # if len(liste) > 0 and liste[-1] == (stop-1):
    #     print("1", stop)
    #     liste.append(stop)
    # elif len(liste) > 2 and liste[-1] != (stop-1):
    #     print("hei")
    #     string += str(liste[0]) + "-" + str(liste[-1]) + " "
    #     liste.clear()
    #     liste.append(stop)
    # elif len(liste) == 2 and liste[-1] != (stop-1):
    #     string += str(liste[0]) + " " + str(liste[1]) + " "
    #     liste.clear()
    #     liste.append(stop)
    # elif len(liste) == 1:
    #     print("hei2")
    #     liste.append(stop)
    #     string += str(liste.pop(0)) + " "   
    # else:
    #     liste.append(stop)
# string += str(liste[0])
# print(liste)