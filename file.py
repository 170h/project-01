def save_to_file(file_name, job):
    file = open(f"{file_name}.csv", "w")
    file.write("Company,Position,Location,URL\n")

    for jobs in job:
        file.write(f"{jobs['company']}, {jobs['position']}, {jobs['location']}, {jobs['link']}\n")

    file.close()
