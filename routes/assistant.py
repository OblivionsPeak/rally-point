"""AI assistant powered by Claude."""
from flask import Blueprint, request, jsonify, session
from routes.dashboard import login_required
import anthropic
from config import ANTHROPIC_KEY

bp = Blueprint('assistant', __name__)

SYSTEM_PROMPT = """You are Rally Point, a VA benefits companion built by a veteran for veterans.

You help veterans understand the VA claims process — denials, evidence, C&P exams, and conditions they may be entitled to claim. You speak plainly, without jargon, like a knowledgeable friend who has been through the process themselves.

When claim context is provided, use it to give specific, personalized answers rather than generic guidance. Reference the veteran's actual conditions, ratings, and deadlines by name. If an appeal deadline is approaching or has passed, prioritize that information.

Important rules:
- You are NOT a lawyer and cannot give legal advice. Always make this clear when relevant.
- When veterans ask about specific ratings or outcomes, explain the criteria but remind them a VSO (Veterans Service Officer) can review their specific case for free.
- For C&P exam questions, always emphasize: describe your WORST day, not your average day.
- For secondary conditions, encourage veterans to research and discuss with their doctor.
- Never guarantee outcomes or ratings.
- Be empathetic. This process is genuinely hard and frustrating.
- Keep answers clear and direct. Veterans don't want fluff."""


@bp.post('/api/assistant')
@login_required
def chat():
    message = request.json.get('message', '').strip()
    history = request.json.get('history', [])
    context = request.json.get('context', '')  # optional extra context e.g. from C&P prep page

    if not message:
        return jsonify({'error': 'No message provided'}), 400
    if not ANTHROPIC_KEY:
        return jsonify({'error': 'AI assistant not configured yet. Add ANTHROPIC_API_KEY to Railway environment variables.'}), 503

    system = SYSTEM_PROMPT + (f'\n\nAdditional context: {context}' if context else '')

    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
        messages = history + [{'role': 'user', 'content': message}]
        response = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=1024,
            system=system,
            messages=messages,
        )
        reply = response.content[0].text
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
