import random
import numpy
def graph(x,y): #Создаём двумерный массив, заполненный гулями
    a = []
    for i in range(y):
        a.append([])
        for j in range(x):
            a[i].append(0)
    return a

def ggraph(n,xn,yn):
	m = 1
	xym = [xn,yn]
	b = graph(xn, yn)
	av = [[-1,-1]]
	try:
		masx = [i for i in range(2,xn)]
		masy = [i for i in range(2,yn)]
	except:
		masx = [1]
		masy = [1]
	while m < n+1:
		x = random.randint(0, xn-1)
		y = random.randint(0, yn-1)
		x0 = av[len(av)-1][0]
		y0 = av[len(av)-1][1]
		a = [x0,y0,x,y]
		if (b[y][x] == 0) and (((abs(a[0]-a[2])==1 and (abs(a[1]-a[3]) in masy) ) or (abs(a[1]-a[3])==1 and abs(a[0]-a[2]) in masx)) or ((a[0] == a[2] or a[0]+1 == a[2] or a[0]-1 == a[2]) and (a[1] == a[3] or a[1]+1 == a[3] or a[1]-1 == a[3])) )or (x0==-1 and y0==-1):
			b[y][x] = m
			av.append([x,y])
			m += 1
			
		else:
			continue
			
	
	return b


def find(matrix, value):
	value_indexs = [ ( matrix.index(row), row.index(value) ) for row in matrix if value in row]
	return value_indexs
def anonim(n,xn,yn,a,resx,resy):

	

	
	Xcoordinates=[]
	Ycoordinates=[]
	Xnull_coordinates=[]
	Ynull_coordinates=[]

	for i in range(1,n+1):
		f=find(a, i)
		if f!=[]:
			index=f[0]
			indeY=index[0]
			indeX=index[1]
			Xcoordinate=int(resx/(xn+1)*(indeX+1))
			Ycoordinate=int(resy/(yn+1)*(indeY+1))
			Xcoordinates.append(Xcoordinate)	
			Ycoordinates.append(Ycoordinate)
	
	ups=[]
	for k in range(xn):
		Xnull_coordinate=int(resx/(xn+1)*(k+1))
		ups.append(Xnull_coordinate)
	for u in range(yn):
		Xnull_coordinates+=ups
	for u in range(yn):
		Ynull_coordinate=int(resy/(yn+1)*(u+1))
		Ynull_coordinates.append(Ynull_coordinate)

	return(Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates)
print(len(ggraph(4, 4, 3)))