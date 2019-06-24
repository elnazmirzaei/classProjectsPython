import random
import timeit

ti = []
for i in range(0,885):
	ti.append(0)
m=300
for d in range(0,885):
	n=(4000+d*1000)

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
	print stop - start