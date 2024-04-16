from commands_verifier import verify_command
from help_menu import help_commands
from product_class import *
from sales_admin import*
from profits import*
from storehouse_admin import*
from costs_admin import*


def main():
    user_command=''
    storehouse=get_items()
    while user_command!='chiudi':
        user_command=input('Inserire comando: ')
        check=verify_command(user_command)
        if check is True:
            if user_command=='aiuto':
                help_commands()

            if user_command=='aggiungi':
                item=new_product()
                item.add(storehouse)

            if user_command=='elenca':
                list_products(storehouse)

            if user_command=='vendita':
                sale(storehouse)

            if user_command=='profitti':
                gross_profit= calculate_gross_profit()
                costs=total_costs(storehouse)
                net_profit= calculate_net_profit(gross_profit,costs)

    register_items(storehouse)

    print('Bye bye')

    
    
if __name__ == "__main__":
    main()

