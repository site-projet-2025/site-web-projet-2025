import turtle as t

t.setup(800,600)
t.shape("turtle")
t.speed(0)

nbr_points = 20## A la place du 20, mettez le nombre que vous souhaitez
esp_point = 360/nbr_points

coord_points = []

t.penup()
t.goto(0,-200)
t.pendown()

for _ in range(nbr_points) :
    t.dot(5,"blue")
    coord_points.append(t.position())
    t.circle(200,esp_point)

for i in range(200):
    t.penup()
    t.goto(coord_points[i%20])## A la place du 20, mettez le nombre que vous souhaitez
    t.pendown()
    t.goto(coord_points[(i*7)%20])## A la place du 20, mettez le nombre que vous souhaitez
                                  ## le 7 est le nombre à multiplier
index_dep = i
while index_dep >= 20 :## A la place du 20, mettez le nombre que vous souhaitez
    index_dep -= 20## A la place du 20, mettez le nombre que vous souhaitez
    print(index_dep)
  
t.goto(coord_points[index_dep])

t.pendown()
index_arr = i*7## le 7 est le nombre à multiplier
while index_arr >=20 :## A la place du 20, mettez le nombre que vous souhaitez
    index_arr -= 20## A la place du 20, mettez le nombre que vous souhaitez
t.goto(coord_points[index_arr])

print(coord_points)

t.exitonclick()