
valor_hora = 99.8
qtd_horas = 10
total_nf = qtd_horas * valor_hora
fator_r = 0.28
prolabore = total_nf * fator_r
anexo_v = total_nf * 0.155
anexo_iii = total_nf *0.06
inss = prolabore * 0.11
ir = ((prolabore - inss) * 0.075)-142.80
tot_anexo_iii = anexo_iii + inss + ir

print('Receita   R${}'.format(total_nf))
print('Prolabore R${}'.format(prolabore))
print('Fator R   {}%'.format(fator_r))
print('Anexo III R${}'.format(anexo_iii))
print('INSS      R${}'.format(inss))
print('IR        R${}\n'.format(ir))

print('III R${}'.format(tot_anexo_iii))
print('V   R${}'.format(anexo_v))
print('dif R${}'.format(anexo_v-tot_anexo_iii))
print('----')
