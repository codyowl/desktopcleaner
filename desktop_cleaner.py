import os
from os import path

path = os.getcwd()

folders_list = [x[0] for x in os.walk(path)]

delete_folder = [i for i in folders_list if not os.listdir(i)]

for folders in delete_folder:
	print "Removing folders :%s" %(folders)
	os.rmdir(folders)
