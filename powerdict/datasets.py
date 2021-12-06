# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/07-dataset-pages.ipynb (unless otherwise specified).

__all__ = ['resource_to_title', 'resource_to_description', 'package_to_homepage', 'resource_to_fields_table_str',
           'extract_resource_elements', 'extract_package_elements', 'resource_to_download_url',
           'identify_datapackage_datasets', 'update_mkdocs_config', 'populate_dataset_pages',
           'move_attribute_source_data_to_docs']

# Cell
import json
import yaml
import numpy as np
import pandas as pd

from frictionless import Package

import os
import shutil
from tqdm import tqdm
from pathlib import Path
from jinja2 import Template

from powerdict import dictionary, openapi

# Cell
resource_to_download_url = lambda resource, package_name, root_path='https://osuked.github.io/Power-Station-Dictionary/attribute_sources': f'{root_path}/{package_name}/{resource["path"]}'

def resource_to_title(resource):
    if 'title' in resource.keys():
        title = resource['title']
    else:
        title = resource['name']

    return title

def resource_to_description(resource):
    if 'description' in resource.keys():
        description = resource['description']
    else:
        description = False

    return description

def package_to_homepage(package):
    if 'homepage' in package.keys():
        homepage = package['homepage']
    else:
        homepage = False

    return homepage

def resource_to_fields_table_str(resource):
    df_fields = pd.DataFrame(resource['schema']['fields'])

    df_fields = df_fields.rename(columns={'name': 'column'}).replace(np.nan, '-')
    df_fields.columns = df_fields.columns.str.capitalize()

    md_str = df_fields.to_markdown(index=False)

    return md_str

def extract_resource_elements(package):
    resource_elements = [
        {
            'title': resource_to_title(resource),
            'download_url': resource_to_download_url(resource, package['name']),
            'description': resource_to_description(resource),
            'fields': resource_to_fields_table_str(resource)
        }
        for resource
        in package.resources
    ]

    return resource_elements

def extract_package_elements(package):
    package_elements = {
        'title': resource_to_title(package),
        'homepage': package_to_homepage(package),
        'description': resource_to_description(package),
        'metadata': dictionary.construct_metadata_table_str(package),
        'resource_elements': extract_resource_elements(package)
    }

    return package_elements

# Cell
def identify_datapackage_datasets(datasets_dir):
    dataset_dirs = [
        elem
        for elem
        in os.listdir(datasets_dir)
        if elem != '.ipynb_checkpoints'
    ]

    datapackage_datasets = [
        dataset_dir
        for dataset_dir
        in dataset_dirs
        if 'datapackage.json' in os.listdir(f'{datasets_dir}/{dataset_dir}')
    ]

    return datapackage_datasets

# Cell
def update_mkdocs_config(
    valid_datasets: list,
    dataset_to_name: dict,
    mkdocs_config_fp: str
):
    with open(mkdocs_config_fp) as fp:
         mkdocs_config = yaml.safe_load(fp)

    nav_datasets_idx = [idx for idx, nav_item in enumerate(mkdocs_config['nav']) if 'Datasets' in nav_item.keys()][0]
    mkdocs_config['nav'][nav_datasets_idx]['Datasets'] = {f'{dataset_to_name[dataset]}': f'datasets/{dataset}.md' for dataset in valid_datasets}

    with open(mkdocs_config_fp, 'w') as fp:
        yaml.dump(mkdocs_config, fp)

    return

def populate_dataset_pages(
    datasets_dir: str='data/attribute_sources',
    dataset_template_fp: str='templates/dataset_page.md',
    mkdocs_config_fp: str='mkdocs.yml',
    dataset_docs_dir: str='docs/datasets'
):
    dataset_to_name = {}
    valid_datasets = identify_datapackage_datasets(datasets_dir)

    for dataset in tqdm(valid_datasets):
        datapackage_json_fp = f'{datasets_dir}/{dataset}/datapackage.json'
        package = Package(datapackage_json_fp, profile='tabular-data-package')

        package_elements = extract_package_elements(package)
        dataset_to_name[dataset] = package_elements['title'].strip()
        save_fp = f'{dataset_docs_dir}/{package["name"]}.md'
        dictionary.populate_and_save_template(dataset_template_fp, save_fp, package_elements=package_elements)

    update_mkdocs_config(valid_datasets, dataset_to_name, mkdocs_config_fp)

    return

# Cell
def move_attribute_source_data_to_docs(
    src_path: str='data/attribute_sources/',
    trg_path: str='docs/attribute_sources/'
):
    if not os.path.exists(trg_path):
        os.mkdir(trg_path)

    shutil.rmtree(trg_path)
    shutil.copytree(src_path, trg_path)

    return