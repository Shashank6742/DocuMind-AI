from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text() or ""

        text = text.strip()

        if text:

            pages.append({
                "page": page_number,
                "text": text
            })

    return pages