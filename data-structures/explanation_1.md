
## Reasoning Behind Decisions:
# step 1: undertand problem
- lru cache
least recently used: if cache is full -> remove least recently used
constructor
get(key: int)
set(key: int, value: int)
--
atribute size
get() if hit(cache hit) return value else return -1 (cache miss)
set() if stack is full -> remove then insert
-> them frequent for each key-value + size of stack

- structure
- test
- complexity
- something need know:
Any, Optional, OrderedDict
python > 3.7 dict is order type
len(dict), type(dict), dict[key], for item in dict.keys(): 1 ,2 ,3
pop(key)/ pop() - last element

# step 2:
- This is a cache, there are methods get(key), set(key, value)
- which atribute needed ?
+ `size` of cache
+ `MAX_SIZE`
+ a `map lru` - save key : value
<!-- + nope: a `map freq` - save key - frequence : because when remove a least recently used element, we must know how many time the element used -->
<!-- // bad idea: because when the frequency change, we need to sort this list again, however there is no time point for it. -->
<!-- nope: if i still want to use this approach so i must use add timepoint and sort the map base on time and frequency, is this work ? -->
<!-- yes: there are another solution, that is i use queue, if get a key then I must change the order -->
-> use deque to save the queue for know which element is latest
-> a `queue`, which let us know which one is oldest

- get(key)
+ if key not existed in `map lru` return -1
+ if found -> increase frequence 1 + move the key to front of queue + return value from lru[key]

- set(key, value)
+ if key existed in map lru -> change value -> move the key to front of queue

+ elif the stack full
    + get the least recently used -> remove it in queue and lru map
    + add new element to `map lru` and `queue`
    + do not increase size

+ else
    + add new element to `map lru` and append key to top of queue
    + increase size of cache

## Time Efficiency:
### get()
best case: O(1)
worst case: O(n) - queue append(), remove()

### set(key, value)
best case: O(1)
worst case: O(n)

## Space Efficiency:
space commplexity: O(n)
