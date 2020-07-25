import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

## data = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx')
## print(data)

time = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['Time'])
data_x = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Position'])
data_y = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['Y Position'])
data_z = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['Z Position'])
data_x_vel = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Velocity'])
data_y_vel = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Velocity'])
data_z_vel = pd.read_excel(r'E:\Python Work\iss_data_90minutes.xlsx', usecols=['X Velocity'])

print(time)
print('--------------------')
print(data_x)
print('--------------------')
print(data_y)
print('--------------------')
print(data_z)
print('--------------------')
print(data_x_vel)
print('--------------------')
print(data_y_vel)
print('--------------------')
print(data_z_vel)
print('--------------------')

plt.plot([1, 3, 6, 9],[5,10,15,20])
plt.ylabel('X Position')
plt.xlabel('Time')
plt.show()