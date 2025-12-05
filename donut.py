import numpy as np
import time
from IPython.display import clear_output

A = 0
B = 0

while True:
    clear_output(wait=True)
    output = []
    z = np.zeros(1760)
    b = [' '] * 1760

    for j in np.linspace(0, 6.28, 90):
        for i in np.linspace(0, 6.28, 90):
            c = np.sin(i)
            d = np.cos(j)
            e = np.sin(A)
            f = np.sin(j)
            g = np.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = np.cos(i)
            m = np.cos(B)
            n = np.sin(B)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y

            if 0 <= o < 1760:
                if D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[int(8 * ((l * h * n + t * m)) % 11)]

    # Join output lines
    for k in range(22):
        output.append("".join(b[k*80:(k+1)*80]))

    print("\n".join(output))

    A += 0.06
    B += 0.04
    time.sleep(0.02)
