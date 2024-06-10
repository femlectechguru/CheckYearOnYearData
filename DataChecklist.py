import csv

def check_name_in_list(name_to_check, list_of_dicts):
    for obj in list_of_dicts:
        if obj['Customer_Name'].lower() == name_to_check.lower():
            return True
    return False


def get_common_names(year_1, year_2, year_3, year_4):
    all_years = [year_1, year_2, year_3, year_4]
    result = []

    for year in all_years:
        with open(f'{year}_Travel_data.csv', 'r') as file:
            csv_file = csv.reader(file)

            for index, line in enumerate(csv_file):
                if (index > 0):
                    print(line, 'if')
                    if (check_name_in_list(line[2], result) == False):
                        x = {
                            # f'{year_1}_client_number': [],
                            # f'{year_2}_client_number': [],
                            # f'{year_3}_client_number': [],
                            # f'{year_4}_client_number': [],
                            "Customer_Name": line[0],
                            year_1: [],
                            year_2: [],
                            year_3: [],
                            year_4: [],
                            f'{year_1}_Frequent_Travels': [],
                            f'{year_2}_Frequent_Travels': [],
                            f'{year_3}_Frequent_Travels': [],
                            f'{year_4}_Frequent_Travels': [],
                            f'{year_1}_Premium': [],
                            f'{year_2}_Premium': [],
                            f'{year_3}_Premium': [],
                            f'{year_4}_Premium': [],
                        }
                        # x[year] = x[year] + [line[0]]
                        x[f'{year}_Frequent_Travels'] = x[f'{year}_Frequent_Travels'] + [line[1]]
                        x[f'{year}_Premium'] = x[f'{year}_Premium'] + [line[2].replace(",", "")]
                        # x[f'{year}_client_number'] = x[f'{year}_client_number'] + [line[0]]
                        result.append(x)
                    else:
                        for d in result:
                            if (d['Customer_Name'].lower() == line[0].lower()):
                                # d[year] = d[year] + [line[1]]
                                d[f'{year}_Frequent_Travels'] = d[f'{year}_Frequent_Travels'] + [line[1]]
                                d[f'{year}_Premium'] = d[f'{year}_Premium'] + [line[2].replace(",", "")]
                                # d[f'{year}_client_number'] = d[f'{year}_client_number'] + [line[0]]



    fields = ['Customer_Name'] + all_years + [f'{year_1}_Frequent_Travels', f'{year_2}_Frequent_Travels', f'{year_3}_Frequent_Travels', f'{year_4}_Frequent_Travels', f'{year_1}_Premium', f'{year_2}_Premium', f'{year_3}_Premium', f'{year_4}_Premium']
    
    # name of csv file  
    filename = "results.csv"
        
    # writing to csv file  
    with open(filename, 'w') as csvfile:  
        # creating a csv dict writer object  
        writer = csv.DictWriter(csvfile, fieldnames = fields)  
            
        # writing headers (field names)  
        writer.writeheader()  
            
        # writing data rows  
        writer.writerows(result)  

    print('Done!!!')

                            


get_common_names("2020", "2021", "2022", "2023")

