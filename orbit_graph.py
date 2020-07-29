import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## data = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx')
## print(data)

# Thanks to Daniel I found out I don't need to call the same file each time, instead use a function that already calls the worksheet, and grab data a lot easier from there.
"""""
time = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['Time'])
data_x = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Position'])
data_y = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['Y Position'])
data_z = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['Z Position'])
data_x_vel = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Velocity'])
data_y_vel = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Velocity'])
data_z_vel = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Velocity'])
"""

grab_data = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', 'Sheet1')
print (grab_data)

time = grab_data['Time']
data_x = grab_data['X Position']
data_y = grab_data['Y Position']
data_z = grab_data['Z Position']

print(time)
print('--------------------')
print(data_x)
print('--------------------')
print(data_y)
print('--------------------')
print(data_z)
print('--------------------')

threeD = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot(data_x,data_y,data_z)
plt.show()

"""
x_graph = plt.figure()
plt.plot(time, data_x, label='Position Vs Time (X-Position)')
plt.xlabel('Time')
plt.ylabel('X Position')
plt.title('Position vs Time')
plt.show()

y_graph = plt.figure()
plt.plot(time, data_y, label='Position Vs Time (Y-Position)')
plt.xlabel('Time')
plt.ylabel('Y Position')
plt.title('Position vs Time')
plt.show()

z_graph = plt.figure()
plt.plot(time, data_z, label='Position Vs Time (Z-Position)')
plt.xlabel('Time')
plt.ylabel('Z Position')
plt.title('Position vs Time')
plt.show()
"""