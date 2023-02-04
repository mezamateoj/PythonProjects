# functions with outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title() 
    formated_l_name = l_name.title()
    return f'{formated_f_name}, {formated_l_name}'


my_name = format_name('mateo', 'meza')
print(my_name)

## multiple return values
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name"""
    formated_f_name = f_name.title() 
    formated_l_name = l_name.title()
    if formated_l_name == '':
        return 'Thast not right'
    return f'{formated_f_name}, {formated_l_name}'


#print(format_name(input('What is your first name: '), input('what is your last name: ')))

format_name()



