#!/usr/bin/env python3
"""Rebuild JSON-LD structured data on every public page, plus sitemap.xml.

Run from the repo root after changing services, prices, or FAQ text:
    python3 scripts/build_seo.py

FAQPage data is read from each page's visible <details><summary> FAQ, so the
structured data always matches what visitors see. Not served (netlify.toml 404s /scripts/*).
"""
import datetime
import html as H
import json
import re

BASE = "https://givingbridgeconsulting.com"
CAL = "https://calendar.app.google/1Do2GPcDJhYSkQES9"
TODAY = datetime.date.today().isoformat()


def ref(i):
    return {"@id": i}


ORG = {
    "@type": ["Organization", "ProfessionalService"], "@id": BASE + "/#org",
    "name": "GivingBridge Consulting", "legalName": "Giving Bridge Consulting LLC",
    "url": BASE + "/", "logo": BASE + "/assets/apple-touch-icon.png", "image": BASE + "/assets/og-image.jpg",
    "slogan": "Fundraising that outlives the moment.",
    "description": "Fundraising strategy and practical AI for nonprofits. GivingBridge helps small development teams, executive directors, and boards build the systems, clarity, and roadmap to turn goodwill into lasting support.",
    "email": "nelvin@givingbridgeconsulting.com", "founder": ref(BASE + "/#nelvin"),
    "address": {"@type": "PostalAddress", "addressLocality": "East Northport", "addressRegion": "NY", "addressCountry": "US"},
    "areaServed": {"@type": "Country", "name": "United States"},
    "sameAs": ["https://www.linkedin.com/company/giving-bridge-consulting/"],
    "knowsAbout": ["Nonprofit fundraising", "Donor strategy", "Donor retention", "Donor segmentation", "Donor journey mapping",
                   "AI for nonprofits", "AI for fundraising", "Nonprofit AI policy", "Associate boards", "Board fundraising", "Major gifts"],
    "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": "nelvin@givingbridgeconsulting.com", "url": CAL},
}
PERSON = {
    "@type": "Person", "@id": BASE + "/#nelvin", "name": "Nelvin Johnson",
    "jobTitle": "Founder, fundraising and AI consultant for nonprofits", "worksFor": ref(BASE + "/#org"),
    "image": BASE + "/assets/nelvin.jpg", "url": BASE + "/#author",
    "sameAs": ["https://www.linkedin.com/in/nelvinjohnson/"],
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "M.S. in Nonprofit Management"},
    "knowsAbout": ["Nonprofit fundraising", "Major gifts", "Donor strategy", "Associate boards", "AI for nonprofits"],
}
WEBSITE = {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "GivingBridge Consulting",
           "publisher": ref(BASE + "/#org"), "inLanguage": "en-US"}
TOVERA = {"@type": "WebSite", "@id": "https://tovera.org/#website", "name": "Tovera", "url": "https://tovera.org",
          "description": "A free, verified calendar of professional events for the nonprofit sector across the U.S. and Canada.",
          "creator": ref(BASE + "/#nelvin"), "isAccessibleForFree": True}
BRIEF = {"@type": "WebSite", "@id": "https://nonprofitaibrief.org/#website", "name": "The Nonprofit AI Brief", "url": "https://nonprofitaibrief.org",
         "description": "A free daily guide to AI for nonprofits, philanthropy, and social impact, drawn from 51 trusted sources.",
         "creator": ref(BASE + "/#nelvin"), "isAccessibleForFree": True}


def service(sid, name, desc, url, stype, price=None):
    s = {"@type": "Service", "@id": sid, "name": name, "description": desc, "serviceType": stype,
         "provider": ref(BASE + "/#org"), "areaServed": {"@type": "Country", "name": "United States"},
         "audience": {"@type": "Audience", "audienceType": "Nonprofit organizations"}, "url": url}
    if price:
        s["offers"] = {"@type": "Offer", "price": price, "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": url}
    return s


HC = service(BASE + "/health-check/#service", "Fundraising Health Check",
             "A written diagnosis of a nonprofit's fundraising across donor retention, pipeline, board, communications rhythm, and AI readiness. Complete a 15-minute questionnaire and receive a personalized PDF report within 48 hours.",
             BASE + "/health-check/", "Fundraising assessment", "79")
SP = service(BASE + "/sprint/#service", "Donor Strategy Sprint",
             "A fixed-scope, three-week project: donor segmentation, a donor journey map, a 90-day engagement calendar, and a live working session with the team.",
             BASE + "/sprint/", "Donor strategy consulting", "1200")
AIS = service(BASE + "/ai-sprint/#service", "AI Fundraising Sprint",
              "A fixed-scope, three-week project that puts AI to work for a nonprofit fundraising team: a workflow audit, a prompt library in the organization's voice, an AI acceptable-use policy that protects donor data, and live team training.",
              BASE + "/ai-sprint/", "AI consulting for nonprofits", "1800")
AIW = service(BASE + "/ai-workshop/#service", "AI for Fundraisers workshop",
              "A 90-minute, hands-on virtual workshop that teaches nonprofit fundraising teams and boards to use AI well and safely on real fundraising tasks.",
              BASE + "/ai-workshop/", "AI training for nonprofits", "1000")
DS = service(BASE + "/#svc-donor-strategy", "Donor Strategy",
             "Project-based donor segmentation, donor journeys for key relationships, and an engagement cadence sized to the team's real capacity. Available as a custom project or the fixed-price Donor Strategy Sprint.",
             BASE + "/#donor-strategy", "Donor strategy consulting")
AIF = service(BASE + "/#svc-ai-fundraising", "AI for Fundraising",
              "Practical, safe AI for nonprofit fundraising teams: donor research, drafting thank-yous, appeals, and grants, an AI policy that covers donor data, and team training. Available as the AI Fundraising Sprint or a team workshop.",
              BASE + "/#ai-fundraising", "AI consulting for nonprofits")
AB = service(BASE + "/#svc-associate-boards", "Associate Board Development",
             "Build or restructure a nonprofit associate board with clear purpose, expectations, and term structure, recruited for influence, generosity, and commitment.",
             BASE + "/#associate-boards", "Board development consulting")


def crumbs(name, url):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}


def clean(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def faq(h, fid):
    items = re.findall(r"<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>", h, re.S)
    if not items:
        return []
    return [{"@type": "FAQPage", "@id": fid, "mainEntity": [
        {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in items]}]


ORG_HOME = dict(ORG, makesOffer=[{"@type": "Offer", "itemOffered": ref(s["@id"]), "price": s["offers"]["price"], "priceCurrency": "USD"}
                                 for s in (HC, SP, AIS, AIW)])

PAGES = {
    "index.html": (lambda h: [WEBSITE, ORG_HOME, PERSON, DS, AIF, AB, HC, SP, AIS, AIW, TOVERA, BRIEF,
                              {"@type": "WebPage", "@id": BASE + "/#webpage", "url": BASE + "/",
                               "name": "GivingBridge Consulting | Fundraising that outlives the moment",
                               "isPartOf": ref(BASE + "/#website"), "about": ref(BASE + "/#org"),
                               "primaryImageOfPage": BASE + "/assets/og-image.jpg"}] + faq(h, BASE + "/#faq"), "/", "1.0"),
    "health-check/index.html": (lambda h: [ORG, HC] + faq(h, BASE + "/health-check/#faq") + [crumbs("Fundraising Health Check", BASE + "/health-check/")], "/health-check/", "0.9"),
    "sprint/index.html": (lambda h: [ORG, SP] + faq(h, BASE + "/sprint/#faq") + [crumbs("Donor Strategy Sprint", BASE + "/sprint/")], "/sprint/", "0.9"),
    "ai-sprint/index.html": (lambda h: [ORG, AIS] + faq(h, BASE + "/ai-sprint/#faq") + [crumbs("AI Fundraising Sprint", BASE + "/ai-sprint/")], "/ai-sprint/", "0.9"),
    "ai-workshop/index.html": (lambda h: [ORG, AIW] + faq(h, BASE + "/ai-workshop/#faq") + [crumbs("AI for Fundraisers workshop", BASE + "/ai-workshop/")], "/ai-workshop/", "0.8"),
    "resources/index.html": (lambda h: [ORG, PERSON, TOVERA, BRIEF,
                                        {"@type": "CollectionPage", "@id": BASE + "/resources/#webpage", "url": BASE + "/resources/",
                                         "name": "Free resources for nonprofits", "author": ref(BASE + "/#nelvin"),
                                         "mainEntity": {"@type": "ItemList", "itemListElement": [
                                             {"@type": "ListItem", "position": 1, "item": ref("https://tovera.org/#website")},
                                             {"@type": "ListItem", "position": 2, "item": ref("https://nonprofitaibrief.org/#website")}]}},
                                        crumbs("Resources", BASE + "/resources/")], "/resources/", "0.7"),
}

urls = []
for path, (graph, url, prio) in PAGES.items():
    h = open(path, encoding="utf-8").read()
    h = re.sub(r'\n<script type="application/ld\+json">.*?</script>', "", h, flags=re.S)
    data = {"@context": "https://schema.org", "@graph": graph(h)}
    block = '\n<script type="application/ld+json">\n' + json.dumps(data, indent=1, ensure_ascii=False) + "\n</script>"
    assert h.count("</head>") == 1, path
    h = h.replace("</head>", block + "\n</head>", 1)
    open(path, "w", encoding="utf-8").write(h)
    faqs = sum(len(g["mainEntity"]) for g in data["@graph"] if g.get("@type") == "FAQPage")
    print(f"{path:28s} {len(data['@graph'])} entities, {faqs} FAQs")
    urls.append((url, prio))

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url, prio in urls:
        f.write(f"  <url><loc>{BASE}{url}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{prio}</priority></url>\n")
    f.write("</urlset>\n")
print("sitemap.xml:", len(urls), "urls")
