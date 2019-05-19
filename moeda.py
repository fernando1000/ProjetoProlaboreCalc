class Moeda:

    def real_brasil(valor):
        a = '{:,.2f}'.format(float(valor))
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        d = c.replace('v', '.')
        return 'R$' + d
