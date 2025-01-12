from requirements.models import Requirement


def create_requirement_model(item):

    requirements_data = {"name": "", "id": "", "description": "", "last-modified": "", "additional_data": {}}
    for child in item.find('Fields'):
        if child.attrib['Name'] in requirements_data.keys():
            requirements_data[child.attrib['Name']] = child.find('Value').text if child.find('Value') is not None else None
        else:
            if child.find('Value') is not None and child.find('Value').text is not None:
                requirements_data['additional_data'][child.get('Name')] = child.find('Value').text

    requirements_data['external_id'] = requirements_data.pop('id')
    requirements_data['external_updated_at'] = requirements_data.pop('last-modified')

    requirement_obj=None
    try:
        requirement_obj = Requirement.objects.get(name=requirements_data['name'])
    except Requirement.DoesNotExist:
        requirement_obj = Requirement(id=None, **requirements_data)
        requirement_obj.save(force_insert=True)
    else:
        if requirements_data['external_updated_at'] != requirement_obj.external_updated_at.replace(second=0, microsecond=0):
            for key, val in requirements_data.items():
                if val not in (None, "", []):
                    requirement_obj.save(force_update=True)
    finally:
        return requirement_obj