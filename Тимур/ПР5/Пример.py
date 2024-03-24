import matplotlib.pyplot as plt

# #1
# plt.plot([1,2,3],[1,4,9],'g.-')
# plt.show()

# #2
# plt.bar(["2012","2013","2014"],[15,10,1],width = 0.4, color = 'green', edgecolor = 'black')
# plt.xlabel('Год')
# plt.ylabel('Количество')
# plt.legend()
# plt.show()

# # 3
# width = 0.4
# plt.bar([x-width/2 for x in range(3)],[15,10,1], width, color = 'green',
# edgecolor = 'black')
# plt.bar([x+width/2 for x in range(3)],[1,8,1], width, color = 'red',
# edgecolor = 'black')
# plt.xticks([x for x in range(3)],["2012","2013","2014"])
# plt.xlabel('Год')
# plt.ylabel('Количество')
# plt.legend()
# plt.show()

# # 4
# plt.pie([15,10,1],labels=["2012","2013","2014"])
# plt.show()

