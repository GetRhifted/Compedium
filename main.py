import csv
import os

CHARACTER_TABLE = '.characters.csv'
CHARACTER_SCHEMA = ['nombre', 'region', 'vision', 'ATK', 'DEF', 'HP', 'CRIT DMG', 'CRIT RATE', 'ELEM MAST', 'ENERG RECHAR']
characters = []

def _initialize_data():
    with open(CHARACTER_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CHARACTER_SCHEMA)

        for row in reader:
            characters.append(row)

def _save_data():
    tmp_table_name = f"{CHARACTER_TABLE}.tmp"
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CHARACTER_SCHEMA)
        writer.writerows(characters)

        os.remove(CHARACTER_TABLE)
        os.rename(tmp_table_name, CHARACTER_TABLE)

def _get_attributes(attribute_name):
    attribute = None

    while not attribute:
        attribute = input(f'Introduce la informacion de {attribute_name} del personaje: ')
    
    return attribute

def _get_attributes_from_input():
    character = {
        'nombre': _get_attributes('nombre'),
        'region': _get_attributes('region'),
        'vision': _get_attributes('vision'),
        'ATK': _get_attributes('ATK'),
        'DEF': _get_attributes('DEF'),
        'HP': _get_attributes('HP'),
        'CRIT DMG': _get_attributes('CRIT DMG'),
        'CRIT RATE': _get_attributes('CRIT RATE'),
        'ELEM MAST': _get_attributes('ELEM MAST'),
        'ENERG RECHAR': _get_attributes('ENERG RECHAR')
    }

    return character

def _character_not_registed(character):
    print(f"No hay un personaje asignado al id {character}")
    print("¿Deseas registrarlo? S/N")

    answer_input = input()
    answer_input = answer_input.upper()

    if answer_input == 'S':
        character = {
            'nombre': _get_attributes('nombre'),
            'region': _get_attributes('region'),
            'vision': _get_attributes('vision'),
            'ATK': _get_attributes('ATK'),
            'DEF': _get_attributes('DEF'),
            'HP': _get_attributes('HP'),
            'CRIT DMG': _get_attributes('CRIT DMG'),
            'CRIT RATE': _get_attributes('CRIT RATE'),
            'ELEM MAST': _get_attributes('ELEM MAST'),
            'ENERG RECHAR': _get_attributes('ENERG RECHAR')
        }
        new_character(character)

    elif answer_input == 'N':
        print("Personaje no registrado")
    
    else:
        pass
        

def list_characters():
    for id, character in enumerate(characters):
        print(f"{id} | {character['nombre']} | {character['region']} | {character['vision']} | {character['ATK']} | {character['DEF']} | {character['HP']} | {character['CRIT DMG']} | {character['CRIT RATE']} | {character['ELEM MAST']} | {character['ENERG RECHAR']}")


def new_character(character):
    global characters

    if character not in characters:
        characters.append(character)
        print(f"El personaje {character['nombre']} ha sido registrado con exito!")
    else:
        print(f"El personaje {character['nombre']} ya se encuentra registrado")

def delete_character(character_uid):
    global characters

    if len(characters) - 1 >= character_uid:
        deleted_character = characters.pop(character_uid)
        print(f"El personaje {deleted_character['nombre']} ha sido eliminado")
    else:
        print("El id indicado no existe en el registro de personajes")

def update_character(character_uid, updated_character):
    global characters

    if len(characters) - 1 >= character_uid:
        characters[character_uid] = updated_character
        print("El personaje se ha actualizado")
    else:
        _character_not_registed(character_uid)

def _print_info():
    print('Bienvenido a Compedium')
    print('+' * 50)
    print('¿Que quieres hacer ahora?')
    print('[L]istar Personajes')
    print('[R]egistrar Personaje')
    print('[A]ctualizar Personaje')
    print('[E]liminar Personaje')
    print('[S]alir de Compedium')


if __name__ == '__main__':
    _initialize_data()
    
    while True:
        _print_info()

        command = input()
        command = command.upper()

        if command == 'L':
            list_characters()

        elif command == 'R':
            character = _get_attributes_from_input()
            new_character(character)
        
        elif command == 'A':
            character_uid = int(_get_attributes('id'))
            if len(characters) - 1 >= character_uid:
                updated_character = _get_attributes_from_input()
                update_character(character_uid, updated_character)
            else:
                _character_not_registed(character_uid)
 
        elif command == 'E':
            character_uid = int(_get_attributes('id'))
            delete_character(character_uid)

        elif command == 'S':
            print('Gracias por usar Compedium, regresa pronto')
            break

        else:
            print('Comando invalido')        
        
        _save_data()
            

