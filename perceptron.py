import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
import random
import randseq as rs



X1=[]
Y1=[]
Z1=[]
X2=[]
Y2=[]
Z2=[]
df = pd.read_csv("3D_Data.csv")
X = list(df['X1'])
Y = list(df['X2'])
Z= list(df['X3'])
label= list(df['Y'])

#data01 = np.random.normal(5,1,size=[50, 3])
#data12 = np.random.normal(50,1,size=[50, 3])



    
X1 = []
Y1 = []
Z1=[]
for i in range(1000):
	
	if label[i]==0:
		X2.append(X[i])
		Y2.append(Y[i])
		Z2.append(Z[i])
		label[i]=-1
	else: 
		X1.append(X[i])
		Y1.append(Y[i])
		Z1.append(Z[i])


	



#print(label)
plt.rcParams["figure.figsize"] = [15.00, 15.50]
plt.rcParams["figure.autolayout"] = False

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

x, y = np.meshgrid(x, y)


fig = plt.figure()

#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111,projection='3d')

""" creating the sactter plot"""

#ax.scatter(X,Y,Z, c='r', marker='o')

def init():
	ax.scatter(0,0,0,c='r',marker='*')
	return ax,

""" the actual perceptron model"""






"""the animation part"""

def updateweights(W,seq,sum,i):
	epsilon=0.01
	alpha=0.001
	count=0
	#print(W)
	#while(sum>epsilon and count<200):
	#Wprev=W.copy()
	value= W[0]+W[1]*X[seq[i]] + W[2]*Y[seq[i]] + W[3]*Z[seq[i]]
	print(value,"and",label[seq[i]])
	count+=1
	if value>0:
		v=1
	else:
		v=-1
	#print("i am in 1",label[seq[i]])
	W[0]+=alpha*(label[seq[i]]-v)
	W[1]+= alpha*(label[seq[i]]-v)*X[seq[i]]
	W[2]+=alpha*(label[seq[i]]-v)*Y[seq[i]]
	W[3]+=alpha*(label[seq[i]]-v)*Z[seq[i]]
	#print("in the loops",W,"  ",count)



	#print(W)
	return [W[0],W[1],W[2],W[3]]


def perceptron(i,seq,sum,weights):
	ax.clear()
	print(i)
	i=i%1000
	#print(weights)
	wprev=weights.copy()

	weights=updateweights(weights,seq,sum,i)
	#print(weights)
	sum=0
	for j in range(len(weights)):
		sum+= (weights[j]-wprev[j])**2
	if sum<0.00001:
		weights=wprev.copy()
	eq=-(weights[1]/weights[3])*x-(weights[2]/weights[3])*y-(weights[0]/weights[3])
	ax.plot_surface(x, y, eq,color='black',alpha=1)
	ax.scatter(X2,Y2,Z2, c='r', marker='o')
	ax.scatter(X1,Y1,Z1, c='g', marker='o')
	return ax,

seq=rs.generateRandom(999)
seq.append(0)
sum=4
weights=np.random.normal(0,1,size=[4,1])#[1,1,1,1]
"""for c in range(201):
	weights.append([1,1,1,1])"""

anim = animation.FuncAnimation(fig,perceptron,fargs=(seq,sum,weights),frames = 2000,init_func = init,interval = 100,repeat=False,blit = True)
#anim.save('perceptron.mp4', writer = 'ffmpeg', fps = 30)		
plt.show()

################################# extra code not needed now #####################################################
