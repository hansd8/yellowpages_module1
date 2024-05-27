data = [
        {
                'nama' : 'Plataran',
                'deskripsi' : 'Restoran',
                'alamat' : 'Jalan Jend. Sudirman No. 54-55',
                'kota' : 'Jakarta Pusat  ',
                'kodepos' : '10270',
                'phone' : '22531199'
        },
        {
                'nama' : 'Paris Sorbet',
                'deskripsi' : 'Restoran',
                'alamat' : 'Jalan Wolter Monginsidi No. 71',
                'kota' : 'Jakarta Selatan',
                'kodepos' : '12180',
                'phone' : '27515207' 
        },
        {
                'nama' : 'Katedral',
                'deskripsi' : 'Ibadah',
                'alamat' : 'Jalan Katedral No. 7B         ',
                'kota' : 'Jakarta Pusat  ',
                'kodepos' : '10710',
                'phone' : '3519186' 
        },
        {
                'nama' : 'Cipinang Mall',
                'deskripsi' : 'Shopping',
                'alamat' : 'Jalan Raya Kalimalang No. 18',
                'kota' : 'Jakarta Timur  ',
                'kodepos' : '13430',
                'phone' : '29483757'
        },
        {
                'nama' : 'Mulia Senayan',
                'deskripsi' : 'Penginapan',
                'alamat' : 'Jalan Asia Afrika Senayan',
                'kota' : 'Jakarta Pusat  ',
                'kodepos' : '10270',
                'phone' : '5747777'
        },
        {
                'nama' : 'Gandaria City',
                'deskripsi' : 'Shopping',
                'alamat' : 'Jalan Sultan Iskandar Muda',
                'kota' : 'Jakarta Selatan',
                'kodepos' : '12240',
                'phone' : '29052888'
        },
        {
                'nama' : 'The Langham',
                'deskripsi' : 'Penginapan',
                'alamat' : 'SCBD 8 Lot. 28            ',
                'kota' : 'Jakarta Selatan',
                'kodepos' : '12190',
                'phone' : '27087888'
        },
        {
                'nama' : 'IPEKA Meruya',
                'deskripsi' : 'Sekolah',
                'alamat' : 'Jalan Meruya Ilir Blok. K',
                'kota' : 'Jakarta Barat  ',
                'kodepos' : '11620',
                'phone' : '58905890'
        },
        {
                'nama' : 'Labschool Kebayoran',
                'deskripsi' : 'Sekolah',
                'alamat' : 'Jalan KH Admad Dahlan No. 14',
                'kota' : 'Jakarta Selatan',
                'kodepos' : '12130',
                'phone' : '47860038'
        },
        {
                'nama' : 'Masjid Istiqlal',
                'deskripsi' : 'Ibadah',
                'alamat' : 'Jalan Taman Wijaya Kusuma',
                'kota' : 'Jakarta Pusat',
                'kodepos' : '10710',
                'phone' : '3811708'
        }        
]

def tampilkan_data(data):
        headers = ["Nama", "Deskripsi", "Alamat", "Kota", "Kodepos", "Phone"]
        keys = ["nama", "deskripsi", "alamat", "kota", "kodepos", "phone"]
        # Calculate the maximum width needed for each column. 
        # Column Width Calculation: Compute the maximum width required for each column based on the longest data in each column.
        column_widths = [max(len(str(entry[key]).strip()) for entry in data) for key in keys]
        column_widths = [max(len(header), width) for header, width in zip(headers, column_widths)]
        # Print top border
        print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
        # Print header row.  Print the table header with the column names left-justified within their respective columns.
        print("|" + "|".join([" " + header.ljust(width) + " " for header, width in zip(headers, column_widths)]) + "|")
        # Print header bottom border
        print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
        # Print data rows. Iterate through the dataset and print each row, with data left-justified within columns.
        for entry in data:
                row = [str(entry.get(key, "")).strip().ljust(width) for key, width in zip(keys, column_widths)]
                print("|" + "|".join([" " + cell + " " for cell in row]) + "|")
        # Print bottom border
        print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

def is_valid_input(abc):
        return bool(abc.strip())

def saveData(data) :
        # Adds data dictionary to the end of the list
        data.append({
                'nama' : namaBaru,
                'deskripsi' : deskripsiBaru,
                'alamat' : alamatBaru,
                'kota' : kotaBaru,
                'kodepos' : kodeposBaru,
                'phone' : phoneBaru
                })
        print('Data successfully saved!')

def filter_data(data, key, value):
    return list(filter(lambda item: value.lower() in item[key].lower(), data))

#Main Loop for Main Menu
while True:
    z = input('Please Press any key to start :')
    if type(z) == str:
        a = input('do you want to read? (yes/no) : ')
        if a.lower() == 'yes':
                # Show Data List when read is chosen
                tampilkan_data(data)
                # This is the main loop for Read and filter Menu
                while True:
                        #Filter Data using description
                        readDeskripsi = input('Do you want to filter using deskripsi bisnis? (yes/no) : ')                     
                        if readDeskripsi == 'yes':
                                #Deskripsi Filter Loop
                                while True:
                                        a1 = input('Coba cari & filter dari deskripsi bisnis : ').lower()
                                        #Checks if the input is in one of the values of the deskripsi keys' values
                                        if filter_data(data,'deskripsi',a1) != []:
                                                #Shows data
                                                tampilkan_data(filter_data(data,'deskripsi',a1))
                                                #Exit Loop and go to filter menu
                                                break
                                        else :
                                                print('Data does not exist')
                                                #Re-run deskripsi loop
                        elif readDeskripsi == 'no':
                                #Filter data using kota
                                readKota = input('Do you want to filter using kota? (yes/no) : ')
                                if readKota == 'yes':
                                        #Filter using kota loop
                                        while True:
                                                a2 = input('Coba cari & filter dari kota bisnis : ').lower()
                                                #Checks if the input is in one of the values of the kota keys' values
                                                if filter_data(data,'kota',a2) != []:
                                                        #Display the data list that contains the searched kota
                                                        tampilkan_data(filter_data(data,'kota',a2))
                                                        #Exit loop to read and filter menu
                                                        break
                                                else :
                                                        print('Data does not exist!')
                                                        #Re-run loop
                                                        continue
                                elif readKota == 'no':
                                        #Filter data using phone number
                                        readPhone = input('Do you want to filter using phone? (yes/no) : ')
                                        if readPhone == 'yes':
                                                #Filter data using phone number loop
                                                while True:
                                                        a3 = input('Coba cari & filter dari phone bisnis : ')
                                                        #Checks if given phone number is in one of the phone keys' values
                                                        if filter_data(data,'phone',a3) != []:
                                                                #Display filtered data list that has the given phone number
                                                                tampilkan_data(filter_data(data,'phone',a3))
                                                                #Exit loop and enters into Read & Filter Menu
                                                                break
                                                        else :
                                                                print('Data does not exist')
                                                                #Re-run Loop
                                        elif readPhone == 'no':
                                                #Asks the user if they want to exit the read menu
                                                readExit = input('Do you want to exit Read? (yes/no) : ')
                                                if readExit == 'yes':
                                                        #Exit the read menu and enters itu main menu
                                                        break
                                                elif readExit == 'no':
                                                        #Re-run the read menu
                                                        continue                                            
        elif a.lower() == 'no':
                b = input('do you want to create? (yes/no) : ')
                if b.lower() == 'yes':
                        #Create Menu Loop
                        while True:
                                #Asks user to input the phone number as new primary key's value
                                create = input('do you want to create new Details of a new business (yes/no) : ')
                                if create == 'yes':
                                        phoneBaru = input('Please input business phone number baru : ')
                                        #Checks if new phone number is already contained in the data list and if the new number is a valid input
                                        if filter_data(data,'phone',phoneBaru) == [] and is_valid_input(phoneBaru):
                                                #New Data Entry Loop
                                                while True:
                                                        namaBaru = input('Masukkan Nama Bisnis baru: ')
                                                        #Checks if new business name is already contained in the data list
                                                        if filter_data(data,'nama',namaBaru) == []:
                                                                while True:
                                                                        deskripsiBaru = input('Masukkan deskripsi bisnis baru : ')
                                                                        #Only allows valid and alphabets as inputs
                                                                        if is_valid_input(deskripsiBaru):
                                                                                break
                                                                
                                                                while True:
                                                                        alamatBaru = input('Masukkan alamat bisnis baru : ')
                                                                        #Only allows valid inputs
                                                                        if is_valid_input(alamatBaru):
                                                                                break
                                                                
                                                                while True:
                                                                        kotaBaru = input('Masukkan kota bisnis baru : ')
                                                                        #Only allows valid and alphabets as inputs
                                                                        if is_valid_input(kotaBaru):
                                                                                break
                                                                
                                                                while True:
                                                                        kodeposBaru = input('Masukkan kode pos bisnis baru : ')
                                                                        #Only allows valid and digits as inputs
                                                                        if kodeposBaru.isdigit():
                                                                                break
                                                                
                                                                #Asks user if they want to save the changes
                                                                saveCreate = input('Do you want to save data? (yes/no) :')
                                                                if saveCreate == 'yes':
                                                                        #Adds new additional data list to the existing data list 
                                                                        saveData(data)
                                                                        #Exit loop and enters ito create menu
                                                                        break
                                                                elif saveCreate == 'no':
                                                                        #Exit loop and enters into create menu
                                                                        break
                                                        else : 
                                                                print('Data already exists!')
                                                                #Re-run and prompts user to give another name again
                                                                continue
                                        else :
                                                print('Data already exists!')
                                                continue
                                elif create == 'no':
                                        createExit = input('Do you want to exit Create? (yes/no) : ')
                                        if createExit == 'yes':
                                                #Exits loop and goes to main menu
                                                break
                                        elif createExit == 'no':
                                                #Re-run loop of create menu
                                                continue
                elif b.lower() == 'no':
                        c = input('do you want to update? (yes/no) : ')
                        if c.lower() == 'yes':
                                #Update Menu Loop
                                while True:
                                        update = input('Do you want to update details of a business? (yes/no) : ')
                                        if update == 'yes':
                                                phone = input('Please input the business phone as an identifier of the business you wish to update : ')
                                                #Checks if there is only one search result for business using the phone number
                                                if len(filter_data(data,'phone',phone)) == 1:
                                                        #Finds which index in the data is the phone number located in
                                                        #Displays the corresponding business that is found
                                                        tampilkan_data(filter_data(data,'phone',phone))
                                                        for i in range(len(data)):
                                                                if phone in data[i]['phone']:
                                                                        indexkey = i
                                                                else:
                                                                        None
                                                        updateConfirm = input('Do you want to continue to update? (Yes/no) : ')
                                                        if updateConfirm == 'yes':
                                                                #Update Key Menu Loop
                                                                while True:
                                                                        updateKey = input('Please enter which column you wish to change : ').lower()
                                                                        #Checks if the user input is one of the key column
                                                                        def check_in_data(updateKey):
                                                                                for i in data:
                                                                                        if updateKey in i:
                                                                                                return True
                                                                                return False
                                                                        if check_in_data(updateKey):
                                                                                updateValue = input('Please enter the new updated value for that column : ')
                                                                                
                                                                                #Saves the update made
                                                                                saveUpdate = input('do you want to save the update? (yes/no) : ')
                                                                                if saveUpdate == 'yes':
                                                                                        #Updates the value being changed to the new value
                                                                                        data[indexkey][updateKey] = updateValue
                                                                                        print('Data successfully updated!')
                                                                                        break
                                                                                elif saveUpdate == 'no':
                                                                                        #Re-run loop
                                                                                        continue
                                                                        else : 
                                                                                print('Column not found!')
                                                        elif updateConfirm == 'no':
                                                                #Re-run Loop
                                                                continue
                                                else :
                                                        print('The data you are looking for does not exists!')
                                                        #Re-run loop
                                                        continue
                                        elif update == 'no':
                                                updateExit = input('Do you want to Exit Update? (yes/no) : ')
                                                if updateExit == 'yes':
                                                        #Exit Update menu Loop
                                                        break
                                                elif updateExit == 'no' :
                                                        #Re-run Update menu Loop
                                                        continue
                        elif c.lower() == 'no' :
                                    d = input('do you want to delete? (yes/no) : ')
                                    if d.lower() == 'yes':
                                        #Delete Menu Loop
                                        while True:
                                                delete = input('Do you want to delete details of a business? (yes/no) : ')
                                                if delete == 'yes' :
                                                       phone = input('Please input the business phone as an identifier of the business you wish to delete : ')
                                                       #Checks if the phone number input gives only 1 search result
                                                       if len(filter_data(data,'phone',phone)) == 1:
                                                                #Displays the corresponding business result found
                                                                tampilkan_data(filter_data(data,'phone',phone))
                                                                #Locates the index at which the business is in the data list
                                                                for i in range(len(data)):
                                                                        if phone in data[i]['phone']:
                                                                                indexkey = i
                                                                        else:
                                                                                None
                                                                deleteAll = input('Do you want to delete all the details of this business? (yes/no) : ')
                                                                if deleteAll == 'yes':
                                                                        deleteConfirm = input('Do you want to continue to Delete all the details? (Yes/no) : ')
                                                                        if deleteConfirm == 'yes':
                                                                                #Deletes the whole business row
                                                                                del data[indexkey]
                                                                                print('Data successfully deleted!')
                                                                                continue
                                                                        elif deleteConfirm == 'no':
                                                                                continue
                                                                elif deleteAll == 'no':
                                                                        #Asks which column the user would like to delete the values is
                                                                        while True:
                                                                                deleteKey = input("Please enter which column where the value will be deleted : ").lower()
                                                                                #Checks if the input is one of the key columns
                                                                                def check_in_data(deleteKey):
                                                                                        for i in data:
                                                                                                if deleteKey in i:
                                                                                                        return True
                                                                                        return False
                                                                                if check_in_data(deleteKey):
                                                                                        #Deletes the value of the corresponding key's value chosen
                                                                                        data[indexkey][deleteKey] = ''
                                                                                        print('Data successfully updated!')
                                                                                        #Exit Loop to delete Menu Loop
                                                                                        break
                                                                                else :
                                                                                        print('Column not found!')
                                                                                        #Re-run partial key delete loop
                                                                                        continue
                                                       else:
                                                              print('The data you are looking for does not exists!')
                                                              #Re-run delete menu loop
                                                              continue
                                                elif delete == 'no' :
                                                        deleteExit = input('Do you want to Exit Delete? (yes/no) : ')
                                                        if deleteExit == 'yes':
                                                               #Exit delete menu loop and enter into main menu
                                                               break
                                                        elif deleteExit == 'no':
                                                               #Re-run Delete menu loop
                                                               continue
                                    elif d.lower() == 'no':
                                            e = input('do you want to exit Program? (yes/no) : ')
                                            if e.lower() == 'yes':
                                                #Exit Main Menu loop and exit program
                                                break
                                            else:
                                                print('The option you entered is not valid!')
                                                #Re-run main menu loop
                                                continue