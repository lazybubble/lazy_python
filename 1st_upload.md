2nd Kata I solved on CodeWars.

The topic is Square Every Digit.

I used a lot of guidance from ChatGPT for remembering the available tools Python has as well as to how to properly use them.
At the beginning, thanks to some other exercises I was doing, I was able to think of the following built-in functions:
  .join
  str()
  int()
  **
  for x in y

  The most difficult part was putting the pieces together, and for that I also used ChatGPT guidance.
  Another problem I found was the fact that integers are not iterable with the for in loop, so the workaround with
  str() and int() was a little complicated too.
  This is what the final code looked like:

  
def square_digits(number):
    numbers = str(number)
    squared = ''.join(str(int(d)** 2) for d in numbers)
    return int(squared)

value = 5324
square_digits(value)

First step for building the function was converting the input (int) into a string by storing it into a new value.

  numbers = str(number)

Then the core of the function, which is where the actual squaring happens.

  squared = ''.join(str(int(d)**2) for d in numbers)

The most important part of the line is where the individual digits are converted into integers then squared
  
  int(d)**2

Then, to make it iterable, it was turned into a string
  
  str(int(d)**2) for d in numbers

Followed by the concatenation of the individual squared digits by storing it into a new variable

squared = ''.join(str(int(d)**2) for d in numbers)

Lastly, in order to return according to the tasks' parameters, the new variable had to be converted into an integer

return = int(squared)

