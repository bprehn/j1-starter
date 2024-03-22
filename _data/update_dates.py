import yaml
from datetime import date, timedelta, datetime 

def calculate_next_years_date(original_date):
    print("Original Date:", original_date) 
    next_year = original_date.year + 1

    # Leap year and date is before March
    if (next_year % 4 == 0 and original_date.year % 100 != 0) or original_date.year % 400 == 0: 
        if original_date.month < 3:  # Check if it's before March
            result = original_date + timedelta(days=365) - timedelta(days=2) 
        else:
            result = original_date + timedelta(days=365) - timedelta(days=1) 
    else:
        result = original_date + timedelta(days=365) - timedelta(days=1)  

    print("Calculated Date:", result)       
    return result 


# ... (Rest of your code remains the same) ...

def update_yaml_dates(yaml_file):
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)

    # Update Specific Dates
    for key in ["test-date-1", "test-date-2", "test-date-3", "test-date-4"]:
        if key in data:
            try: 
                date_str = data[key]  
                current_date = date.fromisoformat(date_str)  # No need for strptime
                data[key] = calculate_next_years_date(current_date).isoformat()
            except Exception as e: 
                print(f"An error occurred while updating '{key}': {e}")

    with open(yaml_file, "w") as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    update_yaml_dates("test_dates.yml")  