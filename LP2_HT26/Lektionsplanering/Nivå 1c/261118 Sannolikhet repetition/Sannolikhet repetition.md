# Sannolikhet repetition
s.284-292

## Agenda
1. Klassisk sannolikhet
2. Relativ frekvens
3. Slumpförsök i flera steg

## Uppvärmning
> Vad är den **horisontella kraftkomposanten** när jag drar en pulka med kraften $100$ newton $30^\circ$ från marken?
> Metod: Rita upp triangel med hypotenusan $100$ och beräkna närliggande kateten som
> $$\cos(30^\circ)=\frac{x}{100} \\ x=100\cdot\cos(30^\circ)=100\cdot \frac{1}{2}=50$$
>
> $\text{Svar: 50 N}$

## Klassisk sannolikhet
$$P(H)=\frac{\text{\# gynnsamma utfall}}{\text{\# totala möjliga utfall}}$$

## Relativ frekvens
$$f_R(H)=\frac{\text{\# gynnsamma observationer}}{\text{\# totalt antal observationer}}$$
> Vad skiljer Klassisk sannolikhet och Relativ frekvens?
> Det handlar om experiment och observationer.

Givet väldigt många observationer så kan $f_R$ användas för att uppskatta sannolikhet. Den relativa frekvensen blir då en så kallad *empirisk sannolikhet*.
$$f_R(H) = P_E(H) \approx P(H)$$

Den första likheten gäller endast om det är tillräckligt många observationer.

## Slumpförsök i flera steg
> Stämmer följande alltid?
> $$P(A\text{ eller }B)=P(A) + P(B)$$

+++ Nej. Vi ritar upp händelserna som mängder.
+++ Visa också med graf.

## Oberoende/beroende händelser
Två tärningskast är *oberoende*. 
> Vad betyder det?

När man kaster den andra tärningen, så spelar det ingen roll alls vad första tärningen visade.
$$P(T_1 = 1\text{ och } T_2 = 1) = P(\text{första blir 1}) \cdot P(\text{första blir 1})$$

Jämför detta med något vi sett tidigare: påsen med olika färgade bollar *utan återläggning*. Om man tar två bollar så *beror det andra draget på* vad man drar första gången.

En påse med 6 röda och 5 blåa. Sannolikheten att dra en blå på andra draget beror på vad du drog först.
$$P(\text{Nästa är blå } | \text{ Första var blå})=\frac{4}{10}=40\%$$

$$P(\text{Nästa är blå } | \text{ Första var röd})=\frac{5}{10}=50\%$$

I praktiken är två händelser $A$ och $B$ *oberoende* om
$$P(A \text{ och }B)=P(A)\cdot P(B)$$ 

Om likheten ej stämmer är de *beroende*.

På sida 298 visar boken hur vi gör ett träddiagram med

EXEMPEL

## Uppgifter
Fortsätt där ni slutade igår. Nya uppgifter på beroende händelser på sida 299.