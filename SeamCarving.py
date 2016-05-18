import sys
def Read_File():
    number_of_args = len(sys.argv)
    file = open(sys.argv[1], "r")
    index = 0
    holder = []
    for line in file:
        line.strip("\n")
        line1 = line.split(", ")
        holder.append(line1)
        index += 1

def Write_to_File(s):
    inputName = sys.argv[1][:len(sys.argv[1])-4]
    filename = inputName + '_distance.txt'
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')
