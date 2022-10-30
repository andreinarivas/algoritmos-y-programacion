def is_prime(rif_client):
  is_prime=True
  number=int(rif_client[-1])
  for x in range(2,number+1):
    if x!=number:
      if number%x==0:
        is_prime=False
        break
      else:
        is_prime=True
  return is_prime
    


def main():
  productos_dicc={'Q':{'linea': 'Quimica', 'precio':1000},'B':{'linea': 'Biologica', 'precio':4000}, 'F':{'linea': 'Farmaceutica', 'precio':2500}}
  run="yes"
  clientes_f=0
  clientes_q=0
  clientes_b=0
  decuentos_totales_f=0
  decuentos_totales_q=0
  decuentos_totales_b=0
  compra_mas=0
  rif_max=0
  total=0
  while run=='yes':
    rif_client=input('Por favor ingrese el rif: \n>>> ')
    while not rif_client.isnumeric():
      rif_client=input('Input Invalido. \nPor favor ingrese el rif: \n>>> ')
    linea_selected=input('Por favor ingrese que linea de productos desea adquirir: \n Q. Quimica \n B. Biologica\n F. Farmaceutica\n >>> ').capitalize()
    while not linea_selected in ['Q', 'B', 'F']:
      print('Opcion invalida\n')
      linea_selected=input('Por favor ingrese que linea de productos desea adquirir: \n Q. Quimica \n B. Biologica\n F. Farmaceutica\n >>> ').capitalize()
    metodo_de_pago=input('Por favor ingrese el metodo de pago a utilizar: \n C. Contado \n R. Credito\n >>> ').capitalize()
    while not metodo_de_pago in ['C', 'R']:
      print('Opcion invalida\n')
      metodo_de_pago=input('Por favor ingrese el metodo de pago a utilizar: \n C. Contado \n R. Credito\n >>> ').capitalize()
    monto_bruto=productos_dicc[linea_selected]['precio']
    descuento=0
    impuesto=0
    if metodo_de_pago=='C':
      descuento+=monto_bruto*0.03
    if monto_bruto%2==0:
      descuento+=monto_bruto*0.02
    if is_prime(rif_client):
      descuento+=monto_bruto*0.05
    if linea_selected!='F':
      impuesto+=monto_bruto*0.12
    monto_total=monto_bruto-descuento+impuesto
    print('****** RECIBO ******')
    print('RIF: {}'.format(rif_client))
    print('LINEA: {}'.format(productos_dicc[linea_selected]['linea']))
    print('METODO DE PAGO: {}'.format(metodo_de_pago))
    print('DESCUENTO: {}'.format(descuento))
    print('IMPUESTO: {}'.format(impuesto))
    print('TOTAL: {}'.format(monto_total))
    print('\n\n')

    if linea_selected=='F':
      clientes_f+=1
      decuentos_totales_f+=descuento
    if linea_selected=='Q':
      clientes_q+=1
      decuentos_totales_q+=descuento
    if linea_selected=='B':
      clientes_b+=1
      decuentos_totales_b+=descuento
    if monto_total>compra_mas:
      compra_mas=monto_total
      rif_max=rif_client
    total+=monto_total
    run=input('Quiere seguir ingresando compras? \n grese "yes" o "no" \n>>> ').lower()
    while not run in ['yes', 'no']:
      run=input('INPUT INVALIDO. \n Quiere seguir ingresando compras? \n Ingrese "yes" o "no" \n>>> ').lower()
  
  print('******** FINAL DEL DIA ********')
  print('TOTAL DE CLIENTES DE PRODUCTOS QUIMICOS: \n {}'.format(clientes_q))
  print('TOTAL DE CLIENTES DE PRODUCTOS BIOLOGICOS: \n {}'.format(clientes_b))
  print('TOTAL DE CLIENTES DE PRODUCTOS FARMACEUTICOS: \n {}'.format(clientes_f))
  print('TOTAL DE DESCUENTOS DE PRODUCTOS QUIMICOS: \n {}'.format(decuentos_totales_q))
  print('TOTAL DE DESCUENTOS DE PRODUCTOS BIOLOGICOS: \n {}'.format(decuentos_totales_b))
  print('TOTAL DE DESCUENTOS DE PRODUCTOS FARMACEUTICOS: \n {}'.format(decuentos_totales_f))
  print('COMPRA MAXIMA: \n MONTO: {} \n RIF: {}'.format(compra_mas,rif_max))
  print('TOTAL DE VENTAL DEL DIA: \n {}'.format(total))
  
  

  


  
    
 

main()