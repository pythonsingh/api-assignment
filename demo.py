import jwt


payload_data = {
            'name':'singh',
            'age':'21',
            'sub':'python'
}

my_secret = 'my_super_secret'
token = jwt.encode(
    payload=payload_data,
    key=my_secret
)
 
print(token)