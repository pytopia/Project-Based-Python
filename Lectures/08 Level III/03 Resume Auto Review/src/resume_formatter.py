from datetime import date

def format_date(date_obj):
    if isinstance(date_obj, date):
        return date_obj.strftime("%B %Y")
    return str(date_obj) if date_obj else ""

def format_personal_info(info):
    if not info:
        return ""

    markdown = f"### {info.get('full_name', 'Name Not Provided')}\n\n"

    contact_info = []
    if info.get('email'):
        contact_info.append(info['email'])
    if info.get('phone'):
        contact_info.append(info['phone'])
    if info.get('address'):
        address = info['address']
        location = f"{address.get('city', '')}, {address.get('state', '')}, {address.get('country', '')}".strip(', ')
        if location:
            contact_info.append(location)
    if info.get('linkedin'):
        contact_info.append(f"[LinkedIn]({info['linkedin']})")
    if info.get('github'):
        contact_info.append(f"[GitHub]({info['github']})")
    if info.get('website'):
        contact_info.append(f"[Website]({info['website']})")

    if contact_info:
        markdown += " | ".join(contact_info) + "\n\n"

    return markdown

def format_summary(summary):
    return f"#### Summary\n\n{summary}\n\n" if summary else ""

def format_work_experience(experience):
    if not experience:
        return ""

    markdown = "#### Work Experience\n\n"
    for job in experience:
        markdown += f"###### {job.get('job_title', 'Position Not Specified')} | {job.get('company', 'Company Not Specified')}\n"
        location = f"{job.get('location', {}).get('city', '')}, {job.get('location', {}).get('state', '')}".strip(', ')
        dates = f"{format_date(job.get('start_date'))} - {format_date(job.get('end_date'))}".strip(' -')
        if location or dates:
            markdown += f"*{location + ' | ' if location else ''}{dates}*\n\n"
        if job.get('description'):
            markdown += f"{job['description']}\n\n"
        if job.get('achievements'):
            markdown += "**Key Achievements:**\n"
            for achievement in job['achievements']:
                markdown += f"- {achievement}\n"
            markdown += "\n"
    return markdown

def format_education(education):
    if not education:
        return ""

    markdown = "#### Education\n\n"
    for edu in education:
        markdown += f"###### {edu.get('degree', 'Degree Not Specified')} {('in ' + edu['field_of_study']) if edu.get('field_of_study') else ''} | {edu.get('institution', 'Institution Not Specified')}\n"
        location = f"{edu.get('location', {}).get('city', '')}, {edu.get('location', {}).get('state', '')}".strip(', ')
        dates = f"{format_date(edu.get('start_date'))} - {format_date(edu.get('end_date'))}".strip(' -')
        if location or dates:
            markdown += f"*{location + ' | ' if location else ''}{dates}*\n\n"
        if edu.get('honors'):
            markdown += "**Honors:**\n"
            for honor in edu['honors']:
                markdown += f"- {honor}\n"
            markdown += "\n"
    return markdown

def format_skills(skills):
    return f"#### Skills\n\n{', '.join(skills)}\n\n" if skills else ""

def format_certifications(certifications):
    if not certifications:
        return ""

    markdown = "#### Certifications\n\n"
    for cert in certifications:
        markdown += f"- **{cert.get('title', 'Certification Not Specified')}** - {cert.get('issuer', 'Issuer Not Specified')}"
        if cert.get('date_obtained'):
            markdown += f" (Obtained: {format_date(cert['date_obtained'])})"
        markdown += "\n"
    return markdown + "\n"

def format_projects(projects):
    if not projects:
        return ""

    markdown = "#### Projects\n\n"
    for project in projects:
        markdown += f"###### {project.get('title', 'Project Title Not Specified')}\n\n"
        if project.get('description'):
            markdown += f"{project['description']}\n\n"
        if project.get('technologies'):
            markdown += f"**Technologies used:** {', '.join(project['technologies'])}\n"
        if project.get('url'):
            markdown += f"**URL:** [{project['url']}]({project['url']})\n"
        markdown += "\n"
    return markdown

def format_languages(languages):
    if not languages:
        return ""

    markdown = "#### Languages\n\n"
    for lang in languages:
        markdown += f"- {lang.get('language', 'Language Not Specified')}: {lang.get('proficiency', 'Proficiency Not Specified')}\n"
    return markdown + "\n"

def format_volunteer_experience(experience):
    if not experience:
        return ""

    markdown = "#### Volunteer Experience\n\n"
    for exp in experience:
        markdown += f"###### {exp.get('role', 'Role Not Specified')} | {exp.get('organization', 'Organization Not Specified')}\n"
        location = f"{exp.get('location', {}).get('city', '')}, {exp.get('location', {}).get('state', '')}".strip(', ')
        dates = f"{format_date(exp.get('start_date'))} - {format_date(exp.get('end_date'))}".strip(' -')
        if location or dates:
            markdown += f"*{location + ' | ' if location else ''}{dates}*\n\n"
        if exp.get('description'):
            markdown += f"{exp['description']}\n\n"
    return markdown

def format_interests(interests):
    return f"#### Interests\n\n{', '.join(interests)}\n\n" if interests else ""

def format_references(references):
    return "#### References\n\nAvailable upon request\n" if references else ""

def format_resume(data):
    sections = [
        format_personal_info(data.get('personal_info')),
        format_summary(data.get('summary')),
        format_work_experience(data.get('work_experience')),
        format_education(data.get('education')),
        format_skills(data.get('skills')),
        format_certifications(data.get('certifications')),
        format_projects(data.get('projects')),
        format_languages(data.get('languages')),
        format_volunteer_experience(data.get('volunteer_experience')),
        format_interests(data.get('interests')),
        format_references(data.get('references'))
    ]

    return "".join(sections).strip()
