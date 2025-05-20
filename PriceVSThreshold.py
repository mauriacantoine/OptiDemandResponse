import matplotlib.pyplot as plt
import numpy as np

threshold = range(25)


# price_1 = np.zeros(threshold)
# price_2 = range(25) 
# price_3 = range(25) 
# price_4 = range(25)

# for loop to calculate price based on threshold, ruuning the file Project_with_functions.ipynb


#matrix, called prices, of dimension of 25 x 4
prices = np.zeros((25, 4))

prices[16,:] = [86.77691016, 706.98262975, 60.37634397, 729.55481677] # 17 kW
prices[17,:] = [82.29184405, 697.45412274, 59.17889014, 726.16162931] # 18 kW 
prices[18,:] = [78.03119409, 689.81340862, 58.14501651, 723.46163358] # 19 kW
prices[19,:] = [73.90665034, 683.22139036, 57.22013428, 721.73268786] # 20 kW

plt.plot(threshold, prices[:,0], 'r', label='Scenario 1')
plt.plot(threshold, prices[:,1], 'g', label='Scenario 2')
plt.plot(threshold, prices[:,2], 'b', label='Scenario 3')
plt.plot(threshold, prices[:,3], 'y', label='Scenario 4')
plt.xlabel('Threshold [kW]')
plt.ylabel('Price [CHF/kWh]')
plt.title('Price vs Threshold')
plt.legend()
plt.show()