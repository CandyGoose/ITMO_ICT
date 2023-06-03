def get_multiplier(unit):
    if unit == 'mm':
        return 10**-3
    if unit == 'cm':
        return 10**-2
    if unit == 'dm':
        return 10**-1
    if unit == 'm':
        return 1
    if unit == 'km':
        return 10**3
    raise ValueError('Undefined unit: {}'.format(unit))
k = 14
un = 'cm'
rez = k * get_multiplier(un)
print(rez)
