import yaml
from datetime import date, timedelta 

def calculate_next_years_date(original_date):
    # Final Formula Adapted for Python
    result = original_date + timedelta(days=365) + \
             (1 if (OR(AND(original_date.year+1 % 4 == 0, original_date.year % 100 != 0),
                     original_date.year % 400 == 0)) else 0) - 1
    return result 


def update_yaml_dates(yaml_file):
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)

    # Find and Update Dates (Customize based on your YAML structure)
    for key, value in data.items():
        if isinstance(value, date):  
            if value.year == date.today().year and value.month >= 4 and value.day >= 15:
                data[key] = calculate_next_years_date(value)  

    with open(yaml_file, "w") as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    update_yaml_dates("MK-Variables.yml")  # Update the filename here if necessary
