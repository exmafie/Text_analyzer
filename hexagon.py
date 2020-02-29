from turtle import left, forward, right, exitonclick, penup, pendown

for k in range(6):
    right(60)
    forward(50)
    for i in range(5):
        left(60)
        forward(50)
    right(180)
    forward(50)
exitonclick()

print(len(num),leno*'*', leno)
