def add_setting(settings,the_tuple):
    key = the_tuple[0].lower()
    value = the_tuple[1].lower()
    if key in list(settings.keys()):
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else :
        settings[f'{key}'] = value 
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'
        
         
def update_setting(settings,the_tuple):
    key = the_tuple[0].lower()
    value= the_tuple[1].lower()
    if key in list(settings.keys()):
        settings[f'{key}'] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(settings,key):
    key = key.lower()
    if key in list(settings.keys()):
        settings.pop(f'{key}',None)
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return "Setting not found!"    

def view_settings(settings):
    if not settings:
        return 'No settings available.' 
    else:
        result = 'Current User Settings:\n'
        for key, value in settings.items():
            result+=f'{key.capitalize()}: {value}\n' 
        return result       


test_settings = {
    'username': 'justin',
    'theme':'dark',
    'phone':795048599
}                    