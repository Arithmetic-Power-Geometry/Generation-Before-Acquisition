def merge_sort(xs, key=lambda x: x):
    if len(xs) <= 1:
        return list(xs)
    m = len(xs)//2
    a = merge_sort(xs[:m], key)
    b = merge_sort(xs[m:], key)
    out=[]; i=j=0
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            out.append(a[i]); i+=1
        else:
            out.append(b[j]); j+=1
    out.extend(a[i:]); out.extend(b[j:])
    return out

def quick_sort(xs, key=lambda x: x):
    if len(xs) <= 1:
        return list(xs)
    p = key(xs[len(xs)//2])
    lo=[x for x in xs if key(x) < p]
    eq=[x for x in xs if key(x) == p]
    hi=[x for x in xs if key(x) > p]
    return quick_sort(lo,key)+eq+quick_sort(hi,key)

def indirect_sort(xs, key=lambda x: x):
    idx = sorted(range(len(xs)), key=lambda i: key(xs[i]))
    return [xs[i] for i in idx]

def certificate_partition_sort(xs, bucket, key=lambda x: x):
    groups={}
    for x in xs:
        groups.setdefault(bucket(x), []).append(x)
    out=[]
    for b in sorted(groups):
        out.extend(sorted(groups[b], key=key))
    exact=sorted(xs, key=key)
    return out if out == exact else exact
