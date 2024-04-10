# Swap the keys and values in a Dictionary in Python

my_dict = {
    'bobby': 'first',
    'hadz': 'last',
    'python': 'topic',
}

new_dict = {
    value: key for key, value in my_dict.items()
}

# 👇️ {'first': 'bobby', 'last': 'hadz', 'topic': 'python'}
print(new_dict)