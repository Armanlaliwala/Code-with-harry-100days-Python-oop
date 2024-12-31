import PyPDF2

def merge_pdfs(pdf_list, output_path):
    # Create a PDF merger object
    merger = PyPDF2.PdfMerger()

    # Iterate over the list of PDF file paths
    for pdf in pdf_list:
        # Append each PDF to the merger
        merger.append(pdf)

    # Write the merged PDFs to the output file
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"Merged {len(pdf_list)} PDFs into {output_path}")

# List of PDF file paths to be merged
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# Output path for the merged PDF
output_file = 'merged.pdf'

# Call the merge_pdfs function
merge_pdfs(pdf_files, output_file)
