class INSS:

    def __init__(self, salario):
        self.__salario = salario

    def calcula(self):
        print('aliquota INSS: {}%'.format(self.__get_aliquota() * 100))
        return self.__salario * self.__get_aliquota()

    def __get_aliquota(self):
        if (self.__salario <= 1751.81):
            return 0.08
        elif (self.__salario <= 2919.72):
            return 0.09
        else:
            return 0.11

#Faixa	De	    Até	    Aliquota
#1	    000	    1751.81	8.00%
#2	    1751.82	2919.72	9.00%
#3	    2919.73	5839.45	11.00%
