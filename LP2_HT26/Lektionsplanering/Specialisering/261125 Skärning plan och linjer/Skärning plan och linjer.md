# Skärning mellan plan och linjer
**Sidorna:** 236-237
**Notera:** Linnea på besök

## Agenda
1. Uppvärmning
2. Skärning mellan linjer och plan
3. Uppgifter

## Uppvärmning
> Undersök om  följande fyra punkter ligger i samma plan. Om ja, vad är planets ekvation?
> $$p_1=\begin{bmatrix}0\\1\\1\end{bmatrix} \quad p_2=\begin{bmatrix}2\\1\\3\end{bmatrix} \quad p_3=\begin{bmatrix}3\\1\\0\end{bmatrix} \quad p_4=\begin{bmatrix}4\\1\\-5\end{bmatrix}$$
> $\text{Lösning:}$
> För ett plan behöver vi en utgångspunkt. Vi väljer $P_1$ som utgångspunkt.
> Nu stället vi upp ett ekvationssystem med de andra tre punkterna insatta i planets *punkt-normal form*.
> $$\begin{cases}A(2-0)+B(1-1)+C(3-1)=0 \\
A(3-0)+B(1-1)+C(0-1)=0 \\
A(4-0)+B(1-1)+C(-4-1)=0 \end{cases}$$
>
> $$\begin{cases}2A+2C=0 \\
3A-C=0 \\
4A+-5C=0 \end{cases}$$
> Från ekvationerna får vi att $A=C=0$.
> Det kan se ut som att $B=0$ också och att vi då får en normalvektor = $\textbf{0}$, men i ekvationerna *försvinner $B$*. Det betyder att $B$ kan vara vilket tal som helst. Vi väljer $B=1$ för enkelhetens skull.
> Planets ekvation:
> $$0(x-0)+1(y-1)+0(z-1)=0 \\ \Rightarrow y=1$$
>
> Vad händer om vi väljer något annat värde på $B$?
> Säg att vi väljer ett godtyckligt värde $k$.
> $$k(y-1)=0 \\ ky-k=0 \\ ky=k \\ y=1$$


## Skärning mellan plan och linje
3 fall
**Fall 1:** Parallell linje
**Fall 2:** Parallell linje som ligger i planet
**Fall 3:** En skärningspunkt