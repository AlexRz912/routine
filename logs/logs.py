def not_found_error(filename):
    print(f"[ERROR] : {filename} not found, please provide a routines.json file into jobs/routine folder")

def unexpected_error_onload(filename, error):
    print(f"[ERROR] : Unexpected error while loading {filename} : {error}")
