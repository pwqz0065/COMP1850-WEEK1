# dictionary
'''a: a variable, = assign

'''
a = 3
iasasd = 3
for i in range(5):
    print(i)

#       0     1           2    3   4      5
adw = ['s', 'computer', "cpu", 3, 3.4, "damn"]
# 's' # char, letter
# "computer" # string

print('\n')

val2 = adw[2]
val3 = adw[3]
print(val3) # indexing adw at position 0
max = len(adw)
print(max)

print('\n')

asdad = a == 4 # boolean expression --> evaluation True/False, 
print(asdad)
print('\n')

for k in range(max):
    if k==3:   
        print(adw[k])
    else:
        print("hello")

print('\n')
sihan = {} # dictionary


#          key :  val
sihan1 = {'name': "sihan"}


sihan2 = {'name': "sihan", 'age': 20}


# print name
print(sihan2['name'])
print(sihan2['age'])

# add new key:val to sihan2
sihan['weight'] = 50
print(sihan)

# wrong! adw[6] = "asda"
adw.append("asda")
print(type[adw])
print(adw)
