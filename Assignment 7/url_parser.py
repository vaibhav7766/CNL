from urllib.parse import urlparse

def parse_url(url):


  parsed_url = urlparse(url)
  return {
    "protocol": parsed_url.scheme,
    "domain": parsed_url.netloc,
    "port": parsed_url.port,
    "path": parsed_url.path
  }

def main():

  url = input("Enter a URL: ")

  parsed_url = parse_url(url)

  print("""
Parsing the URL String: {}
Done !!
Protocol: {}
Domain: {}
Port: {}
Path: {}
""".format(url, parsed_url["protocol"], parsed_url["domain"], parsed_url["port"], parsed_url["path"]))

if __name__ == "__main__":
  main()