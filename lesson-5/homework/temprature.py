def c2f(c): return round(c * 9/5 + 32, 2)
def f2c(f): return round((f - 32) * 5/9, 2)
if __name__ == "__main__":
    print(f"{(f:=float(input('F: ')))}°F -> {f2c(f)}°C")
    print(f"{(c:=float(input('C: ')))}°C -> {c2f(c)}°F")
