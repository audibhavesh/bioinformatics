class BioOutput:
    @staticmethod
    def __save_output_file__(data, filename=None):
        if filename is None:
            with open("/output.txt", "w") as file:
                file.write(data)
        else:
            with open("../bio_output/output_" + filename + ".txt", "w") as file:
                file.write(data)
