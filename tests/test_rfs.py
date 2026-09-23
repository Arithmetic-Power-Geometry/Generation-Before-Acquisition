import random
from rfs import rfs_sort, ResourceVector
from rfs.algorithms import merge_sort, quick_sort, indirect_sort, certificate_partition_sort

def test_exact_without_certificate():
    xs=[5,1,9,2,2,7]
    out,m=rfs_sort(xs)
    assert out==sorted(xs)
    assert m["fallback"]

def test_sound_certificate():
    xs=list(range(1000))
    random.Random(1).shuffle(xs)
    out,m=rfs_sort(xs,certificate=lambda x: x//100)
    assert out==sorted(xs)
    assert m["groups"]==10
    assert not m["fallback"]

def test_unsound_certificate_falls_back():
    xs=[4,1,3,2]
    out,m=rfs_sort(xs,certificate=lambda x: x%2)
    assert out==sorted(xs)
    assert m["fallback"]

def test_baselines_exact():
    xs=[9,1,8,2,7,3,6,4,5]
    expected=sorted(xs)
    assert merge_sort(xs)==expected
    assert quick_sort(xs)==expected
    assert indirect_sort(xs)==expected
    assert certificate_partition_sort(xs,lambda x:x//3)==expected

def test_random_property():
    rng=random.Random(7)
    for n in [1,2,10,100,1000]:
        xs=[rng.randrange(0,10000) for _ in range(n)]
        assert rfs_sort(xs,certificate=lambda x:x//1000)[0]==sorted(xs)

def test_resource_scalarization():
    w=ResourceVector(time=1,writes=10,comparisons=2)
    c=ResourceVector(time=3,writes=4,comparisons=5)
    assert c.scalar(w)==53
