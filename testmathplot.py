import matplotlib.pyplot as plt
import numpy as np
  
# x axis values
x = np.array([0,1,2,3,4,5,6,7,8,9,10])
# corresponding y axis values
y = np.array([0,1.006,2.012,3.018,4.024,5.030,6.036,7.042,8.048,9.054,10.60])
  
# plotting the points 
plt.plot(x, y,'o:r')
plt.title('R = 1kΩ')
# naming the x axis
plt.xlabel('V(v)')
# naming the y axis
plt.ylabel('I(A)')
  
# giving a title to my graph
  
# function to show the plot
plt.show()