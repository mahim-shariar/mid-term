
class Star_Cinema:

    __hall_list = []

    def entry_hall(self, hall_obj):
        self.__hall_list.append(hall_obj)



class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        self.__seats = {}
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        movie = (id, movie_name, time)
        self._show_list.append(movie)
        seat = []
        for i in range(self.rows+1):
            row = []
            for j in range(self.cols+1):
                row.append(0)
            seat.append(row)
        self.__seats[id] = seat

    def book_seats(self, id, row, col):
        if id in self.__seats:
            if 0 <= row <= self.rows and 0 <= col <= self.cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                    print(f"\n\tSeat {row, col} booked successfully !\n")
                else:
                    print('\nThis seat booked already !')
            else:
                print("\nYou give a invalid seat number  !")
        else:
            print("\nThis Show dose not exisit !")

    def view_show_list(self):
        for list in self._show_list:
            print(f"ID: {list[0]}, Movie: {list[1]}, Time: {list[2]}")

    def view_available_seat(self, id):
        if id in self.__seats:
            print(
                f"------------------Available seats For movie Id : {id}------------------")
            for i in range(self.rows+1):
                for j in range(self.cols+1):
                    if self.__seats[id][i][j] == 0:
                        print(f"Seat: ({i}, {j})")

            print(f"\nUpdated sit matrix: {id}\n")
            for i in range(self.rows+1):
                for j in range(self.cols+1):
                    if self.__seats[id][i][j] == 0:
                        print("0", end=" ")
                    else:
                        print("1", end=" ")
                print('')
            print('\n')

            print("---------------------------------------------------------------")
        else:
            print("Invalid ID")


star = Star_Cinema()
hall = Hall(5, 5, 2)
star.entry_hall(hall)

hall.entry_show(6969, "Avengers end game", "10:00 AM")
hall.entry_show(6767, "Spider man", "2:00 PM")

run = True

while run:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

    ch = int(input("Enter Option: "))

    if ch == 1:
        print("----------------------Availavle Shows Today-----------------------")
        hall.view_show_list()
        print("------------------------------------------------------------------")
    elif ch == 2:
        movie_id = int(input("Enter Your Movie Id: "))
        hall.view_available_seat(movie_id)
    elif ch == 3:
        movie_id = int(input("Enter Your Movie Id: "))
        row = int(input("Enter Seat Row: "))
        col = int(input("Enter Seat col: "))
        hall.book_seats(movie_id, row, col)
    elif ch == 4:
        run = False
