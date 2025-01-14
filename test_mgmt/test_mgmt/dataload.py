import os
from pathlib import Path

import yaml
from django.contrib.auth.models import Group, User
from django.db import IntegrityError

from api.models import model_name_map as api_model_name_map

from siteconfig.models import model_name_map as siteconfig_model_name_map
from people.models import model_name_map as people_model_name_map

from program.models import model_name_map as program_model_name_map
from workitems.models import model_name_map as workitems_model_name_map

from requirements.models import model_name_map as requirements_model_name_map
from testdesign.models import model_name_map as testdesign_model_name_map
from automation.models import model_name_map as automation_model_name_map
from execution.models import model_name_map as execution_model_name_map

from api.serializers import serializer_map as api_serializer_map
from siteconfig.serializers import serializer_map as siteconfig_serializer_map
from people.serializers import serializer_map as people_serializer_map

from program.serializers import serializer_map as program_serializer_map
from workitems.serializers import serializer_map as workitems_serializer_map

from requirements.serializers import serializer_map as requirements_serializer_map
from testdesign.serializers import serializer_map as testdesign_serializer_map
from automation.serializers import serializer_map as automation_serializer_map
from execution.serializers import serializer_map as execution_serializer_map

model_name_map = {
    'auth': {'Group': Group, 'User': User},
    'api': api_model_name_map,

    'siteconfig': siteconfig_model_name_map,
    'people': people_model_name_map,

    'program': program_model_name_map,
    'workitems': workitems_model_name_map,
    # 'scheduler': scheduler_model_name_map,

    'requirements': requirements_model_name_map,
    'testdesign': testdesign_model_name_map,
    'automation': automation_model_name_map,
    'execution': execution_model_name_map,
}

serializer_map = {}
serializer_map.update(api_serializer_map)
serializer_map.update(siteconfig_serializer_map)
serializer_map.update(people_serializer_map)
serializer_map.update(program_serializer_map)
serializer_map.update(workitems_serializer_map)
serializer_map.update(requirements_serializer_map)
serializer_map.update(testdesign_serializer_map)
serializer_map.update(automation_serializer_map)
serializer_map.update(execution_serializer_map)


def save_data_to_folder(data_folder: str):
    os.makedirs(data_folder, exist_ok=True)
    for app_to_save in model_name_map.keys():
        print("Going to write " + app_to_save)
        for model_to_save in model_name_map[app_to_save].keys():
            print("Going to write " + model_to_save)
            model_class = model_name_map[app_to_save][model_to_save]
            model_records = model_class.objects.all()
            os.makedirs(Path(data_folder, app_to_save), exist_ok=True)
            # for model_record in model_records:
            file_path = Path(data_folder, app_to_save, model_to_save + ".yaml")
            serializer_cls = serializer_map[model_class]
            if len(model_records) > 0:
                with open(str(file_path), 'w', ) as yaml_file:
                    yaml.dump_all(serializer_cls(model_records, many=True).data, yaml_file, sort_keys=False)


def load_data_from_folder(data_folder: str):
    if os.path.exists(data_folder):
        for app_to_save in model_name_map.keys():
            print("Going to load " + app_to_save)
            if os.path.exists(Path(data_folder, app_to_save)):
                for model_to_save in model_name_map[app_to_save].keys():
                    print("Going to load " + model_to_save)
                    model_class = model_name_map[app_to_save][model_to_save]
                    file_path = Path(data_folder, app_to_save, model_to_save + ".yaml")
                    if os.path.exists(file_path):
                        with open(str(file_path), 'r', ) as yaml_file:
                            model_records_data = yaml.safe_load_all(yaml_file)
                            for model_record_data in model_records_data:
                                m2m_fkeys = {}
                                foreign_keys = {}
                                for key in model_record_data.keys():
                                    field_cls = model_class.__dict__[key].__class__
                                    if 'ToMany' in field_cls.__name__:  # 'related_descriptors' in field_cls.__module__:
                                        m2m_fkeys[key] = model_record_data[key]
                                    if model_record_data[key] and (
                                            'ForwardOneToOne' in field_cls.__name__ or 'ForwardManyToOne' in field_cls.__name__):
                                        model_record_data[key] = model_class.__dict__[
                                            key].field.related_model.objects.get(id=model_record_data[key]['id'])

                                # for foreign_key in foreign_keys.keys():
                                #     del model_record_data[foreign_key]

                                for to_many_key in m2m_fkeys.keys():
                                    del model_record_data[to_many_key]

                                try:
                                    model_record = model_class.objects.create(**model_record_data)
                                    # TODO: Verify keys working well.
                                    print("Created " + str(model_record))
                                except IntegrityError as e:
                                    model_record = model_class.objects.get(id=model_record_data['id'])
                                    print("Ignoring existing data " + str(model_records_data) + str(e))

                                for to_many_key, value in m2m_fkeys.items():
                                    model_record.__getattribute__(to_many_key).set([int(item['id']) for item in value])
