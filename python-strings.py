a = 'first line with single quot\'e'
b = "second \\line with double quote"
c = """ third \\line with triple quote"""
d = 12

print (a)
print (b)
print (c)

print (len(a))

print (a + b)

print (a + str(d))

print ((len(a) + len(b))*2)


print (a.upper())

print (a.find('with'))

print (a.replace('with','in'))


car = "{s},{n} and {m}".format(s='audi',m='bmw',n='scoda')
print (car)