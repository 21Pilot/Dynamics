# Flora Seo 
# Set up 
import matplotlib.pyplot as plt
#declairing variables 
scale=1
forscale=4/scale
# make arrays of size of for loop bc i dont understand the expand function of arrays
e1=[0]*10
e2=[0]*10
v1=[0]*10
v2=[0]*10
# assigning x,y, and velocity values in for loop
for t in range(10):
    e1[t]= .05*t
    e2[t] = (-4.91*t*t+30*t+100)
    v1[t]=.05
    v2[t] = (-9.82*t+30)
    if t<3:
  plt.quiver(e1[t], e2[t], v1[t], v2[t], angles='xy',scale_units='xy', scale=1, color='green')
    # printing x,y values if n
    if t==0 or t==1.0 or t==2.0 or t==3.0 or t==4.0:
        print('At t=' +str(t)+' (e1,e2): '+'('+str(e1[t])+','+str(e2[t])+')')
    

plt.quiver(e1[3], e2[3], v1[3], v2[3], angles='xy',scale_units='xy', scale=1, color='green', label='Velocity')

# plotting the points  
#setting x and y axis limits
plt.xlim(0, 0.35) 
plt.ylim(80, 155)

# naming the x axis 
plt.xlabel('e1i - axis') 
# naming the y axis 
plt.ylabel('e2i - axis') 
  
# giving a title to my graph 
plt.title('Position graph') 
plt.plot(e1,e2, color='red', label='Position')
plt.legend(loc='upper-left')
# function to show the plot 
plt.show() 
