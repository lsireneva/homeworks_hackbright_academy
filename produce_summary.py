
def read_melon_deliveries(day_num, file_path):
    print (f'Day {day_num}')
    the_file = open(file_path)
    for line in the_file:
        #align right
        line = line.rstrip()
        #split line devided be "|"
        words = line.split('|')
        
        #initializing variables  
        melon = words[0]
        count = int (words[1])
        amount = float(words[2])
        print(f"Delivered {count} {melon}s for total of ${amount}")
    
    the_file.close()

    
read_melon_deliveries(1, "um-deliveries-day-1.txt")
read_melon_deliveries(2, "um-deliveries-day-2.txt")
read_melon_deliveries(3, "um-deliveries-day-3.txt")