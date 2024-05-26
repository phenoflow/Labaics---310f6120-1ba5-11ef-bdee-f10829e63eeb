# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"5143","system":"gprdproduct"},{"code":"5172","system":"gprdproduct"},{"code":"50560","system":"gprdproduct"},{"code":"49000","system":"gprdproduct"},{"code":"665","system":"gprdproduct"},{"code":"50886","system":"gprdproduct"},{"code":"53230","system":"gprdproduct"},{"code":"53283","system":"gprdproduct"},{"code":"638","system":"gprdproduct"},{"code":"51909","system":"gprdproduct"},{"code":"48739","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('labaics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["labaics-p2-seretide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["labaics-p2-seretide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["labaics-p2-seretide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
