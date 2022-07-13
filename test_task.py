def isEven_v1(value):
    return value / 2 == value // 2


def isEven_v2(value):
    check_tuple  = map(str, tuple(range(0, 10, 2)))
    return str(value)[-1] in check_tuple


# Циклический буффер:

def add_to_buffer(self, num):
    self.mylist.pop(0)
    self.mylist.append(num)



class circularlist(object):
    def __init__(self, size):
        self.index = 0
        self.size = size
        self.data = []

    def append(self, value):
        if len(self.data) == self.size:
            self.data[self.index] = value
        else:
            self.data.append(value)
        self.index = (self.index + 1) % self.size

    def __getitem__(self, key):
        if len(self.data) == self.size:
            return(self.data[(key + self.index) % self.size])
        else:
            return(self._data[key])

    def __str__(self):
        return self.data.__repr__() + ' (' + str(len(self.data))+' items)'


a = circularlist(3)
a.append('first')
a.append('second')
a.append('third')
print(a)
# ['first', 'second', 'third'] (3 items)

a.append('fourth')
print(a)
# ['fourth', 'second', 'third'] (3 items)

# Сортировка хоара, быстрая сортировка относительно других методов(напр. пузырьком)
import random
def sort_v1(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return sort_v1(l_nums) + e_nums + sort_v1(b_nums)