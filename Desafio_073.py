# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Fluminense.

times = ("Internacional","Flamengo","Atlético-MG","São Paulo","Fluminense","Grêmio","Palmeiras","Santos","Corinthians","Bragantino","Athletico-PR","Ceará","Atlético-GO","Sport","Fortaleza","Bahia","Vasco","Goiás","Coritiba","Botafogo")
print("=-" * 50)
print(f"Lista de Times: {times}")
print("=-" * 50)
print(f"Os cincos primeiros são: {times[0:5]}")
print("=-" * 50)
print(f"Os últimos quatros são: {times[-4:]}")
print("=-" * 50)
print(f"Os times em ordem alfabética são: {sorted(times)}")
print("=-" * 50)
print(f"O Fluminense está na {times.index('Fluminense')+ 1}ª posição")
print("=-" * 50)