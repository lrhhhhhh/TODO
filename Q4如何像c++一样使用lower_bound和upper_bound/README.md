bisect_left和bisect_right是内置bisect包里的函数，使用时需要保证查找的list已经排序
```python

def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
```

bisect_left()找到与target相等的的最左边的那个节点，若没有和target相等的节点的下标，则返回小于target的第一个节点的下标

bisect_right()返回大于target的第一个节点的下标，当target为最后一个节点时或所有节点都比target小时，返回len(list)