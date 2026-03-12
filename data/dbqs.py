"""
Disability Benefits Questionnaire (DBQ) reference data.
Maps conditions to their VA DBQ form names and usage notes.
"""

DBQS = [
    # Mental Health
    {
        'category': 'Mental Health',
        'condition': 'PTSD',
        'dbq': 'Posttraumatic Stress Disorder (PTSD)',
        'notes': 'Covers all PTSD symptoms including sleep, hypervigilance, avoidance, and social/occupational functioning.',
        'keywords': ['ptsd', 'post-traumatic', 'post traumatic', 'trauma', 'mst'],
    },
    {
        'category': 'Mental Health',
        'condition': 'Depression / Anxiety / Bipolar / Other Mental Health',
        'dbq': 'Mental Disorders (other than PTSD and Eating Disorders)',
        'notes': 'Use for depression, anxiety, bipolar disorder, panic disorder, OCD, and other mental health conditions not related to trauma.',
        'keywords': ['depression', 'anxiety', 'bipolar', 'panic', 'ocd', 'mental health', 'psychiatric'],
    },
    {
        'category': 'Mental Health',
        'condition': 'Eating Disorders',
        'dbq': 'Eating Disorders',
        'notes': 'Covers anorexia, bulimia, and related conditions.',
        'keywords': ['eating disorder', 'anorexia', 'bulimia'],
    },

    # Neurological
    {
        'category': 'Neurological',
        'condition': 'Traumatic Brain Injury (TBI)',
        'dbq': 'Traumatic Brain Injury (TBI)',
        'notes': 'Covers cognitive symptoms, behavioral changes, and physical sequelae from head trauma. Often used alongside PTSD DBQ.',
        'keywords': ['tbi', 'traumatic brain injury', 'concussion', 'head injury'],
    },
    {
        'category': 'Neurological',
        'condition': 'Migraines / Headaches',
        'dbq': 'Headaches (including Migraine Headaches)',
        'notes': 'Documents frequency, severity, and prostrating nature of headache episodes — key for achieving a ratable evaluation.',
        'keywords': ['migraine', 'headache', 'headaches'],
    },
    {
        'category': 'Neurological',
        'condition': 'Peripheral Neuropathy',
        'dbq': 'Peripheral Nerves Conditions (Not Including Diabetic Sensory-Motor Peripheral Neuropathy)',
        'notes': 'Covers numbness, tingling, and weakness in extremities from nerve damage.',
        'keywords': ['neuropathy', 'peripheral nerve', 'numbness', 'tingling'],
    },
    {
        'category': 'Neurological',
        'condition': 'Seizure Disorders',
        'dbq': 'Seizure Disorders (Epilepsy)',
        'notes': 'Documents seizure type, frequency, and duration of post-ictal periods.',
        'keywords': ['seizure', 'epilepsy'],
    },

    # Spine
    {
        'category': 'Spine',
        'condition': 'Lower Back (Lumbar / Thoracic Spine)',
        'dbq': 'Thoracolumbar Spine (Back) Conditions',
        'notes': 'Most commonly used musculoskeletal DBQ. Captures range of motion, muscle spasms, and radiculopathy. Critical to have ROM measured on your worst day.',
        'keywords': ['back', 'lumbar', 'thoracic', 'spine', 'disc', 'sciatica', 'lumbago', 'degenerative'],
    },
    {
        'category': 'Spine',
        'condition': 'Neck (Cervical Spine)',
        'dbq': 'Cervical Spine Conditions',
        'notes': 'Separate DBQ from lower back. Captures cervical range of motion and radiculopathy into the arms.',
        'keywords': ['neck', 'cervical', 'cervical spine'],
    },

    # Upper Extremities
    {
        'category': 'Upper Extremities',
        'condition': 'Shoulder / Rotator Cuff',
        'dbq': 'Shoulder and Arm Conditions',
        'notes': 'Covers range of motion, rotator cuff tears, AC joint issues, and instability.',
        'keywords': ['shoulder', 'rotator cuff', 'ac joint'],
    },
    {
        'category': 'Upper Extremities',
        'condition': 'Elbow / Forearm',
        'dbq': 'Elbow and Forearm Conditions',
        'notes': 'Covers lateral epicondylitis (tennis elbow), medial epicondylitis, and other elbow conditions.',
        'keywords': ['elbow', 'forearm', 'epicondylitis', 'tennis elbow'],
    },
    {
        'category': 'Upper Extremities',
        'condition': 'Wrist',
        'dbq': 'Wrist Conditions',
        'notes': 'Covers wrist range of motion, carpal tunnel, and other wrist conditions.',
        'keywords': ['wrist', 'carpal tunnel'],
    },
    {
        'category': 'Upper Extremities',
        'condition': 'Hand / Fingers / Thumb',
        'dbq': 'Hand and Finger Conditions',
        'notes': 'Covers individual finger and hand range of motion. Each finger is separately ratable.',
        'keywords': ['hand', 'finger', 'thumb', 'fingers'],
    },

    # Lower Extremities
    {
        'category': 'Lower Extremities',
        'condition': 'Knee',
        'dbq': 'Knee and Lower Leg Conditions',
        'notes': 'One of the most commonly filed conditions. Covers instability, range of motion, meniscus issues, and post-surgical residuals.',
        'keywords': ['knee', 'meniscus', 'acl', 'patella', 'lower leg'],
    },
    {
        'category': 'Lower Extremities',
        'condition': 'Hip',
        'dbq': 'Hip and Thigh Conditions',
        'notes': 'Covers range of motion, labral tears, and other hip conditions.',
        'keywords': ['hip', 'thigh', 'labral'],
    },
    {
        'category': 'Lower Extremities',
        'condition': 'Ankle',
        'dbq': 'Ankle Conditions',
        'notes': 'Covers range of motion, instability, and post-surgical residuals.',
        'keywords': ['ankle'],
    },
    {
        'category': 'Lower Extremities',
        'condition': 'Foot / Plantar Fasciitis / Flat Feet',
        'dbq': 'Foot Conditions',
        'notes': 'Covers plantar fasciitis, flat feet (pes planus), hallux valgus, and other foot conditions.',
        'keywords': ['foot', 'feet', 'plantar fasciitis', 'flat feet', 'pes planus', 'hallux'],
    },

    # Hearing & ENT
    {
        'category': 'Hearing & ENT',
        'condition': 'Hearing Loss',
        'dbq': 'Hearing Loss',
        'notes': 'Must be completed by an audiologist. Captures pure tone averages and speech discrimination scores used to determine the diagnostic code.',
        'keywords': ['hearing loss', 'hearing', 'deaf'],
    },
    {
        'category': 'Hearing & ENT',
        'condition': 'Tinnitus',
        'dbq': 'Tinnitus',
        'notes': 'Short DBQ — tinnitus is almost always rated at 10%. Still useful for documenting the service connection nexus.',
        'keywords': ['tinnitus', 'ringing', 'ringing in ears'],
    },
    {
        'category': 'Hearing & ENT',
        'condition': 'Sinusitis / Rhinitis / Nose & Throat',
        'dbq': 'Sinusitis and Other Conditions of the Nose, Throat, Larynx and Pharynx',
        'notes': 'Covers chronic sinusitis, rhinitis, and related upper respiratory conditions.',
        'keywords': ['sinus', 'sinusitis', 'rhinitis', 'nose', 'throat', 'larynx'],
    },

    # Cardiovascular
    {
        'category': 'Cardiovascular',
        'condition': 'Hypertension',
        'dbq': 'Hypertension',
        'notes': 'Requires documented blood pressure readings. The rating is based on diastolic pressure and whether medication is required.',
        'keywords': ['hypertension', 'blood pressure', 'high blood pressure'],
    },
    {
        'category': 'Cardiovascular',
        'condition': 'Ischemic Heart Disease / Coronary Artery Disease',
        'dbq': 'Ischemic Heart Disease (including Coronary Artery Disease)',
        'notes': 'Agent Orange presumptive condition for eligible veterans. Rated by METs (exercise tolerance).',
        'keywords': ['heart disease', 'ischemic', 'coronary', 'cad', 'heart attack', 'myocardial'],
    },
    {
        'category': 'Cardiovascular',
        'condition': 'Arrhythmias',
        'dbq': 'Cardiac Arrhythmias',
        'notes': 'Covers AFib, SVT, and other arrhythmias. May be secondary to hypertension or other service-connected conditions.',
        'keywords': ['arrhythmia', 'afib', 'atrial fibrillation', 'svt'],
    },

    # Respiratory
    {
        'category': 'Respiratory',
        'condition': 'Sleep Apnea',
        'dbq': 'Sleep Apnea',
        'notes': 'CPAP requirement triggers a 50% rating. Must document diagnosis via sleep study and treatment.',
        'keywords': ['sleep apnea', 'cpap', 'sleep', 'apnea'],
    },
    {
        'category': 'Respiratory',
        'condition': 'Asthma / Chronic Respiratory Conditions',
        'dbq': 'Respiratory Conditions (other than Tuberculosis and Sleep Apnea)',
        'notes': 'Covers asthma, COPD, chronic bronchitis, and burn pit/toxic exposure respiratory conditions.',
        'keywords': ['asthma', 'copd', 'respiratory', 'bronchitis', 'pulmonary', 'lung'],
    },

    # Endocrine / Metabolic
    {
        'category': 'Endocrine',
        'condition': 'Diabetes Mellitus',
        'dbq': 'Diabetes Mellitus',
        'notes': 'Agent Orange and burn pit presumptive. Rated by treatment required (diet only, oral meds, insulin).',
        'keywords': ['diabetes', 'diabetic', 'blood sugar', 'insulin'],
    },
    {
        'category': 'Endocrine',
        'condition': 'Thyroid Conditions',
        'dbq': 'Thyroid and Parathyroid Conditions',
        'notes': 'Covers hypothyroidism, hyperthyroidism, and thyroid nodules.',
        'keywords': ['thyroid', 'hypothyroid', 'hyperthyroid'],
    },

    # Digestive
    {
        'category': 'Digestive',
        'condition': 'GERD / Esophageal Conditions',
        'dbq': 'Esophageal Conditions (including GERD)',
        'notes': 'Commonly secondary to PTSD (stress-induced). Documents symptoms, weight loss, and treatment.',
        'keywords': ['gerd', 'acid reflux', 'esophagus', 'heartburn', 'esophageal'],
    },
    {
        'category': 'Digestive',
        'condition': 'Stomach / Gastric Conditions / IBS',
        'dbq': 'Stomach, Duodenal and Gastric Conditions',
        'notes': 'Covers IBS, peptic ulcers, and other gastric conditions. IBS is commonly secondary to PTSD.',
        'keywords': ['stomach', 'ibs', 'irritable bowel', 'ulcer', 'gastric', 'gastritis'],
    },

    # Skin
    {
        'category': 'Skin',
        'condition': 'Scars / Disfigurement',
        'dbq': 'Scars/Disfigurement',
        'notes': 'Covers surgical scars, burn scars, and traumatic scars. Each scar is separately ratable.',
        'keywords': ['scar', 'scars', 'disfigurement', 'burn'],
    },
    {
        'category': 'Skin',
        'condition': 'Skin Conditions (Eczema, Psoriasis, Dermatitis)',
        'dbq': 'Skin Diseases',
        'notes': 'Covers psoriasis, eczema, contact dermatitis, and other chronic skin conditions.',
        'keywords': ['skin', 'eczema', 'psoriasis', 'dermatitis', 'rash'],
    },

    # Eyes
    {
        'category': 'Eyes',
        'condition': 'Eye Conditions',
        'dbq': 'Eye Conditions',
        'notes': 'Covers vision loss, eye injuries, cataracts, and other ocular conditions.',
        'keywords': ['eye', 'vision', 'cataracts', 'glaucoma', 'ocular'],
    },

    # Genitourinary
    {
        'category': 'Genitourinary',
        'condition': 'Kidney / Bladder Conditions',
        'dbq': 'Kidney Conditions',
        'notes': 'Covers chronic kidney disease, kidney stones, and bladder conditions.',
        'keywords': ['kidney', 'bladder', 'renal', 'urinary'],
    },

    # Systemic / Other
    {
        'category': 'Systemic',
        'condition': 'Fibromyalgia',
        'dbq': 'Fibromyalgia',
        'notes': 'Rated at 10%, 20%, or 40% based on symptoms and response to treatment.',
        'keywords': ['fibromyalgia', 'fibro'],
    },
    {
        'category': 'Systemic',
        'condition': 'Chronic Fatigue Syndrome',
        'dbq': 'Chronic Fatigue Syndrome',
        'notes': 'Gulf War illness presumptive. Rated by degree of debilitation.',
        'keywords': ['chronic fatigue', 'cfs', 'fatigue'],
    },
    {
        'category': 'Systemic',
        'condition': 'Gulf War General Symptoms',
        'dbq': 'Gulf War General Symptoms Questionnaire',
        'notes': 'For undiagnosed illnesses and medically unexplained symptoms in Gulf War veterans. Covers the full range of presumptive conditions.',
        'keywords': ['gulf war', 'undiagnosed illness', 'presumptive'],
    },
    {
        'category': 'Systemic',
        'condition': 'Cold Injury Residuals',
        'dbq': 'Cold Injury Residuals',
        'notes': 'Covers frostbite residuals, Raynaud\'s phenomenon, and other cold-related conditions.',
        'keywords': ['cold injury', 'frostbite', 'raynaud'],
    },
]


def get_categories():
    seen = []
    for d in DBQS:
        if d['category'] not in seen:
            seen.append(d['category'])
    return seen
