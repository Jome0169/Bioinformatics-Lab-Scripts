import os 


 
List = [Dog1, Dog2]
New_things = []

for item in List:
	for Letter in item:
		New_things.append(Letter[0:2])

print New_things


#os.system(" cat {} {} > {}").format()
