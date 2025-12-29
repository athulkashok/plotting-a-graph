import matplotlib.pyplot as plt
# A very basic graph
#x=[2,4,6,8]
#y=[1,2,3,4]
#plt.plot(x,y)
#plt.show()

# A complex graph

x=[3,9,14]
y=[2,7,11]
plt.plot(x,y, c="red", linewidth=2, label="Line 1" )

#line 2 plots
x2=[1,15,14]
y2=[0,3,12]
plt.plot(x2,y2,c="green", linewidth=2, label="Line 2", linestyle="dashed", marker="o")
#labelling the axis and give the title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("2 line graph")
#Limits of the axis
plt.xlim(1,10)
plt.ylim(0,10)
# Show the legend on the plot
plt.legend()
plt.show()