#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for translating Obsidian notes from Russian to German and English
Uses model i82blikeu/gemma-3n-E4B-it-GGUF:Q3_K_M via Ollama
"""

import os
import re
import json
import time
import requests
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import argparse


class ObsidianTranslator:
    # Default paths configuration
    DEFAULT_SOURCE_DIR = "../content/ru"
    DEFAULT_TARGET_DIR = "../content"
    
    def __init__(self, 
                    source_dir: str = None, 
                    target_langs: Optional[List[str]] = None,
                    model_name: str = "i82blikeu/gemma-3n-E4B-it-GGUF:Q3_K_M",
                    ollama_url: str = "http://localhost:11434",
                    skip_existing: bool = True
                ):
        self.source_dir = Path(source_dir or self.DEFAULT_SOURCE_DIR)
        self.target_langs = target_langs if target_langs is not None else ["en", "de"]
        self.model_name = model_name
        self.ollama_url = ollama_url
        self.skip_existing = skip_existing

        # Language codes for prompts
        self.lang_names = {
            "en": "English",
            "de": "German (Deutsch)"
        }
        
        print("🚀 Initializing translator...")
        print(f"📂 Source folder: {self.source_dir}")
        print(f"🌍 Target languages: {self.target_langs}")
        print(f"🤖 Model: {self.model_name}")
        
    def get_md_files(self) -> List[Path]:
        """Get a list of all .md files in the source folder"""
        md_files = list(self.source_dir.rglob("*.md"))
        print(f"📝 Found {len(md_files)} .md files")
        return md_files
    
    def parse_markdown(self, content: str) -> Tuple[Dict, str]:
        """Split frontmatter and main content"""
        frontmatter = {}
        body = content

        # Check for frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    # Simple frontmatter parser (YAML-like)
                    fm_content = parts[1].strip()
                    for line in fm_content.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            frontmatter[key.strip()] = value.strip()
                    body = parts[2].lstrip('\n')
                except Exception:
                    print("⚠️  Error parsing frontmatter, using entire content")
        
        return frontmatter, body
    
    def create_translation_prompt(self, text: str, target_lang: str) -> str:
        """Create a translation prompt"""
        lang_name = self.lang_names.get(target_lang, target_lang)
        
        prompt = f"""Translate the following technical documentation from Russian to {lang_name}.

IMPORTANT RULES:
1. Preserve ALL Markdown formatting (headers #, lists -, code blocks ```, etc.)
2. Keep Obsidian links [[filename]] exactly as they are - DO NOT translate filenames
3. Keep image references ![[image.jpg]] exactly as they are
4. Keep code blocks and code snippets unchanged
5. Keep URLs and technical identifiers unchanged
6. Translate only the text content, not the structure
7. Maintain the technical terminology accuracy
8. If there are programming terms, keep them in English when appropriate

Text to translate:

{text}

Translation to {lang_name}:"""
        
        return prompt
    
    def translate_with_ollama(self, text: str, target_lang: str) -> Optional[str]:
        """Translate text using Ollama"""
        prompt = self.create_translation_prompt(text, target_lang)
        
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.3,  # Низкая температура для точности
                        "top_k": 40,
                        "top_p": 0.9,
                    }
                },
                timeout=300  # 5 минут timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "").strip()
            else:
                print(f"❌ Error Ollama: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error with Ollama: {e}")
            return None
        except Exception as e:
            print(f"❌ General error during translation: {e}")
            return None
    
    def translate_frontmatter_title(self, title: str, target_lang: str) -> str:
        """Translate only the title from frontmatter"""
        if not title or title.strip() == "":
            return title

        # Special cases for technical terms
        special_terms = {
            "AI": {"en": "AI", "de": "KI"},
            "API": {"en": "API", "de": "API"},  
            "HTML": {"en": "HTML", "de": "HTML"},
            "CSS": {"en": "CSS", "de": "CSS"},
            "JavaScript": {"en": "JavaScript", "de": "JavaScript"},
            "Python": {"en": "Python", "de": "Python"},
            "Java": {"en": "Java", "de": "Java"}
        }
        
        if title.strip() in special_terms:
            return special_terms[title.strip()].get(target_lang, title)
            
        # Если заголовок содержит только цифры и технические термины, оставляем как есть
        if re.match(r'^[\d\.\s\w\-]+$', title) and any(char.isdigit() for char in title):
            return title
            
        prompt = f"Translate ONLY this title to {self.lang_names.get(target_lang, target_lang)}. Give ONLY the translated title, no explanations: {title}"
        
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.2,
                        "max_tokens": 50
                    }
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                translated = result.get("response", "").strip()
                # Убираем возможные артефакты
                translated = translated.strip('"\'').strip()
                return translated if translated else title
            else:
                return title
                
        except Exception:
            return title
    
    def get_target_file_path(self, source_file: Path, target_lang: str) -> Path:
        """Get the path to the target file"""
        # Compute the relative path from source_dir
        rel_path = source_file.relative_to(self.source_dir)

        # Create the path for the target language
        target_path = Path(f"{self.DEFAULT_TARGET_DIR}/{target_lang}") / rel_path
        
        return target_path
    
    def translate_file(self, source_file: Path, target_lang: str) -> bool:
        """Translate a single file"""
        target_file = self.get_target_file_path(source_file, target_lang)

        # Check if we need to skip the existing file
        if self.skip_existing and target_file.exists():
            print(f"⏭️  Skipping (already exists): {target_file}")
            return True

        print(f"🔄 Translating: {source_file} -> {target_file}")
        
        try:
            # Read the source file
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                print(f"⚠️  Empty file: {source_file}")
                return False

            # Parse Markdown
            frontmatter, body = self.parse_markdown(content)

            # Translate the main content
            if body.strip():
                print("   📝 Translating content...")
                translated_body = self.translate_with_ollama(body, target_lang)
                
                if not translated_body:
                    print(f"❌ Failed to translate content of file {source_file}")
                    return False
            else:
                translated_body = body

            # Translate the title in frontmatter
            translated_frontmatter = frontmatter.copy()
            if 'title' in frontmatter:
                print(f"   🏷️  Translating title: {frontmatter['title']}")
                translated_frontmatter['title'] = self.translate_frontmatter_title(
                    frontmatter['title'], target_lang
                )

            # Assemble the translated content
            translated_content = ""
            if translated_frontmatter:
                translated_content += "---\n"
                for key, value in translated_frontmatter.items():
                    translated_content += f"{key}: {value}\n"
                translated_content += "---\n"
            
            translated_content += translated_body

            # Create the directory if it doesn't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Save the translated file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            print(f"✅ Successfully translated: {target_file}")
            return True
            
        except Exception as e:
            print(f"❌ Error translating file {source_file}: {e}")
            return False
    
    def translate_all(self):
        """Translate all files"""
        md_files = self.get_md_files()
        
        if not md_files:
            print("❌ No .md files found for translation")
            return
        
        total_files = len(md_files) * len(self.target_langs)
        current_file = 0

        print(f"\n🎯 Starting translation of {len(md_files)} files into {len(self.target_langs)} language(s)")
        print(f"📊 Total translation operations: {total_files}")
        print("="*60)
        
        start_time = time.time()
        success_count = 0
        
        for source_file in md_files:
            print(f"\n📄 Processing: {source_file.relative_to(self.source_dir)}")
            
            for target_lang in self.target_langs:
                current_file += 1
                print(f"[{current_file}/{total_files}] 🌍 Language: {target_lang}")

                if self.translate_file(source_file, target_lang):
                    success_count += 1
                
                # Небольшая пауза между запросами
                time.sleep(1)
        
        elapsed_time = time.time() - start_time
        print("\n" + "="*60)
        print("🎉 Translation completed!")
        print(f"✅ Successful: {success_count}/{total_files}")
        print(f"⏱️  Elapsed time: {elapsed_time:.1f} sec")

        if success_count < total_files:
            print(f"⚠️  Unsuccessful: {total_files - success_count} files")


def main():
    parser = argparse.ArgumentParser(description='Translate Obsidian notes')
    parser.add_argument('--source', default=ObsidianTranslator.DEFAULT_SOURCE_DIR, help=f'Source folder (default: {ObsidianTranslator.DEFAULT_SOURCE_DIR})')
    parser.add_argument('--langs', nargs='+', default=['en', 'de'], help='Target languages (default: en de)')
    parser.add_argument('--model', default='i82blikeu/gemma-3n-E4B-it-GGUF:Q3_K_M', help='Ollama model')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing files')
    parser.add_argument('--test', action='store_true', help='Test mode - translate only the first 3 files')
    args = parser.parse_args()
    
    translator = ObsidianTranslator(
        source_dir=args.source,
        target_langs=args.langs,
        model_name=args.model,
        skip_existing=not args.overwrite
    )
    
    if args.test:
        print("🧪 Test mode - translating only the first 3 files")
        md_files = translator.get_md_files()[:3]
        translator.get_md_files = lambda: md_files
    
    translator.translate_all()


if __name__ == "__main__":
    main()