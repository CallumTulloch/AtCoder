S = input()
chars = ['A','C','G','T']
seq_len=0
max_len=0
for s in S:
    if s in chars:
        seq_len += 1
    else:
        seq_len = 0
    if(max_len < seq_len):
        max_len = seq_len
print(max_len)