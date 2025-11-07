# Pamphletize

Create an easy-to-print **8.5"×11"** booklet (pamphlet) from a **half-letter (8.5"×5.5")** PDF.

This script automatically:
- 📄 Adds blank pages so the total page count is a multiple of 4  
- 🔢 Reorders pages into proper booklet order (so they fold correctly)  
- 🧩 Combines two half-sized pages into one landscape sheet  
- 🔁 Optionally flips every second sheet by 180° for duplex printers that rotate the back side

---

## 🧰 Requirements

Install [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (used for PDF layout and merging):

```bash
uv pip install pymupdf
````

---

## 🚀 Usage

```bash
uv run pamphletize input.pdf output.pdf --flip-back
```

**Positional arguments:**

* `input.pdf` — Path to your original half-page PDF
* `output.pdf` — Path where the new booklet PDF will be saved

**Optional flags:**

* `--flip-back` — Rotates every second sheet 180° for duplex printers that flip the back page upside-down

---

## 🖨️ Printing Instructions

Once the script produces your `output.pdf`:

1. Open it in your PDF viewer.

2. Set **print settings** as follows:

   * **Double-sided:** ✅ *Enabled* (`Flip on short edge`)
   * **Orientation:** *Landscape*
   * **Scaling:** *Actual size* (no scaling or fit-to-page)
   * **Paper size:** *Letter (8.5" × 11")*

3. Print, fold, and staple in the middle — you now have a perfect half-letter pamphlet.

---

## 🧮 Example

For a 14-page input PDF (`input.pdf`):

* The script pads it to 16 pages (adding 2 blanks)
* Reorders pages into booklet sequence
* Merges pairs of half-pages into 8 full sheets
* Produces `output.pdf`, ready for duplex booklet printing

---

## 🧩 Example Workflow

```bash
# Make a booklet without rotation
uv run main.py input.pdf booklet.pdf

# Make a booklet where every second sheet is rotated 180°
uv run main.py input.pdf booklet.pdf --flip-back
```

---

## 🧠 Notes

* Each sheet (8.5"×11") contains **two 8.5"×5.5" pages**, side by side.
* The resulting PDF is *already arranged* for booklet printing — no need to select "2 pages per sheet" in your print dialog.
* The `--flip-back` option is useful for printers that feed pages differently when duplexing (you can try both ways to see which aligns correctly).

---

<!--
## 🛠️ Example Output

| Input                                                                                                                                                  | Output (Printed + Folded)                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| ![Half-page layout](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Paper_size_DIY_half_letter.svg/300px-Paper_size_DIY_half_letter.svg.png) | ![Booklet layout](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Booklet-printing.svg/300px-Booklet-printing.svg.png) |

*(illustrative example only — not actual output)*
-->
