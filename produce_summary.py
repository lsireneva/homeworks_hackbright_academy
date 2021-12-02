
def read_melon_deliveries(file_name):
    the_file = None
    #file names stored in list we go trough this list
    for name in file_name:
        if name=="um-deliveries-day-1.txt":
            #open the file with name
            the_file = open("um-deliveries-day-1.txt")
            print("Day 1")
            #print information from the file
            print_info_from_file(the_file)
        elif name=="um-deliveries-day-2.txt":
            the_file = open("um-deliveries-day-2.txt")
            print("Day 2")
            print_info_from_file(the_file)
        elif name=="um-deliveries-day-3.txt":
            the_file = open("um-deliveries-day-3.txt")
            print("Day 3")
            print_info_from_file(the_file)
    
    #close the opened file
    the_file.close()

#function for printing specified lines from file
def print_info_from_file(the_file):

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

file_name =["um-deliveries-day-1.txt", "um-deliveries-day-2.txt", "um-deliveries-day-3.txt"]
read_melon_deliveries(file_name)
