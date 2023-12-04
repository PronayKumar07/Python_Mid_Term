class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall_object):
        if isinstance(hall_object, Hall):
            self.__hall_list.append(hall_object)
        else:
            print('INVALID INPUT')   

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info) 

        list_2d = []
        for i in range(self.__rows):
            temp = []
            for j in range(self.__cols):
                temp.append(0)    
            list_2d.append(temp)
        self.__seats[id] = list_2d

    def book_seats(self, id, seat_list):
        self.id = id
            
        for row, col in seat_list:
    
            if self.__rows <= row or self.__cols <= col:
                print('INVALID SEAT')

            else:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                    print(f'SHOW ID : {id} SEAT {row, col} IS BOOKED')
                else:
                    print('THAT SEAT IS ALREADY BOOKED')             


    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self,id):
        if id in self.__seats:
            return self.__seats[id]
        

hall1 = Hall(rows = 5, cols = 5, hall_no = 1)
hall2 = Hall(rows = 5, cols = 5, hall_no = 2)

hall1.entry_show(id = '101', movie_name = 'Movie Name : MUJIB THE MAKING OF NATION', time = 'Time : 10:00 PM')
hall2.entry_show(id = '201', movie_name = 'Movie Name : OPPENHEIMER', time = 'Time : 07:00 PM')

while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEAT')
    print('3. BOOK TICKET')
    print('4. EXIT')

    ch = int(input('ENTER OPTION: '))
    
    if ch == 1:
        print(hall1.view_show_list())
        print(hall2.view_show_list())
    
    elif ch == 2:
        id = input("ENTER SHOW ID : ")
        
        if id == '101' or id == '201':
            print(f'AVAILABLE SEAT FOR SHOW ID {id}:')

            if id == '101':
                print(hall1.view_available_seats(id))
            elif id == '201':
                print(hall2.view_available_seats(id))
        else:
            print('ID IS WRONG. PLEASE GIVE RIGHT ID')

    elif ch == 3:
        Id = input("ENTER SHOW ID : ")

        if Id == '101' or Id == '201':
            if Id == '101':
                n = int(input("ENTER NUMBER OF TICKET: "))

                booking_seats = []
                for i in range(n):
                    row = int(input("Enter Seat Row : "))
                    col = int(input("Enter Seat Col: "))
                    booking_seats.append((row,col))
                    hall1.book_seats(id = Id, seat_list = booking_seats)
            else:
                n = int(input("ENTER NUMBER OF TICKET: "))

                booking_seats = []
                for i in range(n):
                    row = int(input("Enter Seat Row : "))
                    col = int(input("Enter Seat Col: "))
                    booking_seats.append((row,col))                
                    hall2.book_seats(id = Id, seat_list = booking_seats)
        else:
            print('ID IS WRONG. PLEASE GIVE RIGHT ID')
  
    elif ch == 4:
        print("EXIST")
        break