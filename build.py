#!/usr/bin/env python3
"""
Build script for Icon Gallery
Generates categories.json from the icons folder structure
"""

import os
import json
from pathlib import Path

def get_icon_categories():
    """Scan the icons directory and generate category data"""
    icons_dir = Path('icons')
    categories = {}
    
    # Icon mapping for category icons
    category_icons = {
        'cloud': 'bi-cloud-fill',
        'databases': 'bi-database-fill',
        'frameworks': 'bi-layers-fill',
        'ides': 'bi-code-square',
        'programming_languages': 'bi-braces',
        'text_editor': 'bi-pencil-square',
        'social_icons': 'bi-share-fill',
        'storage': 'bi-hdd-fill',
        'os': 'bi-laptop-fill',
        'utils': 'bi-tools',
        'others': 'bi-grid-3x3-gap-fill'
    }
    
    if not icons_dir.exists():
        print("Warning: icons directory not found!")
        return categories
    
    # Get all subdirectories
    for category_path in sorted(icons_dir.iterdir()):
        if category_path.is_dir() and not category_path.name.startswith('.'):
            category_name = category_path.name
            
            # Format display name
            display_name = category_name.replace('_', ' ').title()
            
            # Count icon files
            icon_files = []
            valid_extensions = {'.svg', '.png', '.jpg', '.jpeg', '.gif', '.webp'}
            
            for file_path in category_path.iterdir():
                if file_path.is_file() and file_path.suffix.lower() in valid_extensions:
                    icon_files.append(file_path.name)
            
            # Sort files alphabetically
            icon_files.sort(key=str.lower)
            
            categories[category_name] = {
                'name': display_name,
                'icon': category_icons.get(category_name, 'bi-folder-fill'),
                'count': len(icon_files),
                'files': icon_files
            }
            
            print(f"✓ Found category: {display_name} ({len(icon_files)} icons)")
    
    return categories

def main():
    """Main build function"""
    print("🔨 Building Icon Gallery...")
    print("=" * 50)
    
    # Generate categories data
    categories = get_icon_categories()
    
    if not categories:
        print("❌ Error: No categories found!")
        return 1
    
    # Save to JSON file
    output_file = Path('categories.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(categories, f, indent=2, ensure_ascii=False)
    
    print("=" * 50)
    print(f"✅ Build complete!")
    print(f"📊 Total categories: {len(categories)}")
    print(f"📦 Total icons: {sum(cat['count'] for cat in categories.values())}")
    print(f"💾 Output file: {output_file}")
    
    return 0

if __name__ == '__main__':
    exit(main())
