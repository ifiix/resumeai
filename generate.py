import requests
import json

def generate_resume(name, email, phone, skills):
  url = "https://api.resume.ai/generate"
  data = {
    "name": name,
    "email": email,
    "phone": phone,
    "skills": skills
  }
  response = requests.post(url, data=data)
  if response.status_code == 200:
    resume = response.json()
    return resume
  else:
    raise Exception("Failed to generate resume")

if __name__ == "__main__":
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  phone = input("Enter your phone number: ")
  skills = input("Enter your skills: ")
  resume = generate_resume(name, email, phone, skills)
  print(resume)
