class Spreadsheet:
    def __init__(self, rows: int):
        self.setCells = {}
        self.maxR = rows

    def setCell(self, cell: str, value: int) -> None:
        if 1 <= int(cell[1:]) <= self.maxR:
            self.setCells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.setCells:
            del self.setCells[cell]

    def getValue(self, formula: str) -> int:
        s = 0
        for dt in formula[1:].split('+'):
            if dt[0].isalpha():
                if dt in self.setCells:
                    s += self.setCells[dt]
            else:
                s += int(dt)
        return s
