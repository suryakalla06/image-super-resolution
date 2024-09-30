from gmpy2 import *

def factor(N):
  """
  Algorithm described in the wagstaf-joy of factoring book.
  """
  f = N1 = N - 1
  while f & 1 == 0: f >>= 1
  a = 2
  while a <= N1:
    r1 = powmod(a, f << 1, N) 
    if r1 == 1:
      r = powmod(a, f, N) 
      p = gcd(r - 1, N)
      q = gcd(r + 1, N)
      if (q > p > 1): #and (p * q == N):
        return factor(p) + factor(q)
    a = next_prime(a)
  return [N]

def tests():
  for n in [124620366781718784065835044608106590434820374651678805754818788883289666801188210855036039570272508747509864768438458621054865537970253930571891217684318286362846948405301614416430468066875699415246993185704183030512549594371372159029236099]:
    print(n, factor(n))

if __name__ == "__main__":
  tests()
