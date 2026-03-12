"""Send reminder emails via Resend."""
import os
import resend

resend.api_key = os.environ.get('RESEND_API_KEY', '')

FROM_ADDRESS = os.environ.get('RESEND_FROM', 'Rally Point <reminders@rallypoint.vet>')
APP_URL      = os.environ.get('APP_URL', 'https://web-production-da302.up.railway.app')


def send_stale_claim_reminder(to_email: str, conditions: list) -> bool:
    """Email a veteran about claims with no activity in 30+ days.
    Returns True on success."""
    if not resend.api_key:
        return False

    try:
        resend.Emails.send({
            'from':    FROM_ADDRESS,
            'to':      [to_email],
            'subject': 'Rally Point — Your VA claim needs attention',
            'html':    _build_html(conditions),
            'text':    _build_text(conditions),
        })
        return True
    except Exception as e:
        print(f'[reminders] email to {to_email} failed: {e}')
        return False


def _build_text(conditions: list) -> str:
    items = '\n'.join(f'  • {c}' for c in conditions)
    return f"""Hey,

It's been over 30 days since you logged an update on your VA claim(s):

{items}

VA claims can stall without you noticing. Log in to update your status,
check your evidence checklist, or prep for a C&P exam.

{APP_URL}/dashboard

Stay in the fight,
Rally Point

——
To stop receiving these reminders, delete your account in Account Settings:
{APP_URL}/settings
"""


def _build_html(conditions: list) -> str:
    items = ''.join(
        f'<li style="margin:6px 0; font-size:15px;">{c}</li>'
        for c in conditions
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0; padding:0; background:#0d1117; font-family:system-ui,-apple-system,sans-serif;">
  <div style="max-width:520px; margin:40px auto; padding:32px; background:#161b22; border-radius:10px; border:1px solid #30363d;">

    <div style="font-size:20px; font-weight:700; color:#58a6ff; margin-bottom:24px; letter-spacing:-0.3px;">
      Rally Point
    </div>

    <p style="margin:0 0 16px; line-height:1.7; color:#e6edf3; font-size:15px;">
      It's been over <strong>30 days</strong> since you logged an update on your VA claim(s):
    </p>

    <ul style="margin:0 0 24px; padding-left:20px; color:#e6edf3;">
      {items}
    </ul>

    <p style="margin:0 0 28px; line-height:1.7; color:#8b949e; font-size:14px;">
      VA claims can stall without you noticing. Staying on top of status updates,
      evidence gathering, and C&amp;P prep gives you the best shot at a fair rating.
    </p>

    <a href="{APP_URL}/dashboard"
       style="display:inline-block; background:#1f6feb; color:#ffffff; text-decoration:none;
              padding:12px 28px; border-radius:6px; font-weight:600; font-size:15px;">
      View My Claims
    </a>

    <hr style="margin:32px 0; border:none; border-top:1px solid #30363d;">

    <p style="margin:0; font-size:12px; color:#484f58; line-height:1.6;">
      Stay in the fight.<br>
      To stop receiving these reminders,
      <a href="{APP_URL}/settings" style="color:#58a6ff; text-decoration:none;">delete your account</a>
      in Account Settings.
    </p>

  </div>
</body>
</html>"""
