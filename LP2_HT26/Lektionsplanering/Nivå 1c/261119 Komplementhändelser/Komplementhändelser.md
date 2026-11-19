# Komplementhändelser
s.293-302

## Agenda
1. Uppvärmning
2. Träddiagram
3. Beroende och oberoende händelser
4. Komplementhändelser
5. Pirate token

## Uppvärmning
> I Fortnite kan man, med enorm tur, få en *pirate token* i en kista. Varje kista har en chans på $137500$ att innehålla en pirate token.
> Vad är sannolikhet att inte få en enda pirate token på 10000 kistor?
> $$P(\text{Ej få pirate token})=\frac{137499}{137500}$$
>
> Beroende eller oberoende händelser?
> $$\begin{aligned}P(\text{Ej få pirate token på 10000 kistor})=\\=P(\text{Ej få}) \cdot P(\text{Ej få}) \cdot ... \cdot P(\text{Ej få}) =\\=\{P(\text{Ej få})\text{ 10000 gånger}\}=\Big(\frac{137499}{137500}\Big)^{10000}\end{aligned}$$

## Komplementhändelse
Inledande uppgift som jag inte tror ni kan lösa.

Jag har kollat på varenda match schack som Elliot någonsin spelat. Jag har beräknad den relativa frekvensen, hans winrate, till $57\%$. Vi låter detta approximera hans faktiska winrate.

Vad är sannolikheten att Elliot vinner minst en gång på 5 matcher?

Ett sätt att lösa:
Vi summerar sannolikheterna för alla fall som leder till minst en vinst.
|Match $\rightarrow$|1|2|3|4|5|
|-----|-|-|-|-|-|
|Utfall 1|0|0|0|0|1|
|Utfall 2|0|0|0|1|0|
|Utfall 3|0|0|0|1|1|
|Utfall 4|0|0|1|0|0|
|Utfall 5|0|0|1|0|1|
|...|...|...|...|...|...|
|Utfall 31|1|1|1|1|1|

Vi ska alltså addera 31 sannolikheter. Nu råkar detta vara en perfekt för att använda komplementhändelser.
En komplementhändelse beskriver en motsatshändelse. Matematisk definition:
$$P(H)+P(H^C)=1$$

Om Elliot endast kör en match, vad är sannolikheten att han vinner? $57\%$
Vad är i så fall sannolikheten att han *inte* vinner? Jo, $43\%$.
Detta är sannolikheten för komplementhändelsen. Vi kontrollerar den matematiska definitionen för komplementhändelser.
$$0.57+0.43=1$$ Stämmer!

Vi återgår till exemplet: vi söker sannolikheten att *Elliot vinner minst en gång*. Vad är komplementhändelsen?
$$H=\{\text{Elliot vinner minst en match}\}$$

$$H^C=\{\text{Elliot vinner inga matcher}\}$$

$$P(H^C)=0.43 \cdot 0.43 \cdot 0.43 \cdot 0.43 \cdot 0.43 = 0.43^5 = 0.0147$$

$$P(H) = 1 - P(H^C) = 1 - 0.0147 = 0.9853 = 98.5\%$$

## Pirate token
$$P(\text{Pirate token finns i en kista})=\frac{1}{137500}$$

Sannolikhet att inte få per kista: $$P(\text{Inte få pirate token})=1-\frac{1}{137500}=\frac{137499}{137500}$$

$$H=\{\text{Få minst en pirate token på 20 kistor}\}$$

Vad är komplementhändelsen? Sannolikhet att inte få någon pirate token alls:
$$P(H^C)=\frac{137499}{137500}^{20}$$

$$P(H)=1-P(H^C)=1-\frac{137499}{137500}^{20}=0.0001454 \approx 0.0145\%=145 \text{ ppm}$$
[Pirate token desmos](https://www.desmos.com/calculator/cjd4gwnbnq)


