#!/usr/bin/env python3
"""
MiniMax Image Generation Script
Usage: python minimax-image.py "your prompt" [-n 1] [-a 16:9] [-o output.png] [--expand/--no-expand]
"""

import argparse
import base64
import json
import os
import sys
import requests

API_KEY = os.environ.get("MINIMAX_API_KEY")
BASE_URL = "https://api.minimaxi.com"
MINIMAX_OUTPUT_DIR = "/root/.openclaw/workspace/minimax-images-t2i"

# Ensure output directory exists
os.makedirs(MINIMAX_OUTPUT_DIR, exist_ok=True)

def expand_prompt(prompt):
    """Expand short prompt into detailed image generation prompt using MiniMax API"""
    
    if not API_KEY:
        print("Warning: MINIMAX_API_KEY not set, skipping prompt expansion")
        return prompt
    
    url = f"{BASE_URL}/v1/text/chatcompletion_v2"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """你是一个专业的AI图片生成提示词优化专家。当用户输入一个简单的图片描述时，你需要将其扩展成详细、生动的英文描述。

扩写规则：
1. 将简单描述扩展为详细的英文场景描述
2. 添加光线、氛围、风格等细节（如：soft lighting, cinematic, photorealistic等）
3. 添加视角/角度描述（如：front view, overhead shot, close-up等）
4. 添加画质/风格标签（如：4K, high detail, masterpiece等）
5. 保持原意但让描述更加丰富专业

直接输出扩写后的英文描述，不要解释，不要加括号说明，只输出纯文本描述。"""
    
    payload = {
        "model": "MiniMax-M2.7",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"请扩写这个图片描述：{prompt}"}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
    print("正在扩写提示词...")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            expanded = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            if expanded:
                print(f"✅ 提示词扩写完成")
                print(f"📝 扩写后：{expanded}")
                return expanded
    except Exception as e:
        print(f"Warning: Prompt expansion failed: {e}")
    
    return prompt

def generate_image(prompt, model="image-01", n=1, aspect_ratio="1:1", response_format="url", output=None):
    """Generate image using MiniMax API"""
    
    if not API_KEY:
        print("Error: MINIMAX_API_KEY environment variable not set")
        sys.exit(1)
    
    url = f"{BASE_URL}/v1/image_generation"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "response_format": response_format,
        "n": n
    }
    
    print(f"Generating {n} image(s) with aspect ratio {aspect_ratio}...")
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        sys.exit(1)
    
    result = response.json()
    
    if result.get("base_resp", {}).get("status_code") != 0:
        error_msg = result.get("base_resp", {}).get("status_msg", "Unknown error")
        print(f"API Error: {error_msg}")
        sys.exit(1)
    
    data = result.get("data", {})
    metadata = result.get("metadata", {})
    
    print(f"Success: {metadata.get('success_count', 0)} images generated")
    
    def get_output_path(filename):
        """Resolve output path - use minimax-images dir for relative paths"""
        if filename and (os.path.isabs(filename) or filename.startswith('./')):
            return filename
        if filename:
            return os.path.join(MINIMAX_OUTPUT_DIR, filename)
        return None

    if response_format == "url":
        image_urls = data.get("image_urls", [])
        for i, img_url in enumerate(image_urls):
            print(f"\nImage {i+1}: {img_url}")
            if len(image_urls) == 1 and output:
                output_path = get_output_path(output)
            else:
                output_path = os.path.join(MINIMAX_OUTPUT_DIR, f"image_{i+1}.png")
            
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"Saved to: {output_path}")
            else:
                print(f"Failed to download image")
    else:
        image_base64 = data.get("image_base64", [])
        for i, img_b64 in enumerate(image_base64):
            img_data = base64.b64decode(img_b64)
            if len(image_base64) == 1 and output:
                output_file = get_output_path(output)
            else:
                output_file = os.path.join(MINIMAX_OUTPUT_DIR, f"image_{i+1}.png")
            with open(output_file, 'wb') as f:
                f.write(img_data)
            print(f"Image {i+1} saved to: {output_file}")
    
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MiniMax Image Generation")
    parser.add_argument("prompt", help="Image description/prompt")
    parser.add_argument("-n", "--num", type=int, default=1, help="Number of images to generate (1-9)")
    parser.add_argument("-a", "--aspect", default="1:1", help="Aspect ratio (e.g., 16:9, 4:3, 1:1)")
    parser.add_argument("-m", "--model", default="image-01", choices=["image-01", "image-01-live"], help="Model to use")
    parser.add_argument("-o", "--output", help="Output file path (for single image)")
    parser.add_argument("--format", default="url", choices=["url", "base64"], help="Response format")
    parser.add_argument("--expand", action="store_true", default=True, help="Auto-expand short prompts (default: enabled)")
    parser.add_argument("--no-expand", dest="expand", action="store_false", help="Disable prompt expansion")
    
    args = parser.parse_args()
    
    original_prompt = args.prompt
    
    # Check if prompt is short enough to need expansion (less than 30 chars)
    need_expansion = args.expand and len(original_prompt.strip()) < 30
    
    if need_expansion:
        print(f"📝 原始提示词：{original_prompt}")
        expanded_prompt = expand_prompt(original_prompt)
        use_prompt = expanded_prompt
    else:
        use_prompt = original_prompt
    
    generate_image(
        prompt=use_prompt,
        model=args.model,
        n=args.num,
        aspect_ratio=args.aspect,
        response_format=args.format,
        output=args.output
    )
