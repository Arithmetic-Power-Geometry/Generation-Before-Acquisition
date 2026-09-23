from __future__ import annotations
import math
from collections import defaultdict
from .model import ResourceVector

def _entropy_proxy(groups):
    h=0.0
    for g in groups.values():
        h += math.lgamma(len(g)+1)/math.log(2) if len(g)>1 else 0.0
    return h

def rfs_sort(xs, key=lambda x:x, certificate=None, weights=ResourceVector(time=1, comparisons=1)):
    xs=list(xs)
    if len(xs) <= 1:
        return xs, {"entropy_before":0.0,"entropy_after":0.0,"resource_cost":0.0,"groups":len(xs),"fallback":False}
    if certificate is None:
        out=sorted(xs,key=key)
        n=len(xs)
        cost=n*math.log2(max(n,2))*weights.comparisons
        return out, {"entropy_before":math.lgamma(n+1)/math.log(2),"entropy_after":0.0,"resource_cost":cost,"groups":1,"fallback":True,"comparisons_proxy":n*math.log2(max(n,2))}
    groups=defaultdict(list)
    for x in xs:
        groups[certificate(x)].append(x)
    h0=_entropy_proxy(groups)
    out=[]
    comparisons_proxy=0.0
    for b in sorted(groups):
        g=groups[b]
        out.extend(sorted(g,key=key))
        if len(g)>1:
            comparisons_proxy += len(g)*math.log2(len(g))
    exact=sorted(xs,key=key)
    fallback = out != exact
    if fallback:
        out=exact
        comparisons_proxy=len(xs)*math.log2(len(xs))
    rv=ResourceVector(comparisons=comparisons_proxy)
    return out, {"entropy_before":h0,"entropy_after":0.0,"resource_cost":rv.scalar(weights),"groups":len(groups),"fallback":fallback,"comparisons_proxy":comparisons_proxy}
