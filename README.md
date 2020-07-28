# Install

Install the `cakemail` package using `pip`

```shell script
pip install cakemail
```

# Usage

Create an object from the `CakemailApi` class with your Cakemail username and password.  The object will take care of
all authorization mechanisms automatically.

```python
import cakemail

api = cakemail.Api(username='your@email.com', password='somepassword')
```

Call one of the API operations (refer to the online documentation)

```python
my_account = api.account.get_self_account()
```

# API operations

API operations accept the OpenAPI models as well as python dictionaries.

```python
sender = api.sender.create_sender(
    create_sender=cakemail.models.CreateSender(
        name='My Sender',
        email='someone@gmail.com'
    )
)
sender = api.sender.create_sender(
    create_sender={
        'name': 'My Sender',
        'email': 'someone@gmail.com'    
    }
)
```

You can also unpack a dictionary for all Operation arguments, allowing you to express the entire payload as a single
dictionary :

```python
sender = api.sender.create_sender(
    **{
        'create_sender': {
            'name': 'My Sender',
            'email': 'someone@gmail.com'        
        }   
    }
)
```

# Operation Examples

## Create a Sender
```python
sender = api.sender.create_sender(
    cakemail.models.CreateSender(name='My Sender', email='someone@gmail.com')
)

# look for the confirmation ID in your email inbox
api.sender.confirm_sender(
    cakemail.models.ConfirmSender(confirmation_id='[confirmation ID]')
)
```

## Create a Contact List

```python
my_new_list = api.list.create_list(
    list=cakemail.models.List(
        name='my new list',
        default_sender=cakemail.models.Sender(id=sender.id)
    )
)
```

## Send a transactional email

```python
# expressed as OpenAPI models
api.transactional_email.send_email(
    email=cakemail.models.Email(
        email='destination@gmail.com',
        sender=sender,
        content=cakemail.models.EmailContent(
            subject='Subject line',
            text='Email body',
            encoding='utf-8'
        )
    )
)

# expressed as a dictionary
api.transactional_email.send_email(
    email={
        'email': 'destination@gmail.com',
        'sender': sender,
        'content': {
            'subject': 'Subject line',
            'text': 'Email body',
            'encoding': 'utf-8' 
        }
    }
)
```
