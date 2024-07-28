A=['abc', 'xyz', 'aba', '1221']

for itr in A :
    if itr[0] == itr[len(itr)-1] :
        print(f"Identical String {itr} found at index {A.index(itr)}")
