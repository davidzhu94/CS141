import sys

table = []
seam = 0

def Read_File():
    holder = []
    number_of_args = len(sys.argv)
    file = open(sys.argv[1], "r")
    index = 0
    for line in file:
        line1 = line.split(", ")
        holder.append(line1)
        index += 1
    return holder

def Create_Table(holder):
    table.append(holder[0])
    i = 1
    for i in range(1, len(holder)):
        table.append([])
        for j in range(len(holder)):
            if j == 0:
                table[i].append(float(holder[i][j]) + min(float(table[i-1][j]), float(table[i-1][j+1])))
            elif j == (len(holder[i])-1):
                table[i].append(float(holder[i][j]) + min(float(table[i-1][j]), float(table[i-1][j-1])))
            else:
                table[i].append(float(holder[i][j]) + min(min(float(table[i-1][j]), float(table[i-1][j-1])), float(table[i-1][j+1])))
    thing = float("inf")
    for i in range(len(table)):
        if float(table[len(table)-1][i]) < thing:
            thing = table[len(table)-1][i]
            global seam
            seam = i
    winner = seam
    trace = [[len(table)-1, winner, float(holder[len(table)-1][winner])]]
    for i in range(len(table)-2, -1, -1):
        if winner == 0:
            if float(holder[i][winner]) < float(holder[i][winner+1]):
                trace.append([i, winner, float(holder[i][winner])])
            if float(holder[i][winner+1]) < float(holder[i][winner]):
                winner += 1
                trace.append([i, winner, float(holder[i][winner])])
        elif winner == len(table[winner])-1:
            if float(holder[i][winner]) < float(holder[i][winner-1]):
                trace.append([i, winner, float(holder[i][winner])])
            if float(holder[i][winner-1]) < float(holder[i][winner]):
                winner -= 1
                trace.append([i, winner, float(holder[i][winner])])
        else:
            if float(holder[i][winner]) < float(holder[i][winner+1]) and float(holder[i][winner]) < float(holder[i][winner-1]):
                trace.append([i, winner, float(holder[i][winner])])
            if float(holder[i][winner+1]) < float(holder[i][winner]) and float(holder[i][winner+1]) < float(holder[i][winner-1]):
                winner += 1
                trace.append([i, winner, float(holder[i][winner])])
            if float(holder[i][winner-1]) < float(holder[i][winner]) and float(holder[i][winner-1]) < float(holder[i][winner+1]):
                winner -= 1
                trace.append([i, winner, float(holder[i][winner])])
    return trace

def Write_to_File(s):
    inputName = sys.argv[1][:len(sys.argv[1])-4]
    filename = inputName + '_trace.txt'
    output = open(filename ,'w')
    output.write("Min Seam: ")
    output.write(str(table[len(table)-1][seam]))
    output.write('\n')
    for i in range(0, len(table)):
        output.write(str(s[i]))
        output.write('\n')

Write_to_File(Create_Table(Read_File()))
