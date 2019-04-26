# Huffman-Coding-ARM
## Pre-Requisites
- Linux (Ubuntu- 16.04) 
- Qemu Emulator
  - `sudo apt install binfmt-support qemu qemu-user-static`
- 32-bit Armv7 Cortex-A, hard-float, little-endian (Link)[https://releases.linaro.org/components/toolchain/binaries/latest-7/]
  - `sudo apt install binutils-arm-linux-gnueabihf`
- Python (Not necessary, if want to compare file size)
## How to run the code:
1) Open terminal.
2) Enter the repository folder.
3) Terminal command: ` sh run.sh `
4) Output will be a file **SomeFile.txt** with text which is also displayed on the terminal.
5) Terminal command: `python3 size_comp.py` to print the compression ratio and size of file.
6) Output will be two files: **Original.txt** and **Compressed.txt**, and their sizes can be simultaneously compared. 

## References:
- http://kerseykyle.com/articles/ARM-assembly-hello-world
- Codes for reading files and printing in terminal.(We did take reference)
