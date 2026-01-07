#!/usr/bin/env python3
"""
Demo script showing programmatic usage of the Unlimited Multimedia Generator
"""

from multimedia_generator import UnlimitedMultimediaGenerator

def main():
    print("=" * 70)
    print("UNLIMITED IRON CREATOR - API Demo")
    print("=" * 70)
    print()
    
    # Initialize the generator
    print("1. Initializing generator...")
    generator = UnlimitedMultimediaGenerator()
    print("   ✓ Generator initialized")
    print()
    
    # Generate text
    print("2. Generating text content...")
    text = generator.generate_text(
        "Write a brief introduction about AI-powered content creation",
        max_length=200,
        style="professional"
    )
    print()
    
    # Generate image
    print("3. Generating image...")
    image_path = generator.generate_image(
        "A creative workspace with AI holographic displays",
        size="1920x1080",
        style="futuristic"
    )
    print()
    
    # Generate audio
    print("4. Generating audio...")
    audio_path = generator.generate_audio(
        "Welcome to the future of unlimited creativity",
        type="speech",
        duration=10
    )
    print()
    
    # Generate video
    print("5. Generating video...")
    video_path = generator.generate_video(
        "Digital transformation and innovation",
        duration=5,
        resolution="1920x1080",
        fps=30
    )
    print()
    
    # Complete multimedia project
    print("6. Generating complete multimedia project...")
    results = generator.generate_multimedia_project({
        'text': 'The future of AI is unlimited',
        'image': 'Abstract AI neural network visualization',
        'audio': 'Inspiring technology soundscape',
        'video': 'Data flowing through digital networks'
    })
    print()
    
    print("=" * 70)
    print("✅ Demo completed successfully!")
    print("=" * 70)
    print()
    print(f"All generated files are in: {generator.output_dir}/")
    print()

if __name__ == '__main__':
    main()
