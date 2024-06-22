import requests


create_user_url = 'https://login.auth0.com/api/v2/users'
create_user_data = {
     'connection': 'email',
      'email': 'user@example.com',
      'phone_number': 'string',
      'email_verified': false,
      'phone_verified': false,
}
      'user_metadata': {
  "given_name": "string",
  "family_name": "string",
  "name": "string",
  "nickname": "string",
  "picture": "string",
  "user_id": "string",
  "connection": "string",
  "password": "string",
  "verify_email": false,
  "username": "string"
}


create_user_response = requests.post('https://login.auth0.com/api/v2/users',json=create_user_data)
print(create_user_response.json())
