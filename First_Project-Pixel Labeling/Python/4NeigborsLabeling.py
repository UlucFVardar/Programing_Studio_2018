import PIL.Image

# author=__Uluc Furkan Vardar__

def main (): 
	#allows up to open file from directory path
	fp =open ("/Users/uluc/Desktop/Programing_Studio/First Project/Python/reg.png","rb")
	targetImage=PIL.Image.open(fp)

	#load command gives the pixel rgb values 
	pix =targetImage.load()
	# .size gives us width and hight of the image
	rowSize,columnSize=targetImage.size

	## after take this informations we have to vanihs noises from our image
	for i in range(rowSize):
		for j in range(columnSize):
			pix[i,j]=vanishNoisesFromPixel(pix[i,j])
	#Now our image has no noise only black and white

	#if we have a binary matris that 1 is white and 0 is black operations will be easier
	pixelValues=[[ 0 for x in range(columnSize)] for y in range(rowSize)]
	for i in range(rowSize):
		for j in range(columnSize):
			pixelValues[i][j]=converToBinaryValue(pix[i,j])
	#Now we are end up with a binaryValued matrix that has our pixel informations.

	##Now we have to start !!Labeling!!
	'''
		Algorithm:
			if current pixel is white
				look neighbors (up and left(for 4-neighbors Labeling))
				if 2 neighbors is white look their labels
					if their labels are same current pixel label is setted as up neighbors labels
					else (they are white but labes not same)
						set current label one of the neighbors labels 
						and travel all pixel from start to current and chance left neighbors labels as up neighbors labels
				if only one of the neighbor is white  check which one is white up or left
					if left one is white
						set current pixel labels as left neighbors Labels
					else (up one is white)
						set current pixel labels as up neighbors Labels
				else (2 neighbors are black but current is white)
					increase the labelCounter and set the current pixel LabelValue as labelCounter

	'''
	#addition of our algorithm we use up and left pixel cell of current pixel as a prevention we have to draw a frame
	#four edge of the image must be labeled as black (we cant have to paint the orjin image as black)
	for i in range (rowSize):
		for j in range (columnSize):		
			if i == 0 or j == 0 or i == rowSize-1 or j == columnSize-1:
				pixelValues[i][j]=0
	#We made edges as black
	print "\n\n\n\nbefore labeling pixelValues matrix look like"
	for j in range (columnSize):		
		for i in range (rowSize):
			print pixelValues[i][j],
		print ""

	#creation of labelValues matrix
	labelValues=[[ 0 for x in range (columnSize)] for y in range(rowSize)]
	for i in range (rowSize):
		for j in range (columnSize):
			labelValues[i][j]=0
	#emty labelValues are '0' for this ex.

	#to dont take exception we travel 1 to limit-1 (actually limit is okey but to make symmetrical it's okey)
	#show the steps from algorithm!
	labelCounter=2 #labels start from 2 
	for i in range (1,rowSize-1):
		for j in range (1,columnSize-1):
			if pixelValues[i][j]==1: #current is White
				if pixelValues[i-1][j]==1 and pixelValues[i][j-1]==1:
					if labelValues[i-1][j]==LabelValue[i][j-1]:
						labelValues[i][j]=labelValues[i][j-1]
					else:
						labelValues[i][j]=labelValues[i-1][j]
						for t in range(0,i+1):
							for k in range (0,j+1):
								if labelValues[t][k]==labelValues[i][j-1]:
									labelValues[t][k]=labelValues[i-1][j]
				elif  pixelValues[i-1][j]==1 or pixelValues[i][j-1]==1:
					if pixelValues[i-1][j]==1:
						labelValues[i][j]=labelValues[i-1][j]
					else:
						labelValues[i][j]=labelValues[i][j-1]
				else:##current is white but neighbors are black
					labelValues[i][j]=labelCounter
					labelCounter+=1
			else:
				labelValues[i][j]=1#means blacks labels is one

	#labeling is over 
	print"************"
	print"After labeling what labelValues matrix looks like"
	for j in range (columnSize):		
		for i in range (rowSize):
			print labelValues[i][j],
		print ""
	
#********
def converToBinaryValue(rgbValues):
	if len (rgbValues)==4:
		r,g,b,f=rgbValues
	else:
		r,g,b=rgbValues
	average=(r+g+b)/3
	if average==255 :
		return 1 #means white
	return 0  #means black 
def vanishNoisesFromPixel( rgbValues ):
	#some pictures has another information that's the blur affect r,g,b,and F
	#but we are interested in only R,G,B values to clean noise
	if len (rgbValues)==4:
		r,g,b,f=rgbValues
	else:
		r,g,b=rgbValues
	average=(r+g+b)/3
	if average>200:
		return 255,255,255
	return 0,0,0



if __name__=='__main__':
    main()

