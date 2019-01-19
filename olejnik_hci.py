import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag


t = np.linspace (0, 37.97, 200*38.02)
probkowanie=200
dane = pd.read_csv(r"sub01_trial03.csv", delimiter=',', engine='python')
sygnal=dane["kolumna2"]

przefiltrowany = ag.pasmowozaporowy(sygnal, probkowanie, 49,51)
przefiltrowany2 = ag.pasmowoprzepustowy(przefiltrowany, probkowanie, 1,50)

plt.plot(t, przefiltrowany2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
