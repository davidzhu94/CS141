import sys

holder = []
def Read_File():
    number_of_args = len(sys.argv)
    file = open(sys.argv[1], "r")
    index = 0
    for line in file:
        line1 = line.split(", ")
        holder.append(line1)
        index += 1

def Create_Table():
    table = holder[0]
    print float(holder[0][len(holder[0])-1]) + float(holder[0][len(holder[0])-1])
    print table

Read_File()
Create_Table()

def Write_to_File(s):
    inputName = sys.argv[1][:len(sys.argv[1])-4]
    filename = inputName + '_distance.txt'
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')
