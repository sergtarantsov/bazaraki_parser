def create_imprint(imprint_file, array):
    file=open(imprint_file, 'w')
    for element in array:
        file.write(f"{element}\n")
    file.close()
