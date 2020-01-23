import time 

# read JSON INPUT for write down to JSON results file
def transformer(raw_data, save_file):
    data = raw_data.get('data')
    all_records = data.split('|')

    timestamp = all_records[0]

    # GET THE DATE + TIME FORMAT
    date_record = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

    true_data = all_records.pop(0)

    usable_data = all_records.insert(0, date_record)

    # WRITE TO CSV
    with open(save_file, "w") as output_file:
        output_file.write(message + "\n")
        json.dump(usable_data, outfile)
