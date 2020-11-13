import sys

def solveFile(fileName):
    file = open("in/" + fileName, "r")
    data = file.read().splitlines()
    for i in range(1, len(data)):
        data[i] = data[i].split()

    Interest = {}
    photos = {}
    Direction = {
        'V': [],
        'H': []
    }
    Solution = []
    actualId = 0

    for a in range(1, len(data)):
        _num = int(data[a][1])
        for i in range(2, len(data[a])):
            if data[a][i] in Interest:
                Interest[data[a][i]].append(a-1)
            else:
                Interest[data[a][i]] = []
                Interest[data[a][i]].append(a-1)

        Direction[data[a][0]].append(a-1)


    for v in Interest:
        for i in Interest[v]:
            if i in photos:
                photos[i].append(v)
            else:
                photos[i] = []
                photos[i].append(v)

    def removePhoto(id):
        photos.pop(id)
        for i in Interest:
            if id in Interest[i]:
                for a in range(0, len(Interest[i])):
                    if Interest[i][a] == id:
                        Interest[i][a] = None

    def getDirectionOfPhoto(id):
        if id in Direction['H']:
            return 'H'
        else:
            return 'V'

    def getNextInterestToSearch(id):
        if len(photos) > 0:
            for x in photos[id]:
                if len(Interest[x]) > 0:
                    for y in Interest[x]:
                        if y != None and y != actualId:
                            return y
                else:
                    return id+1
        else:
            return False

    while len(photos) > 2:
        if getDirectionOfPhoto(actualId) == 'H':
            Solution.append(str(actualId)+"\n")
            oldId = actualId
            actualId = getNextInterestToSearch(actualId)
            if not actualId == False:
                removePhoto(oldId)
            else:
                break
        else:
            _solution = str(actualId) + " "
            oldId = actualId
            actualId = getNextInterestToSearch(actualId)
            if not actualId == False:
                removePhoto(oldId)
            else:
                break
            _solution = _solution + str(actualId)+"\n"
            Solution.append(_solution)
            oldId = actualId
            actualId = getNextInterestToSearch(actualId)
            if not actualId == False:
                removePhoto(oldId)
            else:
                break


    solutionFile = open("out/" + "Solution_" + fileName, "w")
    solutionFile.write(str(len(Solution)) + "\n")

    for x in Solution:
        solutionFile.write(x)

    print(fileName + " has been completed. Next")



arrayOfFile = ["a_example", "b_lovely_landscapes", "c_memorable_moments", "d_pet_pictures", "e_shiny_selfies"]

for x in arrayOfFile:
    solveFile(x + ".txt")

print("Execution Completed")