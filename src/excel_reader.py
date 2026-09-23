from openpyxl import load_workbook

from config import EXCEL_PATH


def read_factures(path):
    wb = load_workbook(path)
    ws = wb.active
    lines = []

    for fecha, formato, emisor, total, numero in ws.iter_rows(
        min_row=2, values_only=True
    ):
        line = f"Número: {numero} | Fecha: {fecha} | Emisor: {emisor} | Total: {total} | Formato: {formato}"
        lines.append(line)
    resultado = "\n".join(lines)
    return resultado


if __name__ == "__main__":
    print(read_factures(EXCEL_PATH))
