import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
titanic=sns.load_dataset('titanic')
titanic.head()
sns.jointplot(titanic,'fare','age')
plt.show()
plt.get_fignums()