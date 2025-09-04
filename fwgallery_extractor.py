#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FWGallery MySQL Extractor - Kompletna verzija
=============================================

Skripta za izvlačenje svih slika i meta podataka iz FWGallery ekstenzije 
za Joomla 5 iz MySQL baze.

REQUIREMENTS:
    pip install mysql-connector-python Pillow

Autor: pyz3r
Datum: 2025-08-31
"""

import mysql.connector
import json
import os
from PIL import Image
from datetime import datetime
import sys
# ASCII banner (inserted - will not affect execution)
ASCII_BANNER = """
            ___      _____   _   _     _  _                            
 _ __ ___  / _ \ _ _|___ /  | |_| |__ | || |  _ __                     
| '_ ` _ \| | | | '__||_ \  | __| '_ \| || |_| '_ \                   
| | | | | | |_| | |  ___) | | |_| | | |__   _| | | |                   
|_| |_| |_|\___/|_|_|____/ __\__|_|_|_|_ |_| |_|_|_| _____       _____ 
 _ __ ___ |___ /___ /___  | ___|  | |_| |__ |___ /  |___ / _   _|___ / 
| '_ ` _ \  |_ \ |_ \  / /|___ \  | __| '_ \  |_ \    |_ \| | | | |_ \ 
| | | | | |___) |__) |/ /  ___) | | |_| | | |___) |  ___) | |_| |___) |
|_| |_| |_|____/____//_/  |____/   \__|_| |_|____/  |____/ \__, |____/ 
                                                           |___/       
"""
# =============================================================================
# KONFIGURACIJA
# =============================================================================

# Konfiguracija baze podataka
DB_CONFIG = {
    'host': 'localhost',
    'user': '
    
    'password': '',
    'database': ''
    '',
    'charset': 'utf8mb4',
    'autocommit': True
}

# Osnovna putanja do slika 
BASE_IMAGE_PATH = '/public_html/media/com_fwgallery/'
BASE_URL = 'https://korcula.me/media/com_fwgallery/'

# Prefix za tabele (standardni Joomla)
TABLE_PREFIX = 'josg4_'


# =============================================================================
# FUNKCIJE ZA RAD SA BAZOM
# =============================================================================

def connect_database():
    """Spoji se na MySQL bazu."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print(f"✓ Uspješno spojeno na bazu: {DB_CONFIG['database']}")
        return connection
    except mysql.connector.Error as e:
        print(f"✗ Greška spajanja na bazu: {e}")
        sys.exit(1)

def get_fwgallery_tables(connection):
    """Dobij listu potrebnih FWGallery (FWSG) tabela."""
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE %s", (f"{TABLE_PREFIX}fwsg_%",))
        tables = [table[0] for table in cursor.fetchall()]
        cursor.close()
        
        required = ['fwsg_file', 'fwsg_file_image', 'fwsg_category']
        required_full = [TABLE_PREFIX + r for r in required]
        missing = [r for r in required_full if r not in tables]
        if missing:
            print("✗ Nedostaju FWGallery (FWSG) tablice:", missing)
            print("   Provjeri prefix tabela ili instalaciju FWGallery/FWSG ekstenzije.")
            return []
        
        print(f"✓ Pronađene potrebne FWSG tabele: {required_full}")
        return required_full
    except mysql.connector.Error as e:
        print(f"✗ Greška dohvaćanja tabela: {e}")
        return []

def describe_table_structure(connection, table_name):
    """Opišni strukturu tabele."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        cursor.close()
        return {col[0]: col[1] for col in columns}
    except mysql.connector.Error as e:
        print(f"✗ Greška opisivanja tabele {table_name}: {e}")
        return {}


# =============================================================================
# FUNKCIJE ZA RAD SA FAJLOVIMA
# =============================================================================

def get_image_dimensions_and_size(file_path):
    """
    Dobij dimenzije i veličinu slike iz fajla.
    
    Args:
        file_path (str): Putanja do fajla slike
        
    Returns:
        dict: Rječnik sa width, height, filesize
    """
    result = {'width': None, 'height': None, 'filesize': None}
    
    try:
        if os.path.exists(file_path):
            # Dobij veličinu fajla
            result['filesize'] = os.path.getsize(file_path)
            
            # Dobij dimenzije slike pomoću PIL
            try:
                with Image.open(file_path) as img:
                    result['width'] = img.width
                    result['height'] = img.height
                print(f"    ✓ Čitane dimenzije iz fajla: {result['width']}x{result['height']}")
            except Exception as img_error:
                print(f"    ✗ Greška čitanja slike: {img_error}")
        else:
            print(f"    ⚠️  Fajl ne postoji: {file_path}")
            
    except Exception as e:
        print(f"    ✗ Greška pristupa fajlu {file_path}: {e}")
        
    return result


# =============================================================================
# GLAVNA FUNKCIJA ZA IZVLAČENJE PODATAKA
# =============================================================================

def extract_fwgallery_data(connection):
    """
    Izvuci sve podatke o slikama iz FWGallery (FWSG) baze.

    Returns:
        list: Lista slika sa svim meta podacima
    """
    images_data = []

    try:
        cursor = connection.cursor(dictionary=True)

        # Novi SQL upit prema zadanim poljima i joinovima
        query = f"""
        SELECT
            f.id,
            f.name,
            f.descr,
            f.created,
            f.updated,
            f.category_id,
            c.name AS category_name,
            f.user_id,
            f.alias,
            f.copyright,
            f.downloads,
            f.hits,
            fi.sys_filename,
            fi.filename,
            fi.width,
            fi.height,
            fi.size
        FROM {TABLE_PREFIX}fwsg_file f
        LEFT JOIN {TABLE_PREFIX}fwsg_file_image fi ON f.id = fi.file_id
        LEFT JOIN {TABLE_PREFIX}fwsg_category c ON f.category_id = c.id
        WHERE f.type = 'image'
        """

        print("Izvršavam SQL upit za dohvaćanje slika (FWSG)...")
        cursor.execute(query)
        files = cursor.fetchall()

        if not files:
            print("✗ Nema pronađenih slika u bazi!")
            return []

        print(f"✓ Pronađeno {len(files)} slika u bazi\n")

        for file_data in files:
            print(f"Obrađujem: {file_data.get('name')}")

            image_info = {
                'id': file_data['id'],
                'name': file_data.get('name') or '',
                'description': file_data.get('descr') or '',
                'created': str(file_data['created']) if file_data.get('created') else None,
                'updated': str(file_data['updated']) if file_data.get('updated') else None,
                'category_id': file_data.get('category_id'),
                'category_name': file_data.get('category_name') or '',
                'user_id': file_data.get('user_id'),
                'alias': file_data.get('alias') or '',
                'copyright': file_data.get('copyright') or '',
                'downloads': file_data.get('downloads'),
                'hits': file_data.get('hits'),
                'sys_filename': file_data.get('sys_filename') or '',
                'filename': file_data.get('filename') or '',
                'width': file_data.get('width'),
                'height': file_data.get('height'),
                'size': file_data.get('size')
            }

            # Generiraj putanje i URL
            if file_data.get('sys_filename'):
                image_info['file_path'] = os.path.join(BASE_IMAGE_PATH, file_data['sys_filename'])
                image_info['url'] = BASE_URL + file_data['sys_filename']
            elif file_data.get('filename'):
                image_info['file_path'] = os.path.join(BASE_IMAGE_PATH, file_data['filename'])
                image_info['url'] = BASE_URL + file_data['filename']
            else:
                image_info['file_path'] = ''
                image_info['url'] = ''

            # Ako nema width/height/size, pokušaj iz fajla
            if not (file_data.get('width') and file_data.get('height') and file_data.get('size')):
                file_info = get_image_dimensions_and_size(image_info['file_path'])
                image_info['width'] = image_info['width'] or file_info['width']
                image_info['height'] = image_info['height'] or file_info['height']
                image_info['size'] = image_info['size'] or file_info['filesize']

            images_data.append(image_info)
            print(f"    ✓ Dodano u listu\n")

        cursor.close()

    except mysql.connector.Error as e:
        print(f"✗ Greška SQL upita: {e}")
        return []
    except Exception as e:
        print(f"✗ Neočekivana greška: {e}")
        return []

    return images_data


# =============================================================================
# FUNKCIJE ZA EXPORT
# =============================================================================

def save_gallery_data(images_data, output_file="fwgallery_export.json"):
    """Spremi gallery podatke u JSON fajl."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(images_data, f, ensure_ascii=False, indent=2, default=str)
        print(f"✓ JSON fajl uspješno kreiran: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Greška spremanja JSON fajla: {e}")
        return False

def print_summary(images_data):
    """Prikaži sažetak rezultata."""
    print(f"\n{'='*50}")
    print(f"SAŽETAK IZVLAČENJA")
    print(f"{'='*50}")
    
    print(f"Ukupno slika: {len(images_data)}")
    
    published_count = sum(1 for img in images_data if img.get('published'))
    print(f"Objavljenih slika: {published_count}")
    
    # Kategorije
    categories = set()
    for img in images_data:
        if 'category' in img:
            categories.add(img['category']['title'])
    print(f"Različitih kategorija: {len(categories)}")
    
    # Tagovi
    all_tags = []
    for img in images_data:
        if 'tags' in img:
            all_tags.extend(img['tags'])
    print(f"Različitih tagova: {len(set(all_tags))}")
    
    # Veličine fajlova
    total_size = sum(img.get('filesize', 0) for img in images_data if img.get('filesize'))
    print(f"Ukupna veličina slika: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)")
    
    # Dimenzije
    valid_dimensions = [img for img in images_data if img.get('width') and img.get('height')]
    print(f"Slika sa poznatim dimenzijama: {len(valid_dimensions)}")


# =============================================================================
# GLAVNA FUNKCIJA
# =============================================================================

def main():
    """Glavna funkcija skripte."""
    print("=" * 60)
    print("FWGallery MySQL Extractor")
    print("=" * 60)
    print()
    
    # Spoji se na bazu
    connection = connect_database()
    
    # Provjeri FWGallery tabele
    tables = get_fwgallery_tables(connection)
    if not tables:
        connection.close()
        sys.exit(1)
    
    # Izvuci podatke o slikama
    print("\nPočinjem izvlačenje podataka...\n")
    images_data = extract_fwgallery_data(connection)
    
    # Zatvori konekciju
    connection.close()
    
    if not images_data:
        print("✗ Nema podataka za export!")
        sys.exit(1)
    
    # Spremi JSON
    output_file = f"fwgallery_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    if save_gallery_data(images_data, output_file):
        print_summary(images_data)
        print(f"\n✓ Export završen uspješno!")
        print(f"📁 Fajl: {output_file}")
    else:
        print("✗ Export neuspješan!")
        sys.exit(1)


if __name__ == "__main__":
    main()
