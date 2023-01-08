import random

def graph(x,y):
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



