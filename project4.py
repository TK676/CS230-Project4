names = []
distances = []
def read(fileName):
    inputFile = open(fileName, "r")
    for line in inputFile:
        words = line.split()
        names.append(" ".join(words[0:2]))
        words[2] = float(words[2])
        if words[3] == "mi":
            words[2] = words[2] / 0.62137
            distances.append(float(words[2]))
        else:
           distances.append(float(words[2]))
    inputFile.close()


read("distances.txt")
maximum = max(distances)
winner = names[distances.index(maximum)]
print(winner,maximum, "km")


outputFile = open("winner.txt", "w")
outputFile.write(winner + " " + str(maximum) + " km")
outputFile.close()