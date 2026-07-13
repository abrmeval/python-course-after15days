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
# Dictionary comprehension

```python
names = ["Alex","Beth","Caroline", "Dave","Eleanor", "Freddie"]
```
We can create a new dictionary from a list using Dictionary comprehension syntax.

For example, we say that the key for this dictionary will be the name of the name list, the value will be a random number, then we iterate every name from the list.

Syntax is similar as List comprehension.
```python
import random
students_scores = {name:random.randint(60, 100) for name in names}
```
We can also extend this by adding a condition.
Here we are creating a new dictionary from the previous one, but only adding the students that score is greater than or equals to 60.
The items method returns a key-value pair list
```python
passed_students = {name:score for (name, score) in students_scores.items() if score >= 60}
```
