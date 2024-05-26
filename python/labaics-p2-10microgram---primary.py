# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"7270","system":"gprdproduct"},{"code":"50051","system":"gprdproduct"},{"code":"10968","system":"gprdproduct"},{"code":"25784","system":"gprdproduct"},{"code":"57694","system":"gprdproduct"},{"code":"6526","system":"gprdproduct"},{"code":"6569","system":"gprdproduct"},{"code":"47638","system":"gprdproduct"},{"code":"7268","system":"gprdproduct"},{"code":"1087","system":"gprdproduct"},{"code":"14306","system":"gprdproduct"},{"code":"2723","system":"gprdproduct"},{"code":"7133","system":"gprdproduct"},{"code":"3289","system":"gprdproduct"},{"code":"35725","system":"gprdproduct"},{"code":"11588","system":"gprdproduct"},{"code":"6462","system":"gprdproduct"},{"code":"54742","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('labaics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["labaics-p2-10microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["labaics-p2-10microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["labaics-p2-10microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
