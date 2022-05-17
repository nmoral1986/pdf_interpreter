from tika import parser
import pandas as pd
import os


def get_files():
    path = 'data'
    fls = os.listdir(path)
    return fls


def read_file(pdf_file):
    data = {}
    file_data = parser.from_file(pdf_file)
    text = file_data['content']
    new_text = text.split('\n')
    new_text2 = []

    txt_temp = ''
    flag = False

    for line in new_text:
        if 'DSR-' in line or 'DS-' in line:
            if flag:
                flag = False
                new_text2.append(txt_temp)
                txt_temp = ''
            if '$' in line:
                new_text2.append(line)
            else:
                txt_temp = line
                flag = True
        elif txt_temp and flag:
            txt_temp += line
    for line in new_text2:
        if line == 'DSR-3695923':
            print('ERROR')
        if (('DSR-' in line) and ('$' in line)) or (('DS-' in line) and ('$' in line)):
            s_line = line.split('$')
            dsr_list = s_line[0].split(' ')
            dsr = dsr_list[0]

            val_list = s_line[1].split(' ')
            val = val_list[1].replace(',', '')

            if 'DSR-' in dsr or 'DS-' in dsr:
                data[dsr] = float(val)
    print(data)
    return data


def write_file(data):
    keys = data.keys()
    values = data.values()
    df = pd.DataFrame({"Código de Servicio": keys, "Valor": values})
    df.to_excel("results/result.xlsx")


if __name__ == "__main__":
    dict_t = {}
    files = get_files()
    for file in files:
        dict_t.update(read_file(f'data/{file}'))
    write_file(dict_t)
