from openpyxl import load_workbook

from config import EXCEL_PATH


def read_factures():
    wb = load_workbook(EXCEL_PATH)
    ws = wb.active
    lines = []

    for numero, fecha, emisor, total, formato in ws.iter_rows(
        min_row=2, values_only=True
    ):
        line = f"Factura {numero}, emitida el {fecha} por {emisor}, total {total} (formato: {formato})"
        lines.append(line)
    resultado = "\n".join(lines)
    return resultado


if __name__ == "__main__":
    print(read_factures())