class MergeSort:
    @classmethod
    def merge(cls, l, lo, hi):
        aux = l[lo:hi]
        mid = len(aux)//2 - 1
        i,j = 0, mid+1
        for k in xrange(lo,hi):
            if i > mid: 
                l[k] = aux[j]
                j+=1
            elif j >= hi:
                l[k] = aux[i]
                i+=1
            elif aux[j] < aux[i]:
                l[k] = aux[j]
                j+=1
            else:
                l[k] = aux[i]
                i+=1

    @classmethod
    def sort(cls, l):
        if len(l) <= 1: return l
        mid   = len(l) // 2
        left  = l[0:mid]
        right = l[mid:len(l)]
        l = cls.sort(left) + cls.sort(right)
        cls.merge(l, 0, len(l))
        return l


class QuickSort:
    @classmethod
    def partition(cls, l):

        if len(l) == 0: raise IndexError()
        if len(l) == 1: return 0

        lo, hi, pivot = 0, len(l)-1, l[0]
        i, j = lo+1, hi

        while True:
            while l[i] < pivot:
                if i == hi: break
                i += 1
            while l[j] >= pivot:
                if j == lo: break
                j -= 1 
            if i >= j: break
            l[i], l[j] = l[j], l[i]
            
        l[lo], l[j] = l[j], l[lo]
        return j

    @classmethod
    def sort(cls, l):
        if len(l) <= 1: return l
        index = cls.partition(l)
        return cls.sort(l[:index]) + [l[index]] + cls.sort(l[index+1:])
