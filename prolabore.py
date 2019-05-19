class Prolabore:

    def __init__(self):
        self.__fator_r = 0.28

    def calcula(self, total_nf):
        prolabore = total_nf * self.__fator_r
        return prolabore

    def get_fator_r(self):
        return int(self.__fator_r * 100)