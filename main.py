from tika import parser


def read_file(pdf_file):
    data = {}
    file_data = parser.from_file(pdf_file)
    text = file_data['content']
    new_text = text.split('\n')
    for line in new_text:
        if (('DSR-' or 'DS-') and '$') in line:
            s_line = line.split('$')
            dsr_list = s_line[0].split(' ')
            dsr = dsr_list[0]

            val_list = s_line[1].split(' ')
            val = val_list[1]
            if 'DSR-' in dsr or 'DS-' in dsr:
                data[dsr] = val
    print(data)


if __name__ == "__main__":
    pdf = 'data/FACTURA.pdf'
    read_file(pdf)
