import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

x = [5, 6, 3, 2, 4, 5, 5, 5, 6, 3, 9, 8, 5, 1]
y = [5, 3, 2, 7, 9, 5, 7, 8, 3, 2, 1, 3, 5, 1]
c = [7, 1, 2, 3, 4, 6, 8, 9, 4, 3, 9, 5, 6, 7]
#s = size
#c = green
plt.scatter(x, y, s=100, c=c,cmap='Greens',edgecolors='black',
            linewidths=1, alpha=0.75)


data = pd.read_csv('./data/data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count,likes, c=ratio, cmap='Greens',edgecolors='black',
            linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')
plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')


#cbar = plt.colorbar()
#cbar.set_label('Satisfaction')
plt.tight_layout()
plt.show()
