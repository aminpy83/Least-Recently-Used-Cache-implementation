from collections import OrderedDict


def my_lru_cache(maxsize=3):
    def decorator(func):
        cache = OrderedDict()

        def wrapper(*args):
            # item is already in cache
            if args in cache:
                cache.move_to_end(args)  # behaving as recently used item, so moving to the end
                return cache[args]

            # new item
            result = func(*args)

            # removing LRU if capacity is full
            if len(cache) >= maxsize:
                cache.popitem(last=False)

            # new item
            cache[args] = result
            return result

        return wrapper

    return decorator


'just for test'

@my_lru_cache(maxsize=4)
def fib(n):
    print(f"Calculating fib({n})...")
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Result:", fib(100))

print("---")
