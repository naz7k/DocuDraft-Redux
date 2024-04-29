# DocuDraft
This program allows for easy drafting of Documents in the Open Office XML (.docx) format using pre-defined templates. 

## Requirements
***
* Python >= 3.12
* pip >= 24.0

## Installation
***
Run `python --version` and make sure your Python version is 3.12 or newer.\
Run `pip install -r requirements.txt` in the program directory.

## Usage
***
### Command-Line Interface

Create a folder for your templates within the program directory and place the templates in said folder. The templates should contain keywords slated to be replaced ("wildcards") preceded by a key indicating that they are wildcards (Eg. `<|NAME`). The default directory the program looks in is `./Templates/`

Create a JSON file containing a dictionary for your template settings and define the  setting(s): `"key"`. For example, if the key used for wildcards in your templates is `<|` the JSON file should look as follows:
```commandline
{
    "key": "<|"
}
```
The default location for the template settings is `./Templates/TemplateData.json`

Create a JSON file for the word map. This is where you define the wildcards in the templates which will be replaced and the strings they will be replaced with. The JSON file must contain a dictionary with the wildcards paired to the new words. For example, if your templates use the key `<|` and contain the wildcards `<|NAME` and `<|DATE` the json file may look as follows:
```commandline
{
    "NAME": "John Doe",
    "DATE": "January 1, 2024"
}
```
The default location the program looks in for the word map is `./WordMap.json`. **Do not include the key as part of the wildcards.**


Run `python -m docudraft.docudraft` in the program directory to start the DocuDraft CLI. Make sure that the template and wordmap pointer settings are correct. You may use the command `help` for a list of commands or `help <command>` for usage details on any specific command.


### Graphical User Interface
*Work In Progress*