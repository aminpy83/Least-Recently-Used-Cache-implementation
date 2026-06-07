# Custom LRU Cache Decorator in Python

این پروژه یک پیاده‌سازی شخصی از دکوراتور `lru_cache` در تابع **functools**است. هدف این پروژه بهینه‌سازی توابع سنگین و تکراری از طریق کشینگ **LRU (Least Recently Used)** است، به طوری که با پر شدن ظرفیت حافظه cache، قدیمی‌ترین داده‌ها حذف می‌شوند.

---

## Overview
This repository contains a lightweight, custom implementation of the **Least Recently Used (LRU) Cache** decorator in Python from scratch. 

An LRU cache organizes items in order of use, allowing the system to quickly identify and discard the oldest (least recently used) data when the maximum capacity is reached. This implementation leverages `collections.OrderedDict` to maintain the order of execution efficiently with $O(1)$ time complexity for lookups and updates.

## Why Use an LRU Cache?
When dealing with computationally expensive operations (like recursive functions or heavy data processing), calling the same function with the same arguments repeatedly wastes CPU cycles. An LRU Cache solves this by storing the results of previous function calls.

### Without LRU Cache (The Problem)
Consider a recursive function like Fibonacci. Without caching, the function recalculates the same values over and over again, leading to an exponential time complexity of $O(2^n)$.

```python
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Calculation for fib(50) will take several seconds/minutes!
print(fib(50))