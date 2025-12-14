def number_generator(start, stop):
    for count in range(start,stop+1):
        print(count)

start_num = int(input("Enter a start value"))
stop_num = int(input("Enter a stop value"))

number_generator(start_num, stop_num)