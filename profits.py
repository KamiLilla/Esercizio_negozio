'''
Implementazione funzione di calcolo del profitto lordo del negozio. Il calcolo avviene leggendo il registro delle vendite (.txt) e sommandone i totali.
    return:
        gross_profit= valore totale del profitto lordo (somma delle vendite)
'''


def gross_profit():
    gross_profit=0
    with open ('total_sales_registry.txt','r') as sales:
        for sale in (sales.readlines()):
            get_total=sale.split('=')
            get_total=get_total[1].split('\n')
            total_sale=float(get_total[0])
            gross_profit+=total_sale
   
    return gross_profit

'''
Implementazione funzione di calcolo del profitto netto del negozio. Il profitto netto è dato da p.lordo-costi totali.
    ARGOMENTI:
        gross= valore profitto lordo
        costs= costo totale
'''


def net_profit(gross,costs):
    net_profit=float(gross-costs)
    print (f'Profitti: lordo= {gross:.2f} netto= {net_profit:.2f}')
           
        