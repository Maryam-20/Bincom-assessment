from statistics import mean, median, variance
import random
import psycopg2
from psycopg2 import sql as ql


        
        
        
        
    
try:
    my_con = psycopg2.connect(
        dbname="bincom_db",
        user="postgres",
        password="1234",
        host="localhost",  # or your database host
        port="5432"  # default PostgreSQL port
    )



    # connection = psycopg2.connect(**my_con)
    my_cursor = my_con.cursor()
    # my_cursor = my_con.cursor()

    # my_cursor.execute("""CREATE TABLE bin (
    #     id SERIAL PRIMARY KEY,
    #     Color VARCHAR(20),
    #     Frequency INT
    #     )
        
    #     """)
    # my_con.commit()
except Exception as e:
    print(f"Connection Failed: {e}")
# finally:
#     my_cursor.close()
#     my_con.close()


# self.Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


colorAvailable = []
colDict = {}


def check():
    Colors  =[("GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"),
        ("ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"),
        ("GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"),
        ("BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"),
        ("GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE")

    ]
    Available_color = []
    color_appearance_dict = []
    color_appearance = []
    TotalCol = 0
# To know the varieties of colors available in the Colorslist
    for col in Colors:
        for colB in col:

            if colB not in Available_color:
                Available_color.append(colB.upper())
    print(Available_color)
    
# Looping over the sequence to the number of time each available appear throughout the week
    for col_type in Available_color:
        num = 0
        # print(col_type)
        for col in Colors:
            no_color_appearance  = col.count(col_type)
            # print(no_color_appearance)
            num = num + no_color_appearance
        # print(num)
        color_appearance.append(num)
        # print(color_appearance)
        color_appearance_dict.append({"Type of color": col_type, "No of color": num})
        # print(color_appearance_dict)
            
# INSERTING TO POSTGRESQL DATABASE 
# Insert data into the bin table
        insert_query = """
            INSERT INTO bin (Color, Frequency)
            VALUES (%s, %s)
        """

        data_to_insert = (col_type,  num)

        my_cursor.execute(insert_query, data_to_insert)


        my_con.commit()
        print("Data inserted successfully!")
        my_cursor.close()
        my_con.close()
#To Determine the color shirt with the mean color   
    round_mean = round(mean(color_appearance))
    # print(num)
    # print(color_appearance_dict)
    # print(round_mean)
    for  item in color_appearance_dict:

        if item.get("No of color") == round_mean:
            print(item.get("Type of color") )
        
            break
        
    print(f"The color shirt with the mean color is: no color match\n\n")
    
# FOR THE COLOR MOSTLY WORN THROUGHOUT THE WEEK
    maximum = max(color_appearance)
    for item in color_appearance_dict:
        if item.get("No of color") == maximum:
            print(f"Color mostly worn throughout the week is: {item}\n")
        
# TO DETERMINE THE MEDIAN
    Median =median(color_appearance)
    for item in color_appearance_dict:
        if item.get("No of color") == round(Median):
            print(f"The median color is: {item}\n")
    # print(Median)
    
# TO DETERMINE THE VARIANCE
    var = variance(color_appearance)
    print(f"The variance of the color is: {var}")
    
    
# TO DETERMINE RED COLOR IS CHOSEN AT RANDOM
    for col in Colors:
        len_col = len(col)
        TotalCol += len_col
    print(f"Total color is :{TotalCol}")
    
    for col in Colors:
        random_col = random.choices(col)
    print(f"Color choosen at random is: {random_col}\n")
    probablity = len(random_col)/TotalCol
    
    print(f"The probablity that the choosen color is red is: {probablity}")
            
check()  
# RECURSIVE SEARCHING ALGORITHM
def recursive_search(arr, target, index=0):
    
    if index >= len(arr):
        return -1
    
    
    if arr[index] == target:
        return index
    
    # Recursive case: search the next element
    return recursive_search(arr, target, index + 1)

arr = [2, 4, 3, 5, 7, 8, 9]
target = int(input("Enter a number:  "))

result = recursive_search(arr, target)

print("Index of target:", result if result != -1 else "Not found")

# GENERATE RANDOM FOUR  NUMBER IN BINARY  AND CONVERT TO BASE 10
def generateNum():
    randon_bits = "".join(str(random.randint(0, 1)) for _ in range(10))
    print("Randon number in Binary", randon_bits)
    print("Random number in Decimal", int(randon_bits, 2))
    
generateNum()
# TO DETERMINE THE SUM OF FIRST 50 FINOBACI SEQUENCE
def finobaci():
    finobaci_seq = [0, 1]
    num = 50
    for num in range(2, num):
        next_no = finobaci_seq[-1] + finobaci_seq[-2]
        finobaci_seq.append(next_no)
        
    print(finobaci_seq[:num])
finobaci()