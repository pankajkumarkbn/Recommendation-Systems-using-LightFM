import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

dt = fetch_movielens(min_rating=5.0)

print(repr(dt['train']))
print(repr(dt['test']))
