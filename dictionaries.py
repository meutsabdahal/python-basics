# creating dictionary
day_conversion = {
    'Sun': 'Sunday',
    'Mon': 'Monday',
    'Tue': 'Tuesday',
    'Wed': 'Wednesday',
    'Thu': 'Thursday',
    'Fri': 'Friday',
    'Sat': 'Saturday'
}

# accessing a specific value through different ways
print(day_conversion['Mon'])
print(day_conversion.get('Jan', 'Invalid Key'))
