from inss import INSS
from ir import IR
from moeda import Moeda
from anexo3 import Anexo3
from anexo5 import Anexo5
from prolabore import Prolabore
from nota_fiscal import Nota_fiscal

valor_hora = int(input('Informe seu valor hora: '))
qtd_horas = int(input('Informe a quantidade de horas trabalhadas: '))

total_nf = Nota_fiscal.calcula_valor(qtd_horas, valor_hora)
prolabore = Prolabore().calcula(total_nf)
anexo_v = Anexo5.aplica_imposto(total_nf)
imposto_anexo_iii = Anexo3.aplica_imposto(total_nf)
inss = INSS(prolabore).calcula()
ir = IR(prolabore).calcula(inss)
tot_anexo_iii = Anexo3.calcula_desconto_total(imposto_anexo_iii, inss, ir)

print('')
print('Receita           {}'.format(Moeda.real_brasil(total_nf)))
print('Fator R           {}%'.format(Prolabore().get_fator_r()))
print('Prolabore         {}'.format(Moeda.real_brasil(prolabore)))
print('')
print('Desconto AnexoIII {}'.format(Moeda.real_brasil(imposto_anexo_iii)))
print('Desconto INSS     {}'.format(Moeda.real_brasil(inss)))
print('Desconto IRPF     {}'.format(Moeda.real_brasil(ir)))
print('')
print('Total Desconto Anexo III {}'.format(Moeda.real_brasil(tot_anexo_iii)))
print('Total Desconto Anexo V   {}'.format(Moeda.real_brasil(anexo_v)))
print('Diferença {}'.format(Moeda.real_brasil(anexo_v-tot_anexo_iii)))
print('----------------')
