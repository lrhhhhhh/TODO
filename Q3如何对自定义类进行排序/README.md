python3.4以后？对自定义类数组进行排序，需要在自定义类里面重载以下函数：
```
def __lt__(self):           # 严格小于
    pass

def __gt__(self):           # 严格大于
    pass

def __ge__(self):           # 大于等于
    pass

def __le__(self):           # 小于等于
    pass

def __eq__(self):           # 等于
    pass
    
def __ne__(self):
    pass
```

在使用list.sort()或者sorted()时，默认从小到大排序，调用的是__lt__()，所以只需要实现__lt__()就行了

如果需要使用到<=, >=, >, !=这些操作符号时，记得编写对应的函数

ps:我怎么觉得更加麻烦了，还不如一个__cmp__()搞定
