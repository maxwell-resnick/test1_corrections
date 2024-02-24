"""
@author: maxwellresnick
"""

# Problem 2

def count_unique_proteins(proteins):
    return len({protein.split(".")[0] for protein in proteins})

def count_proteins(proteins):
    proteins_dict = {}
    for protein in proteins:
        unique_family_number = protein.split(".")[0]
        if unique_family_number in proteins_dict:
            proteins_dict[unique_family_number] += 1
        else:
            proteins_dict[unique_family_number] = 1
    return proteins_dict

def merge_protein_counts(protein_dict1, protein_dict2):
    combined_dict = {}
    for key, value in protein_dict1.items():
        combined_dict[key] = (value, protein_dict2.get(key, 0))
    
    for key, value in protein_dict2.items():
        if key not in combined_dict:
            combined_dict[key] = (0, value)
            
    return combined_dict

# Problem 3

months_dict = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def dates_to_iso8601(dates_list):
    new_dates = []
    for date in dates_list:
        split_dates = date.split(" ")
        month = split_dates[0]
        day = split_dates[1].replace(",", "")
        year = split_dates[2]
        
        if int(day) <= 9:
            day = "0" + day
        
        month_numeric = months_dict[month]
        
        new_date = f"{year}-{month_numeric}-{day}"
        new_dates.append(new_date)
        
    return new_dates

def sort_dates(dates_list):
    new_dates = dates_to_iso8601(dates_list)
    sorted_dates = sorted(new_dates)
    
    reverted_dates = []
    inverted_months_dict = {value: key for key, value in months_dict.items()}

    for date in sorted_dates:
        split_date = date.split("-")
        year = int(split_date[0])
        month = split_date[1]
        day = int(split_date[2])
        month_str = inverted_months_dict[month]
        reverted_date = f"{month_str} {day}, {year}"
        reverted_dates.append(reverted_date)
    
    return reverted_dates
