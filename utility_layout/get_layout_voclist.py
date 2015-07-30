size_button = 15
inter = size_button / 4

print('interval lenght: ' + str(inter) + '\n')

l = lambda x, addend: (x + addend) / 100

second_button = l(50, inter / 2 + size_button / 2)
third_button = l(50, -(inter / 2) - size_button / 2)
fourth_button = l(third_button * 100, -inter - size_button)
first_button = l(second_button * 100, inter + size_button)

print('First: ' + str(first_button))
print('Second: ' + str(second_button))
print('Third: ' + str(third_button))
print('Fourth: ' + str(fourth_button))
