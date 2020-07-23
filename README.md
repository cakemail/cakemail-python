# Install

Install the `cakemail` package using `pip`

```shell script
pip install cakemail
```

# Usage

Simply create an object from the `cakemail.Api` class and call one of the API operations (refer to the online documentation)

```python
import cakemail

api = cakemail.Api(username='your@email.com', password='somepassword')

my_account = api.account.get_self_account()
print(my_account)
```

# Examples

## Create a Contact List

```python
import cakemail

api = cakemail.Api(username='email@internet.com', password='password')

my_new_list = api.list.create_list(
    list=api.models.List(name='my new list')
)
print(my_new_list)
```
