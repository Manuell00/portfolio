from __future__ import annotations

from collections import OrderedDict
from copy import copy
from pathlib import Path
from statistics import mean

from openpyxl import load_workbook
from openpyxl.chart import BarChart, DoughnutChart, Reference
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo


ROOT = Path("/Users/manuelcaselli/Downloads/3 - Lavoro/Progetti/portfolio")
SOURCE = Path("/Users/manuelcaselli/Downloads/3 - Lavoro/Fiver/RobertaS-Work/Work.xlsx")
OUTPUT_DIR = ROOT / "output"
WORKBOOK_OUT = OUTPUT_DIR / "spreadsheet" / "RobertaS-FiverWork-showcase.xlsx"
REPORT_OUT = OUTPUT_DIR / "reports" / "roberta-fiverwork-audit.md"
PREVIEW_DIR = OUTPUT_DIR / "previews"

GREEN_BG = "D4EDDA"
GREEN_FG = "155724"
YELLOW_BG = "FFF3CD"
YELLOW_FG = "856404"
RED_BG = "F8D7DA"
RED_FG = "721C24"
NAVY = "17324D"
SLATE = "4F667D"
HEADER = "E8EEF5"
WHITE = "FFFFFF"
LIGHT = "F7FAFC"
GRID = "D7E0EA"
ACCENT = "2F80ED"

THIN_GRAY = Side(style="thin", color=GRID)
BASE_BORDER = Border(left=THIN_GRAY, right=THIN_GRAY, top=THIN_GRAY, bottom=THIN_GRAY)


def make_fill(color: str) -> PatternFill:
    return PatternFill(fill_type="solid", fgColor=color)


def make_font(color: str, *, bold: bool = False, size: int = 11) -> Font:
    return Font(name="Aptos", size=size, bold=bold, color=color)


GREEN_FILL = make_fill(GREEN_BG)
YELLOW_FILL = make_fill(YELLOW_BG)
RED_FILL = make_fill(RED_BG)
TITLE_FILL = make_fill(NAVY)
HEADER_FILL = make_fill(HEADER)
LIGHT_FILL = make_fill(LIGHT)
ACCENT_FILL = make_fill(ACCENT)
GREEN_FONT = make_font(GREEN_FG, bold=True)
YELLOW_FONT = make_font(YELLOW_FG, bold=True)
RED_FONT = make_font(RED_FG, bold=True)


SHEET_CONFIG = OrderedDict(
    {
        "ADL Performance": {
            "new_name": "ADS Performance",
            "title": "ADS PERFORMANCE - REPORT",
            "header_row": 2,
            "freeze": "A3",
            "table_end": "L5",
            "header_labels": [
                "Data",
                "Campagna",
                "Tipo Ads",
                "Impressioni",
                "Click",
                "CTR (%)",
                "Frequenza",
                "CPC (€)",
                "CPM (€)",
                "Spesa (€)",
                "Conversioni",
                "ROAS",
            ],
            "widths": [14, 20, 18, 14, 12, 12, 12, 12, 12, 13, 14, 12],
            "validations": [("C3:C200", '"PRINCIPALE,RETARGETING,LOOKALIKE"')],
            "percent_cols": ["F"],
            "currency_cols": ["H", "I", "J"],
            "integer_cols": ["D", "E", "K"],
            "decimal_cols": ["G", "L"],
            "conditional": {
                "F": [
                    ('AND(F3<>"",F3>=1%)', GREEN_FILL, GREEN_FONT),
                    ('AND(F3>=0.7%,F3<1%,F3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(F3<0.7%,F3<>"")', RED_FILL, RED_FONT),
                ],
                "G": [
                    ('AND(G3<>"",G3<=2.5)', GREEN_FILL, GREEN_FONT),
                    ('AND(G3>2.5,G3<=3.5,G3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(G3>3.5,G3<>"")', RED_FILL, RED_FONT),
                ],
                "H": [
                    ('AND(H3>=0.5,H3<=1.5,H3<>"")', GREEN_FILL, GREEN_FONT),
                    ('AND(H3>1.5,H3<=3,H3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(OR(H3<0.5,H3>3),H3<>"")', RED_FILL, RED_FONT),
                ],
                "I": [
                    ('AND(I3>=5,I3<=12,I3<>"")', GREEN_FILL, GREEN_FONT),
                    ('AND(I3>12,I3<=20,I3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(I3>20,I3<>"")', RED_FILL, RED_FONT),
                ],
                "L": [
                    ('AND(L3>=4,L3<>"")', GREEN_FILL, GREEN_FONT),
                    ('AND(L3>=2.5,L3<4,L3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(L3<2.5,L3<>"")', RED_FILL, RED_FONT),
                ],
            },
        },
        "Email Marketing": {
            "new_name": "Email Marketing",
            "title": "EMAIL MARKETING - REPORT",
            "header_row": 2,
            "freeze": "A3",
            "table_end": "M6",
            "header_labels": [
                "Data Invio",
                "Email Sequenza",
                "Tipo Campagna",
                "Segmento",
                "Email Inviate",
                "Email Aperte",
                "Open Rate (%)",
                "Click Totali",
                "CTR Email (%)",
                "Conversioni",
                "Conv Rate (%)",
                "Disiscrizioni",
                "ROI (€)",
            ],
            "widths": [14, 20, 22, 20, 14, 14, 14, 12, 14, 12, 14, 14, 12],
            "validations": [
                ("C3:C200", '"WELCOME,ABBANDONO CARRELLO,NURTURING,PROMOZIONALE"'),
                ("D3:D200", '"LEAD GOOGLE ADS,LEAD ORGANICO,CLIENTI,TUTTI"'),
            ],
            "percent_cols": ["G", "I", "K"],
            "currency_cols": ["M"],
            "integer_cols": ["E", "F", "H", "J", "L"],
            "conditional": {
                "G": [
                    ('AND(G3<>"",G3>=25%)', GREEN_FILL, GREEN_FONT),
                    ('AND(G3>=18%,G3<25%,G3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(G3<18%,G3<>"")', RED_FILL, RED_FONT),
                ],
                "I": [
                    ('AND(I3<>"",I3>=4%)', GREEN_FILL, GREEN_FONT),
                    ('AND(I3>=2%,I3<4%,I3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(I3<2%,I3<>"")', RED_FILL, RED_FONT),
                ],
                "K": [
                    ('AND(K3<>"",K3>=2.5%)', GREEN_FILL, GREEN_FONT),
                    ('AND(K3>=1%,K3<2.5%,K3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(K3<1%,K3<>"")', RED_FILL, RED_FONT),
                ],
            },
        },
        "Landing Pages": {
            "new_name": "Landing Pages",
            "title": "LANDING PAGES - REPORT",
            "header_row": 2,
            "freeze": "A3",
            "table_end": "L7",
            "header_labels": [
                "Data",
                "Nome Landing",
                "Sorgente Traffico",
                "Dispositivo",
                "Sessioni",
                "Bounce Rate (%)",
                "Tempo Medio (sec)",
                "Scroll > 70% (%)",
                "Click CTA",
                "CTA Rate (%)",
                "Conversioni",
                "Conv Rate (%)",
            ],
            "widths": [14, 22, 20, 14, 12, 15, 16, 16, 12, 13, 12, 13],
            "validations": [
                ("C3:C200", '"GOOGLE ADS,META ADS,ORGANICO,EMAIL,DIRETTO"'),
                ("D3:D200", '"DESKTOP,MOBILE,TABLET"'),
            ],
            "percent_cols": ["F", "H", "J", "L"],
            "integer_cols": ["E", "G", "I", "K"],
            "conditional": {
                "F": [
                    ('AND(F3<>"",F3<=50%)', GREEN_FILL, GREEN_FONT),
                    ('AND(F3>50%,F3<=65%,F3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(F3>65%,F3<>"")', RED_FILL, RED_FONT),
                ],
                "G": [
                    ('AND(G3<>"",G3>=45)', GREEN_FILL, GREEN_FONT),
                    ('AND(G3>=20,G3<45,G3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(G3<20,G3<>"")', RED_FILL, RED_FONT),
                ],
                "J": [
                    ('AND(J3<>"",J3>=8%)', GREEN_FILL, GREEN_FONT),
                    ('AND(J3>=4%,J3<8%,J3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(J3<4%,J3<>"")', RED_FILL, RED_FONT),
                ],
                "L": [
                    ('AND(L3<>"",L3>=3%)', GREEN_FILL, GREEN_FONT),
                    ('AND(L3>=1.5%,L3<3%,L3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(L3<1.5%,L3<>"")', RED_FILL, RED_FONT),
                ],
            },
        },
        "Funnel Analysis": {
            "new_name": "Funnel Analysis",
            "title": "FUNNEL ANALYSIS - REPORT",
            "header_row": 2,
            "freeze": "A3",
            "table_end": "K5",
            "header_labels": [
                "Data",
                "Campagna",
                "Sorgente",
                "Click Ads",
                "Sessioni Landing",
                "Drop-off Ads → Landing (%)",
                "Click CTA",
                "Drop-off Landing → CTA (%)",
                "Checkout Iniziati",
                "Drop-off CTA → Checkout (%)",
                "Acquisti Completati",
            ],
            "widths": [14, 20, 16, 12, 16, 22, 12, 24, 18, 22, 18],
            "validations": [("C3:C200", '"GOOGLE ADS,META ADS,EMAIL"')],
            "percent_cols": ["F", "H", "J"],
            "integer_cols": ["D", "E", "G", "I", "K"],
            "conditional": {
                "F": [
                    ('AND(F3<>"",F3<=10%)', GREEN_FILL, GREEN_FONT),
                    ('AND(F3>10%,F3<=20%,F3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(F3>20%,F3<>"")', RED_FILL, RED_FONT),
                ],
                "H": [
                    ('AND(H3<>"",H3<=85%)', GREEN_FILL, GREEN_FONT),
                    ('AND(H3>85%,H3<=92%,H3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(H3>92%,H3<>"")', RED_FILL, RED_FONT),
                ],
                "J": [
                    ('AND(J3<>"",J3<=20%)', GREEN_FILL, GREEN_FONT),
                    ('AND(J3>20%,J3<=35%,J3<>"")', YELLOW_FILL, YELLOW_FONT),
                    ('AND(J3>35%,J3<>"")', RED_FILL, RED_FONT),
                ],
            },
        },
    }
)


def trim_strings(ws) -> None:
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, str):
                cell.value = cell.value.strip()


def clear_conditional_formatting(ws) -> None:
    ws.conditional_formatting._cf_rules.clear()


def reset_validations(ws) -> None:
    ws.data_validations.dataValidation = []


def add_validation(ws, cell_range: str, formula: str) -> None:
    dv = DataValidation(type="list", formula1=formula, allow_blank=True)
    dv.prompt = "Seleziona un valore dall'elenco"
    dv.error = "Valore non valido"
    ws.add_data_validation(dv)
    dv.add(cell_range)


def style_header_row(ws, row_idx: int, last_col: int) -> None:
    for col_idx in range(1, last_col + 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.fill = HEADER_FILL
        cell.font = make_font(NAVY, bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = BASE_BORDER


def style_body(ws, start_row: int, end_row: int, last_col: int) -> None:
    for row_idx in range(start_row, end_row + 1):
        for col_idx in range(1, last_col + 1):
            cell = ws.cell(row=row_idx, column=col_idx)
            if cell.value is None:
                continue
            if row_idx % 2 == 0:
                cell.fill = LIGHT_FILL
            cell.border = BASE_BORDER
            cell.font = make_font(NAVY)
            align = "center"
            if col_idx in (2, 3, 4):
                align = "left"
            cell.alignment = Alignment(horizontal=align, vertical="center")


def add_conditional_rules(ws, config: dict) -> None:
    for col, rules in config.get("conditional", {}).items():
        cell_range = f"{col}3:{col}200"
        for formula, fill, font in rules:
            ws.conditional_formatting.add(
                cell_range,
                FormulaRule(formula=[formula], fill=copy(fill), font=copy(font)),
            )


def set_number_formats(ws, config: dict) -> None:
    for col in config.get("percent_cols", []):
        for row in range(3, 201):
            ws[f"{col}{row}"].number_format = "0.0%"
    for col in config.get("currency_cols", []):
        for row in range(3, 201):
            ws[f"{col}{row}"].number_format = '€ #,##0.00'
    for col in config.get("integer_cols", []):
        for row in range(3, 201):
            ws[f"{col}{row}"].number_format = "#,##0"
    for col in config.get("decimal_cols", []):
        for row in range(3, 201):
            ws[f"{col}{row}"].number_format = "0.00"
    for row in range(3, 201):
        ws[f"A{row}"].number_format = "dd/mm/yyyy"


def build_table(ws, ref: str, name: str) -> None:
    table = Table(displayName=name, ref=ref)
    table.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=False,
    )
    ws.add_table(table)


def normalize_sheet(ws, config: dict) -> None:
    trim_strings(ws)
    if ws.title != config["new_name"]:
        ws.title = config["new_name"]

    last_col = len(config["header_labels"])
    last_col_letter = get_column_letter(last_col)
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = config["freeze"]
    ws.auto_filter.ref = f"A{config['header_row']}:{last_col_letter}{ws.max_row}"
    ws.row_dimensions[1].height = 28
    ws.row_dimensions[2].height = 22

    for idx, width in enumerate(config["widths"], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    for idx in range(last_col + 1, ws.max_column + 1):
        ws.column_dimensions[get_column_letter(idx)].hidden = True

    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col)
    title_cell = ws["A1"]
    title_cell.value = config["title"]
    title_cell.fill = TITLE_FILL
    title_cell.font = make_font(WHITE, bold=True, size=14)
    title_cell.alignment = Alignment(horizontal="left", vertical="center")

    for col_idx, label in enumerate(config["header_labels"], start=1):
        ws.cell(row=2, column=col_idx).value = label

    style_header_row(ws, 2, last_col)
    style_body(ws, 3, ws.max_row, last_col)
    set_number_formats(ws, config)

    clear_conditional_formatting(ws)
    reset_validations(ws)
    for cell_range, formula in config.get("validations", []):
        add_validation(ws, cell_range, formula)
    add_conditional_rules(ws, config)

    if ws.tables:
        ws.tables.clear()
    build_table(ws, f"A2:{config['table_end']}", f"{ws.title.replace(' ', '')}Table")


def get_numeric(ws, cell_ref: str, default: float = 0.0) -> float:
    value = ws[cell_ref].value
    if value is None:
        return default
    return float(value)


def create_dashboard(wb) -> dict[str, float]:
    if "Performance Dashboard" in wb.sheetnames:
        del wb["Performance Dashboard"]

    dashboard = wb.create_sheet("Performance Dashboard", 0)
    ads = wb["ADS Performance"]
    email = wb["Email Marketing"]
    landing = wb["Landing Pages"]
    funnel = wb["Funnel Analysis"]

    dashboard.sheet_view.showGridLines = False
    dashboard.freeze_panes = "A8"
    for col, width in {
        "A": 4,
        "B": 18,
        "C": 15,
        "D": 18,
        "E": 15,
        "F": 18,
        "G": 15,
        "H": 18,
        "I": 15,
        "J": 18,
        "K": 15,
        "L": 16,
    }.items():
        dashboard.column_dimensions[col].width = width

    dashboard.merge_cells("B2:L2")
    dashboard["B2"] = "Digital Marketing Performance Dashboard"
    dashboard["B2"].fill = TITLE_FILL
    dashboard["B2"].font = make_font(WHITE, bold=True, size=16)
    dashboard["B2"].alignment = Alignment(horizontal="left", vertical="center")
    dashboard.row_dimensions[2].height = 30
    dashboard["B3"] = "Portfolio-ready showcase based on the delivered Fiverr workbook"
    dashboard["B3"].font = make_font(SLATE, size=11)

    kpis = [
        ("B5:D7", "Total Spend", sum(get_numeric(ads, f"J{row}") for row in range(3, 6)), '€ #,##0.00'),
        ("E5:G7", "Average ROAS", mean(get_numeric(ads, f"L{row}") for row in range(3, 6)), "0.00x"),
        ("H5:J7", "Avg Open Rate", mean(get_numeric(email, f"G{row}") for row in range(3, 6)), "0.0%"),
        ("K5:L7", "Avg Landing Conv", mean(get_numeric(landing, f"L{row}") for row in range(3, 6)), "0.0%"),
    ]
    for cell_range, label, value, fmt in kpis:
        dashboard.merge_cells(cell_range)
        tl = cell_range.split(":")[0]
        cell = dashboard[tl]
        cell.value = f"{label}\n{value}"
        cell.fill = LIGHT_FILL
        cell.font = make_font(NAVY, bold=True, size=13)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        for row in dashboard[cell_range]:
            for c in row:
                c.border = BASE_BORDER
        cell.number_format = fmt

    dashboard["B10"] = "Ads Type"
    dashboard["C10"] = "ROAS"
    for idx, row in enumerate(range(3, 6), start=11):
        dashboard[f"B{idx}"] = ads[f"C{row}"].value
        dashboard[f"C{idx}"] = ads[f"L{row}"].value
        dashboard[f"C{idx}"].number_format = "0.00x"

    dashboard["E10"] = "Email Segment"
    dashboard["F10"] = "Open Rate"
    for idx, row in enumerate(range(3, 7), start=11):
        dashboard[f"E{idx}"] = email[f"D{row}"].value
        dashboard[f"F{idx}"] = email[f"G{row}"].value
        dashboard[f"F{idx}"].number_format = "0.0%"

    dashboard["H10"] = "Traffic Source"
    dashboard["I10"] = "Conv Rate"
    for idx, row in enumerate(range(3, 8), start=11):
        dashboard[f"H{idx}"] = landing[f"C{row}"].value
        dashboard[f"I{idx}"] = landing[f"L{row}"].value
        dashboard[f"I{idx}"].number_format = "0.0%"

    dashboard["K10"] = "Funnel Stage"
    dashboard["L10"] = "Avg Drop-off"
    stage_values = [
        ("Ads → Landing", mean(get_numeric(funnel, f"F{row}") for row in range(3, 6))),
        ("Landing → CTA", mean(get_numeric(funnel, f"H{row}") for row in range(3, 6))),
        ("CTA → Checkout", mean(get_numeric(funnel, f"J{row}") for row in range(3, 6))),
    ]
    for idx, (label, value) in enumerate(stage_values, start=11):
        dashboard[f"K{idx}"] = label
        dashboard[f"L{idx}"] = value
        dashboard[f"L{idx}"].number_format = "0.0%"

    for header_cell in ("B10", "C10", "E10", "F10", "H10", "I10", "K10", "L10"):
        dashboard[header_cell].fill = HEADER_FILL
        dashboard[header_cell].font = make_font(NAVY, bold=True)
        dashboard[header_cell].border = BASE_BORDER
        dashboard[header_cell].alignment = Alignment(horizontal="center")

    for area in ("B11:C13", "E11:F14", "H11:I15", "K11:L13"):
        for row in dashboard[area]:
            for cell in row:
                cell.border = BASE_BORDER
                if cell.column in (3, 6, 9, 12):
                    cell.alignment = Alignment(horizontal="center")

    ads_chart = BarChart()
    ads_chart.type = "bar"
    ads_chart.style = 10
    ads_chart.title = "ROAS by Ads Type"
    ads_chart.y_axis.title = "Campaign Type"
    ads_chart.x_axis.title = "ROAS"
    ads_chart.height = 6
    ads_chart.width = 10
    ads_chart.add_data(Reference(dashboard, min_col=3, min_row=10, max_row=13), titles_from_data=True)
    ads_chart.set_categories(Reference(dashboard, min_col=2, min_row=11, max_row=13))
    ads_chart.legend = None
    dashboard.add_chart(ads_chart, "B17")

    email_chart = BarChart()
    email_chart.style = 11
    email_chart.title = "Email Open Rate by Segment"
    email_chart.y_axis.title = "Open Rate"
    email_chart.height = 6
    email_chart.width = 10
    email_chart.add_data(Reference(dashboard, min_col=6, min_row=10, max_row=14), titles_from_data=True)
    email_chart.set_categories(Reference(dashboard, min_col=5, min_row=11, max_row=14))
    email_chart.legend = None
    dashboard.add_chart(email_chart, "G17")

    landing_chart = DoughnutChart()
    landing_chart.style = 26
    landing_chart.title = "Landing Conversion Mix"
    landing_chart.height = 7
    landing_chart.width = 8
    landing_chart.add_data(Reference(dashboard, min_col=9, min_row=10, max_row=15), titles_from_data=True)
    landing_chart.set_categories(Reference(dashboard, min_col=8, min_row=11, max_row=15))
    dashboard.add_chart(landing_chart, "B31")

    funnel_chart = BarChart()
    funnel_chart.style = 12
    funnel_chart.title = "Average Funnel Drop-off"
    funnel_chart.y_axis.title = "Drop-off"
    funnel_chart.height = 7
    funnel_chart.width = 10
    funnel_chart.add_data(Reference(dashboard, min_col=12, min_row=10, max_row=13), titles_from_data=True)
    funnel_chart.set_categories(Reference(dashboard, min_col=11, min_row=11, max_row=13))
    funnel_chart.legend = None
    dashboard.add_chart(funnel_chart, "H31")

    dashboard["B46"] = "Audit Notes"
    dashboard["B46"].font = make_font(NAVY, bold=True, size=12)
    dashboard["B47"] = "Aligned headers, cleaned typos, rebuilt validations and added a portfolio-ready dashboard with native Excel charts."
    dashboard["B47"].font = make_font(SLATE, size=10)

    return {
        "total_spend": round(sum(get_numeric(ads, f"J{row}") for row in range(3, 6)), 2),
        "avg_roas": round(mean(get_numeric(ads, f"L{row}") for row in range(3, 6)), 2),
        "avg_open_rate": round(mean(get_numeric(email, f"G{row}") for row in range(3, 6)) * 100, 1),
        "avg_landing_conv": round(mean(get_numeric(landing, f"L{row}") for row in range(3, 6)) * 100, 1),
    }


def write_report(metrics: dict[str, float]) -> None:
    REPORT_OUT.write_text(
        "\n".join(
            [
                "# RobertaS Fiverr Workbook Audit",
                "",
                "## Verdict",
                "The delivered workbook was broadly correct in structure, validations, and conditional formatting logic.",
                "It was usable as a client delivery, but not yet optimized as a portfolio/Fiverr showcase.",
                "",
                "## Main Issues Found",
                "- `ADL Performance` was not aligned with the guide wording (`ADS Performance`).",
                "- Several labels had typos or inconsistent naming, including `Dropp-off` and `Conv Rate` without `%`.",
                "- `ROI (%)` did not match the guide, which requested `ROI (€)`.",
                "- The workbook had no auto-filters and no chart/dashboard layer.",
                "- Some dropdown definitions contained trailing spaces.",
                "",
                "## Improvements Added In Showcase",
                "- Normalized titles, headers, number formats, data validation, and conditional formatting.",
                "- Added a `Performance Dashboard` sheet with KPI cards and four native Excel charts.",
                "- Upgraded sheet styling for cleaner presentation in a portfolio context.",
                "",
                "## KPI Snapshot",
                f"- Total Spend: EUR {metrics['total_spend']:.2f}",
                f"- Average ROAS: {metrics['avg_roas']:.2f}x",
                f"- Average Open Rate: {metrics['avg_open_rate']:.1f}%",
                f"- Average Landing Conversion Rate: {metrics['avg_landing_conv']:.1f}%",
                "",
                f"Workbook output: `{WORKBOOK_OUT}`",
            ]
        ),
        encoding="utf-8",
    )


def write_svg_previews(metrics: dict[str, float]) -> None:
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    cover_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
<rect width="1600" height="900" fill="#F4F8FB"/>
<rect x="72" y="64" width="1456" height="772" rx="28" fill="#FFFFFF" stroke="#D7E0EA" stroke-width="2"/>
<rect x="72" y="64" width="1456" height="140" rx="28" fill="#17324D"/>
<text x="128" y="132" font-family="Aptos, Segoe UI, Arial" font-size="48" font-weight="700" fill="#FFFFFF">Excel Performance Dashboard</text>
<text x="128" y="176" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#D7EAF7">Fiverr delivery upgraded for portfolio and showcase use</text>
<rect x="128" y="250" width="280" height="150" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="438" y="250" width="280" height="150" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="748" y="250" width="280" height="150" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="1058" y="250" width="280" height="150" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<text x="160" y="300" font-family="Aptos, Segoe UI, Arial" font-size="22" fill="#4F667D">Total Spend</text>
<text x="160" y="356" font-family="Aptos, Segoe UI, Arial" font-size="42" font-weight="700" fill="#17324D">EUR {metrics['total_spend']:.2f}</text>
<text x="470" y="300" font-family="Aptos, Segoe UI, Arial" font-size="22" fill="#4F667D">Average ROAS</text>
<text x="470" y="356" font-family="Aptos, Segoe UI, Arial" font-size="42" font-weight="700" fill="#17324D">{metrics['avg_roas']:.2f}x</text>
<text x="780" y="300" font-family="Aptos, Segoe UI, Arial" font-size="22" fill="#4F667D">Open Rate</text>
<text x="780" y="356" font-family="Aptos, Segoe UI, Arial" font-size="42" font-weight="700" fill="#17324D">{metrics['avg_open_rate']:.1f}%</text>
<text x="1090" y="300" font-family="Aptos, Segoe UI, Arial" font-size="22" fill="#4F667D">Landing Conv.</text>
<text x="1090" y="356" font-family="Aptos, Segoe UI, Arial" font-size="42" font-weight="700" fill="#17324D">{metrics['avg_landing_conv']:.1f}%</text>
<rect x="128" y="460" width="560" height="250" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="760" y="460" width="578" height="250" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<text x="160" y="510" font-family="Aptos, Segoe UI, Arial" font-size="26" font-weight="700" fill="#17324D">What was improved</text>
<text x="160" y="560" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">• Corrected naming, labels and formatting</text>
<text x="160" y="605" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">• Rebuilt dropdowns and conditional rules</text>
<text x="160" y="650" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">• Added dashboard sheet with native charts</text>
<text x="160" y="695" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">• Styled for portfolio and Fiverr presentation</text>
<text x="792" y="510" font-family="Aptos, Segoe UI, Arial" font-size="26" font-weight="700" fill="#17324D">Sheets included</text>
<text x="792" y="560" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">ADS Performance</text>
<text x="792" y="605" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">Email Marketing</text>
<text x="792" y="650" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">Landing Pages</text>
<text x="792" y="695" font-family="Aptos, Segoe UI, Arial" font-size="24" fill="#4F667D">Funnel Analysis + Dashboard</text>
</svg>"""
    dashboard_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
<rect width="1600" height="900" fill="#EFF5FA"/>
<rect x="80" y="70" width="1440" height="760" rx="26" fill="#FFFFFF" stroke="#D7E0EA" stroke-width="2"/>
<text x="130" y="130" font-family="Aptos, Segoe UI, Arial" font-size="40" font-weight="700" fill="#17324D">Dashboard Preview</text>
<rect x="130" y="170" width="250" height="110" rx="18" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="405" y="170" width="250" height="110" rx="18" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="680" y="170" width="250" height="110" rx="18" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="955" y="170" width="250" height="110" rx="18" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="1230" y="170" width="240" height="110" rx="18" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="130" y="340" width="630" height="390" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<rect x="810" y="340" width="610" height="390" rx="20" fill="#F7FAFC" stroke="#D7E0EA"/>
<text x="170" y="395" font-family="Aptos, Segoe UI, Arial" font-size="28" font-weight="700" fill="#17324D">ROAS by Ads Type</text>
<rect x="190" y="440" width="320" height="36" rx="8" fill="#2F80ED"/>
<rect x="190" y="500" width="180" height="36" rx="8" fill="#7DB3F4"/>
<rect x="190" y="560" width="500" height="36" rx="8" fill="#17324D"/>
<text x="190" y="433" font-family="Aptos, Segoe UI, Arial" font-size="18" fill="#4F667D">PRINCIPALE</text>
<text x="190" y="493" font-family="Aptos, Segoe UI, Arial" font-size="18" fill="#4F667D">RETARGETING</text>
<text x="190" y="553" font-family="Aptos, Segoe UI, Arial" font-size="18" fill="#4F667D">LOOKALIKE</text>
<text x="850" y="395" font-family="Aptos, Segoe UI, Arial" font-size="28" font-weight="700" fill="#17324D">Average Funnel Drop-off</text>
<rect x="860" y="435" width="110" height="220" rx="12" fill="#2F80ED"/>
<rect x="1020" y="305" width="110" height="350" rx="12" fill="#7DB3F4"/>
<rect x="1180" y="515" width="110" height="140" rx="12" fill="#17324D"/>
<text x="855" y="690" font-family="Aptos, Segoe UI, Arial" font-size="18" fill="#4F667D">Ads→Landing</text>
<text x="1000" y="690" font-family="Aptos, Segoe UI, Arial" font-size="18" fill="#4F667D">Landing→CTA</text>
<text x="1155" y="690" font-family="Aptos, Segoe UI, Arial" font-size="18" fill="#4F667D">CTA→Checkout</text>
</svg>"""
    (PREVIEW_DIR / "roberta-showcase-cover.svg").write_text(cover_svg, encoding="utf-8")
    (PREVIEW_DIR / "roberta-showcase-dashboard.svg").write_text(dashboard_svg, encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.joinpath("spreadsheet").mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.joinpath("reports").mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    wb = load_workbook(SOURCE)
    for original_name, config in SHEET_CONFIG.items():
        normalize_sheet(wb[original_name], config)

    metrics = create_dashboard(wb)
    wb.properties.creator = "Codex"
    wb.properties.lastModifiedBy = "Codex"
    wb.save(WORKBOOK_OUT)

    write_report(metrics)
    write_svg_previews(metrics)


if __name__ == "__main__":
    main()
