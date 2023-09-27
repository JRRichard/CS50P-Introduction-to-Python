class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError ("Exceeding jar capacity")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size or n >self.capacity:
            raise ValueError("Not a logical action")
        self.size -= n

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity
    
    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be greater or equal to zero")
        self._capacity = capacity

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size
    @size.setter
    def size(self, size):
        self._size = size

# Test out the implementation of the class
#jar = Jar()
# jar.deposit(4)
# jar.withdraw(2)
#print(jar)