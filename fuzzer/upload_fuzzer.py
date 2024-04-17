import requests
import os
from bs4 import BeautifulSoup  

# The URL where the file will be posted
UPLOAD_URL = 'http://localhost:3000/upload'

# The local path to the base file you're uploading
BASE_FILE_PATH = 'test_file.txt' 

# Path to your SecList file
SECLIST_PATH = 'SecList/Fuzzing/extensions-most-common.fuzz.txt' 
SECLIST_ALL_PATH = 'SecList/Fuzzing/file-extensions.txt'

def get_csrf_token(session, form_page_url):
    response = session.get(form_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
    return token

def upload_file(session, file_path, csrf_token):
    files = {'file_upload': (os.path.basename(file_path), open(file_path, 'rb'))}
    data = {'authenticity_token': csrf_token}
    response = session.post(UPLOAD_URL, data=data, files=files, allow_redirects=True)
    if "File type not allowed" in response.text:
        return response.status_code, "DENIED"
    elif "File uploaded successfully" in response.text:
        return response.status_code, "ACCEPTED"
    else:
        return response.status_code, response.reason

def main():
    # Create a session object to persist cookies and headers across requests
    session = requests.Session()
    
    # URL of the page with the upload form
    FORM_PAGE_URL = 'http://localhost:3000/welcome' 
    
    # Get CSRF token
    csrf_token = get_csrf_token(session, FORM_PAGE_URL)
    
    # Read the list of extensions from the SecList file
    with open(SECLIST_ALL_PATH, 'r') as f:
        extensions = f.read().splitlines()

    # Test the upload with each extension
    for ext in extensions:
        # Modify the file name based on the current extension
        test_file_path = f"{BASE_FILE_PATH}.{ext}"

        # Copy the base file to a new file with the current extension
        with open(BASE_FILE_PATH, 'rb') as base_file:
            with open(test_file_path, 'wb') as test_file:
                test_file.write(base_file.read())

        # Upload the file and print the result
        status_code, reason = upload_file(session, test_file_path, csrf_token)
        print(f".{ext} : {reason}") if reason == "ACCEPTED" else None

        # Remove the test file
        try:
            os.remove(test_file_path)
        except OSError as e:
            print(f"Error deleting test file {test_file_path}: {e.strerror}")

    print(f"Finished testing.")

if __name__ == '__main__':
    main()
