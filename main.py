#!/usr/bin/env python3
"""
YouTube Shorts Automation System - Main Script
Generates historical fact videos for YouTube Shorts
"""

import os
import json
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class HistoricalFactsGenerator:
    """Generate upbeat, child-friendly historical facts for YouTube Shorts"""
    
    def __init__(self):
        self.facts_database = [
            {
                "title": "The Great Emu War",
                "fact": "In 1932, Australia declared war on emus! The military was sent to fight thousands of emus destroying crops. The emus won!",
                "category": "animal_trials",
                "year": "1932"
            },
            {
                "title": "Trial of the Pig",
                "fact": "In medieval Europe, pigs were actually put on trial and executed for crimes! One pig was even dressed in a jacket during its trial.",
                "category": "animal_trials",
                "year": "1386"
            },
            {
                "title": "The Dancing Plague",
                "fact": "In 1518, people in Strasbourg couldn't stop dancing for days! A woman started dancing alone, then dozens joined her. It was called a plague!",
                "category": "weird_history",
                "year": "1518"
            },
            {
                "title": "King Tut's Curse",
                "fact": "When King Tutankhamun's tomb was opened in 1922, people thought a curse would strike. It didn't! It was just a legend.",
                "category": "ancient_history",
                "year": "1922"
            },
            {
                "title": "The Shortest War",
                "fact": "The shortest war in history lasted only 38 to 45 minutes! It was between Britain and Zanzibar in 1896.",
                "category": "wars",
                "year": "1896"
            },
            {
                "title": "Cleopatra's Bathing Beauty",
                "fact": "Cleopatra bathed in milk! She believed it made her skin beautiful and smooth. Now that's dedication to skincare!",
                "category": "ancient_history",
                "year": "69BC"
            },
            {
                "title": "Napoleon's Height Mystery",
                "fact": "Everyone thinks Napoleon was super short, but he was actually 5'7\" - average height for his time! The myth came from British propaganda.",
                "category": "famous_people",
                "year": "1769"
            },
            {
                "title": "The Pigeon Postal Service",
                "fact": "Before email, messenger pigeons carried mail! In WWI, a pigeon named Cher Ami saved 194 soldiers' lives by delivering a message.",
                "category": "animals",
                "year": "1918"
            },
            {
                "title": "Medieval Unicorn Horn",
                "fact": "Medieval people thought narwhal tusks were unicorn horns and paid fortunes for them! Some doctors even tried to use them as medicine.",
                "category": "medieval",
                "year": "1400s"
            },
            {
                "title": "The Great London Smog",
                "fact": "In 1952, London was covered in such thick smog that people couldn't see across the street! It killed over 12,000 people in just a few weeks.",
                "category": "disasters",
                "year": "1952"
            },
        ]
    
    def get_random_fact(self, category=None):
        """Get a random historical fact, optionally filtered by category"""
        import random
        
        if category:
            facts = [f for f in self.facts_database if f['category'] == category]
        else:
            facts = self.facts_database
        
        return random.choice(facts) if facts else None
    
    def get_all_facts(self):
        """Return all facts in the database"""
        return self.facts_database
    
    def export_facts_to_json(self, filename='historical_facts.json'):
        """Export facts database to JSON file for easy viewing"""
        with open(filename, 'w') as f:
            json.dump(self.facts_database, f, indent=2)
        print(f"✅ Facts exported to {filename}")
    
    def generate_batch(self, num_videos=5):
        """Generate a batch of video scripts from historical facts"""
        import random
        
        batch = []
        used_facts = set()
        
        for i in range(num_videos):
            fact = self.get_random_fact()
            
            # Avoid duplicates in batch
            while fact and fact['title'] in used_facts:
                fact = self.get_random_fact()
            
            if fact:
                used_facts.add(fact['title'])
                script = self.create_video_script(fact)
                batch.append({
                    'id': i + 1,
                    'fact': fact,
                    'script': script,
                    'generated_at': datetime.now().isoformat()
                })
        
        return batch
    
    def create_video_script(self, fact):
        """Create a simple video script from a historical fact"""
        return {
            'title': fact['title'],
            'opening': f"Did you know? {fact['title']}!",
            'main_fact': fact['fact'],
            'closing': "History is amazing! Did that surprise you? 🤯",
            'duration_seconds': 30,
            'year': fact['year']
        }
    
    def save_batch_to_file(self, batch, filename='video_batch.json'):
        """Save generated batch to file for later use"""
        with open(filename, 'w') as f:
            json.dump(batch, f, indent=2)
        print(f"✅ Batch saved to {filename}")
        return filename


class VideoCreator:
    """Create video files from scripts (placeholder for actual video generation)"""
    
    def __init__(self):
        self.output_dir = 'generated_videos'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def create_video_from_script(self, script, fact_id):
        """
        Create a video from a script.
        This is a placeholder - in production, integrate with OpenSora 2 or Vivideo API
        """
        filename = f"{self.output_dir}/historical_fact_{fact_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        
        # Placeholder - actual video generation would happen here
        print(f"📹 Video creation prepared for: {script['title']}")
        print(f"   Script: {script['main_fact']}")
        print(f"   Output: {filename}")
        
        return {
            'filename': filename,
            'script': script,
            'status': 'ready_for_generation'
        }


class SchedulingManager:
    """Manage scheduling of videos for YouTube upload"""
    
    def __init__(self):
        self.schedule_file = 'upload_schedule.json'
        self.schedule = self.load_schedule()
    
    def load_schedule(self):
        """Load existing schedule or create new one"""
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r') as f:
                return json.load(f)
        return {'videos': []}
    
    def add_to_schedule(self, video_info, upload_date):
        """Add a video to the upload schedule"""
        entry = {
            'video_id': video_info.get('id'),
            'title': video_info.get('fact', {}).get('title'),
            'filename': video_info.get('script', {}).get('title'),
            'scheduled_upload': upload_date.isoformat(),
            'status': 'scheduled',
            'created_at': datetime.now().isoformat()
        }
        self.schedule['videos'].append(entry)
        self.save_schedule()
        return entry
    
    def save_schedule(self):
        """Save schedule to file"""
        with open(self.schedule_file, 'w') as f:
            json.dump(self.schedule, f, indent=2)
        print(f"✅ Schedule saved to {self.schedule_file}")
    
    def generate_upload_schedule(self, num_videos=7, start_date=None):
        """Generate upload schedule for next N days"""
        Perfect for offshore work - schedule everything upfront!
        """
        if start_date is None:
            start_date = datetime.now()
        
        schedule = []
        for i in range(num_videos):
            upload_date = start_date + timedelta(days=i)
            schedule.append({
                'day': i + 1,
                'upload_date': upload_date.strftime('%Y-%m-%d'),
                'upload_time': '09:00:00'
            })
        
        return schedule


def main():
    """Main automation flow"""
    print("=" * 60)
    print("🎬 YouTube Shorts Historical Facts Automation System 🎬")
    print("=" * 60)
    print()
    
    # Initialize components
    facts_gen = HistoricalFactsGenerator()
    video_creator = VideoCreator()
    scheduler = SchedulingManager()
    
    # Generate batch of videos
    print("📚 Generating historical facts batch...")
    batch = facts_gen.generate_batch(num_videos=5)
    print(f"✅ Generated {len(batch)} video scripts\n")
    
    # Display generated facts
    print("Generated Videos:")
    print("-" * 60)
    for video in batch:
        fact = video['fact']
        print(f"\n📌 Video {video['id']}: {fact['title']}")
        print(f"   Category: {fact['category']}")
        print(f"   Fact: {fact['fact']}")
        print(f"   Year: {fact['year']}")
    
    print("\n" + "=" * 60)
    
    # Save batch to file
    facts_gen.save_batch_to_file(batch)
    
    # Generate upload schedule
    print("\n📅 Generating upload schedule (7 days)...")
    upload_schedule = scheduler.generate_upload_schedule(num_videos=7)
    
    for day_schedule in upload_schedule:
        print(f"   Day {day_schedule['day']}: {day_schedule['upload_date']} at {day_schedule['upload_time']}")
    
    scheduler.save_schedule()
    
    print("\n" + "=" * 60)
    print("✅ SETUP COMPLETE!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Files created:")
    print("   - video_batch.json (your video scripts)")
    print("   - upload_schedule.json (your upload schedule)")
    print("   - historical_facts.json (all available facts)")
    print("\n2. Integrate with video generation tool:")
    print("   - OpenSora 2 API")
    print("   - Vivideo API")
    print("   - Or use CapCut manually with scripts")
    print("\n3. For YouTube upload:")
    print("   - Use YouTube Studio to upload videos")
    print("   - Schedule them using the dates in upload_schedule.json")
    print("\n4. Run this script periodically to generate new batches!")
    print("=" * 60)


if __name__ == '__main__':
    main()