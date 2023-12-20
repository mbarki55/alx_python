def fibonacci_sequence(n):
    fibonacci =[0,1]
    while len(fibonacci) < n:
        next_numb = fibonacci[-1]+ fibonacci[-2]
        fibonacci = n + next_numb
    return fibonacci [:n]
   

