import taichi as ti

ti.init(arch=ti.gpu)

N = 1000

grid = ti.field(dtype=ti.f32, shape=(N, N))
next_grid = ti.field(dtype=ti.f32, shape=(N, N))


@ti.kernel
def initialize():
    for i, j in grid:
        grid[i, j] = ti.random(ti.i32) % 2


@ti.func
def count_neighbors(x, y):
    total = 0
    for dx in ti.static(range(-1, 2)):
        for dy in ti.static(range(-1, 2)):
            if dx != 0 or dy != 0:
                nx = (x + dx) % N
                ny = (y + dy) % N
                total += grid[nx, ny]
    return total


@ti.kernel
def update():
    for i, j in grid:
        n = count_neighbors(i, j)

        if grid[i, j] == 1:
            # alive
            if n < 2 or n > 3:
                next_grid[i, j] = 0
            else:
                next_grid[i, j] = 1
        else:
            # dead
            if n == 3:
                next_grid[i, j] = 1
            else:
                next_grid[i, j] = 0

    for i, j in grid:
        grid[i, j] = next_grid[i, j]


gui = ti.GUI("conways game of life", (N, N))

initialize()

while gui.running:
    update()
    gui.set_image(grid)
    gui.show()
