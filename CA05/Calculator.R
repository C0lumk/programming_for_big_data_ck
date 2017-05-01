# Program for a simple calculator with 10 functions

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x, y) {
  
  return(x / y)
}

exponent <- function(x, y) {
  return(x ** y)
}

cube <- function(x) {
  return(x ** 3)
}

square <- function(x) {
  return(x ** 2)
}

exponential <- function(x) {
  round(exp(x),2)
}

rectanglePerimeter <- function(x,y) {
  return((x+y) * 2)
}

pythagorus <- function(x,y) {
  round(sqrt(x ** 2 + y ** 2),2)
}

sin <- function(x) {
  sin(x)
}

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = as.integer(readline(prompt="Enter choice[1/2/3/4]: "))

num1 = as.integer(readline(prompt="Enter first number: "))
num2 = as.integer(readline(prompt="Enter second number: "))

operator <- switch(choice,"+","-","*","/")
result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2))

print(paste(num1, operator, num2, "=", result))