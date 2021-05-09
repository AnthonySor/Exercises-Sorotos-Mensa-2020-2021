#try:
#    x=int(input('Gimme a number'))
#    if (x > 100):
#        raise NameError("Value over 100")
#    x=x+10
#    print(x)
#except ValueError:
#    print('You didnt give me an interger')
#except NameError:
#    print('Value over 100')
#except:
#    print('Oops, something went terribly wrong')

#try:
#    Firstnumber = int(input('I am the divisionizer, what number do you want to be the numerator?'))
#    if(Firstnumber == 0):
#        raise NameError ('You didnt give me an interger')
#    Secondnumber = int(input('Denomerator?'))
#    if(Secondnumber == 0):
#        raise NameError ('You didnt give me an interger')
#    print(Firstnumber / Secondnumber)
#except NameError:
#    print('Not an interger')