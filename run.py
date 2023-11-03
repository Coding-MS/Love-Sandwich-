import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_Cilent = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_Cilent.open('love_sandwiches')

def get_sales_data():
    """ Get sales figures input from the user """
    while True: 
        print ("Please enter sales data from the last market")
        print ("Data should be six numbers,separated by commas")
        print ("Example: 35,40,30,66,70,32\n")

        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        validate_data(sales_data)

        if validate_data(sales_data):
            print("Data is valid!")
            break 
    return sales_data

def validate_data(values):
   """ Validation function """
   print(values)
   try: 
        if len(values) != 6 :
            raise ValueError(
                f"Exactly 6 values required, you have provided {len(values)}"
             )
   except ValueError as e:
       print (f"Invalid data: {e}, please try again \n")
       return False

   return True 

def update_sales_worksheet(data):
    """ Update the sale worksheet through adding a new row with a list data """
    print ("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")
    

data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)


