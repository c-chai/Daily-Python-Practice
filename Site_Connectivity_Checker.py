import urllib.request
import urllib.error

def main(url):
    # Add 'http://' if the URL does not start with 'http://' or 'https://'
    # For this program you don't have to add 'www' 
    if not (url.startswith('http://') or url.startswith('https://')):
        print("Adding 'http://' to the URL.")
        url = 'http://' + url

    try:
        response = urllib.request.urlopen(url)
        print(f"Connected to {url} successfully")
        print("The response code was:", response.getcode())
    except urllib.error.URLError as e:
        print(f"Failed to connect to {url}")
        print("Error:", e)
    except ValueError:
        print(f"Invalid URL format: {url}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print('This is the site connectivity checker program')
input_url = input('Input the URL of the site that you want to check: ')

main(input_url)
