import os
import readin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1_1_5_4.settings')

import django
#django.setup()

from pineapple.models import Category, Page


CatList,ItemList = readin.readDescription()
ImList = readin.ImageList()

# print ImageList[1].show()
# CAtLsit : category 
# ItemList : items inside category.  

def populate1():
	# 1st loop for category list 
	for x in range (len(ItemList)):
		# create new category with views and likes.
		catergory1 = add_cat(CatList[x-1], 124,34)
		for y in range (len(ItemList[x])):
			#print ImList[x-1][y] , ItemList[x][y]['title']
			if (len(ItemList[x][y]) < 3):
				ItemList[x][y]['description'] = " "
			add_page(cat   = catergory1, 
				 	 title = ItemList[x][y]['title'], 
				 	 des   = ItemList[x][y]['description'], 
				 	 price = float(ItemList[x][y]['price']),
				 	 image = ((ImList[x-1][y]))
				 	 )

def printResult ():
	for c in Category.objects.all():
		for p in Page.objects.filter(category =c):
			print " - {0} - {1}". format(str(c), str(p))

def add_page(cat, title, des, image, price):
    p = Page.objects.get_or_create(category=cat, title=title, image= image)[0]
    p.des=des
    p.price = price
    p.save()
    return p

def add_cat(name, view,likes):
	if (Category.objects.filter(name =name).exists()):
		c=Category.objects.get(name=name)
		 
	c= Category.objects.get_or_create(name= name)[0]
	c.view = view
	c.likes = likes
	c.save()
	return c

if __name__ == '__main__':
	print "Start populating script ..."
	populate1()
	#printResult()




# populate :
# create a .txt file that store all the menu info then read in and parse it.... 
# bettter than hardcode it. 
# break them down to 4 file 
# 1 is appertizer
# 2 is entree
# 3 drinks
# 4 picture ( 3 small file to seperate pics)
# all pics must label from 1 to n for easy reading purposes. 




