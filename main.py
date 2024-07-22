import requests

# urls = [
#         'https://shantanuuchak.tech' , 
#         'https://quastech.in',
#         'https://innovaccer.com/contact-us',
#         'https://www.infogain.com/about/contact-us/']

# res = requests.get('https://shantanuuchak.tech')


#function to split"
def split_quote(text):
  return text.split('"')

# function to replace mailto
def remove_mailto(email_str):
  return email_str.replace("mailto:", "")

#function to find email
def find_email(data_list):
  emails_list = []
  for el in data_list:
    if "@" in el and "." in el and "/" not in el:
      emails_list.append(remove_mailto(el))
  return emails_list
  
# function to request url
def fetch(url):
  res = requests.get(url)

  if res.status_code == 200:
    return res.text

  print(f"Failed with error code {res.status_code}")
  return ""



# Iterating over urls
urls = []

while True:
  user_input = input("Enter a URL or N to exist : ")
  if user_input == "N":
    print("URL List Ready!")
    break

  if "://" not in user_input:
    print("Enter a valid URL!")
  else:
    urls.append(user_input)



emails = []
for url in urls:
  data = fetch(url)
  data_list = split_quote(data)
  email_list = find_email(data_list)
  emails.extend(email_list)
  # remove duplicates
  unique = set(emails)
print(unique)

f = open('unique.txt','w')
f.write(str(unique))
f.close()










# to remove common using iteration

# unique_emails = []
# for email in emails:
#   if email not in unique_emails:
#     unique_emails.append(email)

# print(unique_emails)




# x = fetch(urls[0])
# print(x)

# if res.status_code == 200:
#   data_list = split_quote(res.text)
#   email = find_email(data_list)
#   print(email)
# else:
#   print(f"Request failed. Try again {res.status_code}")
