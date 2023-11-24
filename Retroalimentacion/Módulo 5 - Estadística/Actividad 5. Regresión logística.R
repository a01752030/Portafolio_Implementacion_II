#Paso 1. Definir las hipótesis

$H_0:\mu=11.7$
$H_1:\mu\neq11.7$
#Estadistico  
$\bar{x}$

$\mu_{\bar{x}=11.7$,$\sigma_{\bar{x}}=\frac{s}{\sqrt{n}}}$  
  
#Paso 2 Regla de decisión
  
$\alpha=0.2$

```{r}
x = c(17, 11, 12, 23, 20, 23, 15, 16, 23, 22, 18, 23, 25, 14, 12, 12, 20, 18, 
      12, 19, 11, 11, 20, 21, 11, 18, 14, 13, 13, 19, 16, 10, 22, 18, 23)
alpha = 0.02
n= lenght(x)
tO = qt(alpha/2,n-1)
cat("t0 = ",tO)
```
t0 = -2.527977

*|t*|>2.53
p < 0.02
  
#Paso 3 Análisis del resultado

```{r}
m = mean(x)
s  sd(X)
sm = s/sqrt(n)
te=(11.49-m)/sm
cat("t* = ",te)
``` 

*Calculo de valor p*
valorp = 2* pt(te,n-1)
cat("Valor p = ",valorp)
  
#Paso 4 Conclusiones  
#Como el valor p(0.05173) es mayor que 0.02, entonces no rechazo h0. Como |t*| (2.07)
#es menor que 2.53, entonces rechazo h0
#En el contexto del problema estp significa que...

##Más facil paso 3:
t.test(X,alternative="two sided",mu=11.7,conf.level=0.98)
