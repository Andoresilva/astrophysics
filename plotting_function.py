import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  Reading the data from csv file and assigning each header value:
#The data used Is no available due to copyright from other author that Used to work with me, the data Is about different photoionization models of planetary nebulae simulated fdrom the Cloudy code.


df_modelos = pd.read_csv("Modelos (5).csv", delimiter=";", header=None, names=["numero", "abund", "n", "L", "Teff", "co_ArII", "flux_ArII", "co_ArIII", "flux_ArIII", "co_Ar5",
                         "flux_Ar5", "co_Ar5_13", "flux_Ar5_13", "co_ne2", "flux_ne2", "co_ne3", "flux_ne3", "co_ne3_36", "flux__ne3_36", "co_ne5", "flux_ne5", "co_ne5_24", "flux_ne5_24"])


#   Creating the function to plot curves for different parameters, the function already calls the plt.plot, so I just need to call the right parameters and run:

def plot_curve(df_modelos, abundancia, densidade, luminosidade, cor, linha, marker):

    curva1 = df_modelos[(df_modelos["abund"] == abundancia)
                        & (df_modelos["n"] == densidade) & (df_modelos["L"] == luminosidade)]

    eixoX = curva1["Teff"]
    n1 = curva1["flux_ne3"]
    n2 = curva1["flux_ne2"]

    tt, aa, nn = zip(*sorted(zip(eixoX, n1, n2)))

    razao1b = []
    npt1b = len(tt)

    for i in range(0, npt1b):
        razao1b.append(10.**aa[i]/10.**nn[i])
        print("==> ", i, tt[i], aa[i], nn[i])

    plt.plot(tt, razao1b, marker=marker, linestyle=linha,
             color=cor)


#  Defining the plot parameters for visual representation
plt.figure(figsize=(15, 12))

abundancia = 'partial'
densidade = [2, 3, 4, 5]
den = ['xkcd:azure', 'xkcd:green', 'xkcd:orange', 'xkcd:red']
#cor = 'xkcd:green'
luminosidade = [2, 3, 4]
lin = ['-.', '-', '--']
marker = ''

# Iterating through the parameters to get the values I want to plot
for i, L in enumerate(luminosidade):
    linha = lin[i]
    for i, D in enumerate(densidade):
        cor = den[i]
        plot_curve(df_modelos, abundancia, D, L, cor, linha, marker)


plt.yscale("log")
# plt.xscale("log")
plt.tick_params(direction='in', which='both', bottom='on',
                top='on', left='on', right='on', length=10)
plt.xticks(size=20)
plt.yticks(size=20)
plt.minorticks_on()
plt.ylim(0.1, 100)
plt.xlim(20, 400)

plt.title("", {'fontsize': 20}, fontweight='bold')
plt.xlabel("Temperatura (10 $^3$K)", {'fontsize': 30}, fontweight='bold')
plt.ylabel("[NeIII]/[NeII]", {'fontsize': 30}, fontweight='bold')

#Plotting the reason between the ionic flux forbidden emission lines [Ne III]/[Ne III]:
outpu = "./N1_N2.png"

plt.savefig(output, dpi=200, pad_inches=0.2, bbox_inches="tight")


## FIGURA 2 ##
plt.close()
plt.figure(figsize=(15, 12))

abundancia2 = 'partial'
densidade2 = [3, 4]
den2 = ['xkcd:green', 'xkcd:orange']
#cor2 = 'xkcd:green'
luminosidade2 = [2, 3, 4]
lin2 = ['-.', '-', '--']
marker2 = ''

for i, L in enumerate(luminosidade2):
    linha2 = lin2[i]
    for i, D in enumerate(densidade2):
        cor2 = den2[i]
        plot_curve(df_modelos, abundancia2, D, L, cor2, linha2, marker2)

abundancia2 = 'S0.2'
densidade2 = [3, 4]
den2 = ['xkcd:green', 'xkcd:orange']
#cor = 'xkcd:green'
luminosidade2 = [2, 3, 4]
lin2 = ['-.', '-', '--']
marker2 = 'o'

for i, L in enumerate(luminosidade2):
    linha2 = lin2[i]
    for i, D in enumerate(densidade2):
        cor2 = den2[i]
        plot_curve(df_modelos, abundancia2, D, L, cor2, linha2, marker2)

abundancia2 = 'S5'
densidade2 = [3, 4]
den2 = ['xkcd:green', 'xkcd:orange']
#cor2 = 'xkcd:green'
luminosidade2 = [2, 3, 4]
lin2 = ['-.', '-', '--']
marker2 = 'v'

for i, L in enumerate(luminosidade2):
    linha2 = lin2[i]
    for i, D in enumerate(densidade2):
        cor2 = den2[i]
        plot_curve(df_modelos, abundancia2, D, L, cor2, linha2, marker2)

plt.yscale("log")
# plt.xscale("log")
plt.tick_params(direction='in', which='both', bottom='on',
                top='on', left='on', right='on', length=10)
plt.xticks(size=20)
plt.yticks(size=20)
plt.minorticks_on()
plt.ylim(0.1, 100)
plt.xlim(20, 400)

plt.title("$f_d & $f_S$", {'fontsize': 20}, fontweight='bold')
plt.xlabel("Temperatura (10 $^3$K)", {'fontsize': 30}, fontweight='bold')
plt.ylabel("[NeIII]$_{15.5 \mu m}$/[NeII]$_{12.8 \mu \mathrm{m}}$",
           {'fontsize': 30}, fontweight='bold')

# Plotting the curves from the solar dust abundance lines and sulfur photoionization lines

output2 = "./solar_vs_sulfur_curves.png"

plt.savefig(output2, dpi=200, pad_inches=0.2, bbox_inches="tight")

plt.close()



