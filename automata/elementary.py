import taichi as ti
import numpy as np

# rules
rule_30 = [0, 1, 1, 1, 1, 0, 0, 0]
rule_90 = [0, 1, 0, 1, 1, 0, 1, 0]
rule_110 = [0, 1, 1, 0, 1, 1, 1, 0]
rule_184 = [1, 0, 1, 1, 1, 0, 0, 0]
experiment = [0, 1, 0, 0, 1, 0, 1, 0]


def elementary(grid_size, rule_array):
    ti.init(arch=ti.gpu)  # or ti.cpu

    # grid size
    N = grid_size
    STEPS = grid_size

    # taichi fields
    state = ti.field(dtype=ti.i32, shape=N)
    next_state = ti.field(dtype=ti.i32, shape=N)
    grid = ti.field(dtype=ti.f32, shape=(STEPS, N))

    # rule stuff
    rule = ti.field(dtype=ti.i32, shape=8)
    rule.from_numpy(np.array(rule_array, dtype=np.int32))

    @ti.kernel
    def initialize():
        for i in range(N):
            state[i] = 0
        state[N // 2] = 1  # single active cell

    @ti.kernel
    def step(t: ti.i32):
        for i in range(N):
            left = state[(i - 1 + N) % N]
            center = state[i]
            right = state[(i + 1) % N]

            idx = left * 4 + center * 2 + right
            next_state[i] = rule[idx]

        for i in range(N):
            state[i] = next_state[i]
            grid[t, i] = state[i]

    gui = ti.GUI("playground", res=(N, STEPS))

    initialize()

    t = 0
    while gui.running:
        if t < STEPS:
            step(t)
            t += 1

        # draw grid
        gui.set_image(grid.to_numpy())
        gui.show()
