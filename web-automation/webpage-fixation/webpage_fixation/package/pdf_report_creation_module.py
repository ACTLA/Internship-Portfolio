# package\pdf_report_creation_module.py
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import time
import datetime
from random import randint
import whois


def traceroute_website(url) -> str:
    import subprocess
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    try:
        tracert_result = subprocess.run(
            ['tracert', parsed_url.netloc], capture_output=True, text=True)
        return tracert_result.stdout
    except Exception as e:
        return str(e)


def get_whois_info(url):
    whois_info = whois.whois(url)
    return whois_info


def parse_whois_info_to_pdf_using_reportlab(canvas, whois_info):
    canvas.setFillColor(colors.grey)
    canvas.setFont('FreeSans', 14)
    text = canvas.beginText(40, int(A4[1]-100))
    text.setFont('FreeSans', 14)
    text.textLine(
        "Информация о владельце сайта c использованием сервиса Whois:")
    text.textLine("")
    for key, value in whois_info.items():
        if type(value) == list:
            for item in value:
                text.textLine(f"{key}: {item}")
                text.textLine("")
        else:
            text.textLine(f"{key}: {value}")
            text.textLine("")
    canvas.drawText(text)


def parse_traceroute_info_to_pdf(canvas, url):
    canvas.setFillColor(colors.grey)
    canvas.setFont('FreeSans', 14)
    text = canvas.beginText(40, int(A4[1]-100))
    text.setFont('FreeSans', 14)
    text.textLine(
        "Информация, полученная с помощью Traceroute:")
    for line in traceroute_website(url).splitlines():
        text.textLine(line)
    canvas.drawText(text)


def draw_traceroute_page_with_traceroute_info(canvas, url, page_number, protocol_number) -> None:
    draw_header(canvas, url, page_number, protocol_number)
    parse_traceroute_info_to_pdf(canvas, url)
    draw_page_number(canvas, page_number)
    canvas.showPage()


def draw_page_number(canvas, page_number):
    text = canvas.beginText(A4[0]/2, 20)
    text.setFont('FreeSans', 5)
    text.textLine(f"{page_number}")
    canvas.drawText(text)


def draw_header(canvas, url, page_number, protocol_number) -> None:
    timestamp = datetime.datetime.now().strftime(f"%d-%m-%Y %H:%M:%S")
    canvas.setFillColor(colors.grey)
    canvas.setFont('FreeSans', 5)
    w, h = A4
    text = canvas.beginText(20, int(h-20))
    text.setFont('FreeSans', 5)
    text.textLine(f"Приложение № {
                  page_number} к протоколу автоматизированного осмотра информации в сети интернет № {protocol_number}")
    text.textLine(
        f"Внешний вид страницы в сети интернет, расположенной по адресу {url}")
    text.textLine(f"Время создания: {
                  timestamp}")
    canvas.drawText(text)


def draw_initial_page_with_whois_info(canvas, url, page_number, protocol_number) -> None:
    draw_header(canvas, url, page_number, protocol_number)
    parse_whois_info_to_pdf_using_reportlab(canvas, get_whois_info(url))
    draw_page_number(canvas, page_number)
    canvas.showPage()


def create_website_photorecording_pdf_report(progressbar, **pdf_options) -> None:

    protocol_number = randint(1000, 9999)
    screenshots_with_timestamp = pdf_options['screenshots']
    c = canvas.Canvas(pdf_options['pdf_report_file_path'], pagesize=A4)
    i = 0
    page_number = 1

    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))

    draw_initial_page_with_whois_info(
        c, pdf_options['url'], page_number, protocol_number)
    page_number += 1

    progressbar["value"] = 60

    draw_traceroute_page_with_traceroute_info(
        c, pdf_options['url'], page_number, protocol_number)
    page_number += 1

    progressbar["value"] = 75

    iters_for_progressbar = 20 // len(screenshots_with_timestamp)
    for screenshot in screenshots_with_timestamp:
        i += 1
        progressbar["value"] = int(75 + iters_for_progressbar * i)
        if i % 2 == 1:
            draw_header(c, pdf_options['url'], page_number,
                        protocol_number)
            c.drawString(
                20, A4[1]-57, f"Скриншот № {i}  Дата создания: {screenshot[1]}")
            c.drawImage(screenshot[0], 20, -30, width=A4[0]-50, height=A4[1]-30,
                        showBoundary=True, preserveAspectRatio=True, anchor='n')
            continue
        if i % 2 == 0:
            c.drawString(
                20, 435, f"Скриншот № {i}  Дата создания: {screenshot[1]}")
            c.drawImage(screenshot[0], 20, -380, width=A4[0]-50, height=A4[1]-30,
                        showBoundary=True, preserveAspectRatio=True, anchor='n')
            draw_page_number(c, page_number)
            page_number += 1
            c.showPage()
            continue
    c.save()


if __name__ == "__main__":
    # print(A4)
    pass
