# Hadamard-Walsh

This is a first attempt into understanding application of Hadamard-Walsh in computing of Linear Charateristics of given S-box.

In general we can state that an S-box receive integer values of n-bit (which can be splitted in order to search results), and returns integer with t-bit in size.

Let ![s](https://latex.codecogs.com/svg.latex?S) be an S-box, compute differential characteristics of ![s](https://latex.codecogs.com/svg.latex?S) denoted by ![diff](https://latex.codecogs.com/svg.latex?D_{\Delta}^{\delta}(S)):

![equals1](https://latex.codecogs.com/svg.latex?D_%7B%5CDelta%7D%5E%7B%5Cdelta%7D%28S%29%20%3D%20%5C%23%5C%7B%28x%2Cy%29%20%5Cin%20input%5E%7B2%7D%20%3A%20x%20%5Coplus%20y%20%3D%20%5CDelta%2C%20S%28x%29%20%5Coplus%20S%28y%29%20%3D%20%5Cdelta%20%5C%7D)

Linear characteristics of ![s](https://latex.codecogs.com/svg.latex?S) are denoted with ![linchr](https://latex.codecogs.com/svg.latex?\mathcal{L}_{M}^{m}(S)) standing for the difference between:
* number of input elements ![x](https://latex.codecogs.com/svg.latex?x) such that bitwise scalar products ![scalprodin](https://latex.codecogs.com/svg.latex?(M|x)) and ![scalprodout](https://latex.codecogs.com/svg.latex?(m|S(x))) are equals modulo 2
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
Another interesting thing is to split ![T](https://latex.codecogs.com/svg.latex?T(x)) in two halves.

Since input ![x](https://latex.codecogs.com/svg.latex?x) is a number in range ![range](https://latex.codecogs.com/svg.latex?[0,2^n%29) *"splitting in two halves"* means dividing by two the upperbound, so ![x](https://latex.codecogs.com/svg.latex?x) for function ![T](https://latex.codecogs.com/svg.latex?T(x)) will be in range ![range](https://latex.codecogs.com/svg.latex?[0,\frac{2^n}{2}%29) that is ![range](https://latex.codecogs.com/svg.latex?[0,2^{n-1}%29), now define ![x](https://latex.codecogs.com/svg.latex?x) in this new range and splitting ![T](https://latex.codecogs.com/svg.latex?T(x)) in ![T0](https://latex.codecogs.com/svg.latex?T_0(x)) that is equals to ![T](https://latex.codecogs.com/svg.latex?T(x)) (remembering we reduce upper bound of ![x](https://latex.codecogs.com/svg.latex?x)) and  ![T1](https://latex.codecogs.com/svg.latex?T_1(x)=T(2^{n-1}+x)).

The last equation ![T1](https://latex.codecogs.com/svg.latex?T_1(x)=T(2^{n-1}+x)) is obtained considering ![x](https://latex.codecogs.com/svg.latex?x\in[0,2^{n-1}%29) but when sum it to ![2n-1](https://latex.codecogs.com/svg.latex?2^{n-1})(equals multiplying ![2n-1](https://latex.codecogs.com/svg.latex?2^{n-1}) by ![2](https://latex.codecogs.com/svg.latex?2)) function's argument size will be ![n](https://latex.codecogs.com/svg.latex?n) in bit.

So ![T0](https://latex.codecogs.com/svg.latex?T_0(x)) and ![T1](https://latex.codecogs.com/svg.latex?T_1(x)=T(2^{n-1}+x)) takes ![2n-1](https://latex.codecogs.com/svg.latex?2^{n-1}) in two different range: first one in ![range](https://latex.codecogs.com/svg.latex?[0,2^{n-1}%29) the second one (remaining ![x](https://latex.codecogs.com/svg.latex?x) in ![range](https://latex.codecogs.com/svg.latex?[0,2^{n-1}%29)) in ![range](https://latex.codecogs.com/svg.latex?[2^{n-1},2^{n}%29).

So from this equation is natural consider this (note that mask now is reduced in size with ![x](https://latex.codecogs.com/svg.latex?x) that is ![Mn](https://latex.codecogs.com/svg.latex?M<2^{n-1}) then we do another equation to compute second halves with input masks computed as  ![Mnp](https://latex.codecogs.com/svg.latex?2^{n-1}+M)):

![first_semp](https://latex.codecogs.com/svg.latex?\mathcal{L}_{M}^{1}(S)=%20\sum_{x}%20(-1)^{(x|M)}%20\cdot%20(-1)^{S(x)}=%20\sum_{x}%20(-1)^{(x|M)}%20\cdot%20T(x))
![second_eq](https://latex.codecogs.com/svg.latex?=%20\sum_{x%3C2^{n-1}}%20(-1)^{(x|M)}%20\cdot%20T_0(x)+\sum_{x%3C2^{n-1}}%20(-1)^{(x|M)}%20\cdot%20T_1(x)=)

Please note that in ![st](https://latex.codecogs.com/svg.latex?\sum_{%78%3C2^{n-1}}%20(-1)^{(x|M)}%20\cdot%20T_1(x)) seems that second halves for ![x](https://latex.codecogs.com/svg.latex?x) is not aligned with  ![T1](https://latex.codecogs.com/svg.latex?T_1(x)=T(2^{n-1}+x)). But for this equation ![Mn](https://latex.codecogs.com/svg.latex?M<2^{n-1}) and this mean that the most significant bit for ![x](https://latex.codecogs.com/svg.latex?x) is useless for bitwise scalar multiplication with ![M](https://latex.codecogs.com/svg.latex?M) since is ![n-1](https://latex.codecogs.com/svg.latex?n-1) in size. 
So this means that is equal consider ![xn](https://latex.codecogs.com/svg.latex?%78<2^{n-1}) for ![fsterm](https://latex.codecogs.com/svg.latex?(-1)^{(x|M)}) multypling it with corresponding ![T1](https://latex.codecogs.com/svg.latex?T_1(x)=T(2^{n-1}+x)) which consider ![x](https://latex.codecogs.com/svg.latex?x) expanded to ![n](https://latex.codecogs.com/svg.latex?n) bits.


So now imaging to split S-box into two halves ![s0](https://latex.codecogs.com/svg.latex?S_0) and ![s1](https://latex.codecogs.com/svg.latex?S_1), according with ![T0](https://latex.codecogs.com/svg.latex?T_0) and ![T1](https://latex.codecogs.com/svg.latex?T_1) (this could bring to confusion but ![mone](https://latex.codecogs.com/svg.latex?T(x)=(-1)^{S(x)) and splitting this by values of ![x](https://latex.codecogs.com/svg.latex?x) means that we never use some sbox values for the first halves of input as well as we don't use other sbox values for second halves of input), we can introduce last simplification:

![third_eq](https://latex.codecogs.com/svg.latex?=\mathcal{L}_{M}^{1}(S_0)%20+\mathcal{L}_{M}^{1}(S_1))


What we can note is: what about input masks ![M](https://latex.codecogs.com/svg.latex?M)? Last equation is with input mask ![Mn](https://latex.codecogs.com/svg.latex?M<2^{n-1}), now compute linear characteristics with masks from ![lb](https://latex.codecogs.com/svg.latex?2^{n-1}) to ![ub](https://latex.codecogs.com/svg.latex?2^{n}-1):

![eq2](https://latex.codecogs.com/svg.latex?\mathcal{L}_{2^{n-1}+M}^{1}(S)=\sum_{x%3C2^{n-1}}(-1)^{(x|M)}\cdot%20T_0(x)-\sum_{x%3C2^{n-1}}(-1)^{(x|M)}\cdot%20T_1(x))

Steps on this equation seems not to be straightforward, the key to understand all of this is to consider bitwise scalar product, in fact the above equation have the first summation defined for the first halves of ![x](https://latex.codecogs.com/svg.latex?x), the second one authors don't want to rewrite summation for different ![x](https://latex.codecogs.com/svg.latex?x). Remembering that the most significant bit for ![x](https://latex.codecogs.com/svg.latex?x) is one and the mask is added with ![ub](https://latex.codecogs.com/svg.latex?2^{n-1}) so bitwise scalar product has always 1 in most significant bit term. Therefore considering ![st](https://latex.codecogs.com/svg.latex?\sum_{%78%3C2^{n-1}}%20(-1)^{(x|M)}%20\cdot%20T_1(x)) for ![M](https://latex.codecogs.com/svg.latex?M) added with ![ub](https://latex.codecogs.com/svg.latex?2^{n-1}) is equal to considering all ![x](https://latex.codecogs.com/svg.latex?x) in ![ub](https://latex.codecogs.com/svg.latex?2^{n-1}) misaligned with ![T1](https://latex.codecogs.com/svg.latex?T_1) but with minus to all results implies that all terms that are considered positive will be switch to negative and vice-versa. So when values of ![Sxm](https://latex.codecogs.com/svg.latex?S(x)|m) is equal ![xM](https://latex.codecogs.com/svg.latex?x|M) modulo two then have ![min1](https://latex.codecogs.com/svg.latex?-1) as impact while one of the two previous terms are different then the impact become ![plus1](https://latex.codecogs.com/svg.latex?+1), that is the most significant bit for ![Mp](https://latex.codecogs.com/svg.latex?M+2^{n-1}) and  ![x](https://latex.codecogs.com/svg.latex?x) in second halves cause the most significant bit in scalar product to be always one, so is equal revert result for compressed bit length (from  ![n](https://latex.codecogs.com/svg.latex?n) to  ![nm1](https://latex.codecogs.com/svg.latex?n-1)).


finally:

![fourth_eq](https://latex.codecogs.com/svg.latex?=\mathcal{L}_{M}^{1}(S_0)%20-\mathcal{L}_{M}^{1}(S_1))


All this discussion is used to produce an algorithm that, given table which represents ![T](https://latex.codecogs.com/svg.latex?T), gives new table in output: ![wt](https://latex.codecogs.com/svg.latex?W(T)) such that for each position ![wt](https://latex.codecogs.com/svg.latex?M) in table  ![T](https://latex.codecogs.com/svg.latex?T):

 ![W(T)](https://latex.codecogs.com/svg.latex?W_M(T)=\mathcal{L}_{M}^{1}(S)) 
 
 Without using the Walsh transform compute Linear Charecteristics, for each output masks, of S-Box of ![t](https://latex.codecogs.com/svg.latex?t) output bit and ![n](https://latex.codecogs.com/svg.latex?n) input bit is ![compbase](https://latex.codecogs.com/svg.latex?O(2^{2n+t})).
 
 With Walsh transform, for each output mask ![m](https://latex.codecogs.com/svg.latex?m), we build table ![Sm](https://latex.codecogs.com/svg.latex?S_m(x)=(m|S(x))) with single bit of output proceed as above. 
 
Observe that Walsh Transform time complexity is ![compw](https://latex.codecogs.com/svg.latex?O(n%20\cdot%202^{n})) and computation of linear characteristics reduced time to ![compf](https://latex.codecogs.com/svg.latex?O(n%20\cdot%202^{n+t}))

