a=5
b=2

try:
    print("resouce open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)

except ZeroDivisionError as e:
      print("hey,you cannot divide",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something went wrong")
finally:
      print("resouce closed")
