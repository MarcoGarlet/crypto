# Hadamard-Walsh

This is a first attempt into understanding application of Hadamard-Walsh in computing of Linear Charateristics of given S-box.

In general we can state that an S-box receive integer values of n-bit (which can be splitted in order to search results), and returns integer with t-bit in size.

Let ![s](https://latex.codecogs.com/svg.latex?S) be an S-box, compute differential characteristics of ![s](https://latex.codecogs.com/svg.latex?S) denoted by ![diff](https://latex.codecogs.com/svg.latex?D_{\Delta}^{\delta}(S)):

![equals1](https://latex.codecogs.com/svg.latex?D_%7B%5CDelta%7D%5E%7B%5Cdelta%7D%28S%29%20%3D%20%5C%23%5C%7B%28x%2Cy%29%20%5Cin%20input%5E%7B2%7D%20%3A%20x%20%5Coplus%20y%20%3D%20%5CDelta%2C%20S%28x%29%20%5Coplus%20S%28y%29%20%3D%20%5Cdelta%20%5C%7D)

Linear characteristics of ![s](https://latex.codecogs.com/svg.latex?S) are denoted with ![linchr](https://latex.codecogs.com/svg.latex?\mathcal{L}_{M}^{m}(S)) standing for the difference between:
* number of input elements ![x](https://latex.codecogs.com/svg.latex?x) such that bitwise scalar products ![scalprodin](https://latex.codecogs.com/svg.latex?(M|x)) and ![scalprodout](https://latex.codecogs.com/svg.latex?(m|S(x)))
* number of pairs such that these scalar product are different

Pay attention on implementation of bitwise scalar product, for ![a](https://latex.codecogs.com/svg.latex?a) and ![b](https://latex.codecogs.com/svg.latex?b) is:

![bitwiseprod](https://latex.codecogs.com/svg.latex?(a|b)%20=%20\sum_{i%20=%200}^{l-1}%20a_ib_imod%202)

assuming ![a](https://latex.codecogs.com/svg.latex?a) and ![b](https://latex.codecogs.com/svg.latex?b) having ![l](https://latex.codecogs.com/svg.latex?l) bit.


Now the Walsh transform is a kind of discrete Fourier transform with lot of application in coding theory and cryptography. 
Among all possible use one of the most interesting is of course the fast computation of linear characteristics.

Consider case with S-boxes with single bit of output i.e. ![teq](https://latex.codecogs.com/svg.latex?t=1), in that case is useful considering ![m](https://latex.codecogs.com/svg.latex?m) equals to 1, becoming straightforward rewriting:

![linearmone](https://latex.codecogs.com/svg.latex?\mathcal{L}_{M}^{1}(S)%20=%20\sum_{(x|M)%20=%20S(x)}%201%20-%20\sum_{(x|M)%20\ne%20S(x)}%201=)

including all in one summation:

![simplinearw](https://latex.codecogs.com/svg.latex?=%20\sum_{x}%20(-1)^{(x|M)}%20\cdot%20(-1)^{S(x)})


Now we can rewrite ![mone](https://latex.codecogs.com/svg.latex?(-1)^{S(x)) as ![T](https://latex.codecogs.com/svg.latex?T(x))



