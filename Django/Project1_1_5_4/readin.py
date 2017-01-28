from PIL import Image
import glob

# read in item name , price and description. 
# store the category title at cat
# item in each cat at category. : [1], [2], [3]... and so on.
# Shoud clean up the code later. make a little more pythonic

def readDescription ():
    category = []
    cat =[]
    menuItem = []
    file = open('menu.txt', 'r')
    for line in file:
        list = line.strip().split('-')
        if len(list[0]) == 1:
            category.append(list[1])
            cat.append(list[1])
            category[int(list[0])-1] = menuItem[:]
            menuItem = []
            continue
        else : 
            if len(list) >=3:
                item={
                    "title": list[0] ,
                    "price" : list[1],
                    "description": list[2]
                    }
            else: 
                item={
                    "title": list[0],
                    "price": list[1]
                }
        menuItem.append(item)
    file.close()
    #print cat , category[3]
    return cat, category

# read in image and store in imgList
# images are from 1 to ...n 

def ImageList ():
    imList = []
    temp = []
    list, _ = readDescription()
    for item in list[:-1]:
        for filename in glob.glob('static/images/pics/%s/*jpg' %(item)):
            temp.append(filename)
        imList.append(temp)  
        temp = []   

    return imList

if __name__ == '__main__':
    readDescription()
    ImageList()

