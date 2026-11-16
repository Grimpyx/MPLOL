# Linjer i rymden
s.228

## Agenda
1. Vektorform
2. Parameterform
3. Skärande linjer

## Entry ticket

## Vektorform
Inleda med en enhetsvektor gånger parameter t

Tänk er en riktningsvektor $\vec{r}$ som börjar i origo. Om vi multiplicerar med en parameter $t\in\mathbb{R}$ så har vi definierat *alla* punkter som ligger längs vektorn.
$$L(t)=t\vec{r}$$
> Exempel:
> $$L(t)=t\begin{bmatrix}\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{bmatrix}$$

==Visa på desmos.==

Problemet är att vi endast utgår från origo. Hur får vi en helt godtycklig linje? Vi utgår från samma, fast vi adderar en förskjutning/"offset" $P_0$. Detta kallas för en linje på *vektorform*
$$L(t)=P_0+t\vec{r}$$
> Exempel:
> $$L(t)=\begin{bmatrix}0\\1\\0\end{bmatrix}+t\begin{bmatrix}\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{bmatrix}$$

## Parameterform

$L(t)$ betyder att för ett givet $t$ så får vi en punkt $(x,y,z)$Säg att $P_0$ har komponenterna $x_0$, $y_0$, $z_0$, och riktningsvektorn $\vec{r}$ har komponenterna $a$, $b$, $c$.
Då går linjens ekvation att skriva som
$$L(t)=\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}x_0\\y_0\\z_0\end{bmatrix}+t\begin{bmatrix}a\\b\\c\end{bmatrix}$$
Detta ger oss tre olika ekvationer, vilket vi kallar en linje på *parameterform*.
$\begin{cases}x=x_0+at\\y=y_0+bt\\z=z_0+ct\end{cases}$

> Elevaktivitet: spå tillsammans bordsvis/med grannen:
> Vad blir den tidigare linjen vi definierade på parameterform?
>
> Exempel, samma linje som innan:
> $$\begin{cases}x=\frac{1}{\sqrt2}t \\ y=1+\frac{1}{\sqrt2}t \\ z=0\end{cases}$$

## Skärande linjer
Vi ska undersöka skärande linjer.
Säg att vi har två linjer.
Hur många lösningsfall kan vi ha?
> Två linjer kan ha en av tre möjliga lösningsfall:
> - En enda korsningspunkt
> - Oändligt många
> - Inga

## Uppifter

## Exit ticket