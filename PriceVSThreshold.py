import matplotlib.pyplot as plt
import numpy as np

threshold = range(35)  # Power threshold from 1 kW to 35 kW

#matrix, called prices, of dimension of 25 x 4
prices = np.zeros((35, 4))

prices[0,:] = [np.nan,np.nan,np.nan,np.nan] # 1 kW
prices[1,:] = [np.nan,np.nan,np.nan,np.nan] # 2 kW
prices[2,:] = [np.nan,np.nan,np.nan,np.nan] # 3 kW
prices[3,:] = [np.nan,np.nan,np.nan,np.nan] # 4 kW 
prices[4,:] = [np.nan,np.nan,np.nan,np.nan] # 5 kW
prices[5,:] = [np.nan,np.nan,np.nan,np.nan] # 6 kW
prices[6,:] = [np.nan,np.nan,np.nan,np.nan] # 7 kW
prices[7,:] = [np.nan,np.nan,np.nan,np.nan] # 8 kW
prices[8,:] = [np.nan,np.nan,np.nan,np.nan] # 9 kW
prices[9,:] = [np.nan,np.nan,np.nan,np.nan] # 10 kW
prices[10,:] = [135.186,np.nan,np.nan,np.nan] # 11 kW
prices[11,:] = [111.486,np.nan,66.7757 ,np.nan] # 12 kW
prices[12,:] = [101.785,np.nan,61.4007,np.nan] # 13 kW
prices[13,:] = [90.6215,np.nan,51.0415,np.nan] # 14 kW
prices[14,:] = [83.3167,np.nan,47.5635,np.nan] # 15 kW
prices[15,:] = [76.7737,725.95,45.1911,732.967] # 16 kW
prices[16,:] = [70.7681,701.061,43.6884,715.66] # 17 kW
prices[17,:] = [65.1448,688.594,42.491,709.464] # 18 kW 
prices[18,:] = [59.825,679.977,41.4571,706.771] # 19 kW
prices[19,:] = [54.7428,672.594,40.5322,705.045] # 20 kW
prices[20,:] = [49.7721,665.709,39.692,703.68] # 21 kW
prices[21,:] = [44.9984,659.414,38.9196,702.575] # 22 kW
prices[22,:] = [40.4614,653.484,38.2103,701.583] # 23 kW
prices[23,:] = [36.0458,647.815,37.5509,700.687] # 24 kW
prices[24,:] = [31.7295,642.384,36.9236,699.883] # 25 kW
prices[25,:] = [27.7041,637.134,36.3327,699.137] # 26 kW
prices[26,:] = [23.7943,631.995,35.7846,698.448] # 27 kW
prices[27,:] = [19.9891,627.125,35.2548,697.805] # 28 kW
prices[28,:] = [16.1968,622.388,34.7513,697.195] # 29 kW
prices[29,:] = [12.5764,617.786,34.2837,696.644] # 30 kW
prices[30,:] = [9.07126,613.34,33.8467,696.111] # 31 kW
prices[31,:] = [5.68371,609.053,33.4118,695.593] # 32 kW
prices[32,:] = [2.3517,605.006,32.9783,695.125] # 33 kW
prices[33,:] = [-0.768382,601.109,32.5725,694.684] # 34 kW
prices[34,:] = [-3.78913,597.373,32.2155,694.244] # 35 kW

#plot
plt.plot(threshold, prices[:,0], 'r', label='Scenario 1')
plt.plot(threshold, prices[:,1], 'g', label='Scenario 2')
plt.plot(threshold, prices[:,2], 'b', label='Scenario 3')
plt.plot(threshold, prices[:,3], 'y', label='Scenario 4')
plt.axvline(x=19, color='k', linestyle='--', linewidth=0.5)
plt.axhline(y=59.825, color='k', linestyle='--', linewidth=0.5)
plt.axhline(y=679.977, color='k', linestyle='--', linewidth=0.5)
plt.axhline(y=41.4571, color='k', linestyle='--', linewidth=0.5)
plt.axhline(y=706.771, color='k', linestyle='--', linewidth=0.5)
plt.xlabel('Power Threshold [kW]')
plt.ylabel('Price [CHF]')
plt.title('Total cost objective function, depending on the power threshold')
plt.grid(True)
plt.legend()
plt.savefig('plots/Graph_Cost_VS_Threshold.png', dpi=300, bbox_inches='tight')
plt.show()
