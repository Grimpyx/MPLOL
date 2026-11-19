import random

N=10
nr_gynnsam = 0
nr_total = 0

# Kollar hur många 6:or det blir på N st tärningskast
for i in range(N):
    # kasta tärning, och läs av
    throw = random.randint(1,6)
    if throw == 6:
        # Om vi får 6:a, inkrementera antal gynnsamma
        nr_gynnsam += 1
    nr_total += 1

# Skriv ut output i konsollen
print(f"P(H) = 1/6 = {1/6:.6f}, men f_R(H) = {nr_gynnsam/nr_total:.6f}")