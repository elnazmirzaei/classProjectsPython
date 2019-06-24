ma=[300,5000,10000]
for m in ma:
	print('hi')
	st1="result"
	st2=".txt"
	d=5
	st=st1+str(m)+st2
	print st
	cd=[1,2,3,4,5]

	fo = open(st, "wb")
	for item in cd:
	  fo.write("%s\n" % cd)


#Q1
cd=[9.205461025238037, 101.988116979599, 209.9898488521576, 317.99421787261963, 424.3412389755249, 542.182553768158, 653.6534531116486, 770.7186529636383, 887.711963891983, 1031.2933731079102, 1130.9600219726562]

x=[]
for d in range(0,11):
		x.append(4000+d*99600)

import matplotlib.pyplot as plt

plt.plot(x,cd)
plt.ylabel('Time')
plt.xlabel('n')
plt.show()