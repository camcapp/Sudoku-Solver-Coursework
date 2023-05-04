def write_into(file_to_write: str, content: str):
    file_to_write = open(file_to_write, 'w')
    file_to_write.write(content)
    file_to_write.close()


grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]


# grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]

def get_row(line: str):
    line = line.removesuffix(']\n').removeprefix('[')
    numbers = line.split(',')
    row = []
    for e in numbers:
        row.append(int(e))

    return row


class FileManager:
    def __init__(self, file_to_read: str):
        self.file_name = file_to_read
        self.file = open(file_to_read)

    def read_grid(self):
        grid = []
        lines = self.file.readlines()
        j = int(lines.pop().removesuffix('\n'))
        i = int(lines.pop().removesuffix('\n'))
        for line in lines:
            row = get_row(line)
            grid.append(row)

        return [(grid, i, j)]

    def close(self):
        self.file.close()
