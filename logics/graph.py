import random,time
def graph(x,y): #Создаём двумерный массив, заполненный гулями
    a = []
    for i in range(y):
        a.append([])
        for j in range(x):
            a[i].append(0)
    return a

def ggraph(n,xn,yn):
	m = 0
	b = graph(xn, yn)
	av = [[-1,-1]]
	masx = [i for i in range(0,xn)]
	masy = [i for i in range(0,yn)]
	timing = time.time()
	while m < n+1:
		x = random.randint(0, xn-1)
		y = random.randint(0, yn-1)
		x0 = av[len(av)-1][0]
		y0 = av[len(av)-1][1]
		a = [x0,y0,x,y]
		if not((abs(x-x0)==abs(y-y0) and abs(y-y0)!=1)or (y==y0 and abs(x-x0)!=1) or (x==x0 and abs(y-y0)!=1)) and x0 in masx and y0 in masy and x in masx and y in masy and (b[y][x] == 0) or (x0==-1 and y0==-1):
			b[y][x] = m
			av.append([x,y])
			m += 1
	
		if time.time() - timing > 0.06:
			b = None
			break
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