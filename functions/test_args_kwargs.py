print('--------------------Test *ARGS---------------------------------------')

print('--------------------Test *KWARGS---------------------------------------')

def display_data(**my_details):
    print(my_details)

def display_data_with_parameters(company='Dont Share', **my_details):
    print(company,' AND ', my_details)

my_details = {'name': 'Shalini', 'age':27}
display_data(**my_details)
display_data_with_parameters(**my_details)
display_data_with_parameters(company = 'Planview', **my_details)

my_complete_details = {'name': 'shalini', 'age': 28, 'company': 'Planview'}
display_data_with_parameters(**my_complete_details)


# display_data('vfv')
print('---------------------------------------------------------------------')
