class IR:

    def __init__(self, salario):
        self.__salario = salario

    def __get_aliquota(self):
        salario = self.__salario
        if (salario <= 1903.98):
            return 0.000
        elif (salario <= 2826.65):
            return 0.075
        elif (salario <= 3751.05):
            return 0.150
        elif (salario <= 4664.68):
            return 0.225
        else:
            return 0.275

    def __get_deducao(self):
        aliquota = self.__get_aliquota()
        print('aliquota IRPF: {}%'.format(aliquota * 100))
        if (aliquota == 0.075):
            return 142.80
        elif (aliquota == 0.150):
            return 354.80
        elif (aliquota == 0.225):
            return 636.13
        elif (aliquota == 0.275):
            return 869.36
        else:
            return 0

    def calcula(self, inss):
        ir = ((self.__salario - inss) * self.__get_aliquota()) - self.__get_deducao()
        return ir

#Faixa	De	    Até	        Aliquota	Dedução
#1	    0.00	1903.98	    0.00%	    0.00
#2	    1903.99	2826.65	    7.50%	    142.80
#3	    2826.66	3751.05	    15.00%	    354.80
#4	    3751.06	4664.68	    22.50%	    636.13
#5	    4664.69	999999.99	27.50%	    869.36