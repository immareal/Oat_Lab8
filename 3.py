from PIL import Image
im = Image.open("TestPicture.jpg")
imgse = im.copy()
imgmax = im.copy()
imgcyan = im.copy()
w,h = imgse.size

for i in range (w) :
    for j in range (h) :
        r,g,b = imgse.getpixel((i,j))

        nr = int(0.393*r + 0.769*g +0.189*b)
        ng = int(0.349*r +0.686*g +0.168*b)
        nb = int(0.272*r + 0.534*g + 0.131*b)

        if nr > 255: nr = 255
        else: nr = nr
        if ng > 255: ng = 255
        else: ng = ng
        if nb > 255: nb = 255
        else: nb = nb
        imgse.putpixel((i,j),(nr,ng,nb))

        m = max(r,g,b)
        imgmax.putpixel((i,j),(m,m,m))

        cr = int(0.1*r + 0.2*g)
        cg = int(0.3*r + 0.6*g)
        cb = int(0.6*g + 0.9*b)

        cr = min(255, cr)
        cg = min(255, cg)
        cb = min(255, cb)

        imgcyan.putpixel((i, j), (cr, cg, cb))


imgmax.save('result1.jpg')
imgse.save('result2.jpg')
imgcyan.save('result3.jpg')