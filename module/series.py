# every python file is by default is a module, and the name of the module is name of the file without py extension
# name of the module is series
# house only library, reusable functions that generate mathematical series
def odd_series(n):
    series = ''
    for i in range(1, n+1, 2):
        series += str(i) + ' '
    return series

def even_series(n):
    series = ''
    for i in range(0, n+1, 2):
        series += str(i) + ' '
    return series