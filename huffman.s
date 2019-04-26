@@@ Main file for executing Huffman encoding (File name can be changed here)

@@@ External Methods
    .global status
    .global init_counts
    .global init_sorted_chars
    .global count_from_file
    .global print_counts
    .global sorted
    .global print_sorted
    .global sort_chars
    .global print_sorted
    .global open_read
    .global check_read_error
    .global exit
    .global close
    .global tree_start
    .global print_tree_arr
    .global num_tree
    .global print_num_arr

@@@ Exported Methods
    .global _start

@@@ Code Section
    
_start:
    BL      status              @ Print status
    BL      init_counts         @ Initialize memory
    LDR     R0, =in_path        @ Set file path
    BL      open_read           @ Open file for reading
    BL      check_read_error    @ Check for errors
    MOV     R4, R0              @ R4 = File Handle (Also still in R0)
    BL      count_from_file     @ Count characters from file handle
    BL      print_counts        @ Print counts
    BL      init_sorted_chars   @ Initialize memory
    BL      sort_chars          @ Sort characters
    BL      print_sorted        @ Print sorted characters
    BL      tree_start          @ Making tree
    BL      print_tree_arr      @ Print Tree array
    BL      num_tree            @ Create tree indexing array
    BL      print_num_arr       @ Print the above
    MOV     R0, R4              @ Set file handle to close
    BL      close               @ Close file
    MOV     R0, #0              @ Normal return code
    B       exit                @ exit

@@@ Data Section
    
    .data

in_path: .asciz "file1.txt"
out_path_1: .asciz "binary_file.txt"
out_path_2: .asciz "compressed_binary_file.txt"
