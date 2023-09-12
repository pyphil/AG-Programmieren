# test
```python
def ocr_scan(filepath):
    # get text from pdf
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # always add complete text from images to text variable as well
    # if no text in pdf: convert to image and then to searchable pdf
    images = convert_from_path(filepath, dpi=300, fmt='tiff')
    writer = PdfWriter()
    if text == "":
        for image in images:
            page = pytesseract.image_to_pdf_or_hocr(image, lang="deu", extension='pdf')
            pdf = PdfReader(io.BytesIO(page))
            writer.add_page(pdf.pages[0])
            # export pdf to same filename as searchable pdf if only image
            with open(filepath, 'wb') as f:
                writer.write(f)
    else:
        for image in images:
            text += pytesseract.image_to_string(image, lang="deu")

    return text
```
