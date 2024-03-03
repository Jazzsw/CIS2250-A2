'''
unemploymentByYear.py
    Author(s): Elliott Rahming (1263495)

    Project: Milestone 1
    Date of Last Update: March 3, 2024

    Functional Summary:
         unemploymentByYear.py takes in a year range, a province, and an industry as commandline parameters, then reads the data from the industries file

         Commandline Parameters: 4
                argv[1] = province
                argv[2] = industry
                argv[3] = start year
                argv[4] = end year
                
    The file is a CSV file with the following columns:
        1. Year (Industry file only contains 2018-2023 at the moment)
        2. Province
        3. Labour Force characteristics
        4. North American Industry Classification System (NAICS)
        5. Value

    The valid industries include:
        1. Total (all industries)
        2. Goods-producing sector
        3. Agriculture
        4. Forestry, fishing, mining, quarrying, oil and gas
        5. Forestry and logging and support activities for forestry
        6. Fishing, hunting and trapping
        7. Mining, quarrying, and oil and gas extraction
        8. Utilities
        9. Construction
        10. Manufacturing
        11. Durables
        12. Non-durables
        13. Services-producing sector
        14. Wholesale and retail trade
        15. Wholesale trade
        16. Retail trade
        17. Transportation and warehousing
        18. Finance, insurance, real estate, rental and leasing
        19. Finance and insurance
        20. Real estate and rental and leasing
        21. Professional, scientific and technical services
        22. Business, building and other support services
        23. Educational services
        24. Health care and social assistance
        25. Information, culture and recreation
        26. Accommodation and food services
        27. Other services (except public administration)
        28. Public administration

    # Example Usage: python3 unemploymentByIndustry.py Newfoundland Total 2018 2019
'''
import sys

import csv

def main (argv):

    if len(argv) != 5:
        print("Usage: unemploymentByIndustry.py <province> <industry> <start year> <end year>")
        sys.exit(1)
    
    province = argv[1]
    industry = argv[2]
    startYear = int(argv[3])
    endYear = int(argv[4])

    # Open the file
    try:
        industry_file = open("industries.csv", encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format("industries.csv", err), file=sys.stderr)
        sys.exit(1)

    dataReader = csv.reader(industry_file)

    # Calculate the average for each year in the specified province and industry then display them at the end
    years = list(range(startYear, endYear + 1))
    yearSums = [0] * len(years)
    yearCounts = [0] * len(years)

    # Iterates through the CSV and adds the value to the sum for the corresponding year
    found = False
    provinceName = ""
    for row in dataReader:
        # Skips the first row
        if row[0] == "REF_DATE":
            continue
        # Checks if the row is in the specified province and industry and if the value is a valid number and not empty
        elif province.lower() in row[1].lower() and industry.lower() in row[3].lower() and row[4] != '' and int(row[0]) in years:
            # Adds the value to the sum for the corresponding year
            yearSums[years.index(int(row[0]))] += float(row[4])
            yearCounts[years.index(int(row[0]))] += 1
            found = True
            provinceName = row[1]

    # Prints the average unemployment rate for each year
    print("Average unemployment rate for " + industry + " in " + provinceName + " from " + str(startYear) + " to " + str(endYear) + ":")
    for i in range(len(years)):
        if yearCounts[i] != 0:
            print(str(years[i]) + ": {:.2f}%".format(yearSums[i] / yearCounts[i]))
        else:
            print(str(years[i]) + ": No data available")
    
    industry_file.close()

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)

# End of File

    
