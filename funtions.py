import pandas as pd
import numpy as np
from helperQ3 import *
from config import ID2NAME_NUMPY, HIERARCHY_NUMPY, convert_np_to_df


def find_parent_of_className(className):
    classIDs, indices = get_classID(className = className)

    print(f"There are {len(indices)} classIDs corresponding to the class name {className}")

    for i, classID in enumerate(classIDs):
        parentID = find_parent_by_ID(classID = classID)
        childClassNames = get_className(classID = classID)
        parentClassNames = get_className(classID = parentID)
        print(f'##ID: {classID}\
                \nchild : {classID} --  {childClassNames} \
                \nparent: {parentID} --  {parentClassNames}')
        

def find_ancestor_of_className(className):
    classIDs, indices = get_classID(className = className)
    print(f"There are {len(indices)} classIDs corresponding to the class name {className}\
            Ancestor of each ID is sorted by ascending relation (parent, grandparent,...)")

    for i, classID in enumerate(classIDs):
        print(f'##ID {classID}')
        ancestorIDs = find_ancestor(classID=classID)
        df_ancestor = get_df_from_listID(listID=ancestorIDs)
        print(df_ancestor)

                
def find_siblings_of_className(className):
    classIDs, indices = get_classID(className = className)
    print(f"There are {len(indices)} classIDs corresponding to the class name {className}")
    for i, classID in enumerate(classIDs):
        print(f'##Sibling of ID {classID} -- {className}')
        parentID = find_parent_by_ID(classID = classID)
        siblingIDs = find_child_of_parent(classID = parentID)
        siblingIdxs = np.searchsorted(ID2NAME_NUMPY[:, 0], siblingIDs)
        df_sibling = [ID2NAME_NUMPY[idx] for idx in siblingIdxs]
        df_sibling = convert_np_to_df(df_sibling)
        print(df_sibling)
        
        
def find_classID_from_className(className):
    classIDs, indices = get_classID(className = className)
    print(f"There are {len(indices)} classIDs corresponding to the class name {className}")
    classNames = [ID2NAME_NUMPY[idx] for idx in indices]
    classNames = convert_np_to_df(classNames)
    print(classNames)
           
def find_common_ancestor_of_classes(className1, className2):
    ancestorData1 = []
    ancestorData2 = []
    classIDs1, indices1 = get_classID(className = className1)
    classIDs2, indices2 = get_classID(className = className2)
    for i, classID1 in enumerate(classIDs1):
        ancestorIDs1 = find_ancestor(classID = classID1)
        ancestorData1.append(ancestorIDs1)
    for i, classID2 in enumerate(classIDs2):
        ancestorIDs2 = find_ancestor(classID = classID2)
        ancestorData2.append(ancestorIDs2)
        
    for i,ancestors1 in enumerate(ancestorData1):
        for j,ancestors2 in enumerate(ancestorData2):
            commonAncestor = find_duplicated_elements(ancestors1, ancestors2)
            if commonAncestor != False:
                print(f'{classIDs1[i]} and {classIDs1[j]} have common ancestors:')
                print(commonAncestor)
            else: 
                print('2 classNames have no common ancestor')

# className = 'object'

# find_common_ancestor_of_classes('object', 'target')

