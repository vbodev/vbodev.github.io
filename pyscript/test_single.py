#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick test for translating a single file
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from translate_notes import ObsidianTranslator
from pathlib import Path

# Create translator
translator = ObsidianTranslator()

# Test on a specific file
test_file = Path("content/ru/Development Languages/1. Java/05. Spring Boot.md")

if test_file.exists():
    print(f"🔄 Testing translation of file: {test_file}")

    # Translate to English
    print("🇺🇸 Translating to English...")
    result_en = translator.translate_file(test_file, "en")
    print(f"✅ Result EN: {result_en}")

    # Translate to German
    print("🇩🇪 Translating to German...")
    result_de = translator.translate_file(test_file, "de")
    print(f"✅ Result DE: {result_de}")

    print("🎉 Test completed!")
else:
    print(f"❌ File not found: {test_file}")