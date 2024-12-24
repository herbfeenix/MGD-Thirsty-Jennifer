import json

def process_scene_json(file_path):
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Assuming 'EventText' is a top-level key
    for event in data["EventText"]:
        scene_name = event["NameOfScene"]
        print(f"Processing {scene_name}...")
        dialogue_lines = event["theScene"]
        
        for i, dialogue in enumerate(dialogue_lines):
            # Splitting the dialogue line by '|n|' to handle new lines
            sub_lines = dialogue.split('|n|')
            line_number = 1
            for line in sub_lines:
                if len(line) > 430:
                    # Find the word that contains the 430th character
                    words = line.split()
                    char_count = 0
                    for word_index, word in enumerate(words):
                        char_count += len(word) + 1  # Adding 1 for space or punctuation
                        if char_count >= 430:
                            break

                    # Extract the two words before and after, if they exist
                    before = words[word_index-2:word_index] if word_index >= 2 else words[:word_index]
                    after = words[word_index+1:word_index+3] if word_index + 1 < len(words) else words[word_index+1:]

                    print(f"Line {i+1}.{line_number}: {' '.join(before)} {words[word_index]} {' '.join(after)}")
                line_number += 1

# Example usage
file_path = 'SuckubusCombatEvents.json'
process_scene_json(file_path)
