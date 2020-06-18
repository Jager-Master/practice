#App to abbreviate first 3 characters of the month, given a month number

def main():
    #List month abbreviations
    months = "JanFebMarAprJunJulAugSepOctNovDec"

    user_no = int(input("Please input month no (between 1-12): "))
    pos = (user_no - 1) * 3

    month_abb = months[pos:pos+3]

    print("The month abbreviation is ", month_abb)

main()


