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
  if (x == 0) {
    return ("undefined")
  }
  else if (y == 0) {
    return("undefined")
  }
  else return(x / y)
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
print("5.Exponent")
print("6.Cube")
print("7.Square")
print("8.Exponential")
print("9.RectanglePerimeter")
print("10.Pythagorus")
print("11.Sine")

choice = as.integer(readline(prompt="Enter choice: "))

num1 = as.integer(readline(prompt="Enter first number: "))
num2 = as.integer(readline(prompt="Enter second number: "))

operator <- switch(choice,"add","subtract","multiply","divide","exponent","cube","square","exponential","rectanglePerimeter","pythagorus","sine")
result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), exponent(num1, num2), cube(num1), square(num1), exponential(num1),rectanglePerimeter(num1, num2),pythagorus(num1, num2), sin(num1, num2))

print(paste("First number:",num1,"Second number:", num2, "Operator:",operator, "Result:", result))