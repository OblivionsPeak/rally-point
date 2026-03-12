"""
Secondary condition suggestions keyed by primary condition keyword.
Each suggestion includes the condition name, why it's connected, and
what evidence typically links them.
"""

SECONDARIES = {
    'ptsd': [
        {
            'condition': 'Sleep Apnea',
            'why': 'PTSD hyperarousal and nightmares disrupt sleep architecture, which is well-documented to cause or worsen obstructive sleep apnea. VA frequently grants sleep apnea as secondary to PTSD.',
            'evidence': 'Sleep study (polysomnography) + nexus letter from your doctor connecting PTSD to sleep disruption.',
        },
        {
            'condition': 'Migraines',
            'why': 'Chronic stress, hyperarousal, and sleep disruption from PTSD are established triggers for migraines. Secondary nexus is commonly accepted.',
            'evidence': 'Medical records showing migraine diagnosis + doctor statement linking onset/worsening to PTSD.',
        },
        {
            'condition': 'GERD / Acid Reflux',
            'why': 'Chronic stress and anxiety from PTSD directly affects gut function and increases stomach acid production. GERD secondary to PTSD is widely accepted.',
            'evidence': 'GI diagnosis records + nexus letter connecting stress/PTSD to GI symptoms.',
        },
        {
            'condition': 'Hypertension',
            'why': 'Chronic PTSD-related stress keeps the body in a heightened state that raises blood pressure over time. Research directly supports this link.',
            'evidence': 'Blood pressure readings over time + doctor statement linking chronic stress/PTSD to hypertension.',
        },
        {
            'condition': 'Depression (MDD)',
            'why': 'PTSD and depression are highly comorbid — they share neurological pathways. If PTSD came first, depression can be rated as secondary.',
            'evidence': 'Mental health records showing depression diagnosis after PTSD + psychiatrist/psychologist nexus letter.',
        },
    ],

    'sleep apnea': [
        {
            'condition': 'Hypertension',
            'why': 'Untreated sleep apnea repeatedly drops oxygen levels at night, which strains the cardiovascular system and causes high blood pressure.',
            'evidence': 'Sleep study results + doctor statement linking sleep apnea to blood pressure elevation.',
        },
        {
            'condition': 'Depression',
            'why': 'Chronic sleep deprivation from sleep apnea is a well-documented cause of depression and mood disorders.',
            'evidence': 'Mental health diagnosis + doctor statement connecting poor sleep quality to depression.',
        },
        {
            'condition': 'Erectile Dysfunction',
            'why': 'Sleep apnea disrupts testosterone production and blood flow, both of which contribute to ED.',
            'evidence': 'Medical records for ED + nexus letter connecting to sleep apnea.',
        },
        {
            'condition': 'GERD / Acid Reflux',
            'why': 'The pressure changes during sleep apnea episodes can push stomach acid upward, causing or worsening GERD.',
            'evidence': 'GI records + doctor statement linking sleep apnea episodes to acid reflux.',
        },
    ],

    'back': [
        {
            'condition': 'Radiculopathy',
            'why': 'Spinal conditions that cause nerve root compression result in radiculopathy — pain, numbness, or weakness radiating into arms or legs. This is a separate ratable condition.',
            'evidence': 'MRI or nerve conduction study showing nerve involvement.',
        },
        {
            'condition': 'Hip Condition',
            'why': 'Altered gait and posture from a back condition transfers abnormal stress to the hips over time, causing degenerative changes.',
            'evidence': 'Hip imaging + doctor statement linking altered gait from back condition to hip deterioration.',
        },
        {
            'condition': 'Knee Condition',
            'why': 'Same gait compensation mechanism — limping or favoring one side due to back pain puts uneven wear on the knees.',
            'evidence': 'Knee imaging + doctor statement about gait compensation from back condition.',
        },
        {
            'condition': 'Sleep Disorder',
            'why': 'Chronic back pain disrupts sleep by making it difficult to find a comfortable position and causing nighttime pain.',
            'evidence': 'Sleep study or doctor notes documenting pain-related sleep disruption.',
        },
        {
            'condition': 'Depression',
            'why': 'Chronic pain is one of the strongest predictors of depression. Long-term loss of function and activity limitation takes a significant mental health toll.',
            'evidence': 'Mental health diagnosis + doctor statement connecting chronic pain to depressive symptoms.',
        },
    ],

    'tbi': [
        {
            'condition': 'Migraines',
            'why': 'Post-traumatic headaches/migraines are one of the most common TBI residuals. They are often separately ratable.',
            'evidence': 'Neurology records documenting migraine frequency and severity.',
        },
        {
            'condition': 'PTSD',
            'why': 'TBI and PTSD frequently co-occur from the same traumatic event. If not already claimed, PTSD may be separately ratable.',
            'evidence': 'Mental health evaluation establishing PTSD diagnosis.',
        },
        {
            'condition': 'Sleep Disorder',
            'why': 'TBI disrupts the brain\'s sleep regulation centers, causing insomnia, hypersomnia, or other sleep disorders.',
            'evidence': 'Sleep study + neurologist statement connecting TBI to sleep dysregulation.',
        },
        {
            'condition': 'Depression / Anxiety',
            'why': 'Mood disorders are well-documented TBI residuals due to changes in brain chemistry and frontal lobe function.',
            'evidence': 'Psychiatric evaluation documenting mood symptoms onset after TBI.',
        },
        {
            'condition': 'Tinnitus',
            'why': 'Head trauma frequently damages the auditory system. Tinnitus after TBI is a common separately ratable condition.',
            'evidence': 'Audiology evaluation + records documenting onset after the head injury.',
        },
    ],

    'tinnitus': [
        {
            'condition': 'Hearing Loss',
            'why': 'Tinnitus and hearing loss share the same root cause — noise exposure or acoustic trauma. Both are separately ratable. Many veterans claim tinnitus but forget to claim hearing loss.',
            'evidence': 'Audiogram showing hearing thresholds in the speech frequencies.',
        },
        {
            'condition': 'Sleep Disorder',
            'why': 'Tinnitus is loudest at night in quiet environments, making it a well-documented cause of chronic sleep disruption.',
            'evidence': 'Doctor notes or sleep study documenting tinnitus-related sleep difficulty.',
        },
        {
            'condition': 'Depression / Anxiety',
            'why': 'The chronic nature of tinnitus and associated sleep deprivation are established causes of depression and anxiety.',
            'evidence': 'Mental health records + doctor statement connecting tinnitus burden to mood symptoms.',
        },
    ],

    'hearing': [
        {
            'condition': 'Tinnitus',
            'why': 'Acoustic trauma that causes hearing loss almost always causes tinnitus too. If you haven\'t claimed both, you\'re likely leaving a claim on the table.',
            'evidence': 'Audiological evaluation documenting tinnitus alongside hearing loss.',
        },
        {
            'condition': 'Depression',
            'why': 'Hearing loss causes social withdrawal, communication difficulty, and isolation — all strong risk factors for depression.',
            'evidence': 'Mental health diagnosis + doctor statement connecting hearing loss-related isolation to depression.',
        },
    ],

    'knee': [
        {
            'condition': 'Hip Condition',
            'why': 'Knee instability or limited mobility alters gait and transfers abnormal load to the hip joint, causing secondary degeneration.',
            'evidence': 'Hip imaging + orthopedic or primary care statement linking gait changes to hip deterioration.',
        },
        {
            'condition': 'Back Condition',
            'why': 'Compensating for knee pain changes posture and spinal loading, contributing to back problems over time.',
            'evidence': 'Spinal imaging + doctor statement linking compensatory movement to back symptoms.',
        },
    ],

    'hypertension': [
        {
            'condition': 'Erectile Dysfunction',
            'why': 'Hypertension damages blood vessel walls and restricts blood flow, which is a primary cause of ED. Also note: many hypertension medications list ED as a side effect.',
            'evidence': 'Medical records for ED + doctor statement or medication documentation linking hypertension/medication to ED.',
        },
        {
            'condition': 'Heart Disease / Ischemic Heart Disease',
            'why': 'Chronic hypertension is the leading risk factor for heart disease. If you have an Agent Orange presumptive exposure, ischemic heart disease may also be separately claimable.',
            'evidence': 'Cardiology records + doctor statement about hypertension as contributing cause.',
        },
    ],

    'diabetes': [
        {
            'condition': 'Peripheral Neuropathy',
            'why': 'Diabetic peripheral neuropathy (numbness/pain in feet and hands) is a direct complication of diabetes. It is separately ratable and very commonly under-claimed.',
            'evidence': 'Nerve conduction study or neurological exam documenting neuropathy.',
        },
        {
            'condition': 'Erectile Dysfunction',
            'why': 'Diabetes damages nerves and blood vessels throughout the body, including those responsible for sexual function.',
            'evidence': 'Medical records for ED + endocrinologist or urologist nexus letter.',
        },
        {
            'condition': 'Hypertension',
            'why': 'Diabetes and hypertension are strongly linked — diabetes damages blood vessels and contributes to elevated blood pressure.',
            'evidence': 'Blood pressure records + doctor statement connecting diabetes to vascular effects.',
        },
        {
            'condition': 'Eye Condition (Diabetic Retinopathy)',
            'why': 'Diabetes damages the blood vessels in the retina. Diabetic retinopathy is a separately ratable vision condition.',
            'evidence': 'Ophthalmology records documenting retinal changes.',
        },
        {
            'condition': 'Kidney Disease (Nephropathy)',
            'why': 'Diabetic nephropathy is one of the most common complications of long-term diabetes and is separately ratable.',
            'evidence': 'Nephrology or primary care records documenting kidney function decline.',
        },
    ],

    'migraine': [
        {
            'condition': 'Depression / Anxiety',
            'why': 'Chronic migraines significantly increase the risk of depression and anxiety due to pain burden, activity limitation, and sleep disruption.',
            'evidence': 'Mental health diagnosis + doctor statement connecting migraine burden to mood symptoms.',
        },
        {
            'condition': 'Sleep Disorder',
            'why': 'Migraines frequently disrupt sleep, and poor sleep is both a trigger and a result of migraines.',
            'evidence': 'Sleep study or doctor notes documenting migraine-related sleep disruption.',
        },
    ],
}


def get_secondaries(condition: str) -> list:
    """Return secondary condition suggestions based on keyword matching."""
    condition_lower = condition.lower()
    for keyword, suggestions in SECONDARIES.items():
        if keyword in condition_lower:
            return suggestions
    return []
