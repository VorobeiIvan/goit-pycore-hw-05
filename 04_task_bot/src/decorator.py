def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide both name and phone number."  
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide both name and phone number." 
        except TypeError:
            return "Invalid format. Please provide both name and phone number." 
    return inner
