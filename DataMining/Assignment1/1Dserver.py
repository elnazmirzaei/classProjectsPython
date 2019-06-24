import random
import timeit


ma=[300,5000,10000]
m=5000
for ww in range(0,1):
	ti = []
	for i in range(0,11):
		ti.append(0)
	
	for d in range(0,11):
		n=(4000+d*99600*2)

		start = timeit.default_timer()


		cd = []
		for i in range(0,m):
			cd.append(0)


		for q in range(1,m):
			variable = []
			for i in range(0,n+1):
				variable.append(0)

			flag=1
			k=0
			while flag:
				value=random.randint(0,n)
				variable[value]=variable[value]+1
				k=k+1
				if variable[value]==2:
					flag=0

			cd[q]=k



		stop= timeit.default_timer()
		ti[d]=stop - start
		print d
		print stop - start
	########
st1="new1result"
st2=".txt"
st=st1+str(m)+st2
fo = open(st, "wb")
for item in ti:
	fo.write("%s\n" % ti)
fo.close()





#####################################
