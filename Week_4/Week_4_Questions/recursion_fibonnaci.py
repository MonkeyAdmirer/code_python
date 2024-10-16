
def fib(x):
    memory = {0 : 0, 1: 1}

    def helper(n):
        if n in memory:
            return memory[n]
        else:
            memory[n] = helper(n-1) + helper(n-2)
            return helper[n]
        
    return helper(x)
# end of fib
print(f"The {10}th fibonnaci number is: {fib(10)}")