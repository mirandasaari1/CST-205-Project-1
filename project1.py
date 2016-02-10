#making 9 pictures into objects
myPicture=pickAFile()
print(myPicture)
pic1=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic2=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic3=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic4=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic5=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic6=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic7=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic8=makePicture(myPicture)
myPicture=pickAFile()
print(myPicture)
pic9=makePicture(myPicture)
#list of pictures
pictures=[pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9]
#assigning height of the picture
height=getHeight(pic1)
#assigning width of the picture
width=getWidth(pic1)
#Creating the Empty picture
newpic=makeEmptyPicture(width,height)
#empty lists
colorBlue=[]
colorRed=[]
colorGreen=[]
#Looping through to get the pixels
for x in range(0,width):
  for y in range(0,height):
    for imagenumber in range (0,9):
      pixel=getPixel(pictures[imagenumber],x,y)
      red= getRed(pixel)
      green= getGreen(pixel)
      blue= getBlue(pixel)
      colorRed.append(red)
      colorBlue.append(blue)
      colorGreen.append(green)
    colorRed.sort()
    colorBlue.sort()
    colorGreen.sort()
    medianRed=colorRed[4]
    medianBlue=colorBlue[4]
    medianGreen=colorGreen[4]
    setRed(getPixel(newpic,x,y),medianRed)
    setGreen(getPixel(newpic,x,y),medianGreen)
    setBlue(getPixel(newpic,x,y),medianBlue)
    colorRed=[]
    colorBlue=[]
    colorGreen=[]
#Showing pic without the man
show(newpic)