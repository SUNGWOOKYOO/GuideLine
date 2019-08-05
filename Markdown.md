# 수식 표현 정리

 [ref1](https://en.wikipedia.org/wiki/Help:Displaying_a_formula#Formatting_using_TeX) [ref2](https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/)

<expression> \left ...  <expression> \right 

\begin{<func>} ... \end{<func>}

----

### Formula

$$
<left> = \left \{
\begin{matrix} 
<right1> & if <cond1> \\ 
<right2> & if <cond2> \\ 
<right3> & if <cond3> \\
\end{matrix}\right.
$$

---

$$
\underset{<cond>}{\operatorname{<op>}}
$$

---

### Matrix

{cc} 는 가운데로 정렬
$$
\left( \begin{array}{cc} 
a & b \\
c & d
\end{array}\right)
\left( \begin{array}{cc} 
e & f \\ 
g & h
\end{array}\right)
$$

$$
\begin{bmatrix}
0 & \cdots & 0 \\
\vdots & \ddots & \vdots \\
0 & \cdots & 0
\end{bmatrix}
$$

