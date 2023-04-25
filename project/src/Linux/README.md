<h3 align="center"> commands </h3>

### convert the grammar to a word network 

```bash
HParse grammar.txt wdnet.txt
```
### call HCompv to create `mfcc` files 

```bash
HCopy -T 1 -C coding_cfg.txt -S coding_scp.txt
```

### Compute global parameters

In this step we will compute the global mean and variance and set all of the Gaussians ina given *HMM* to have the same mean and variance.
We will use the tool `HComV`.

> <u>**Note:**</u>
> 
> **create a directory `hmm0` before executing the command**

```bash
HCompV -C train_cfg.txt -f 0.01 -m -S train_scp.txt -M hmm0 proto
```
The previous command will scan the given set of files, and create a new `hmmfile` in the directory `hmm0` containing the updated means and variances, also it will create the file `vFloors` for variance flooring.

### Create Master `HMM` file

### Running the recognizer

```bash
HVite -H hmm1/hmm.txt -C run_cfg.txt -w wdnet.txt -p 0.0 -s 5.0 dictionary.txt ModelsList.txt
```