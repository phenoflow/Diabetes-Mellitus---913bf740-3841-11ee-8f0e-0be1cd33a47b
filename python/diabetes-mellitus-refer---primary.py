# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2023.

import sys, csv, re

codes = [{"code":"8H4F.00","system":"readv2"},{"code":"8H4e.00","system":"readv2"},{"code":"8H7C.00","system":"readv2"},{"code":"8H7f.00","system":"readv2"},{"code":"8HTE100","system":"readv2"},{"code":"8HTe.00","system":"readv2"},{"code":"8HTk.00","system":"readv2"},{"code":"8HVU.00","system":"readv2"},{"code":"8Hj0.00","system":"readv2"},{"code":"8Hj3.00","system":"readv2"},{"code":"8Hj4.00","system":"readv2"},{"code":"8Hj5.00","system":"readv2"},{"code":"8Hl1.00","system":"readv2"},{"code":"8Hl4.00","system":"readv2"},{"code":"8IEQ.00","system":"readv2"},{"code":"8IEa.00","system":"readv2"},{"code":"ZL62500","system":"readv2"},{"code":"ZL62600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-refer---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-refer---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-refer---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
