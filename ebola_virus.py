# Import the modules
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from ebola_data import dates, infection_data
import math

# Define the SEIR model
def seir_model(t, y, beta, gamma, sigma):
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]


# Parameters; we will have to determine them later on
beta = 0.0001 # Exposure Rate
sigma = 0.01 # Infection Rate
gamma = 0.003 # Recovery Rate

S0 = 7140000 - 3000# Average population of the three countries - those who were infected
E0 = 1000
I0 = 2000
R0 = 0

t = np.linspace(0, 597, 597) # Time that one will study the graph

# Stocking the solutions of the different differential equations into a value
sol = solve_ivp(seir_model, [0, 597], [S0, E0, I0, R0], args = (beta, gamma, sigma), t_eval = t)    

print(sol.y[0])

plt.plot(sol.t, sol.y[0], "b", label = "Susceptible")
plt.plot(sol.t, sol.y[1], "y", label = "Exposed")
plt.plot(sol.t, sol.y[2], "r", label = "Infected")
plt.plot(sol.t, sol.y[3], "g", label = "Recovered")
plt.scatter(dates, infection_data, s = 2, marker='o', color='blue', label='Infected People')

plt.title("SEIR Model")
plt.xlabel("Time / days")
plt.ylabel("Amount of People")
plt.legend()
plt.show()



"""observation = infection_data
# Here, we are finding the optimal couples (beta, gamma, sigma) such that the error function is minimal
# We will plot the data on a heatmap
maximum_error = []
gam_bet_sig = []
bet_sig = []
for gam in gamma :
    for bet in beta:
        for sig in sigma:
            error = []            
            sol = solve_ivp(seir_model, [0, 597], [S0, E0, I0, R0], args = (bet, gam, sig), t_eval = t)    
        
            for data in range(len(observation)):
                error.append(abs(sol.y[1][data] - observation[data])) #The optimisation function g
            
        error.append(sum(error))
    bet_sig.append(maximum_error)
gam_bet_sig.append(bet_sig)
    

sns.heatmap(gam_bet_sig, cmap="YlGnBu", xticklabels = gamma, yticklabels = beta, zticklabels = sigma)
plt.legend()
plt.show()
"""