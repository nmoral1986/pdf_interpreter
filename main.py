import tabula


def read_file(pdf_file):
    table = tabula.read_pdf(pdf_file, pages=3)
    print(table[0])


if __name__ == "__main__":
    pdf = 'data/FACTURA.pdf'
    read_file(pdf)
