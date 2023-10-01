import re
import os
import zipfile

class GenStyledProject:
    def __init__(self, raw_data):
        self.parsed_images = {}
        self.raw_data = self.parse_images(raw_data)
        self.styled_project_path = './starter_styled'
        self.destination_path = './compiled'
        self.name_of_component = self.raw_data.split(':')[0].split('export const ')[1]
        self.code_of_component = self.raw_data.split('return (\n')[1].split(')')[0]
        self.style_code = self.raw_data.split('"styled-components"\n\n')[1]

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
        os.system(f'cp -r {self.styled_project_path} {self.destination_path}')
        # insert code of component into App.tsx
        with open(f'{self.destination_path}/starter_styled/src/App.tsx', 'r', encoding='utf-8') as file:
            data = file.read()
        data = data.replace('_BASE_STYLE', self.name_of_component)
        with open(f'{self.destination_path}/starter_styled/src/App.tsx', 'w', encoding='utf-8') as file:
            file.write(data)
        # insert code and rename component file
        os.rename(f'{self.destination_path}/starter_styled/src/components/_BASE_STYLE.tsx', f'{self.destination_path}/starter_styled/src/components/{self.name_of_component}.tsx')
        with open(f'{self.destination_path}/starter_styled/src/components/{self.name_of_component}.tsx', 'r', encoding='utf-8') as file:
            data = file.read()
        # replace name of component
        data = data.replace('_BASE_STYLE', self.name_of_component)
        # insert code of component
        data = data.replace('/* ELEMENT */', self.insert_images(self.code_of_component))
        with open(f'{self.destination_path}/starter_styled/src/components/{self.name_of_component}.tsx', 'w', encoding='utf-8') as file:
            file.write(data)
        # read styles file
        with open(f'{self.destination_path}/starter_styled/src/styles.ts', 'r', encoding='utf-8') as file:
            data = file.read()
        # insert styles
        data = data.replace('/* STYLES */', self.style_code)
        with open(f'{self.destination_path}/starter_styled/src/styles.ts', 'w', encoding='utf-8') as file:
            file.write(data)

    def zip_project(self, name) -> str:
        """ Zips generated project with given name and returns path to zip """
        zip_path = f'{self.destination_path}/{name}.zip'
        zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(f'{self.destination_path}/starter_styled'):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), f'{self.destination_path}/starter_styled'))
        zipf.close()
        # remove generated project
        os.system(f'rm -rf {self.destination_path}/starter_styled')
        return zip_path
