from pdf2image import convert_from_path
import os
import sys
import time

def sources():
    arr = os.listdir("C:/data/source/1/")
    source = "C:/data/source/1/"
    return arr,source
arr, source = sources()

def ConvertToImage(arr, source):
    for arrs in arr :
        pathname=arrs[:-4]
        pathname=pathname.replace(" ", "")
        outputDir = "source/"+pathname+'/'    
        files=source+arrs
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        images = convert_from_path(files, 500)

        for i, image in enumerate(images):
            fname =str(i)+'.png'
            image.save(outputDir+fname)
ConvertToImage(arr, source)

        
