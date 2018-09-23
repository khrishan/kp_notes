# with open('binary', 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i])) # we should't need to puta for loop as bytes takes a list

# with open('binary', 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes(range(17)))

# with open('binary', 'br') as bin_file:
#     for b in bin_file:
#         print(b)

# x07 is a beep character

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open('binary2', 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big')) # stores the MSB first (how you'd write it)
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big')) # only need three but convention to have an even number of bits
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little')) # opposite to big

with open('binary2', 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)