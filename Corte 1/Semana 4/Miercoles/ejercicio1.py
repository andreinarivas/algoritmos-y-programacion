
products = {
      "mobiles": {
          "Apple": [
              {
                  "id": 1,
                  "name": "iPhone 7",
                  "price": 300
              },
              {
                  "id": 2,
                  "name": "iPhone 8",
                  "price": 350
              },
              {
                  "id": 3,
                  "name": "iPhone Xr",
                  "price": 450
              },
              {
                  "id": 4,
                  "name": "iPhone Xs",
                  "price": 460
              },
              {
                  "id": 5,
                  "name": "iPhone 11",
                  "price": 900
              },
              {
                  "id": 6,
                  "name": "iPhone 12",
                  "price": 1100
              },
              {
                  "id": 7,
                  "name": "iPhone 13",
                  "price": 1300
              },
          ],
          "Samsung": [
              {
                  "id": 8,
                  "name": "Samsung Galaxy Beam",
                  "price": 150
              },
              {
                  "id": 9,
                  "name": "Samsung Galaxy S6",
                  "price": 200
              },
              {
                  "id": 10,
                  "name": "Samsung Galaxy S7",
                  "price": 300
              },
          ],
          "Xiaomi": [
              {
                  "id": 11,
                  "name": "Xiaomi Redmi Note 8",
                  "price": 250
              },
              {
                  "id": 12,
                  "name": "Xiaomi Redmi Note 8 Pro",
                  "price": 300
              },
          ]
      },
      "laptops": {
          "DELL": [
              {
                  "id": 13,
                  "name": "Dell Inspiron 15",
                  "price": 600
              },
              {
                  "id": 14,
                  "name": "Dell Latitude 14",
                  "price": 650
              },
          ],
          "MAC": [
              {
                  "id": 15,
                  "name": "MacBook Pro 13",
                  "price": 900
              },
              {
                  "id": 16,
                  "name": "MacBook M1",
                  "price": 1500
              },
          ]
      },
  }

run = 'yes'
purchases={}
purchase_counter=0
add=1
while run == 'yes':
  option=input('\nPlease enter a valid option: \n1. Show inventory \n2. Register purchase \n3.Quit \n>>> ')
  while not option.isnumeric() and not option in ["1","2"]:
    option=input('Invalid Input. \nPlease enter a valid option: \n1. Show inventory \n2. Register purchase \n>>> ')
  option=int(option)
  if option==1:
    option=input('Please enter a valid option: \n1. Mobiles \n2. Laptops \n>>> ')
    while not option.isnumeric() and not option in ["1","2"]:
      option=input('Invalid Input. \nPlease enter a valid option: \n1. Show inventory \n2. Register purchase \n>>> ')
    option=int(option)
    if option == 1:
      option='mobiles'
    if option == 2:
      option='laptops'
    for brands, types in products[option].items():
      print("{}\n".format(brands))
      for x in products[option][brands]:
        for info, data in x.items():
          print('{}: {}'.format(info.capitalize(), data))
        print(' \n')
  if option==2:
    add=1
    new_purchases={'name': "", 'last name':'', "ID": 0,}
    purchase_counter+=1
    purchase_items=[]
    while add==1:
        product_id=input('Please enter the ID of the product you would like to get: \n>>>')
        product_selected=None
        for types, brands in products.items():
            for brand, list_products in brands.items():
                for x in list_products:
                    if x.get('id')==int(product_id):
                        product_selected=x['name']
                        purchase_items.append(product_id)
        add=int(input('Would you like to purchase more items? \n1. yes \n2.no \n>>> '))
    for info in new_purchases.keys():
        new_purchases[info]=input("Please enter the client's {}: \n>>> ".format(info))
    new_purchases['items ID']=purchase_items
    purchases[purchase_counter]=new_purchases
    print('******** RECEIPT *********\n')
    total=0
    for info, data in purchases[purchase_counter].items():
        if info=='items ID':
            for y in purchase_items:
                for types, brands in products.items():
                    for brand, list_products in brands.items():
                        for x in list_products:
                            if x.get('id')==int(y):
                                item=x['name']
                                cost=x['price']
                                total+=cost
                                print ('\n{}            {}'.format(item, cost))
        else:
            print('{}: {}'.format(info.title(),data))
    print('\n TOTAL: {}'.format(total))


  if option==3:
    run='no'  


    
    
  

