import turtle
turtle.showturtle()
turtle.hideturtle()
list0 = turtle.textinput("piechart","input a string:")
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
def vowelCount(string0):
  a = 0
  e = 0
  i = 0
  o = 0
  u = 0
  for c in string0:
    if c =='a' or c == 'A':
      a +=1
    if c =='e' or c == 'E':
      e +=1
    if c =='i' or c == 'I':
      i +=1
    if c =='o' or c == 'O':
      o +=1
    if c =='u' or c == 'U':
      u +=1
  return [a,e,i,o,u]
def pieChart(flist):
    vList = vowelCount(flist)
    c = 0
    s = 0
    i = 0
    slist = ["A","E","I","O","U"]
    s = vList[0]+vList[1]+vList[2]+vList[3]+vList[4]
    for f in vList:
        if i == 0:
            turtle.color("red")
        elif i == 1:
            turtle.color("blue")
        elif i == 2:
            turtle.color("green")
        elif i == 3:
            turtle.color("yellow")
        else:
            turtle.color("orange")
        turtle.begin_fill()
        turtle.circle(100,vList[i]/s*360)
        x = turtle.xcor()
        y = turtle.ycor()
        turtle.goto(0,0)
        turtle.end_fill()
        turtle.penup()
        turtle.right(vList[i]/s*180+90)
        turtle.fd(turtle.distance(x,y)/2)
        turtle.color("black")
        if f != 0:
            turtle.write(slist[i],True,"center",font=("Arial", 15, "normal"))
        turtle.goto(x,y)
        turtle.left(vList[i]/s*180+90)
        turtle.pendown()
        i += 1
def main():
    pieChart(list0)
if __name__ == '__main__':
    main()
