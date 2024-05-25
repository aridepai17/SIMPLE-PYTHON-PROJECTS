import tabulate 
import csv 

def referencechart():
    """
    This function is used to create a reference chart of the 
    bmi scale for the user, this requires a csv file 'bmi.csv'
    and two libraries ''tabulate'' and ''csv''. Does not return 
    anything
    """
    list2 = []
    with open('bmi.csv') as file1:
        list1 = csv.reader(file1)
        for line in list1:
            list2.append(line)
        
        print("Here you can take the reference chart. \n")
        print(tabulate.tabulate(list2[1:], headers=list2[0], tablefmt="fancy_grid"))
        
def calculatebmi(height, weight):
    try:
        bmi = round(weight / (height**2), 2)
        return bmi
    except  ZeroDivisionError:
        return None
    
def interpretbmi(bmi):
    if bmi is None:
        return "Enter a valid height."
    
    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif 18.5 <= bmi < 25:
        return f"Your BMI is {bmi}, you have a normal weight."
    elif 25 <= bmi < 30:
        return f"Your BMI is {bmi}, you are overweight."
    elif 30 <= bmi < 35:
        return f"Your BMI is {bmi}, you are obese."
    elif 35 <= bmi < 40:
        return f"Your BMI is {bmi}, you are clinically obese."
    else:
        return f"Your BMI is {bmi}, you are morbidly obese."
    
def main():
    referencechart()
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        
        bmi = calculatebmi(height, weight)
        result = interpretbmi(bmi)
        print(result)
        
    except ValueError:
        print("Enter valid values for height and weight.")
        
if __name__ == "__main__":
    main()
    

