# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from PIL import Image
import random

from models import Tile

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from math import *
import cmath
import os
import simplejson
import time
import base64
import cStringIO
import re







def home(request):
    dic = {'request' : request}
    return render_to_response("home.html", dic , context_instance=RequestContext(request))

def test(request,z,x,y):
    dic = {'request' : request}
    return render_to_response("test.html", dic , context_instance=RequestContext(request))

@csrf_exempt
@require_POST
def api(request,z,x,y):
    datauri = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='
    post = request.POST
    arurl = post['arurl']
    
    #magic
    imgstr = re.search(r'base64,(.*)', arurl).group(1)
    tempimg = cStringIO.StringIO(imgstr.decode('base64'))

    im = Image.open(tempimg)

    image_pre_path = '%s/%s/'%(z,x)
    image_path = os.path.join("/home/panosfirbas/webapps/static_mandelbrot/media/"+image_pre_path) 
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    
    im.save(image_path +y+ '.png', 'PNG')
    tile = Tile(z=z,x=x,y=y)
    tile.save()

    return HttpResponse("1")



# def mandel(c,it):
#         ''''''
#         if abs(1-cmath.sqrt(1-4*c))<=1:
#             return it-1
#         z=0
#         for i in xrange(0,it):
#             z = z**2 + c
#             if abs(z) > 2:
#                 return i
#                 break
#         return i

# itr=100
# colours=[]
# for n in xrange(itr):
#     blue=int(sin(((2*pi)/itr)*n)*255)
#     green=int(sin(((2*pi)/itr)*n-(pi/2))*255)
#     red=int(sin(((2*pi)/itr)*n-pi)*255)
#     if red<0:
#         red=0
#     if blue<0:
#         blue=0
#     if green<0:
#         green=0
#     colours.append((red,green,blue))

# while len(colours)<itr:
#        colours.append((0,0,0))


# def make_tile(z,x,y):
#     resolutionx = 256                       #Resolution of the X axis (ATTENTION, the Y axis res. is calculated automatically and might become huge
#     resolutiony = 256                       #int(((finishy-starty)/(finishx-startx))*resolutionx)+1
#     #limits for the BIG image
#     big_x_left,big_x_right,big_y_bottom,big_y_top = -2.5,1.1,-1.3,1.3
#     big_step_x = big_x_right - big_x_left
#     big_step_y = big_y_top - big_y_bottom

#     if z!= 0:
#         step_x,step_y = big_step_x/2.**z , big_step_y/2.**z
#     else: 
#         step_x,step_y = big_step_x,big_step_y

#     start_x = big_x_left + x*step_x
#     start_y = big_y_top - y*step_y #this seems wrong
#     finish_x = start_x + step_x
#     finish_y = start_y - step_y

#     yx = resolutionx/ step_x
#     sx = start_x*yx
#     fx = finish_x*yx

#     yy = resolutiony/ step_y
#     sy = start_y*yy
#     fy = finish_y*yy

#     p_x_step = step_x / resolutionx
#     p_y_step = step_y / resolutiony

#     data=[]

    
#     # ran = xrange(int(sx),int(fx+1),int(1))

#     for px in xrange(resolutionx):

#         row_data=[]
#         for py in xrange(resolutiony):
#             real = start_x + px*p_x_step + p_x_step/2. #The middle of pixel start left / pixel start right, somewhat optimized
#             imaginary = start_y - py*p_y_step - p_y_step/2.
#             c=(real)+1j*(imaginary)
#             l = mandel(c, itr)
#             row_data.append(l)
#         data.append(row_data)

#     im = Image.new('RGB', (256,256))
#     im.putdata([colours[data[x][y]] for y in xrange(256) for x in xrange(256) ])
#     return im

    # im.save("./test.png")

# def image(request,z,x,y):
#     tiles = Tile.objects.all().filter(z=z).filter(x=x).filter(y=y)
#     image_pre_path = '%s/%s/%s'%(z,x,y)
#     image_path = os.path.join("/home/panosfirbas/webapps/static_mandelbrot/media/", image_pre_path)
#     # print "get coords:"
#     try : 
#         tile = tiles[0]
#         image = Image.open(image_path+'.png')
#         print '%s/%s/%s I got to load it !'%(z,x,y)
#     except: 
#         image = make_tile(int(z),int(x),int(y))
#         if not os.path.exists(image_path):
#             os.makedirs(image_path)
        
#         image.save(image_path + '.png', 'PNG')
#         tile = Tile(z=z,x=x,y=y)
#         tile.save()
#         print '%s/%s/%s I had to make it !'%(z,x,y)
    
    
    

#     # serialize to HTTP response
#     response = HttpResponse(mimetype="image/png")
#     image.save(response, "PNG")
#     return response


import json 

def exists(request,z,x,y):
    tiles = Tile.objects.all().filter(z=z).filter(x=x).filter(y=y)
    try : 
        tile = tiles[0]
        json_data = json.dumps({"HTTPRESPONSE":1})    
    except:
        json_data = json.dumps({"HTTPRESPONSE":0})
        
    
    
    # json data is just a JSON string now. 
    return HttpResponse(json_data, mimetype="application/json")