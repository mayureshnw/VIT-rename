import os

monthDict={'Jan':'1','Feb':'2','Mar':'3','Apr':'4','May':'5','Jun':'6','Jul':'7','Aug':'8','Sep':'9','Oct':'10','Nov':'11','Dec':'12'}

def filechange(filename):
	name = filename
	global monthDict
	day = name[22:24]
	month = name[25:28]
	year = name[31:33]
	date = year+'-'+monthDict[month]+'-'+day
	sub = name[39:]
	newName=date+'_'+sub
	return newName

fileNew=[]
fileOld=[]
for filename in os.listdir("."):
	if filename.startswith("FALLSEM2014-15_"):
		fileOld.append(filename)
		newName = filechange(filename)
		os.rename(filename,newName)
		fileNew.append(newName)


for i in range(len(fileOld)):
	print fileOld[i]+" :: File Changed to  :: "+fileNew[i]