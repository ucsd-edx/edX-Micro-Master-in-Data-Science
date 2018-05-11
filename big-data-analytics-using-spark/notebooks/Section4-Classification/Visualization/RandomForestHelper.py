import re
import sklearn.datasets as datasets
import pandas as pd
import pydotplus
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz


def remove_gini_impurity(graph_val):
    return re.sub(r'gini = (.*)<br/>s', "s", graph_val)

def generate_tree(rf, tree_index=0, height=0, width=0): 
    dot_data = StringIO()
    export_graphviz(rf.estimators_[tree_index], out_file=dot_data, filled=True, rounded=True, special_characters=True)
    graph_val = remove_gini_impurity(dot_data.getvalue())
    graph = pydotplus.graph_from_dot_data(graph_val) 
    print("Decision Tree", tree_index, ": ")
    if height > 0 and width > 0:
        display(Image(graph.create_png(), height=height, width=width))
    else:
        display(Image(graph.create_png()))

def predict_category(rf, sample):
    pred_list = []
    a = np.array([1, 2, 3])
    for child in rf.estimators_:
        pred_list.append(child.predict(sample))
    dtree_pred = np.array(pred_list, dtype=int).T
    final_pred = np.array(rf.predict(sample), dtype=int).reshape(len(sample), 1)
    pred = np.concatenate((dtree_pred, final_pred), axis=1)
    return pred

def generate_html(rf, sample, pred):
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

