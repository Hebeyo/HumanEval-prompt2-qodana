def search(lst):
    frq = {}
    for i in lst:
        frq[i] = frq.get(i, 0) + 1;
    ans = -1
    for i in frq:
        if frq[i] >= i:
            ans = max(ans, i)
    
    return ans
