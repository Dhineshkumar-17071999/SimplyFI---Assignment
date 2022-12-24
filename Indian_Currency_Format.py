import decimal 
def currencyInIndiaFormat(n):
  decimal_format = decimal.Decimal(str(n))  # Simultaneously Converting the integer into String format and converting the String into Decimal Format
  Currency = '{0:.2f}'.format(decimal_format) # Add Two more digits for the correct format
  length = len(Currency) # Find the length of the integer
  i = length - 1 
  result = '' # Initially asign the result variable with empty value
  flag = 0 
  k = 0
  while i>=0:
    if flag==0:
      result = result + Currency[i] # Adding numbers in result variable in reverse order
      if Currency[i]=='.': 
        flag = 1
    elif flag==1:
      k = k + 1
      result = result + Currency[i] # Adding numbers in result variable in reverse order
      if k==3 and i-1>=0: # Finding the currency format to add ','.
        result = result + ',' # Adding ',' in result variable
        flag = 2
        k = 0
    else:
      k = k + 1
      result = result + Currency[i]
      if k==2 and i-1>=0: # Finding the currency format to add ','.
        result = result + ',' # Adding ',' in result variable
        flag = 2
        k = 0
    i = i - 1 # To get the numbers from last
  result = result[::-1] # Store the values in Correct Order
  return result[:-3] # Remove the last three index and return the output

if __name__ == "__main__": # Main function Starting
  numbers = int(input()) # Get the integer value from user
  print(currencyInIndiaFormat(numbers))  # Calling the currencyInIndianFormat Function