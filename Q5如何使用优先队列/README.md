PriorityQueue是线程安全的

使用headpq会比较轻量级一些

headpq.heappush()传入一个list和一个item，把这个list当成堆，
动态维护这个堆(list)

headpq.headpop()返回并删除堆里的最小值

headpq.heapify()接受一个list，并将这个list维护成一个堆

headpq还有很实用的nlargest()和nsmallest(),即返回堆中最大的n个和最小的n个节点

