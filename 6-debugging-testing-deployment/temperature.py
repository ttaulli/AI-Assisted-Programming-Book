def temperature_convert(value, from_unit, to_unit):
    if from_unit.lower() == 'f':
        celsius = (value - 32) * 5/9
    elif from_unit.lower() == 'k':
        celsius = value - 273.15
    else:
        celsius = value
    
    if to_unit.lower() == 'f':
        return celsius * 9/5 + 32
    elif to_unit.lower() == 'k':
        return celsius + 273.15
    else:
        return celsius

def length_convert(value, from_unit, to_unit):
    conversions_to_meter = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'mi': 1609.34
    }
    
    meters = value * conversions_to_meter.get(from_unit.lower(), 0)
    return meters / conversions_to_meter.get(to_unit.lower(), 1)

def weight_convert(value, from_unit, to_unit):
    conversions_to_kg = {
        'kg': 1,
        'g': 0.001,
        'lb': 0.453592,
        'oz': 0.0283495
    }
    
    kg = value * conversions_to_kg.get(from_unit.lower(), 0)
    return kg / conversions_to_kg.get(to_unit.lower(), 1)

def volume_convert(value, from_unit, to_unit):
    conversions_to_liter = {
        'l': 1,
        'ml': 0.001,
        'gal': 3.78541,
        'cup': 0.236588,
        'fl_oz': 0.0295735
    }
    
    liters = value * conversions_to_liter.get(from_unit.lower(), 0)
    return liters / conversions_to_liter.get(to_unit.lower(), 1)

def main():
    print("Unit Conversion Program")
    print("=======================")
    print("1. Temperature (c/f/k)")
    print("2. Length (m/km/cm/mm/ft/in/mi)")
    print("3. Weight (kg/g/lb/oz)")
    print("4. Volume (l/ml/gal/cup/fl_oz)")
    print("5. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if choice == 5:
                print("Thank you for using the conversion program!")
                break
                
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
                
            value = float(input("Enter the value to convert: "))
            
            if choice == 1:
                from_unit = input("Enter the source unit (c/f/k): ")
                to_unit = input("Enter the target unit (c/f/k): ")
                result = temperature_convert(value, from_unit, to_unit)
                print(f"{value} {from_unit.upper()} = {result:.2f} {to_unit.upper()}")
                
            elif choice == 2:
                from_unit = input("Enter the source unit (m/km/cm/mm/ft/in/mi): ")
                to_unit = input("Enter the target unit (m/km/cm/mm/ft/in/mi): ")
                result = length_convert(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
                
            elif choice == 3:
                from_unit = input("Enter the source unit (kg/g/lb/oz): ")
                to_unit = input("Enter the target unit (kg/g/lb/oz): ")
                result = weight_convert(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
                
            elif choice == 4:
                from_unit = input("Enter the source unit (l/ml/gal/cup/fl_oz): ")
                to_unit = input("Enter the target unit (l/ml/gal/cup/fl_oz): ")
                result = volume_convert(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()