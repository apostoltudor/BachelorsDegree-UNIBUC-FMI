import json
import random
import os

def smart_augment():
    # 1. Load the regexes/wordlists
    try:
        with open('regexes.json', 'r', encoding='utf-8') as f:
            lexicon = json.load(f)
    except FileNotFoundError:
        print("Error: regexes.json not found.")
        return

    # 2. Define Templates for each category
    templates = {
        "Politics & Public Personalities": [
            "Primarul e un {insult_general}, a furat tot.",
            "Nu mai votați {insult_general}ul ăsta de politician.",
            "Toți parlamentarii sunt niște {insult_general}i.",
            "Ministrul ăla e o {insult_general}ă ordinară.",
            "Să vă f**t în gură de politicieni {insult_general}i.",
            "Uitați-vă la {insult_general}ul ăla cum minte la TV."
        ],
        "Sports & Rivalry": [
            "Arbitrul ăsta e un {insult_general}, ne-a furat meciul.",
            "Jucați ca niște {misogyny} de fricoși.",
            "Marș la vestiare, {insult_general}ule, nu meriți tricoul ăsta.",
            "Futu-vă-n cur de blatiști și {insult_general}i.",
            "Antrenorul e un {insult_general} bătut în cap.",
            "Să-mi bag pula în echipa voastră de {insult_general}i."
        ],
        "Misogyny & Objectification": [
            "Uită-te la {misogyny} aia cum se plimbă pe stradă.",
            "Ești o {misogyny} ordinară, te-ai culcat cu tot orașul.",
            "Marș la {religious_family} de {misogyny}, că politica e pentru bărbați.",
            "Ești o {misogyny} bătută în cap, taci dracului.",
            "Ce pretenții să ai de la o {misogyny} ca tine?",
            "Ești doar o {misogyny} pusă acolo să dai din fund."
        ],
        "Ableism & Mental Stigma": [
            "Ești un {ableism}, nu ești în stare de nimic.",
            "Marș la {ableism}ule, du-te la Bălăceanca.",
            "Un {ableism} ca tine n-ar trebui să vorbească.",
            "Ești {ableism} de-a dreptul, se vede pe fața ta.",
            "Băi {ableism}ule, taci drq că ești penibil.",
            "Ești o {ableism}ă care consumă aerul degeaba."
        ],
        "Hate Speech & Discriminatory": [
            "E plin de {ethnic} prin cartier, nu mai ai loc de ei.",
            "Marș la tine în {ethnic}ie, nu ne mai strica țara.",
            "Sunteți niște {ethnic}i ciorditori, aveți furatul în sânge.",
            "Futu-vă-n cur de {lgbtq}i, vreți drepturi dar sunteți bolnavi.",
            "Uite la {lgbtq}ul ăla cum merge pe stradă, ce mizerie.",
            "Ești un {ethnic} împuțit, spală-te înainte să intri aici."
        ],
        "Family & Religious Invective": [
            "Futu-ți {religious_family} de nesimțit.",
            "Să te bată {religious_family} de jegos.",
            "Mă piș pe {religious_family} de ratat.",
            "Să-ți moară tot {religious_family} de hoț.",
            "Futu-vă-n cruce de {insult_general}i.",
            "Biserica mă-tii de {insult_general} bătut în cap."
        ]
    }

    # 3. Augmentation Logic
    augmented_data = []
    
    # We aim for 200 items per category to start
    target_count = 200

    for category, cat_templates in templates.items():
        print(f"Augmenting {category}...")
        for i in range(target_count):
            template = random.choice(cat_templates)
            
            # Fill placeholders
            sentence = template.format(
                insult_general=random.choice(lexicon['insults_general_expanded']),
                ethnic=random.choice(lexicon['ethnic_and_racial_hate']),
                misogyny=random.choice(lexicon['misogyny_and_objectification']),
                lgbtq=random.choice(lexicon['anti_lgbtq_and_gender_slurs']),
                ableism=random.choice(lexicon['ableism_and_mental_stigma']),
                religious_family=random.choice(lexicon['religious_and_family_invective'])
            )
            
            augmented_data.append({"text": sentence, "category": category})

    # 4. Save
    output_file = 'dataset_v2_augmented.json'
    
    # Also include the original data from dataset_v1_smart
    if os.path.exists('dataset_v1_smart.json'):
        with open('dataset_v1_smart.json', 'r', encoding='utf-8') as f:
            original_data = json.load(f)
        final_data = original_data + augmented_data
    else:
        final_data = augmented_data

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"\nAugmentation Complete!")
    print(f"Added {len(augmented_data)} template-based phrases.")
    print(f"Final size: {len(final_data)}")
    
    # Distribution
    counts = {}
    for d in final_data:
        counts[d['category']] = counts.get(d['category'], 0) + 1
    
    print("\nNew Distribution:")
    for cat, count in counts.items():
        print(f" - {cat}: {count}")

if __name__ == "__main__":
    smart_augment()
