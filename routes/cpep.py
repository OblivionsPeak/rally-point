"""C&P Exam Prep routes."""
from flask import Blueprint, render_template
from supabase_client import svc_client
from routes.dashboard import login_required

bp = Blueprint('cpep', __name__)

# Condition-specific tips keyed by lowercase keywords
CONDITION_TIPS = {
    'ptsd': [
        "Describe how PTSD affects your daily life — relationships, work, sleep, going out in public.",
        "Mention hypervigilance: being on edge in crowds, checking exits, startling easily.",
        "Talk about nightmares and sleep disruption — how often, how it affects your day.",
        "Describe avoidance: places, people, or situations you stay away from because of triggers.",
        "Be honest about anger, irritability, or emotional numbness — these count.",
        "If you've had panic attacks, describe them in detail: how often, what triggers them, how long they last.",
        "Mention how it affects your ability to hold a job or maintain relationships.",
    ],
    'tinnitus': [
        "Describe the sound: ringing, buzzing, hissing — and whether it's constant or intermittent.",
        "Explain how it disrupts your sleep — do you need white noise, do you wake up because of it?",
        "Mention concentration problems: difficulty focusing at work, in conversations.",
        "If it causes headaches or dizziness, say so.",
        "Describe your worst days — when is it loudest, what makes it worse?",
    ],
    'sleep': [
        "Describe how many hours you actually sleep vs. how many you're in bed.",
        "Mention how often you wake up and whether you can fall back asleep.",
        "Explain the daytime impact: fatigue, difficulty concentrating, falling asleep at work.",
        "If you've had a sleep study, bring documentation.",
        "Describe how sleep problems affect your relationships and daily function.",
    ],
    'back': [
        "Describe your range of motion: how far can you bend forward, backward, side to side?",
        "Explain what activities you can no longer do or have difficulty with.",
        "Mention how long you can sit or stand before pain forces you to change position.",
        "Describe pain on your worst days: location, severity (1–10), what makes it worse.",
        "If you have radiculopathy (pain/numbness down legs), describe it specifically.",
        "Mention sleep disruption caused by pain.",
    ],
    'knee': [
        "Describe how far you can flex and extend the knee.",
        "Explain instability: does it give out, do you need a brace?",
        "Mention what you can no longer do: stairs, kneeling, standing for long periods.",
        "Describe pain on worst days and what triggers it.",
        "If you have flare-ups, describe frequency and severity.",
    ],
    'hearing': [
        "Describe real situations where hearing loss causes problems: conversations, TV volume, phone calls.",
        "Mention how often you ask people to repeat themselves.",
        "Explain workplace impact: missing instructions, difficulty in meetings.",
        "Describe any social withdrawal caused by difficulty following conversations.",
        "Bring your audiogram results if you have them.",
    ],
    'tbi': [
        "Describe cognitive symptoms: memory problems, difficulty concentrating, word-finding issues.",
        "Mention headaches: frequency, severity, triggers, how long they last.",
        "Explain mood changes: irritability, depression, anxiety since the injury.",
        "Describe sleep disruption and fatigue.",
        "Be specific about daily tasks that are harder now than before the injury.",
    ],
    'depression': [
        "Describe days when you can't get out of bed or complete basic tasks.",
        "Mention social withdrawal: avoiding friends, family, activities you used to enjoy.",
        "Explain work impact: missed days, difficulty concentrating, performance issues.",
        "Be honest about hopelessness, worthlessness, or any thoughts of self-harm.",
        "Describe how long episodes last and how often they occur.",
    ],
    'anxiety': [
        "Describe physical symptoms: racing heart, sweating, shortness of breath during anxiety.",
        "Explain situations you avoid because of anxiety.",
        "Mention how it affects work: deadlines, performance, calling in sick.",
        "Describe the frequency and duration of anxiety episodes.",
        "Be honest about how it affects relationships and daily decisions.",
    ],
    'shoulder': [
        "Describe your range of motion: how high can you raise your arm forward, sideways, behind you?",
        "Explain what you can no longer do: overhead work, lifting, reaching behind your back.",
        "Mention pain at rest vs. pain with movement.",
        "Describe weakness and how it limits daily activities.",
        "If you have flare-ups, describe frequency and what triggers them.",
    ],
}

GENERAL_TIPS = [
    {
        'heading': 'Describe your WORST day — not your average day',
        'body': 'The examiner is rating your condition at its worst. Veterans naturally minimize symptoms. When asked how you are, describe the hardest days — the days you can\'t function, not the days you push through.',
    },
    {
        'heading': 'Don\'t say "I\'m doing fine" or "it\'s not that bad"',
        'body': 'Military training conditions you to tough it out. At a C&P exam, that works against you. You\'re not complaining — you\'re accurately reporting a service-connected condition.',
    },
    {
        'heading': 'Explain how it affects your daily life',
        'body': 'The VA rates functional impairment, not just diagnosis. Describe work, relationships, sleep, driving, household tasks — anything the condition makes harder.',
    },
    {
        'heading': 'Be specific about frequency and severity',
        'body': 'Instead of "I have back pain sometimes," say "I have severe pain 4–5 days a week that limits me to sitting for 20 minutes at a time." Numbers and specifics matter.',
    },
    {
        'heading': 'The examiner is not your doctor',
        'body': 'Their job is to document your condition for rating purposes, not to treat you. Be thorough and complete — don\'t assume they\'ll ask the right follow-up questions.',
    },
    {
        'heading': 'Bring someone who knows your worst days',
        'body': 'A buddy statement from a spouse, family member, or fellow veteran describing what they\'ve witnessed carries real weight. Submit it before or at the exam.',
    },
]


def get_condition_tips(condition: str) -> list:
    """Return condition-specific tips based on keyword matching."""
    condition_lower = condition.lower()
    for keyword, tips in CONDITION_TIPS.items():
        if keyword in condition_lower:
            return tips
    return []


@bp.get('/claims/<claim_id>/cpep')
@login_required
def prep(claim_id):
    user_id = session_user_id()
    claim   = svc_client.table('claims').select('*').eq('id', claim_id).maybe_single().execute()
    if not claim.data or claim.data['user_id'] != user_id:
        from flask import redirect, url_for
        return redirect(url_for('dashboard.home'))

    condition_tips = get_condition_tips(claim.data['condition'])
    return render_template(
        'cpep.html',
        claim=claim.data,
        general_tips=GENERAL_TIPS,
        condition_tips=condition_tips,
    )


def session_user_id():
    from flask import session
    return session['user']['id']
