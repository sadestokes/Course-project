def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetHoursWorked():
    hoursworked = input("Enter hours worked: ")
    return hoursworked
def GetHourlyRate():
    hourlyrate = input("Enter hourly rate: ")
    return hourlyrate
def GetTaxRate():
    taxrate = input("Enter tax rate: ")
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours: .2f}")
    print("Hourly Rate: ", f"{hourlyrate: .2f}")
    print("Gross Pay: ", f"{grosspay: .2f}")
    print("Tax Rate:", f"{taxrate: %.2f}")
    print("Income Tax: ", f"{incometax: .2f}")
    print("Net Pay: ", f"{netpay: .2f}")



    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours: .2f}")
    print(f"Total Gross Pay:  {TotGrossPay: .2f}")
    print(f"Total Tax: {TotTax: .2f}")
    print(f"Total Net Pay: {TotNetpay: .%2f")

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked()
        if (hours.upper() == "END"):
            break
        hourlyrate = GetHourlyRate()
        if (hourlyrate.upper() == "END"):
            break
        taxrate - GetTaxRate()
        if (taxrate.upper() == "END"):
            break
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += taxrate,incometax
        TotNetPay += netpay


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)


