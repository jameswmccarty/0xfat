"""

Level 29

You see a room which is 10x10m wide (0x0 to 9x9).
Every square has the exact temperature of 19°C. We apply continuously 176°C heat to the field 0x3
What is the temperature (rounded to whole numbers) in the field 5x7 after 61 iterations according to the Gauss-Seidel iteration

//field is an 2D array
//heat is also an 2D array that only contains the heat that should be applied to field
for(var i=0;i<canvas.width/cellsize;i++)
        for(var j=0;j<canvas.height/cellsize;j++)
            field[i][j] = (0.25 * (field[i-1][j]+field[i+1][j]+field[i][j-1]+field[i][j+1]) + heat[i][j]);

"""

initial_temp = 19
input_heat   = 176
input_field  = (0,3)
measure_field = (5,7)
iterations    = 61

board = []
for _ in range(10):
	board.append([initial_temp]*10)

def step():
	global board
	for j in range(10):
		for i in range(10):
			new_heat = 0
			for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
				nx,ny = i+dx,j+dy
				if nx >= 0 and nx < 10 and ny >=0 and ny < 10:
					new_heat += board[ny][nx]
			new_heat *= 0.25
			if (i,j) == input_field:
				new_heat += input_heat
			board[j][i] = new_heat

for _ in range(iterations+1):
	step()

for line in board:
	print([ round(x) for x in line ])
print(round(board[measure_field[1]][measure_field[0]]))
