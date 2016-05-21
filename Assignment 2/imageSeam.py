from PIL import Image

import sys

table = []
seam = 0

myimage = Image.open(sys.argv[1])
myimage.load()
print myimage.size, myimage.mode
a = myimage.getpixel((2,1))
b = myimage.getpixel((1,2))

def _distance(rgb1, rgb2):
    return sum((a-b)**2 for a,b in zip(rgb1, rgb2))

def energy(image, row, col, height, width):
    result = 0
    pixel = image.getpixel((row, col))
    for c in (col-1, col+1):
        if 0 <= c < width:
            result += _distance(pixel, image.getpixel((row, c)))
    for r in (row-1, row+1):
        if 0 <= r < height:
            result += _distance(pixel, image.getpixel((r, col)))
        if col in (0, width):
            result *= 2
    return result


def getPixels(image):
    holder = []
    width, height = image.size
    #a =  energy(image, 0, 2, height, width)
    #b = energy(image, 0, 3, height, width)
    wHolder = []
    #wHolder.append(a)
    #wHolder.append(b)
    for i in range(width):
        for j in range(height):
            wHolder.append(float(energy(image, i, j, width, height)))
        holder.append(wHolder)
        wHolder = []
    print holder
    return holder



getPixels(myimage)
print "getpixels works"

def Create_Table(holder):
    table.append(holder[0])
    i = 1
    print "bananas"
    for i in range(1, len(holder)):
        table.append([])
        for j in range(len(holder[i])):
            print i, j
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

Write_to_File(Create_Table(getPixels(myimage)))

