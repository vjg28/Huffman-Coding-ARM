# Huffman-Coding-ARM
## Warning**
- The tree is implemented using an [array](https://nptel.ac.in/courses/106103069/51), and the architecture supports 32 bits registers, so there is a limitation on the maximum index value that can be stored. The maximum value of the tree index is 2^32 -1 (limit for int values). 
- If the tree has 32 or more elements, then in the worst case condition, the index value may exceed the limit and the code will not perform as expected. So, if anyone plans to try a new ***file.txt***, do ensure that it has less than 32 unique characters for huffman coding to work. Other than that, the code is entirely designed to take all 256 ascii characters and will perform as expected till the tree indexing part.
## Prerequisites:
- Linux (Ubuntu- 16.04) 
- Qemu Emulator
  - `sudo apt install binfmt-support qemu qemu-user-static`
- 32-bit Armv7 Cortex-A, hard-float, little-endian [Link](https://releases.linaro.org/components/toolchain/binaries/latest-7/)
  - `sudo apt install binutils-arm-linux-gnueabihf`
- Python (Not necessary, if want to compare file size)
## How to run the code:
1) Open terminal.
2) Enter the repository folder.
3) Terminal command: ` sh run.sh `
4) Output will be a file **SomeFile.txt** with text which is also displayed on the terminal.
5) Terminal command: `python3 size_comp.py` to print the compression ratio and size of file.
6) Output will be two files: **Original.txt** and **Compressed.txt**, and their sizes can be simultaneously compared. 

## File Structure
- huffman.s (Original work)
  - count.s (Original work)
    - all other files (Helper functions)

Do read `run.sh` before running the code. Every major function called in `huffman.s` is from `count.s` and only helper files are referenced from some other places.
## References:
- http://kerseykyle.com/articles/ARM-assembly-hello-world
- Codes for reading files and printing in terminal.(We did take reference from some other people's work.)

## TO DO:
- Tree implementation without array
