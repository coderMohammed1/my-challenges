# this will implemnt python round method in anoter way
# try it yourself before taking a look

def round2(n:float,places:int):
    """
    round numbers to a chosen number of places

    
    :param n: the number you want to round (float)
    :param places: the number of places you want to round to (int)

        return -1  
    :type n: float
    :type places: int
    :return: return a float(rounded number)
    :rtype: float
    :time and memory complexity: O(1) [constant (too fast and good)]
    """
    if places>0:
      mult=10**(places+1)
      n=int(n*mult)

      lastdigit=n%10
      n=int(n/10)

      if lastdigit>=5:
         n=n+1
         n=n/(mult/10)
         return n
      else:
            n=n/(mult/10)
            return n
    else:
