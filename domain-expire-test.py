import whois
from datetime import datetime

def lambda_handler(event, context):
    domain_name = event['google.com']
    
    # Get domain information
    domain = whois.whois(domain_name)
    
    # Check if domain expiration date is available
    if domain.expiration_date:
        # Get the first expiration date from the list (in case of multiple dates)
        expiration_date = domain.expiration_date[0]
        
        # Get the current date
        current_date = datetime.now()
        
        # Calculate the remaining days until expiration
        remaining_days = (expiration_date - current_date).days
        
        # Prepare the response
        response = {
            'domain': domain_name,
            'expiration_date': expiration_date.strftime('%Y-%m-%d'),
            'remaining_days': remaining_days
        }
    else:
        # Domain expiration date not found
        response = {
            'domain': domain_name,
            'expiration_date': 'N/A',
            'remaining_days': 'N/A'
        }
    
    return response
