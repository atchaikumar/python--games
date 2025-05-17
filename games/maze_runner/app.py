import tkinter as tk
import time

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 'S', 0, 1, 0, 0, 0, 'E', 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

CELL_SIZE = 40
ROWS = len(maze)         # 7
COLS = len(maze[0])      # 9

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Runner Game")
        
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()

        self.status_label = tk.Label(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=5)

        reset_btn = tk.Button(root, text="Reset Game", command=self.reset_game, bg="red", fg="white")
        reset_btn.pack(pady=5)

        self.start_pos = self.find_start()
        self.reset_game()

        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.update_timer()

    def find_start(self):
        for r in range(ROWS):
            for c in range(COLS):
                if maze[r][c] == 'S':
                    return (r, c)
        return (1, 1)  # Default fallback

    def reset_game(self):
        self.player_pos = self.start_pos
        self.steps = 0
        self.start_time = time.time()
        self.game_over = False
        self.status_label.config(text="Steps: 0 | Time: 0s")
        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                val = maze[row][col]
                color = "white"
                if val == 1:
                    color = "black"
                elif val == 'S':
                    color = "green"
                elif val == 'E':
                    color = "red"
                self.canvas.create_rectangle(
                    col * CELL_SIZE, row * CELL_SIZE,
                    (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE,
                    fill=color, outline="gray"
                )
        r, c = self.player_pos
        self.canvas.create_oval(
            c * CELL_SIZE + 10, r * CELL_SIZE + 10,
            (c + 1) * CELL_SIZE - 10, (r + 1) * CELL_SIZE - 10,
            fill="blue"
        )

    def move(self, dr, dc):
        if self.game_over:
            return
        r, c = self.player_pos
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < ROWS and 0 <= new_c < COLS and maze[new_r][new_c] != 1:
            self.player_pos = (new_r, new_c)
            self.steps += 1
            self.draw_maze()
            self.status_label.config(text=f"Steps: {self.steps} | Time: {int(time.time() - self.start_time)}s")
            if maze[new_r][new_c] == 'E':
                self.win_game()

    def win_game(self):
        self.game_over = True
        time_taken = int(time.time() - self.start_time)
        self.canvas.create_text(
            COLS * CELL_SIZE // 2, ROWS * CELL_SIZE // 2,
            text=f"YOU WIN!\nSteps: {self.steps}\nTime: {time_taken}s",
            font=("Arial", 20, "bold"), fill="orange"
        )

    def update_timer(self):
        if not self.game_over:
            elapsed = int(time.time() - self.start_time)
            self.status_label.config(text=f"Steps: {self.steps} | Time: {elapsed}s")
        self.root.after(1000, self.update_timer)

    def move_up(self, event): self.move(-1, 0)
    def move_down(self, event): self.move(1, 0)
    def move_left(self, event): self.move(0, -1)
    def move_right(self, event): self.move(0, 1)

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()
