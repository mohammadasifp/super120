import random

numbers = [10, 20, 30, 40, 50]
letters = ['A', 'B', 'C', 'D', 'E']

print("Random Integer (1-10):", random.randint(1, 10))

print("Random Float (0-1):", random.random())

print("Random Float (5-10):", random.uniform(5, 10))

print("Random Choice:", random.choice(numbers))

print("Random Sample (3 values):", random.sample(numbers, 3))

print("Random Choices (with replacement):", random.choices(numbers, k=5))

random.shuffle(numbers)
print("Shuffled List:", numbers)

print("Random Range:", random.randrange(1, 20, 2))

print("Random Letter:", random.choice(letters))