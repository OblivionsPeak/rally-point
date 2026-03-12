"""
Pre-populated evidence checklists keyed by condition keyword.
Matched case-insensitively against claim.condition.
"""

EVIDENCE = {
    'ptsd': [
        'VA mental health evaluation',
        'Stressor statement (VA Form 21-0781)',
        'Buddy statements from fellow service members',
        'Service records documenting the traumatic event',
        'Private therapist or psychiatrist records',
        'C&P exam results',
    ],
    'tbi': [
        'Military records documenting the incident (LOD)',
        'Neurological evaluation',
        'Neuropsychological testing results',
        'Brain imaging (MRI or CT scan)',
        'Private neurologist or psychiatrist records',
        'Buddy statements from witnesses',
    ],
    'sleep apnea': [
        'Sleep study (polysomnogram) results',
        'CPAP prescription or usage records',
        'Nexus letter linking sleep apnea to service',
        'Service treatment records showing sleep complaints',
        'Private sleep specialist records',
    ],
    'back': [
        'Imaging (X-ray, MRI, or CT of spine)',
        'Range-of-motion measurements from doctor',
        'Service treatment records showing back injury',
        'Nexus letter from treating physician',
        'Private orthopedic or pain management records',
    ],
    'knee': [
        'Imaging (X-ray or MRI of knee)',
        'Range-of-motion measurements',
        'Service treatment records showing knee injury',
        'Nexus letter from treating physician',
        'Surgical records if applicable',
    ],
    'tinnitus': [
        'Audiological evaluation (hearing test)',
        'Service records showing noise exposure duties (MOS)',
        'Nexus letter or statement from audiologist',
    ],
    'hearing': [
        'Audiological evaluation (hearing test)',
        'Speech discrimination scores',
        'Service records showing noise exposure duties',
        'Nexus letter from audiologist',
    ],
    'hypertension': [
        'Blood pressure readings over time (6+ months)',
        'Primary care physician treatment records',
        'Nexus letter linking hypertension to service',
        'Service treatment records showing elevated BP',
    ],
    'diabetes': [
        'Lab results (HbA1c, fasting glucose)',
        'Endocrinologist or primary care records',
        'Agent Orange exposure documentation (if applicable)',
        'Nexus letter from treating physician',
    ],
    'migraine': [
        'Neurologist or headache specialist records',
        'Headache diary or log',
        'Medication history for migraines',
        'Nexus letter linking migraines to service',
        'Service treatment records showing headache complaints',
    ],
    'shoulder': [
        'Imaging (X-ray or MRI of shoulder)',
        'Range-of-motion measurements',
        'Service treatment records showing shoulder injury',
        'Nexus letter from treating physician',
        'Surgical records if applicable',
    ],
    'depression': [
        'VA or private mental health evaluation',
        'Psychiatrist or psychologist treatment records',
        'Nexus letter linking depression to service',
        'Buddy statements if helpful',
    ],
    'anxiety': [
        'VA or private mental health evaluation',
        'Psychiatrist or psychologist treatment records',
        'Nexus letter linking anxiety to service',
    ],
    'burn pit': [
        'DD-214 showing qualifying service location and dates',
        'Deployment orders to qualifying country',
        'Medical records for the claimed condition',
        'PACT Act presumptive condition documentation',
    ],
    'cancer': [
        'Pathology report and biopsy results',
        'Oncologist treatment records',
        'DD-214 showing qualifying service (burn pit / Agent Orange)',
        'PACT Act or Agent Orange presumptive documentation',
        'Nexus letter if not a presumptive condition',
    ],
}

# Universal docs added to every claim
UNIVERSAL = [
    'DD-214 (Certificate of Release or Discharge)',
    'Service treatment records (STRs)',
    'VA treatment records',
    'Personal statement (VA Form 21-4138)',
]


def get_suggestions(condition: str) -> list:
    """Return suggested evidence docs for a condition. Always includes universal docs."""
    condition_lower = condition.lower()
    specific = []
    for keyword, docs in EVIDENCE.items():
        if keyword in condition_lower:
            specific = docs
            break
    # Universal first, then condition-specific (deduped)
    seen = set()
    result = []
    for doc in UNIVERSAL + specific:
        if doc not in seen:
            seen.add(doc)
            result.append(doc)
    return result
