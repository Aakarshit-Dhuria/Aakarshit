# String Comparison

x = 'India'
print(x == 'India')
print(x == 'india')

# Comparison operator checks from the first letter itself
print('apple'>'one')   # Alphabetically o is greater than a so it is false
print('four'<'ten')
# If first letter is same then it keeps on checking next letters
print('ab'<'az')
print('abcdef'<'abcde')  #As f is greater than nothing,so this is false