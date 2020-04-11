import covid19
a=covid19.get_active()
c=covid19.get_cured()
d=covid19.get_death()
m=covid19.get_migrated()
total=a+c+d+m
print(total)
