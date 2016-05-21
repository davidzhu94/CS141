from PIL import Image

import sys

myimage = Image.open("test.jpg")
myimage.load()
print myimage.size, myimage.mode
a = myimage.getpixel((2,1))
b = myimage.getpixel((1,2))

def _distance(rgb1, rgb2):
    return sum((a-b)**2 for a,b in zip(rgb1, rgb2))

def energy(row, col, height, width):
    result = 0
    pixel = get_pixel(row, col)
    for c in (col-1, col+1):
        if 0 <= c < width:
            result += _distance(pixel, get_pixel(row, c))
    for r in (row-1, row+1):
        if 0 <= r < height:
            result += _distance(pixel, get_pixel(r, col))
        if col in (0, width):
            result *= 2
    return result

def getPixels(image):
    width, height = image.size();
    print width, height

getPixels(myimage)

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

print _distance(a, b)

