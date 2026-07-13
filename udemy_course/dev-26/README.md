# List comprehension
```python
numbers = [1, 2, 3, 4]
```
A for loop common syntax
```python
new_list = []
for n in numbers:
    new_n = n + 1
    new_list.append(new_n)
```
A list comprehension syntax equivalent to a standard for loop

We say that, inside the brackes, the for loop is in and before that for loop, the code to execute after every iteratino of the for loop.
Then every itereation is going to be appended to to the new_list (n + 1).
```python
new_list = [n + 1 for n in numbers]
```
It works with strings too, we can iterate every char from the string using list comprehension.
The new list will have all the chars from the string
```python
name ="Angela"
new_list = [letter for letter in name]
```

It also works with range type
```python
new_numbers = [number * 2 for number in range(1,5)]
```

## Conditional List Comprehension
We can also add a condition in order to execute the code before the for loop statement.

For example, we iterate through every name, but if name has a specific length, then the code  before the for loop will be executed

In this case it will return a name, and that name will be appended to the new list.
```python
names = ["Alex","Beth","Caroline", "Dave","Eleanor", "Freddie"]
short_list = [name for name in names if len(name) < 5]
uppercase_list = [name.upper() for name in names if len(name) >= 5]
```