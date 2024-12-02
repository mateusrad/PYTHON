met = float(input('Digite a medida em metros:'))

cn = met * 100
mm = met * 1000
dc = met/10
km = met/1000
ec = met/10



print('O valor digitado é:\n{:.2f} metros\n{:.2f} centímetros\n{:.2f} milímetros'
      '\n{:.2f} decametros\n{:.2f} Quilometros\n{:.2f} ectometros'.format(met,cn,mm,dc,km,ec))


