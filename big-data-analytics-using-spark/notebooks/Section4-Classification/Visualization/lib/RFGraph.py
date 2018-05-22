import re
import sklearn.datasets as datasets
import pandas as pd
import pydotplus
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
from lib.RandomForestHelper import *
import matplotlib.pyplot as plt

def clean_dotty_data(graph_val):
    '''
    Removes the gini impurity field from the tree to generate a clean graph
    '''
    return re.sub(r'gini = (.*)<br/>s', "s", graph_val)

def generate_tree(rf, tree_index=0, height=0, width=0):
    '''
    Generates a pictorial representation of a decision tree
    '''
    dot_data = StringIO()
    export_graphviz(rf.estimators_[tree_index], out_file=dot_data, filled=True, rounded=True, special_characters=True)
    graph_val = clean_dotty_data(dot_data.getvalue())
    graph = pydotplus.graph_from_dot_data(graph_val) 
    print("Decision Tree", tree_index, ": ")
    if height > 0 and width > 0:
        display(Image(graph.create_png(), height=height, width=width))
    else:
        display(Image(graph.create_png()))

def generate_html(rf, sample, pred):
    '''
    Generates a html table with the predictions of all decision trees for each sample for the given dataset
    '''
    n_estimators = len(rf)
    sample_list = list(sample.index)
    dtree_list = []
    for i in range(n_estimators):
        dtree_list.append("DTree " + str(i))
    dtree_list.append("Prediction")
    pred_df = pd.DataFrame(pred, index=sample_list, columns=dtree_list)
    html = pred_df.to_html()
    html += "<br>Legend: <ul><li>0: Iris setosa</li><li>1: Iris virginica</li><li>2: Iris versicolor</li></ul>"
    return html

def generate_simplex(p1, p2, p3, label, legend=None):
    A = [0, 1, 0.5]
    B = [0, 0, 0.87]
    
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111)
    #Necessary to plot the Axis
    A.append(A[0])
    B.append(B[0])
    plt.plot(A,B)
    
    x_list_0, y_list_0, x_list_1, y_list_1, x_list_2, y_list_2 = get_rf_predictions(p1, p2, p3, label, A, B)
    plt.scatter(x_list_0, y_list_0, c='r')
    plt.scatter(x_list_1, y_list_1, c='g')
    plt.scatter(x_list_2, y_list_2, c='b')
    
    if legend:
        plt.legend(legend)
        
    plt.plot([0.75, 0.5], [0.435, 0.29], 'm:')
    plt.plot([0.25, 0.5], [0.435, 0.29], 'm:')
    plt.plot([0.5, 0.5], [0, 0.29], 'm:')
    
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.2, 1)
    plt.show()
