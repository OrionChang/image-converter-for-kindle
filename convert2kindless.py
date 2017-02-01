from PIL import Image, ImageOps
import re, os, sys, errno

SIZE = 1072,1448
IMAGEEXT = re.compile(".*\.(jpg|jpeg)", re.IGNORECASE)

def ensuredirs(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise

try:
    image_dir = sys.argv[1]
except:
    print "Please specify a directory"
    exit(1)


counter = 0

files = os.listdir(image_dir)
for file in files:
    if IMAGEEXT.match(file):
        f = os.path.join(image_dir, file)
        print f
        img = Image.open(f)
        
        # rotate landscape images
        if img.size[0] > img.size[1]:
            img = img.rotate(90)
    
        # resize and crop the image to fit in 1072*1448 screen
        img = ImageOps.fit(img, SIZE, Image.ANTIALIAS)
        
        # convert to grayscale
        img = img.convert('L')
        
        # screensaver naming
        file_name = "bg_ss" + str(counter).zfill(3) + ".png"
        counter+=1
        
        # save to ./ss directory
        ensuredirs(os.path.join(image_dir,'ss'))
        fout = os.path.join(image_dir, 'ss', file_name)
        img.save(fout, "PNG")
