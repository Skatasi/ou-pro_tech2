def get_sqrt_by_bi(a):
    x = 1.0
    epsilon = 0.01
    step = abs(a-x)
    # x = 1.0 を中心に誤差がepsilon以下になるように二分探査する。
    while abs(x**2 - a)>=epsilon:
        step /= 2
        if x**2 > a:
            x -= step
        else:
            x += step
        if abs(x**2 - a) <= epsilon:
            return x

def get_sqrt_by_newton(a):
    x = 1.0
    epsilon = 0.01
    # x = 1.0 を中心に誤差がepsilon以下になるように二分探査する。
    while abs(x**2 - a)>=epsilon:
        func_x = x**2 - a
        funcd_x = 2*x
        x = x - func_x / funcd_x
        if abs(x**2 - a) <= epsilon:
            return x

def main():
    a = float(input("Please a positive integer: "))
    print("The square root of", a ,"is", get_sqrt_by_bi(a))

if __name__ == "__main__":
    main()