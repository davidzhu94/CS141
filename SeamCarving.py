import sys

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
    table = []
    table.append(holder[0])
    print float(holder[0][len(holder[0])-1]) + float(holder[0][len(holder[0])-1])
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
    print thing

def Find_Trace():

Create_Table(Read_File())

def Write_to_File(s):
    inputName = sys.argv[1][:len(sys.argv[1])-4]
    filename = inputName + '_distance.txt'
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')
