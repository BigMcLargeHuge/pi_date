from mpmath import mp
import pandas as pd

try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

mp.dps = 10000  # set number of digits
pistr = str(mp.pi)
testDates = []
confirmedDates = []
for year in range(1000, 2023):
    for month in range(1,13): #fuck leading zeros
        if(month == 2):
            days = range(1,29) #fuuuuuuck leapyears
        elif(month == 9 or month == 4 or month == 6 or month == 11):
            days = range(1,31)
        else:
            days = range(1,32)
        for day in days:
            testDates.append(str(month) + str(day) + str(year))

numberConfirmedDates = len(testDates)
numberConfirmedDates
# testDates.append('314')

digit = 7
file1 = open("myfile.txt", "w")
done = False
# while done == False:
df = pd.DataFrame(columns = ['date', 'decimal', 'to go'])
df.to_csv('pi.csv', index=False)
total = len(testDates)
while len(confirmedDates) < numberConfirmedDates:
    digit = digit + 1
    mp.dps = digit
    pistr = str(mp.pi).replace('.', '')
    if digit > 30:
        # print("digit: " + str(digit))
        # print("pistr 1: " + str(pistr))
        pistr = pistr[(digit - 20):]
    # print("pistr 2: " + str(pistr))
    if(digit % 1000 == 0):
        df = pd.DataFrame(confirmedDates)
        df.to_csv('pi.csv', mode='a', index=False, header=False)
        confirmedDates = []
        print("Remaining: "+ str(len(testDates)) + "  percent to go: " + str(len(testDates)/total) + "%  digit: " + str(digit))

    # print(pistr)
    for theDate in testDates:
        # print(theDate)
        # print(pistr)
        if theDate in pistr:
            testDates.remove(theDate)
            confirmedDates.append({"date": theDate, "decimal": digit, "to go": len(testDates)})
            # file1.writelines("date: " + str(theDate) + ", decimal: " + str(digit) + "\n")
            # print(confirmedDates)
            # done = True
            # break
