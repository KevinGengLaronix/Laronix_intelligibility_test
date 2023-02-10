# Laronix Naturalness Test

## Simple explanation of this opensource

1. Create wav directory like the below example. Each set contains wav files and their file lists for the methods you want to compare. It's easier to understand if you actually browse the wav directory. The number of methods in each set does not have to match.

```
wav/
 |---- set1/
 |      |-- method1/
 |      |-- method1.list
 |
 |---- set2
 |      |-- method2/
 |      |-- method3/
 |      |-- method2.list
 |      |-- method3.list
 |
 |---- set3
 |      |-- method4/
 |      |-- method5/
 |      |-- method4.list
 |      |-- method5.list
 |
 ```
 The command ```find wav/set1 -name "*.wav" | grep "method1" > wav/set1/method1.list``` will be helpful to create list files.

2. Rewrite mos.js depending on the structure of the wav directory. You only need to customize the part from line 45.

3. Rewrite index.html as you like. Note that my email address is written as contact info, so you may have to change it to your own one.

4. Use Github Pages to deploy your own test. The test automatically emits a csv file when the test finishes.

If you want to conduct tests other than a MOS test, you need to modify the code significantly depending on the test.
You can utilize [ABXTest](https://github.com/chomeyama/ABXTest) if you want to conduct ABX test.

Please feel free to ask any questions you may have.

## What's in each set:
Here is the strategy of select each sets sentences.
1. Each set contains 4 types of audio, `HEALTHY`, `PAL`, `TEP`, `EL`. 7 of them are contained in each set so totally 28.

2. To make sure there is no extra information (like the same content in both `HEALTHY` and `PAL`), each method is split up in 4 groups, and each set contains a exclusive combination of 4 methods. e.p `(1,2,3,4)` and `(4, 3, 2, 1)`

3. Sentence length: To guarantee each sets distribution, we select 5 short sentences  `(8 <= WORDLEN <= 13)` and 3 long sentences `(WORDLEN >= 15)` in each group.


