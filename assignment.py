import pandas as pd  # importing panda library

input_data = "1. Add new client details/record.\n2. Search client details (Client ID).\n3. Remove any client details.\n4. Print all the client’s details.\n5. Order the stored client's details by name.\n6. Order the stored client's details by Selected Products\n7. Save the client's details into the file.\n8. Exit.\n"
data_c = {}        # the list with all details
Input_c = 1        # a variable that you can manage
SL = 1             # the number that you are choosing


def client_F(SL, Input_c):   # the Client details and you enter
    if SL == 1:               # Click 1 for creating new client then enter details, then is incremented as +1 as in Client ID, for example if this is first client
                              # He will be Client ID 1, then we can manage, delete it
        client = {}
        client["Name_"] = input("Enter Name:  ")
        client["Address_"] = input("Enter Address:  ")
        client["Phone_Number_"] = input("Enter Phone Number:  ")
        client["Email_Address_"] = input("Enter Email Address:  ")
        client["Product_Details_"] = input("Enter Selected Product \n[Software, Laptops & PC, Games, Office Tools or Accessories]:  ")
        data_c[Input_c] = client
        Input_c += 1
    if SL == 2:            # the searching for Client ID from the Data in Data_c this is the actual data
        data = int(input("Enter Client ID:  "))
        if data in data_c:
            print(data_c[data])
        else:
            print("Not available  in database.  ")
    if SL == 3:          # delete the client data from data_c , from SL 1 , was created ID , we can delete here
        d = int(input("Enter Client ID:  "))
        if d in data_c:
            del data_c[d]
            print("Client data deleted.  ")
        else:
            print("This client ID does not exist  ")
    if SL == 4:                       # Shows all the data in data_c with print
        print(data_c)
        SL = int(input(input_data))
    if SL == 5:                         # Sorting data_c with help of lambda - a non existing function used for sorting
        for i in sorted(data_c, key=lambda x: data_c[x]['Name_']):
            print(data_c[i])
    if SL == 6:
        for i in sorted(data_c, key=lambda x: data_c[x]['Product_Details_']):
            print(data_c[i])
    if SL == 7:
        data_f = pd.DataFrame.from_dict(data_c)  # creating dataframe from given csv file
        data_f1 = data_f.T                      # storing this dataframe in a csv file
        data_f1.to_csv('Client_Data.csv', index=False) # Path where you want to store the exported CSV file



while SL != 8:           # if you click 8 , means that the program terminates
    SL = int(input(input_data))
    client_F(SL, Input_c)
    if SL == 1:
        Input_c += 1


