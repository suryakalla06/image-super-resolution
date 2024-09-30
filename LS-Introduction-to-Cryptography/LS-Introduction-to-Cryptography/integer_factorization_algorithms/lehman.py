from gmpy2 import *


def cuberoot(n):
  a,b = iroot(n,3)
  return a


def lehman(n):
    """
    based on: https://programmingpraxis.com/2017/08/22/lehmans-factoring-algorithm/
    """
    if is_congruent(n, 2, 4):
        return []

    for k in range(1, cuberoot(n), 1):
        nk4 = n*k << 2
        ki4 = isqrt(k) << 2
        ink4 = isqrt(nk4) + 1
        i6,_ = iroot(n, 6)
        ink4i6ki4 = ink4 + (i6 // (ki4))
        for a in range(ink4, ink4i6ki4 + 1, 2):
            b2 = (a * a) - nk4
            if is_square(b2):
                b = isqrt(b2)
                p = gcd(a + b, n)
                q = gcd(a - b, n)
                return p, q
    return []

def tests():
  N = [124620366781718784065835044608106590434820374651678805754818788883289666801188210855036039570272508747509864768438458621054865537970253930571891217684318286362846948405301614416430468066875699415246993185704183030512549594371372159029236099]
  for n in N:
    p,q = lehman(n)
    print(n,p,q)
    assert p*q == n

if __name__ == "__main__":
  tests()

