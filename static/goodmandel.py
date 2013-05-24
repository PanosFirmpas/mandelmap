from math import *
import sys,os
from PIL import Image


import cmath



step=1
itr=1000


colours=[]
for n in xrange(itr):
	blue=int(sin(((2*pi)/itr)*n)*255)
	green=int(sin(((2*pi)/itr)*n-(pi/2))*255)
	red=int(sin(((2*pi)/itr)*n-pi)*255)
	if red<0:
		red=0
	if blue<0:
		blue=0
	if green<0:
		green=0
	colours.append((red,green,blue))

while len(colours)<itr:
	   colours.append((0,0,0))

def bintuple(integ):
    s = bin(integ)
    a= [int(s[i:i+3], 2) for i in xrange(0, len(s), 3)]
    return a

def generate_tiles_for(zmin,zooms):
    
    istepx = 3.6
    istepy = 2.6
    for zl in xrange(zmin,zooms):
        if zl>0:
            stepx,stepy = istepx/(2.**zl),istepy/(2.**zl)
        else:
            stepx,stepy = istepx,istepy
        startx = -2.5 
        starty = -1.3 
        for yc in xrange(2**zl):
            for xc in xrange(2**zl):
                sx = startx + xc*stepx
                fx = sx + stepx
                sy = starty + yc*stepy
                fy = sy + stepy
                yield  zl,xc,yc,sx,fx,-sy,-fy



def mandel(c,it):
        ''''''
        if abs(1-cmath.sqrt(1-4*c))<=1:
            return it-1
        z=0
        for i in xrange(0,it):
            z = z**2 + c
            if abs(z) > 2:
                return i
                break
        return i
        # else:
        #     return True  

a,b = int(sys.argv[1]),int(sys.argv[2])
for gzl,gxc,gyc,gsx,gfx,gsy,gfy in generate_tiles_for(a,b):
    data=[]
    resolutionx = 256						#Resolution of the X axis (ATTENTION, the Y axis res. is calculated automatically and might become huge
    resolutiony = 256                       #int(((finishy-starty)/(finishx-startx))*resolutionx)+1



    startx = gsx
    finishx = gfx
    starty = -gsy
    finishy = -gfy



#    print startx,finishx,starty,finishy
    yx = resolutionx/ abs(finishx - startx)
    sx = startx*yx
    fx = finishx*yx

    yy = resolutiony/ abs(finishy-starty)
    sy = starty*yy
    fy = finishy*yy

    ran = xrange(int(sx),int(fx+step),int(step))

    for i,x in enumerate(ran):

        row_data=[]
        for y in xrange(int(sy),int(fy+step),int(step)):
            c=(float(x)/float(yx))+1j*(float(y)/float(yy))
            z=c
            # for l in xrange(1,itr):
            #     z=(z**2)+c;
            #     if abs(z)>2:
            #         break
            l = mandel(c, itr)
            row_data.append(l)
        data.append(row_data)

        # sys.stdout.write("\r%f%%" %(float(i)/len(ran)*100))

    im = Image.new('RGB', (256,256))
    im.putdata([colours[data[x][y]] for y in xrange(256) for x in xrange(256) ])

    if not os.path.exists("./ndump/%d/%d/"%(gzl,gxc)):
        os.makedirs("./ndump/%d/%d/"%(gzl,gxc))
    im.save("./dump/%d/%d/%d.png"%(gzl,gxc,gyc))
    
