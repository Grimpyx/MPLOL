# 📐 Markdown Math & LaTeX Cheat Sheet

This cheat sheet covers the standard LaTeX syntax used for formatting mathematical expressions in Markdown documents (supported by VS Code preview extensions, GitHub, Jupyter, Obsidian, etc.).

---

## 1. Basic Syntax & Enclosure

| Description | LaTeX Syntax | Rendered Output |
| :--- | :--- | :--- |
| **Inline Math** | `$f(x) = x^2$` | $f(x) = x^2$ |
| **Block / Display Math** | `$$f(x) = x^2$$` | $$f(x) = x^2$$ |
| **Fractions** | `\frac{a}{b}` | $\frac{a}{b}$ |
| **Subscripts** | `x_{n+1}` | $x_{n+1}$ |
| **Superscripts (Exponents)** | `x^{10}` | $x^{10}$ |
| **Square Roots** | `\sqrt[n]{x}` | $\sqrt[n]{x}$ |
| **Text inside Math** | `\text{speed} = \frac{\text{distance}}{\text{time}}` | $\text{speed} = \frac{\text{distance}}{\text{time}}$ |

---

## 2. Common Arithmetic & Operators

| Description | LaTeX Syntax | Rendered Output |
| :--- | :--- | :--- |
| **Multiplication** | `a \times b \cdot c` | $a \times b \cdot c$ |
| **Division** | `a \div b` | $a \div b$ |
| **Plus-Minus** | `x = \pm y` | $x = \pm y$ |
| **Relations** | `a \le b \neq c \approx d \ge e` | $a \le b \neq c \approx d \ge e$ |
| **Summation** | `\sum_{i=1}^{n} i` | $\sum_{i=1}^{n} i$ |
| **Product** | `\prod_{i=1}^{n} i` | $\prod_{i=1}^{n} i$ |
| **Limits** | `\lim_{x \to 0} \frac{\sin x}{x}` | $\lim_{x \to 0} \frac{\sin x}{x}$ |

---

## 3. Calculus & Integrals

| Description | LaTeX Syntax | Rendered Output |
| :--- | :--- | :--- |
| **Derivative (Leibniz)** | `\frac{df}{dx}` | $\frac{df}{dx}$ |
| **Derivative (Lagrange / Prime)** | `f'(x) \quad \text{and} \quad f''(x)` | $f'(x) \quad \text{and} \quad f''(x)$ |
| **Partial Derivative** | `\frac{\partial y}{\partial x}` | $\frac{\partial y}{\partial x}$ |
| **Indefinite Integral** | `\int f(x) \, dx` | $\int f(x) \, dx$ |
| **Definite Integral** | `\int_{a}^{b} f(x) \, dx` | $\int_{a}^{b} f(x) \, dx$ |
| **Double Integral** | `\iint_D f(x,y) \, dx \, dy` | $\iint_D f(x,y) \, dx \, dy$ |

---

## 4. Greek Letters

| Name | Lowercase Syntax | Lower Output | Uppercase Syntax | Upper Output |
| :--- | :--- | :--- | :--- | :--- |
| **Alpha / Gamma** | `\alpha` | $\alpha$ | `\Gamma` | $\Gamma$ |
| **Beta / Delta** | `\beta` | $\beta$ | `\Delta` | $\Delta$ |
| **Gamma / Theta** | `\gamma` | $\gamma$ | `\Theta` | $\Theta$ |
| **Delta / Lambda** | `\delta` | $\delta$ | `\Lambda` | $\Lambda$ |
| **Epsilon / Sigma** | `\epsilon`, `\varepsilon` | $\epsilon, \varepsilon$ | `\Sigma` | $\Sigma$ |
| **Theta / Phi** | `\theta` | $\theta$ | `\Phi` | $\Phi$ |
| **Lambda / Psi** | `\lambda` | $\lambda$ | `\Psi` | $\Psi$ |
| **Mu / Omega** | `\mu` | $\mu$ | `\Omega` | $\Omega$ |
| **Pi** | `\pi` | $\pi$ | `\Pi` | $\Pi$ |
| **Sigma** | `\sigma` | $\sigma$ | `\Sigma` | $\Sigma$ |

---

## 5. Brackets & Parentheses (Auto-Sizing)

| Description | LaTeX Syntax | Rendered Output |
| :--- | :--- | :--- |
| **Scaled Parentheses** | `\left( \frac{a}{b} \right)` | $\left( \frac{a}{b} \right)$ |
| **Scaled Square Brackets** | `\left[ \frac{a}{b} \right]` | $\left[ \frac{a}{b} \right]$ |
| **Scaled Curly Braces** | `\left\{ \frac{a}{b} \right\}` | $\left\{ \frac{a}{b} \right\}$ |
| **Absolute Value / Norm** | `\left\| \frac{a}{b} \right\|` | $\left\| \frac{a}{b} \right\|$ |

---

## 6. Multi-line Equations & Systems

| Description | LaTeX Syntax | Rendered Output |
| :--- | :--- | :--- |
| **Aligned Equations** | `\begin{aligned} (x+2)^2 &= x^2 + 2(2x) + 4 \\ &= x^2 + 4x + 4 \end{aligned}` | $\begin{aligned} (x+2)^2 &= x^2 + 2(2x) + 4 \\ &= x^2 + 4x + 4 \end{aligned}$ |
| **Piecewise Functions** | `f(x) = \begin{cases} x^2 & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}` | $f(x) = \begin{cases} x^2 & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$ |

---

## 7. Matrices, Vectors & Accents

| Description | LaTeX Syntax | Rendered Output |
| :--- | :--- | :--- |
| **Plain Matrix** | `\begin{matrix} a & b \\ c & d \end{matrix}` | $\begin{matrix} a & b \\ c & d \end{matrix}$ |
| **Parentheses Matrix** | `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ |
| **Bracket Matrix** | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ |
| **Vector** | `\vec{v} \quad \text{or} \quad \mathbf{v}` | $\vec{v} \quad \text{or} \quad \mathbf{v}$ |
| **Unit Vector / Hat** | `\hat{i}` | $\hat{i}$ |
| **Bar / Mean** | `\bar{x}` | $\bar{x}$ |
| **Dot (Time Derivative)** | `\dot{x}, \ddot{x}` | $\dot{x}, \ddot{x}$ |