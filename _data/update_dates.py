import yaml
from datetime import date, timedelta 

def calculate_next_years_date(original_date):
    # ... (Our refined date calculation logic) ...
    return original_date + timedelta(days=365) + \
            (1 if (OR(AND(original_date.year+1 % 4 == 0, original_date.year % 100 != 0), 
                    original_date.year % 400 == 0)) else 0) - 1

def update_yaml_dates(yaml_file):
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)

    # Update Specific Dates
    for key in ["mk-xmas-vacation", "mk-mlk-day", "mk-pres-day", "mk-xmas-eve", "mk-xmas-wed"]:
        if key in data:
            date_str = data[key].split(",")[0]  # Extract date part
            current_date = date.fromisoformat(date_str)
            if current_date.year == date.today().year and current_date.month >= 4 and current_date.day >= 15:
                data[key] = calculate_next_years_date(current_date).isoformat() + data[key][10:] 

    with open(yaml_file, "w") as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    update_yaml_dates("MK-Variables.yml")  # Update the filename here if necessary
