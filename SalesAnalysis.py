import os, glob, time

_path     = '/HOMEPATH/data/'
_path_in  = 'in/'
_path_out = 'out/'

def getArchive(_path, _path_in):
    if os.path.isdir(_path + _path_in):
        os.chdir(_path + _path_in)
        for archive in glob.glob("*"):
            return archive

def getSalesData(_archive):
    content_in = open(str(_archive), 'r')

    dictTotalSales = {}
    dictSales      = {}

    sellersQty             = 0
    customersQty           = 0
    mostExpensiveSaleId    = 0
    mostExpensiveTotalSale = 0
    worstSeller            = ''

    for line in content_in:
        lineId = line[0:3]

        # Salesman
        if lineId == '001':
            sellersQty += 1
            lineId, salesmanId, salesmanName, salesmanSalary = line.split('ç')

            dictTotalSales[salesmanName] = 0

        # Customer
        elif lineId == '002':
            customersQty += 1

        # Data Sales
        elif lineId == '003':

            lineId, saleId, itemData, salesmanName = line.split('ç')

            salesmanName = salesmanName.replace('\n','')

            itemData = itemData.replace('[','').replace(']','')
            itemData = itemData.replace(',','\n')
            itemData = itemData.replace('-',',')
            itemData = str(itemData).splitlines()

            totalSale = 0
            for itens in itemData:
                item = str(itens).split(',')

                itemQty   = float(item[1])
                itemPrice = float(item[2])
                totalSale += (itemQty * itemPrice)

            mostExpensiveSaleId    = saleId if totalSale > mostExpensiveTotalSale else mostExpensiveSaleId
            mostExpensiveTotalSale = totalSale if totalSale > mostExpensiveTotalSale else mostExpensiveTotalSale

            dictTotalSales[salesmanName] = (dictTotalSales[salesmanName]+0) + totalSale

            worstSeller = min(dictTotalSales.keys(), key=(lambda k: dictTotalSales[k]))

    dictSales['Qtde Clientes']      = customersQty
    dictSales['Qtde Vendedores']    = sellersQty
    dictSales['Id Venda mais Cara'] = mostExpensiveSaleId
    dictSales['O Pior Vendedor']    = worstSeller

    content_in.close()

    # Save Output Archive - Sales Analysis
    if os.path.isdir(_path + _path_out):
        os.chdir(_path + _path_out)

    content_out = open(str('AnaliseVendas_' + _archive), 'w')

    for item in dictSales.items():
        content_out.write( str(item[0]) + ': ' + str(item[1]) + '\n' )

    content_out.close()

    return True


def main():
    while True:
        archive = getArchive (_path, _path_in)
        if archive != None:
            print ('processing Data Sales - ' + archive)

            # Process Archive
            try:
                if getSalesData (archive):
                    # Remove Archive
                    if os.path.isdir(_path + _path_in):
                        os.chdir(_path + _path_in)

                    if os.path.exists( str(archive) ):
                        os.remove( str(archive) )
            except:
                print ('Unexpected Error')

if __name__ == '__main__':
    main()
