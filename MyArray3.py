class MyArray3:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def remove(self,index):
        # 判断下标是否超出范围
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        # 从左到右，逐个元素向左挪动一位
        for i in range(index,self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def insert(self, index, element):
        # 判断下标是否超出范围
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        # 从右向左循环，逐个元素向右挪一位
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]
        # 腾出的位置加入新元素
        self.array[index] = element
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])

array = MyArray3(4)
array.insert(0,10)
array.insert(0,11)
array.insert(0,15)
array.remove(1)
array.output()
