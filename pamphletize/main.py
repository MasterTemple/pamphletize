import fitz  # PyMuPDF
import math
import sys

def make_booklet(input_path, output_path):
    doc = fitz.open(input_path)
    total_pages = len(doc)

    # Pad to multiple of 4
    padded_total = math.ceil(total_pages / 4) * 4
    blank_pages = padded_total - total_pages

    # Booklet order (same logic as before)
    order = []
    left = padded_total
    right = 1
    while right < left:
        order.extend([left, right, right + 1, left - 1])
        right += 2
        left -= 2

    # Create new document (8.5x11 landscape)
    sheet_width = 11 * 72   # 11 inches
    sheet_height = 8.5 * 72 # 8.5 inches
    half_width = sheet_width / 2

    new_doc = fitz.open()

    def get_page_or_blank(num):
        if 1 <= num <= total_pages:
            return doc.load_page(num - 1)
        else:
            # Return a blank white page
            blank = fitz.open()
            blank.new_page(width=8.5*72, height=5.5*72)
            return blank.load_page(0)

    # Create each sheet (2 pages per side)
    for i in range(0, len(order), 2):
        left_page_num = order[i]
        right_page_num = order[i+1]

        # Create new landscape sheet
        sheet = new_doc.new_page(width=sheet_width, height=sheet_height)

        # Get pages (original or blank)
        left_page = get_page_or_blank(left_page_num)
        right_page = get_page_or_blank(right_page_num)

        # Define target rectangles
        left_rect = fitz.Rect(0, 0, half_width, sheet_height)
        right_rect = fitz.Rect(half_width, 0, sheet_width, sheet_height)

        # Insert both pages scaled to fit
        sheet.show_pdf_page(left_rect, left_page.parent, left_page.number)
        sheet.show_pdf_page(right_rect, right_page.parent, right_page.number)

    # Save final PDF
    new_doc.save(output_path)
    print(f"✅ Created booklet-ready PDF: {output_path}")
    print("Now print double-sided (flip on short edge), no scaling needed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: uv run main.py input.pdf output.pdf")
        sys.exit(1)
    make_booklet(sys.argv[1], sys.argv[2])
