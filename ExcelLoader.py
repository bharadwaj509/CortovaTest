import csv
import logging

class ExcelLoader():
    def loadFile(self, file_list):

        # initiating the number of users to 1
        count_of_users = 1

        # looping through each of the files
        for filename in file_list:
            try:
                # if the file does not open or not found, it will through an exception
                with open(filename, mode = "r") as csvfile:
                    logging.info("Processing file %s", filename)
                    csv_reader = csv.reader(csvfile, delimiter=',')
                    try:
                        # if the file does not contain any data, it will through an exception
                        header = next(csv_reader)
                        for row in csv_reader:
                            # if the row contains more than 2 data, an error will be logged.
                            if len(row) == 2:
                                full_name = row[0].split()
                                email = row[1]
                                yield [count_of_users, full_name[0], full_name[-1], email]
                                count_of_users = count_of_users+1
                            else:
                                logging.error("File %s has more than 2 columns at row %s.", filename, count_of_users)
                    except:
                        logging.error("File %s does not have data.", filename)
            except:
                logging.error("File %s not found. Please verify.", filename)
