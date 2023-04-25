HTK-Windows

- `.\HParse.exe .\grammar.txt wdnet.txt`
- `.\HCopy.exe -T 1 -C .\coding_cfg.txt -S .\coding_scp.txt`
- `.\HCompV.exe -C .\train_cfg.txt -f 0.01 -m -S .\train_scp.txt -M .\hmm0\ proto`
- ` .\HERest.exe -C .\train_cfg.txt t -I .\trans.mlf -t 250.0 150.0 1000.0 -S .\train_scp.txt -H .\hmm0\hmm.txt -M hmm1 .\ModelsList.txt`
- ` .\HERest.exe -C .\train_cfg.txt t -I .\trans.mlf -t 250.0 150.0 1000.0 -S .\train_scp.txt -H .\hmm1\hmm.txt -M hmm1 .\ModelsList.txt`
- `.\HERest.exe -C .\train_cfg.txt t -I .\trans.mlf -t 250.0 150.0 1000.0 -S .\train_scp.txt -H .\hmm2\hmm.txt -M hmm1 .\ModelsList.txt`
- ` .\HERest.exe -C .\train_cfg.txt t -I .\trans.mlf -t 250.0 150.0 1000.0 -S .\train_scp.txt -H .\hmm3\hmm.txt -M hmm1 .\ModelsList.txt`
- `HERest -C train_cfg.txt -I trans.mlf -t 250.0 150.0 1000.0 -S train_scp.txt -H hmm0/hmm.txt -M hmm1 ModelsList.txt`
- `HERest -C train_cfg.txt -I trans.mlf -t 250.0 150.0 1000.0 -S train_scp.txt -H hmm1/hmm.txt -M hmm2 ModelsList.txt`
- `HERest -C train_cfg.txt -I trans.mlf -t 250.0 150.0 1000.0 -S train_scp.txt -H hmm2/hmm.txt -M hmm3 ModelsList.txt`

RUN & TEST

```PowerShell
HVite -H hmm3/hmm.txt -C run_cfg.txt -w wdnet.txt -p 0.0 -s 5.0 dictionary.txt ModelsList.txt
```