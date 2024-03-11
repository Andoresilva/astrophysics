
import numpy as np
import matplotlib.pyplot as plt

# lendo o arquivo espectro_exemplo.txt
dados = np.loadtxt("low-res_M_1-37.tbl", float)
# atribuindo à variável x os valores da primeira coluna do arquivo
x = dados[:, 0]
# atribuindo à variável y os valores da segunda coluna do arquivo
y = dados[:, 1]
# atribuindo à variável erro os valores da terceira coluna do arquivo
erro = dados[:, 2]

# Agora vamos plotar o gráfico:

plt.figure(figsize=(15, 12))  # definindo o tamanho da figura a ser criada 8x6?
# comando para plotar x por y com linha fina de cor preta, com barra de erro em vermelho
plt.errorbar(x, y, color="black", linestyle="solid", linewidth=2,
             yerr=erro, ecolor="red", capsize=2)  # fmt='.-',


# ajustando o título do gráfico
plt.title("M 1-37", {'fontsize': 26}, fontweight='bold')
# nomeando o eixo x do gráfico
plt.xlabel("Comprimento de onda ($\mu$m)", {'fontsize': 26}, fontweight='bold')
plt.ylabel("Fluxo [Jy sr$^{-1}$]", {'fontsize': 26},
           fontweight='bold')  # nomeando o eixo y

plt.vlines(x=[6.2, 6.98, 7.5, 7.7, 8.6, 9, 11.3, 12.4, 12.8], ymin=[0.4, 1.4, 0.3, 0.3, 0.2, 0.2, 0.6, 0.6, 5], ymax=[
           1, 2.5, 4, 2, 3, 1, 4, 3, 5.4], colors='black', ls='--', lw=2, label='vline1')

#ax.text(6.6, 0.09, r'[Ar III]', fontsize=15)
plt.annotate('PAH', (6, 1.5), fontsize=24)
plt.annotate('[ArII]', (6.5, 2.6), fontsize=24)
plt.annotate('H 6-3', (7.3, 4.2), fontsize=24)
plt.annotate('PAH', (7.6, 2.2), fontsize=24)
plt.annotate('PAH', (8.4, 3.2), fontsize=24)
plt.annotate('[Ar III]', (8.7, 1.2), fontsize=24)
plt.annotate('PAH', (11.1, 4.2), fontsize=24)
plt.annotate('H 6-7', (11.8, 3.2), fontsize=24)
plt.annotate('[NeII]', (12.5, 5.5), fontsize=24)


plt.tick_params(direction='in', which='both', bottom='on',
                top='on', left='on', right='on')
plt.xticks(size=18)
plt.yticks(size=18)
plt.minorticks_on()


arquivo_de_saida = "./esp_m137_menor.png"

plt.savefig(arquivo_de_saida, dpi=200, pad_inches=0.2, bbox_inches="tight")
