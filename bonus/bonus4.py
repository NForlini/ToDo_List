filenames = ["1.text.txt", "2.phones.txt", "3.accounts.txt"]

for filename in filenames:
    filename=filename.replace('.','-',1)
    print(filename)

#you cannot change a str but you CAN use.replace to replace the old str with a new str
#and that new str is the character you want changed.
#__old is the chara you wanna change
#__new is the new chara you wanna change it to
#__count is how many instances change of that. in this case 1 means only the first one.


#list = ['this','is','a','list'] - mutable (CAN be modified) has append
#tuple = ('this','is','a','tuple') - immutable (CANNOT be modified) NO append
