import numpy as np
from config import ID2NAME_NUMPY, HIERARCHY_NUMPY, convert_np_to_df


def get_className(dfNumpy = ID2NAME_NUMPY, classID = None):
    """Get name of class from Id of class"""
    
    index = np.where(dfNumpy == classID)
    return dfNumpy[index[0].item()][1]


def get_classID(dfNumpy = ID2NAME_NUMPY, className = None):
    """Get classID from className
    Example: className is 'object', have many IDs contain that className"""
    classNameArray = dfNumpy[:, 1]
    indices = find_indices(classNameArray, className)
    ##remove fail index##
    failIndices = []
    for i,index in enumerate(indices):
        value = dfNumpy[index][1]
        x = value.split(", ")
        if className not in x:
            failIndices.append(i)
        else:
            pass
    indices = np.delete(indices, failIndices)
    classIDs = [dfNumpy[i][0] for i in indices]
    
    return classIDs, indices

def find_indices(array, element):
    """Find indices of element where appearance in array"""
    
    array = array.astype('<U36')
    indices = np.flatnonzero(np.core.defchararray.find(array,element)!=-1)
    return indices
    
def find_parent_by_ID(dfNumpy = HIERARCHY_NUMPY, classID = None):
    """find child's parent by ID of child"""
    
    childClassIDs = dfNumpy[:,1]
    childIdxs = find_indices(childClassIDs, classID)
    parents = [dfNumpy[i][0] for i in childIdxs]
    if len(parents) == 0:
        return False
    else:
        return parents[0]
    
def find_child_of_parent(dfNumpy=HIERARCHY_NUMPY, classID=None):
    """find parent's children by Id of parent"""
    
    parentClassIDs = dfNumpy[:,0]
    indices = find_indices(parentClassIDs, classID)
    childClassIDs = [dfNumpy[i][1] for i in indices]
    return childClassIDs
    
def find_ancestor(dfNumpy=HIERARCHY_NUMPY, classID=None):
    """find IDs of ancestors based on classID"""
    ancestorIDs = []
    parentID = classID
    while True:
        parentID = find_parent_by_ID(classID = parentID)
        if parentID == False:
            break
        else:
            ancestorIDs.append(parentID)
    
    return ancestorIDs

def get_df_from_listID(dfNumpy = ID2NAME_NUMPY, listID = None):
    idxs = np.searchsorted(dfNumpy[:, 0], listID)
    df = [ID2NAME_NUMPY[idx] for idx in idxs]
    return convert_np_to_df(df)

def find_duplicated_elements(arrayA, arrayB):
    commonElements = np.intersect1d(arrayA, arrayB)
    if len(commonElements) != 0:
        return commonElements
    else:
        return False
