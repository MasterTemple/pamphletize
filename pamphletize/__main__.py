import fitz  # PyMuPDF
import math
import sys
import argparse

def make_booklet(input_path, output_path, flip_back=False):
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
        
        # 🔄 Optionally rotate every second sheet
        if flip_back and (i // 2) % 2 == 1:
            sheet.set_rotation(180)

    # Save final PDF
    new_doc.save(output_path)
    print(f"✅ Created booklet-ready PDF: {output_path}")
    if flip_back:
        print("Note: Every second sheet rotated 180° for duplex alignment.")
    print("Print double-sided (flip on short edge), actual size.")


def cli():
    parser = argparse.ArgumentParser(description="Convert PDF into booklet layout (2-up, ordered, optional flip).")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("output", help="Output PDF file")
    parser.add_argument("--flip-back", action="store_true",
                        help="Rotate every second sheet by 180° for duplex printing")
    args = parser.parse_args()

    make_booklet(args.input, args.output, flip_back=args.flip_back)


if __name__ == "__main__":
    cli()
