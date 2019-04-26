"""
Work done by Varshil, Aniket and Shreyas
"""
# Delete old object & executable files
rm -rf *.o
rm -rf huffman
# Create all object files using assembler
arm-linux-gnueabihf-as -g  -o syscalls.o syscalls.s
arm-linux-gnueabihf-as -g  -o numbers.o numbers.s
arm-linux-gnueabihf-as -g  -o strings.o strings.s
arm-linux-gnueabihf-as -g  -o files.o files.s
arm-linux-gnueabihf-as -g  -o errors.o errors.s
arm-linux-gnueabihf-as -g  -o count.o count.s
arm-linux-gnueabihf-as -g  -o huffman.o huffman.s
# Link those object files using a linker
arm-linux-gnueabihf-ld  syscalls.o numbers.o strings.o files.o errors.o count.o huffman.o -o huffman
# Run the executable file
qemu-arm huffman 2>&1 | tee SomeFile.txt
