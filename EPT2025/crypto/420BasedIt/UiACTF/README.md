# 420BasedIt

Author: surprior

## Description

```
I was gonna write a crypto challenge, but then I got high...

Anyway, what's cooking **chef**? #420BasedIt!
```

## Provided challenge files

```
4'S\WyZP[/H5lb.63dR#0<\F?Sr[*,!WAi\Hty3}hvOtlb-u>V$E=<6)yymg@YZ}K42#%6]OKvIRS*3r8:^7I^Y{g<Rg=#6eEyR!]Wcg)1RcVGlu.h%kY5][\Zf^@2DP@?:NYM2vbCE1
```

## Solve

The hint in the description “what’s cooking **chef**?” and “#420BasedIt”, made us think of **CyberChef** and **base encodings**.

We figured “420BasedIt” might mean a combination of base encodings whose numbers add up to 420. After experimenting with different base layers in **CyberChef**, and letting **Magic** help out a bit, we found the right combination that decoded `EPT{I5_th3_Ch3f_1n_yet?}`.

![CyberChef magic](image-1.png)

So the flag was found with first using `From Base 92` -> `From Base 85` -> `From Base 85` -> `From Base 65` -> `From Base 62` -> `From Base 32`

The total “base” value indeed summed to **420**. Nice.

![420](image.png)

