#!/usr/bin/env python

from PIL import Image

sizes = [(120,120), (720,720), (1600,1600)]
files = ['tilda.jpg']

for image in files:
    print image
    for size in sizes:
        i = Image.open(image)
        i.thumbnail(size)
        i.load()
        li = image.split('.')
        fname = li[0] + '_' + str(size[0]) + '.' + li[1]
        i.save(fname)
