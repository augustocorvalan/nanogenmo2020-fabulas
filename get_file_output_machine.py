def output_file(file_name: str, output: str):
    fo = open(file_name, "w+")
    fo.write(output)

    # Close opend file
    fo.close()
