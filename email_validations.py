
from email_validator import validate_email, EmailNotValidError 

email = "my+address@mydomain.acs"

def validate_email_address(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(f"Email address {email} is not valid: {e}")
        return False
      
try:
  # Validate.
  valid = validate_email(email)
  
  

  # Update with the normalized form.
  email = valid.email
except EmailNotValidError as e:
  # email is not valid, exception message is human-readable
  print(str(e))
    