def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a = 0
    b = 1
    while a < n:
        print(a, end='    ')
        a, b = b, a+b
    # print('')

# Now call the function we just defined:
fib(2000)


# a = current val of b
# b = previous val of a + b
