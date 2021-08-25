#copy random crop x times
from os import listdir
from os.path import isfile, join, isdir
import torchvision
from PIL import Image
import random

def main(height, width, count, src, path):
    """
    Parameters
    ----------
    count :
        desired number of output crops
    src : str
        Patrh to look for tif Images to random crop
    path : str
        Path to store output crops.
    """
    croper = torchvision.transforms.Compose ([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.RandomCrop((height,width)),
        torchvision.transforms.ToPILImage()])
    
    onlyfiles = [join(src, f) for f in listdir(src) if f.endswith('.tif')]
    for i in range(count):
        file = random.choice(onlyfiles)
        image = Image.open(file)
        crop = croper(image)
        crop.save(join(path,str(i+1)+".tif"))    

if __name__ == '__main__':
    main(height=400,width=400,count=5000,src='/home/ps815691/git/PSSR/datasources/IMM10ms/train',path='/home/ps815691/datasets/reftest')
