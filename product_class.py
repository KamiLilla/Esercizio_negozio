from sales_admin import*
from commands_verifier import verify_command
from costs_admin import register_cost


'''
Implementazione classe per la creazione di oggeti di tipo 'Product'. I prodotti li aggiunge l'utente in input grazie alle funzioni 'new_product' e 'add'.

'''
class Product:
   
    def __init__(self,name,qnt,sale_price,cost):
        self.name=name
        self.quantity=qnt
        self.sale_price=sale_price
        self.cost=cost
    
    
    '''
    Aggiunge il prodotto acquisito da input utente all'interno del dizionario contente tutti i prodotti in negozio (magazzino)
        ARGOMENTI:
            product_storage= dizionario contenente tutti i prodotti presenti in magazzino
    '''

    
    def add(self,product_storage):
        if self.name not in product_storage:
            product_storage[self.name]= {'quantità':self.quantity,'prezzo di vendita':self.sale_price,'prezzo di acquisto':self.cost}
        
        else:
            product_storage[self.name]['quantità']+=self.quantity
        
        print( f'AGGIUNTO: {self.quantity} X {self.name}')
       
    
'''
Funzione che permette di acquisite da input utente un prodotto acquistato dal negozio e creare un oggetto di tipo Product. Si registra subito il costo del prodotto all'interno del file 'total_costs_registry.txt'.
    return:
        Product= oggetto appartenente alla classe Product
'''
            
def new_product(product_storage):
    
    name=str(input('Nome del prodotto: '))
   
    check=is_in_storage(product_storage,name)
    
    if check is True:
        try:
            quantity=int(input('Quantità: '))
            while quantity<0:
                print('Inserire quantità valida')
                quantity=int(input('Quantità: '))

        except ValueError as e:
            print(e)
            quantity=int(input('Quantità: '))

            while type(quantity)!= int or quantity<0:
                print('Inserire quantità valida')
                quantity=int(input('Quantità: '))

        cost=product_storage[name]['prezzo di acquisto']  
        sale_price=product_storage[name]['prezzo di vendita']

    else:
        
        try:
            quantity=int(input('Quantità: '))
            while quantity<0:
                print('Inserire quantità valida')
                quantity=int(input('Quantità: '))

        except ValueError as e:
            print(e)
            quantity=int(input('Quantità: '))

            while type(quantity)!= int or quantity<0:
                print('Inserire quantità valida')
                quantity=int(input('Quantità: '))

        try:    
            cost=float(input('Prezzo di acquisto: '))
            while cost<0:
                print('Inserire prezzo di acquisto valido')
                cost=float(input('Prezzo di acquisto: '))
        
        except ValueError as e:
            print(e)
            cost=float(input('Prezzo di acquisto: '))

            while type(cost)!= float or cost<0:
                print('Inserire costo valido')
                cost=float(input('Prezzo di acquisto: '))
        
        try:
            sale_price=float(input('Prezzo di vendita: '))
            while sale_price<0:
                print('Inserire prezzo di vendita valido')
                sale_price=float(input('Prezzo di vendita: '))
            
        except ValueError as e:
            print(e)
            sale_price=float(input('Prezzo di vendita: '))
            while type(sale_price)!= float or sale_price<0:
                print('Inserire prezzo valido')
                sale_price=float(input('Prezzo di vendita: '))
   
    register_cost(name,quantity,cost)
        
    return Product(name,quantity,sale_price,cost)



'''
Funzione di controllo presenza in magazzino del prodotto aggiunto dall'utente
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino
        name= nome del prodotto da cercare
    return:
        boolean True or False

'''
def is_in_storage(product_storage,name):
    storage=list(product_storage.keys())
    if name in storage:
        return True
    
    return False



        
        
        
   
            
    

        
