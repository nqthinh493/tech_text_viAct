from funtions import find_ancestor_of_className, find_parent_of_className, find_siblings_of_className, find_common_ancestor_of_classes


def function_switcher(function_code):
    if function_code == '1':
        className = input('Please enter className \
            \nEx: target, object, plane...\
            \nclassName: ')
        find_siblings_of_className(className=className)
    elif function_code == '2':
        className = input('Please enter className \
            \nEx: target, object, plane...\
            \nclassName: ')
        find_parent_of_className(className=className)
    elif function_code == '3':
        className = input('Please enter className \
            \nEx: target, object, plane...\
            \nclassName: ')
        find_ancestor_of_className(className=className)
    elif function_code == '4':
        className1 = input('Please enter 2 className to find common ancestor\
            \nEx: target, object, plane...\
            \nclassName1: ')
        className2 = input('className2: ')
        print('Processing...')
        find_common_ancestor_of_classes(className1, className2)
    else:
        print("Please enter function code [1, 2, 3, 4]")


if __name__ == "__main__":
    print('Choose function code\
            \n1: find_siblings_of_className\
            \n2: find_parent_of_className\
            \n3: find_ancestor_of_className\
            \n4: find_common_ancestor_of_classes')

    function_code = input()
    function_switcher(function_code)


