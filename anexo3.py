class Anexo3:

    def aplica_imposto(total_nf):
        anexo_iii = total_nf * 0.06
        return anexo_iii

    def calcula_desconto_total(imposto_anexo_iii, inss, ir):
        tot_anexo_iii = imposto_anexo_iii + inss + ir
        return tot_anexo_iii