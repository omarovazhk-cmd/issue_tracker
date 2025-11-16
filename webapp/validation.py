def validate(data):
    errors = {}
    summary = (data.get('summary') or '').strip()
    if summary == '':
        errors['summary'] = 'Данное поле обязательное'
    elif len(summary) < 3:
        errors['summary'] = 'Название задачи должно быть длиннее 3 символов'

    if not data.get('status'):
        errors['status'] = 'Данное поле обязательное'

    description = (data.get('description') or '').strip()
    if description == '':
        errors['description'] = 'Данное поле обязательное'

    return errors
