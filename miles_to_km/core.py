import logging

def set_up_logging():
    # Set up Logging
    # Create a named logger
    logger = logging.getLogger('__miles_to_km__')
    logger.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Set the formatter for the console handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                                datefmt='%m/%d/%Y %I:%M:%S%p')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    return logger

logger = set_up_logging()

def miles_to_km(miles: float) -> float:
    """
    Converts miles to kilometers
    
    Args:
        miles (float): Miles to convert to kilometers
    
    Returns:
        float: Kilometers
        
        Raises:
            TypeError: If input is not a float or int        
    """
    if isinstance(miles, float) or isinstance(miles, int) or isinstance(miles, str):
        km = miles * 1.60934
        logger.info(f'{miles} miles is {km} km')
        return round(km, 2)
    else:
        logger.error(f'Input must be a float, int or str. Input was {type(miles)}')
        raise TypeError(f'Input must be a float or int. Input was {type(miles)}')


def km_to_miles(km: float) -> float:
    """
    Converts kilometers to miles
    
    Args:
        km (float): Kilometers to convert to miles
        
    Returns:
        float: Miles
        
    Raises:
        TypeError: If input is not a float or int
    """
    if isinstance(km, float) or isinstance(km, int) or isinstance(km, str):
        miles = km / 1.60934
        logger.info(f'{km} km is {miles} miles')
        return round(miles, 2)
    else:
        logger.error(f'Input must be a float, int or str. Input was {type(km)}')
        raise TypeError(f'Input must be a float or int. Input was {type(km)}')
