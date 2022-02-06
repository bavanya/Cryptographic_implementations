### Practical Assignment 1 -
Demonstrating the Avalanche effect observed in the rounds of the DES algorithm.

Three experiments are performed and the results are plotted as a box plot to understand
the extent of the Avalanche effect in each of the three experiments.

#### Experiments are as follows:

**Experiment 1**-

We take a hexadecimal plain text p0 and take 5 other hexadecimal plain texts 
such that all 5 of them have hemming distance 1 wrt p0.

Now to track the avalanche effect, we calculate the hemming distance between each of the calculated 
cipher texts of p1, p2, p3, p4, p5 and the calculated cipher text of p0 for each round.

Now we will have 5 data points for the hemming distance at each round, using which we generate a box plot.

**The 6 plain text and secret key pairs used in this experiment are**-
| PK HEX           | PK BINARY                                                        | Key HEX          | Key BINARY                                                       |
| ---------------- | ---------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------- |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132537 | 0001001000110100010101101010101111001101000100110010010100110111 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132576 | 0001001000110100010101101010101111001101000100110010010101110110 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD13253E | 0001001000110100010101101010101111001101000100110010010100111110 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132534 | 0001001000110100010101101010101111001101000100110010010100110100 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132532 | 0001001000110100010101101010101111001101000100110010010100110010 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |

**The box plot generated is as follows**-

![alt text](https://github.com/bavanya/Network_security_assignments/blob/main/PA1_Avalanche_effect_DES_algo/plots/case1.png)

**Experiment 2**-

Here instead of taking hemming distance of 1 between p0 and 5 other plain texts, 
we take p1, p2, p3, p4, p5 such that each pi has a different hemming distance wrt p0. 

Now similar to experiment 1, we generate the box plot with the 5 data points 
we obtain for each round of DES algorithm.

**The 6 plain text and secret key pairs used in this experiment are**-
| PK HEX           | PK BINARY                                                        | Key HEX          | Key BINARY                                                       |
| ---------------- | ---------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------- |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132537 | 0001001000110100010101101010101111001101000100110010010100110111 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132535 | 0001001000110100010101101010101111001101000100110010010100110101 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132531 | 0001001000110100010101101010101111001101000100110010010100110001 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132539 | 0001001000110100010101101010101111001101000100110010010100111001 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132529 | 0001001000110100010101101010101111001101000100110010010100101001 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |

**The box plot generated is as follows**-

![alt text](https://github.com/bavanya/Network_security_assignments/blob/main/PA1_Avalanche_effect_DES_algo/plots/case2.png)

**Experiment 3**-

The only difference between this experiment and the first experiment is that here, instead of taking 5 different
plain texts at a hemming distance of 1 from p0, we take 5 different secret keys k1, k, k3, k4, k5 
at a hemming distance of 1 from secret key k0.

Now similar to experiment 1, we generate the box plot with the 5 data points 
we obtain for each round of DES algorithm.

**The 6 plain text and secret key pairs used in this experiment are**-
| PK HEX           | PK BINARY                                                        | Key HEX          | Key BINARY                                                       |
| ---------------- | ---------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------- |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCDD | 1010101010111011000010010001100000100111001101101100110011011101 |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCFD | 1010101010111011000010010001100000100111001101101100110011111101 |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCDF | 1010101010111011000010010001100000100111001101101100110011011111 |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCD9 | 1010101010111011000010010001100000100111001101101100110011011001 |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCD5 | 1010101010111011000010010001100000100111001101101100110011010101 |
| 123456ABCD132536 | 0001001000110100010101101010101111001101000100110010010100110110 | AABB09182736CCCD | 1010101010111011000010010001100000100111001101101100110011001101 |

**The box plot generated is as follows**-

![alt text](https://github.com/bavanya/Network_security_assignments/blob/main/PA1_Avalanche_effect_DES_algo/plots/case3.png)
