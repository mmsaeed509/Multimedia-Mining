<h3 align="center"> HTK </h3>

# Installation


### on Arch Linux (Arch-based & Exodia OS)

```bash
sudo pacman -U exodia-htk-3.5-1-any.pkg.tar.zst
```

### On any Linux distro

#### for `HTK-3.4.1`

```bash

# Extract #
tar -xvzf HTK-3.4.1.tar.gz

# Compiling #
./configure --prefix=/usr
make all
sudo make Install

```

#### for `HTK-3.5.beta-2.tar.gz`

```bash

# Extract #
tar -xvzf HTK-3.5.beta-2.tar.gz

# Compiling #
cd htk

# Compiling HTKLib at first, then HLMLib, then HTKTools and HLMTools #

# Compiling HTKLib #
cd HTKLib

make -f MakefileCPU all
make -f MakefileCPU install
sudo cp -r lib/* /usr/lib
cd ..

# Compiling HLMLib #
cd HLMLib

make -f MakefileCPU all
make -f MakefileCPU install
sudo cp -r lib/* /usr/lib
cd ..

# Compiling HTKTools #
cd HTKTools

make -f MakefileCPU all
make -f MakefileCPU install
cd ..
sudo cp -r bin.cpu/* /usr/bin
rm bin.cpu

# Compiling HLMTools #
cd HLMTools

make -f MakefileCPU all
make -f MakefileCPU install
cd ..
sudo cp -r bin.cpu/* /usr/bin

# Clean #
cd HTKLib
make -f MakefileCPU clean
cd ..

cd HLMLib
make -f MakefileCPU clean
cd ..

cd HTKTools
make -f MakefileCPU clean
cd ..

cd HLMTools
make -f MakefileCPU clean
cd ..

```