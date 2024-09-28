from collections import Counter
my_dict = {'a':10,'b':20,'c':30,'d':40,'e':50}
a = Counter(my_dict)
high = a.most_common(3)
print("Dictionary with 3 highest values:",high)
