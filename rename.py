import os

monthDict={'Jan':'1','Feb':'2','Mar':'3','Apr':'4','May':'5','Jun':'6','Jul':'7','Aug':'8','Sep':'9','Oct':'10','Nov':'11','Dec':'12'}

def filechange(filename):
	global monthDict

	if filename[0:3]=="FAL":
		name=filename[1:]
	elif filename[0:3]=="WIN":
		name=filename

	day = name[21:23]
	try:
		int(day)
		month = name[24:27]
		year = name[30:32]
		date = year+'-'+monthDict[month]+'-'+day
		sub = name[38:]
		newName=date+'_'+sub
	except:
		newName = name[21:]
	return newName


fileNew=[]
fileOld=[]

for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
    	way = os.path.join(dirname, filename)
    	if filename.startswith("FALLSEM20") or filename.startswith("WINSEM20"):
    		try:
	    		newName = filechange(filename)
	    		way = os.path.join(dirname, filename)
	    		os.rename(way,os.path.join(dirname,newName))
	    		fileNew.append(newName)
	    		fileOld.append(filename)
	    	except:
	    		print " FileName Error : "+ filename


for i in range(len(fileOld)):
	print fileOld[i]+" :: File Changed to  :: "+fileNew[i]