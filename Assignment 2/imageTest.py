from PIL import Image
myimage = Image.open("test.png")
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

print _distance(a, b)

