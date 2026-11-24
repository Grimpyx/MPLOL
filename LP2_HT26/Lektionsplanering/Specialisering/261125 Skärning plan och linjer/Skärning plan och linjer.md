# Skärning mellan plan och linjer
**Sidorna:** 236-237
**Tid:** 12:45-14:05

## Agenda
1. Uppvärmning
2. Skärning mellan linjer och plan
3. Uppgifter

## Uppvärmning
Det nya materialet är enkelt så jag börjar med att ge er en uppgift på plan.

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
> Rita upp på tavlan

Tre olika fall kan uppstå.
**Fall 1:** Linjen och planet är parallellt
**Fall 2:** Linjen ligger i planet
**Fall 3:** Linjen korsar planet och de har en gemensam punkt

Betrakta följande plan: $\pi \text{ : } 4x+y+2z=12$.

> Vad kan vi säga om planet $\pi$ och linjen $$L_1(t)=\begin{cases}x=3+t\\y=4-2t\\z=1+2t\end{cases}$$

$$\begin{aligned}4(3+t)+(4-2t)+2(1+2t)&=12 \\
12+4t+4-2t+2+4t&=12 \\
6t&=-6 \\ t&=-1\end{aligned}$$
$t=-1$ satisfierar alltså ekvationen, vilket betyder att de har en punkt gemensamt i $t=-1 \Rightarrow P=(2,6,-1)$.

> Vad kan vi sägaom planet $\pi$ och linjen $$L_2(t)=\begin{bmatrix}2\\1\\3\end{bmatrix}-\begin{bmatrix}-1\\2\\1\end{bmatrix}t$$

$x=2+t$, $y=1-2t$, och $z=3-t$.
Insatt i planets ekvation får vi
$$\begin{aligned}4(2+t)+(1-2t)+2(3-t)&=12 \\
8+4t+1-2t+6-2t&=12 \\
15=12\end{aligned}$$

Eftersom likheten inte stämmer, oavsett värde på $t$, så har $\pi$ och $L_2$ ingen gemensam punkt. De är alltså parallella.
Vad säger detta om skalärprodukten mellan planets normal och linjens riktningsvektor?
$$\vec{n}_\pi \cdot \vec{r}_2=\begin{bmatrix}4\\1\\2\end{bmatrix} \cdot \begin{bmatrix}1\\-2\\-1\end{bmatrix}=4-2-2=0$$

> Vad kan vi säga om planet $\pi$ och linjen $$L_3(t)=\begin{cases}x=1+t\\y=2-2t\\z=3-t\end{cases}$$
>
> Testa själva!

$$\begin{aligned}4(1+t)+(2-2t)+2(3-t)&=12 \\
4+4t+2-2t+6-t&=12 \\
12=12\end{aligned}$$

Likheten stämmer oavsett värde på $t$. Linjen ligger alltså i planet. Testar med skalärprodukt igen.
$$\vec{r}_2 = \vec{r}_3 \Rightarrow \vec{n}_\pi \cdot \vec{r}_3=0$$

## Uppgifter
Repetera linjer och plan tills ni känner er redo att räkna på skärning mellan linjer och plan: s. 237.

## Exit ticket
> Ett plan $\pi$ går igenom punkterna $P_1=(0,0,8)$ och $P_2=(4,4,0)$. Bestäm planets ekvation så att det blir vinkelrätt mot planet 
>
> $\psi \text{ : } x+2y-z=0$
> $\text{Lösning:}$
> För att definiera ett plan behöver vi tre punkter. Annars kommer den inte ha låst rotation.
> $$\vec{n}_\psi=(1,2,-1) \text{ pekar parallellt längs }\pi$$
Om vi adderar $\vec{n}_\psi$ på en existerande punkt i planet, säg $P_1$, så får vi en till som också existerar i planet.
$$P_3=P_1 + \vec{n}_\psi=\begin{bmatrix}0\\0\\8\end{bmatrix}+\begin{bmatrix}1\\2\\-1\end{bmatrix}=\begin{bmatrix}1\\2\\7\end{bmatrix}$$
Vi utgår från punkt-normal form, och väljer $P_1$ som vår punkt:
$$A(x-0)+B(y-0)+C(z-8)=0  \\ Ax+By+Cz=8C$$
> Vi stoppar in punkterna $P_2$ och $P_3$ och skapar ett ekvationssystem.
$$\begin{cases} 4A+4B+0C=8C \\
1A+2B+7C=8C\end{cases}$$
>
>$$\begin{cases} A+B=2C \\
A+2B=C\end{cases}$$
>
> $$A=3C \quad \quad B=-C$$
>
> Väljer vi $C=1$ får vi planets normalvektor till
>
>$$\vec{n}_\psi=\begin{bmatrix}A\\B\\C\end{bmatrix}=\begin{bmatrix}3\\-1\\1\end{bmatrix}$$
>
> $\text{Svar:}$ Planets ekvation blir $\pi \text{ : } 3x-y+z=8$
>
> Är planen orthogonala?
> $$\vec{n}_\psi \cdot \vec{n}_\pi=\begin{bmatrix}1\\2\\-1\end{bmatrix} \cdot \begin{bmatrix}3\\-1\\1\end{bmatrix}=1\cdot3+2\cdot(-1)+(-1)\cdot 1=3-2-1=0$$