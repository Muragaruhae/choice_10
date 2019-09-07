S = input()
while len(S) >= 5:
    if len(S) >= 7 and S[-7:] == "dreamer":
        S = S[:-7]
        continue
    if len(S) >= 6 and S[-6:] == "eraser":
        S = S[:-6]
        continue
    elif S[-5:] == "dream" or S[-5:] == "erase":
        S = S[:-5]
        continue
    else:
        break
if len(S) == 0:
    print("YES")
else:
    print("NO")