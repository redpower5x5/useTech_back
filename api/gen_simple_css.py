import re as re
import os
import zipfile

class GenCSSProject:
    def __init__(self, raw_data):
        self.parsed_images = {}
        self.raw_data = self.parse_images(raw_data)
        self.css_project_path = './starter_project'
        self.destination_path = './compiled'
        self.name_of_component = self.raw_data.split(':')[0].split('export const ')[1]
        self.code_of_component = self.raw_data.split('return (\n')[1].split(')')[0]
        self.css_code = '* {\n  font-family: Arial, sans-serif !important;\n}\n' + self.raw_data.split('}\n\n')[1]

    def parse_images(self, data) -> str:
        """extract base64 images from components code, save them in dict and replace in code with placeholders"""
        # find all images in code
        images = re.findall(r'src="(.*?)"', data)
        # replace images with placeholders with corresponding number
        for i, image in enumerate(images):
            data = data.replace(image, f'__IMG_{i}__')
            # save images in dict
            self.parsed_images[f'__IMG_{i}__'] = image
        return data

    def insert_images(self, data) -> str:
        """insert images into code"""
        for placeholder, image in self.parsed_images.items():
            data = data.replace(placeholder, image)
        return data

    def insert_data_into_files(self):
        """Insert data into files"""
        # create copy of starter project in compiled folder
        os.system(f'cp -r {self.css_project_path} {self.destination_path}')
        # insert code of component into App.js
        with open(f'{self.destination_path}/starter_project/src/App.tsx', 'r', encoding='utf-8') as file:
            data = file.read()
        data = data.replace('_BASE_CSS', self.name_of_component)
        with open(f'{self.destination_path}/starter_project/src/App.tsx', 'w', encoding='utf-8') as file:
            file.write(data)
        # insert code and rename component file
        os.rename(f'{self.destination_path}/starter_project/src/components/_BASE_CSS.tsx', f'{self.destination_path}/starter_project/src/components/{self.name_of_component}.tsx')
        with open(f'{self.destination_path}/starter_project/src/components/{self.name_of_component}.tsx', 'r', encoding='utf-8') as file:
            data = file.read()
        # replace name of component
        data = data.replace('_BASE_CSS', self.name_of_component)
        # insert code of component
        data = data.replace('/* ELEMENT */', self.insert_images(self.code_of_component))
        with open(f'{self.destination_path}/starter_project/src/components/{self.name_of_component}.tsx', 'w', encoding='utf-8') as file:
            file.write(data)
        # insert css code
        with open(f'{self.destination_path}/starter_project/src/index.css', 'w', encoding='utf-8') as file:
            file.write(self.css_code)

    def zip_project(self, name) -> str:
        """ Zips generated project with given name and returns path to zip """
        zip_path = f'{self.destination_path}/{name}.zip'
        zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(f'{self.destination_path}/starter_project'):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), f'{self.destination_path}/starter_project'))
        zipf.close()
        # remove generated project
        os.system(f'rm -rf {self.destination_path}/starter_project')
        return zip_path

