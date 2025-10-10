#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script to check translation progress
"""

from pathlib import Path
import json

def check_translation_progress():
    """Check translation progress"""
    
    source_dir = Path("content/ru")
    target_langs = ["en", "de"]

    # Count source files
    source_files = list(source_dir.rglob("*.md"))
    total_source = len(source_files)

    print(f"📊 Translation Statistics")
    print(f"{'='*50}")
    print(f"📝 Source files (ru): {total_source}")

    for lang in target_langs:
        target_dir = Path(f"content/{lang}")
        if target_dir.exists():
            translated_files = list(target_dir.rglob("*.md"))
            translated_count = len(translated_files)
            progress = (translated_count / total_source) * 100 if total_source > 0 else 0
            
            print(f"🌍 {lang.upper()}: {translated_count}/{total_source} ({progress:.1f}%)")

            # Show latest translated files
            if translated_files:
                print(f"   📄 Latest files:")
                for f in sorted(translated_files, key=lambda x: x.stat().st_mtime, reverse=True)[:3]:
                    rel_path = f.relative_to(target_dir)
                    mtime = f.stat().st_mtime
                    print(f"      - {rel_path}")
        else:
            print(f"🌍 {lang.upper()}: folder not found")
    
    print(f"{'='*50}")

def list_recent_files():
    """Show recently created files"""
    import time

    print(f"\n🕒 Recently created files (last 10 minutes):")

    for lang in ["en", "de"]:
        target_dir = Path(f"content/{lang}")
        if target_dir.exists():
            current_time = time.time()
            recent_files = []
            
            for f in target_dir.rglob("*.md"):
                if current_time - f.stat().st_mtime < 600:  # 10 минут
                    recent_files.append(f)
            
            if recent_files:
                print(f"\n🌍 {lang.upper()}:")
                for f in sorted(recent_files, key=lambda x: x.stat().st_mtime, reverse=True):
                    rel_path = f.relative_to(target_dir)
                    mtime = time.strftime('%H:%M:%S', time.localtime(f.stat().st_mtime))
                    print(f"   {mtime} - {rel_path}")

if __name__ == "__main__":
    check_translation_progress()
    list_recent_files()