import random
def graph(x,y): #Создаём двумерный массив, заполненный гулями
    a = [[0] * x for _ in range(y)]
    return a

def ggraph(n,xn,yn):
	m = 1
	b = graph(xn, yn)
	x0 = 0
	y0 = 0
	iteration=0
	while m < n+1:
		x = random.randint(0, xn-1)
		y = random.randint(0, yn-1)
		if not((abs(x-x0) == abs(y-y0) and abs(y-y0) != 1)or (y == y0 and abs(x-x0) != 1) or (x == x0 and abs(y-y0) != 1)) and (b[y][x] == 0) or (m == 1):
			b[y][x] = m
			x0 = x
			y0 = y
			m += 1

		else:
			iteration+=1	
			if iteration>xn*yn*n:
				h=ggraph(n,xn,yn)
				return h
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