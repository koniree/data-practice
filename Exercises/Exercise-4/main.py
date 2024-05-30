import os
import csv
import io
import json

def translate_json(file, csv_filename):
            readfile = json.load(file)
            column = list(readfile.keys())
            rows = list(readfile.values())
            for key_main, value in readfile.items():
                if isinstance(value,dict):
                    for key, val in value.items():
                        #for key in value.keys():
                        column.append(f"{key_main}_{key}")
                        
                        #column[column.index(key_main)]
                        #for val in value.values():
                        rows.append(f"{key}_{val}")

            index_c = column.index(key_main)
            column.remove(column[index_c])
            index_r = rows.index(value)
            rows.remove(rows[index_r])
                      

                    #nested_dict = dict(value)
                    #subheader = nested_dict.keys()
                    #subvalue = nested_dict.values()
                    #column.append(subheader)

                 #except Exception as e: pass


            new_csv = open(os.path.join("./data/",csv_filename), 'w', newline='')
            
                
            csv_writer = csv.writer(new_csv)
            count = 0
            if count == 0:
                csv_writer.writerow(column)
                count += 1
            csv_writer.writerow(rows)
            
            

def get_json(dir):
    list_file = []
    for roots, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".json"):
                list_file.append(os.path.join(roots,file))
    return list_file
                
                
def main():
    list_file = get_json("./data")
    print(list_file)
    for path in list_file:
        with open(path, encoding='utf-8') as file:
            newfilename = os.path.basename(path).split('/')[-1].replace(".json",".csv")
            translate_json(file, newfilename)
            

    
    #translate_json("file-1.json","file-1.csv")
    



if __name__ == "__main__":
    main()
