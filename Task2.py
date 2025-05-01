class Parent:
    def __init__(self):
        self.matrix = [
            [2,3,1,1],
            [4,1,2,2],
            [3,2,3,3]
        ]
class Equations(Parent):

    def step1(self):
        for i in range(3):   #0,1,2
            mainnum=self.matrix[i][i]     #[i][i] => القطر الرئيسي

            for j in range(4):
                self.matrix[i][j]=self.matrix[i][j] / mainnum  # عشان اخلي القطر ب 1

            for k in range(i+1,3):
                zeros=self.matrix[k][i]     # الارقام اللي عايزاها تبقي ب صفر اللي تحت ال 1

                for j in range(4):
                    self.matrix[k][j]=self.matrix[k][j]-zeros*self.matrix[i][j]    #[[1 , 1.5, .5 , 0.5]
                                                                                    #[4,   1,    2,  2  ]
                                                                                    #[3,   2,    3,  3]]
    def display(self):
        for row in self.matrix:
            print(row)

    def solve(self):
        z = self.matrix[2][3]
        y = self.matrix[1][3] - self.matrix[1][2] * z
        x = self.matrix[0][3] - self.matrix[0][1] * y - self.matrix[0][2] * z
        return x, y, z

eq = Equations()
eq.step1()
eq.display()

x, y, z = eq.solve()
print("x = ", x)
print("y = ", y)
print("z = ", z)

