import csv, json, math, os, random, statistics, time
from rfs import rfs_sort, ResourceVector
from rfs.algorithms import merge_sort, quick_sort, indirect_sort, certificate_partition_sort

OUT="artifacts"
os.makedirs(OUT,exist_ok=True)

def datasets(n,seed=42):
    rng=random.Random(seed)
    uniform=[rng.randrange(0,10*n) for _ in range(n)]
    nearly=list(range(n))
    for _ in range(max(1,n//100)):
        i,j=rng.randrange(n),rng.randrange(n); nearly[i],nearly[j]=nearly[j],nearly[i]
    clustered=[]
    for b in range(100):
        base=b*100000
        clustered.extend(base+rng.randrange(1000) for _ in range(n//100))
    while len(clustered)<n: clustered.append(rng.randrange(1000))
    rng.shuffle(clustered)
    return {"uniform":uniform,"nearly_sorted":nearly,"clustered":clustered}

def timed(fn,xs,reps=3):
    ts=[]; out=None
    for _ in range(reps):
        a=list(xs); t=time.perf_counter(); out=fn(a); ts.append(time.perf_counter()-t)
    assert out==sorted(xs)
    return statistics.median(ts)

rows=[]
for n in [1000,5000,10000]:
    for kind,xs in datasets(n).items():
        span=max(xs)-min(xs)+1 if xs else 1
        width=max(1,math.ceil(span/32))
        cert=lambda x,w=width,m=min(xs): (x-m)//w
        algs={"python_timsort":lambda a:sorted(a),"merge_sort":lambda a:merge_sort(a),"quick_sort":lambda a:quick_sort(a),"indirect_sort":lambda a:indirect_sort(a),"certificate_partition":lambda a:certificate_partition_sort(a,cert),"rfs":lambda a:rfs_sort(a,certificate=cert)[0]}
        for name,fn in algs.items():
            rows.append({"n":n,"dataset":kind,"algorithm":name,"seconds":timed(fn,xs)})

with open(f"{OUT}/benchmark.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

resource_rows=[]
for n in [1000,5000,10000,50000]:
    rng=random.Random(n); xs=[rng.randrange(0,10*n) for _ in range(n)]
    width=max(1,(10*n)//32); cert=lambda x,w=width:x//w
    for profile,weights in {"comparison_expensive":ResourceVector(comparisons=10,time=1),"write_expensive":ResourceVector(comparisons=1,writes=100,time=1),"balanced":ResourceVector(comparisons=1,time=1,writes=1,movement=1)}.items():
        out,m=rfs_sort(xs,certificate=cert,weights=weights); assert out==sorted(xs)
        resource_rows.append({"n":n,"profile":profile,**m})

with open(f"{OUT}/resource_metrics.csv","w",newline="") as f:
    keys=resource_rows[0].keys(); w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); w.writerows(resource_rows)

summary={"claim":"RFS is experimental resource-relative exact sorting; no universal asymptotic speedup is claimed.","benchmark_rows":len(rows),"resource_rows":len(resource_rows),"datasets":["uniform","nearly_sorted","clustered"],"algorithms":["python_timsort","merge_sort","quick_sort","indirect_sort","certificate_partition","rfs"]}
with open(f"{OUT}/summary.json","w") as f: json.dump(summary,f,indent=2)
print(json.dumps(summary,indent=2))
