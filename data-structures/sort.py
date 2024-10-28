# self.freq = dict(sorted(self.freq.items(), key=lambda item: item[1]))
# timepoint in c++
# {key: {timepoint, value}, {freq, value}}

# my_dict = {'a': 3, 'b': 1, 'c': 2}

# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))
# print(sorted_dict)

# other = {'a': {'freq': 11, "time": 11}, 'b': {'freq': 22, "time": 22}, 'c': {'freq': 33, "time": 33}}
# lst = other.items()
# print(lst)
# for key, value in lst:
#     print(key, value)


from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.remove('b'))
# print(q.popleft())
# print(q.popleft())

print("\nQueue after removing elements")
print(q)