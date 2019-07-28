string = '900 km'

def handle_dash_in_text(text = ''):
    filtered_text = text.split(' ')[0]
    if filtered_text == '-':
        return '0'
    if filtered_text.find('.') != -1:
        return int(filtered_text.replace('.', ''))
    else:
        return int(filtered_text)

print(handle_dash_in_text(string))