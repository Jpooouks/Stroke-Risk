import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_custom_scatter(data, x, y, hue_column, class_0_alpha=0.3,
                        class_1_alpha=0.8, class_0_color='blue', class_1_color='red'):
    
    sns.scatterplot(data=data[data[hue_column] == 0], 
                    x=x, y=y, 
                    color=class_0_color, alpha=class_0_alpha, label='Class 0')

    sns.scatterplot(data=data[data[hue_column] == 1], 
                    x=x, y=y, 
                    color=class_1_color, alpha=class_1_alpha, label='Class 1')

    plt.title(f'Scatterplot of {x} vs. {y}, Highlighting {hue_column}')
    plt.legend()
    plt.show()
