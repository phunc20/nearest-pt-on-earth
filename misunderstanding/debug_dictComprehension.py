import numpy as np

ps = range(1, 4)
#ps = list(range(1, 4))
norms = { p: (lambda x: np.linalg.norm(x, ord=p)) for p in ps }
#norms = { p: lambda x: np.linalg.norm(x, ord=p) for p in ps }
print(f"norms = {norms}")

a = np.array([3,4])
b = np.array([-3,7])
for p in ps:
    print(f"norms[{p}](a-b) = {norms[p](a-b)}")
