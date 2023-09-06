# from functions import trig, globalFuncs, statistics
# import curses
# from curses import textpad



# def draw_menu(stdscr):
#     functions = []
#     k = 1
#     mode = "FUNCTION"
#     stdscr.clear()
#     stdscr.refresh()
#     curses.start_color()
#     curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
#     while (k != ord('q')):
#         height, width = stdscr.getmaxyx()
#         statusbarstr = "WIDTH: {}, HEIGHT: {}".format(width, height) + " | MODE: {}".format(mode)
#         stdscr.attron(curses.color_pair(3))
#         stdscr.addstr(height-1, 0, statusbarstr)
#         stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
#         stdscr.attroff(curses.color_pair(3))
#         stdscr.refresh()
#         k = stdscr.getch()
#         mode = detectShortCut(stdscr, k, mode)
#         if mode == "FUNCTION":
#             draw_functions(stdscr, functions)
#         elif mode == "GRAPH":
#             draw_graph(stdscr, functions)
#         elif mode == "STATISTICS":
#             draw_statistics(stdscr)
#         elif mode == "VIEW":
#             draw_view(stdscr)
#         else:
#             stdscr.addstr(0, 0, "ERROR: Mode not found")
#             stdscr.refresh()

# def draw_functions(stdscr, functions):
#     height, width = stdscr.getmaxyx()
#     rows = height // 5
#     cols = width // 48
#     stdscr.clear()
#     for i in range(cols):
#         for j in range(rows):
#             stdscr.addstr(j*5, i*48, "Function {}".format(i*rows + j + 1), curses.A_BOLD)
#             stdscr.addstr(j*5 + 1, i*48, "f(x) = ")
#     k = ""
#     curses.curs_set(1)
#     stdscr.move(1, 7)
#     line = 1
#     column = 7
#     while k != 27:
#         k = stdscr.getch()
#         # allow fo user to type in function in front of f(x) = and wait for enter
#         # if enter is pressed, add function to list of functions
#         # if esc is pressed, return to menu
#         # if backspace is pressed, delete last character
#         # if delete is pressed, delete entire line
#         # if up is pressed, move up one line
#         # if down is pressed, move down one line
#         # if left is pressed, move left one character
#         # if right is pressed, move right one character

#         if k == curses.KEY_UP:
#             if line == 1:
#                 pass
#             else:
#                 line -= 5
#                 stdscr.move(line, 7)
#         elif k == curses.KEY_DOWN:
#             if line == rows:
#                 pass
#             else:
#                 line += 5
#                 stdscr.move(line, 7)
#         elif k == curses.KEY_LEFT:
#             if column == 7:
#                 pass
#             else:
#                 column -= 1
#                 stdscr.move(line, column)
#         elif k == curses.KEY_RIGHT:
#             if column == 48:
#                 pass
#             else:
#                 column += 1
#                 stdscr.move(line, column)
#         elif k == curses.KEY_BACKSPACE:
#             if column == 7:
#                 pass
#             else:
#                 column -= 1
#                 stdscr.addstr(line, column, " ")
#                 stdscr.move(line, column)
#         elif k == curses.KEY_DC:
#             column = 7
#             stdscr.move(line, column)
#             for i in range(41):
#                 stdscr.addstr(line, column + i, " ")
#             stdscr.move(line, column)
#         elif k == 10:
#             pass
#         else:
#             stdscr.addstr(line, column, chr(k))
#             column += 1
#             stdscr.move(line, column)
                
#     stdscr.refresh()


# def draw_graph(stdscr, functions):
#     stdscr.clear()
#     stdscr.addstr(0, 0, "Graph")
#     stdscr.refresh()

# def draw_statistics(stdscr):
#     stdscr.clear()
#     stdscr.addstr(0, 0, "Statistics")
#     stdscr.refresh()

# def draw_view(stdscr):
#     stdscr.clear()
#     stdscr.addstr(0, 0, "View")
#     stdscr.refresh()
            

# def detectShortCut(stdscr, k, mode):
#     if k == 32:
#         k = stdscr.getch()
#         if k == ord('f'):
#             return "FUNCTION"
#         elif k == ord('g'):
#             return "GRAPH"
#         elif k == ord('s'):
#             return "STATISTICS"
#         elif k == ord('v'):
#             return "VIEW"
#         else:
#             return mode
#     else:
#         return mode

# def main():
#     curses.wrapper(draw_menu)

# if __name__ == "__main__":
#     main()

from rich.table import Table

from textual import events
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Static, Input, DataTable


class graph(Static):
    """The physical graph displayed on the screen"""
    def on_mount(self) -> None:
        grid = Table.grid()
        grid.add_column()
        grid.add_column()
        grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
        self.update(grid)
    

class functionEntryBox(Static):
    """An entry box for a function"""
    def compose(self) -> ComposeResult:
        yield Input(classes="inputBox")


class consoleCalc(App):
    TITLE = "Console Graphing Calculator"
    CSS_PATH = "main.tcss"
    BINDINGS = [
        ("a", "add_entryBox", "Add EntryBox"),
        ("r", "remove_entryBox", "Remove EntryBox"),
        ("q", "quit", "Quit")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield graph()
        yield ScrollableContainer(functionEntryBox(), functionEntryBox(), functionEntryBox(), classes="functionEntryBoxesContainer", id="entryBoxes")
        

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_add_entryBox(self) -> None:
        new_entryBox = functionEntryBox()
        self.query_one("#entryBoxes").mount(new_entryBox)
        new_entryBox.scroll_visible()
    
    def action_remove_entryBox(self) -> None:
        entryBoxes = self.query("functionEntryBox")
        if len(entryBoxes) > 3:
            entryBoxes.last().remove()

if __name__ == "__main__":
    app = consoleCalc()
    app.run()