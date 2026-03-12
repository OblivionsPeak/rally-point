"""
National VSO directory data.
Each entry: name, abbreviation, tagline, description, specialty, phone, website.
"""

VSOS = [
    {
        'name':        'Disabled American Veterans',
        'abbr':        'DAV',
        'tagline':     'Best for: disability ratings & C&P prep',
        'description': 'Exclusively focused on veterans with service-connected disabilities. '
                       'DAV reps are among the most experienced at building nexus arguments '
                       'and fighting low ratings. Free to join, free claims help.',
        'phone':       '1-800-827-1000',
        'website':     'https://www.dav.org',
        'best_for':    ['disability ratings', 'appeals', 'C&P prep'],
    },
    {
        'name':        'Veterans of Foreign Wars',
        'abbr':        'VFW',
        'tagline':     'Best for: full-spectrum claims support',
        'description': 'One of the largest VSOs with accredited claims agents across all 50 states. '
                       'Strong track record on initial claims, increases, and supplemental appeals. '
                       'Also provides financial assistance for veterans in crisis.',
        'phone':       '1-816-756-3390',
        'website':     'https://www.vfw.org',
        'best_for':    ['initial claims', 'increases', 'financial assistance'],
    },
    {
        'name':        'American Legion',
        'abbr':        'AL',
        'tagline':     'Best for: education, employment & benefits',
        'description': 'The largest wartime veterans organization. Accredited service officers '
                       'assist with claims, education benefits (GI Bill), and employment. '
                       'Strong community network with posts in virtually every county.',
        'phone':       '1-800-433-3318',
        'website':     'https://www.legion.org',
        'best_for':    ['GI Bill', 'employment', 'community support'],
    },
    {
        'name':        'AMVETS',
        'abbr':        'AMVETS',
        'tagline':     'Best for: all-era veterans & advocacy',
        'description': 'Open to all honorably discharged veterans regardless of era or conflict. '
                       'AMVETS service officers assist with VA claims and benefits, with a '
                       'strong focus on legislative advocacy at the federal level.',
        'phone':       '1-877-726-8387',
        'website':     'https://amvets.org',
        'best_for':    ['all eras', 'legislative advocacy', 'claims'],
    },
    {
        'name':        'Paralyzed Veterans of America',
        'abbr':        'PVA',
        'tagline':     'Best for: spinal cord & neurological conditions',
        'description': 'Specializes in spinal cord injury/dysfunction and diseases of the '
                       'central nervous system. If your claims involve TBI, paralysis, MS, '
                       'or similar neurological conditions, PVA reps have deep expertise.',
        'phone':       '1-800-424-8200',
        'website':     'https://pva.org',
        'best_for':    ['TBI', 'spinal cord', 'neurological conditions'],
    },
    {
        'name':        'Wounded Warrior Project',
        'abbr':        'WWP',
        'tagline':     'Best for: post-9/11 veterans & mental health',
        'description': 'Focused on veterans of the post-9/11 era. Beyond claims help, '
                       'WWP provides mental health programs, career counseling, and peer '
                       'support networks. Strong on PTSD, TBI, and MST claims.',
        'phone':       '1-888-997-2586',
        'website':     'https://www.woundedwarriorproject.org',
        'best_for':    ['post-9/11', 'PTSD', 'mental health', 'MST'],
    },
    {
        'name':        'National Veterans Legal Services Program',
        'abbr':        'NVLSP',
        'tagline':     'Best for: complex denials & BVA appeals',
        'description': 'Not a traditional VSO — NVLSP is a nonprofit law firm that represents '
                       'veterans pro bono at the Court of Appeals for Veterans Claims (CAVC). '
                       'If you\'ve been denied after BVA, NVLSP is who you want.',
        'phone':       '1-202-265-8305',
        'website':     'https://www.nvlsp.org',
        'best_for':    ['BVA denials', 'CAVC appeals', 'complex cases'],
    },
    {
        'name':        'Vietnam Veterans of America',
        'abbr':        'VVA',
        'tagline':     'Best for: Vietnam-era & Agent Orange claims',
        'description': 'Exclusively for Vietnam-era veterans. Deep expertise in Agent Orange '
                       'presumptive conditions, PTSD claims from Vietnam service, and the '
                       'unique evidence challenges that era presents.',
        'phone':       '1-800-882-1316',
        'website':     'https://vva.org',
        'best_for':    ['Agent Orange', 'Vietnam-era', 'PTSD'],
    },
]
