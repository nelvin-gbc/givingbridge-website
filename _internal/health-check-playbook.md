# Health Check playbook (internal)

Not published: `netlify.toml` returns 404 for `/_internal/*`.

## The flow, end to end

1. **Buyer pays $79** through the Stripe Payment Link on `/health-check/`.
2. **Stripe redirects** to `/health-check/questionnaire/?session_id={CHECKOUT_SESSION_ID}`. The form stores that ID in a hidden `stripe_session_id` field, so every submission can be matched to a payment in Stripe (Payments → search the session ID).
3. **They submit the questionnaire.** Netlify saves it (Netlify → site → Forms → `health-check`) and emails you, once the form notification is set up.
4. **You write the report within 48 hours.** Start from `_internal/health-check-report.html`: open it in Chrome, edit the text, then File → Print → Save as PDF.
5. **Send the report (email 1, Day 0)** from HubSpot to the buyer's email, with the PDF attached. Create the contact in HubSpot if it isn't there yet.
6. **Enroll them in the HubSpot sequence "Health Check follow-up"** (emails 2–5 below). Sequences stop automatically if they reply or book a meeting.

### Why HubSpot Sequences instead of EmailJS

EmailJS sends one email when something triggers it. It can't wait two days and send the next one. Your HubSpot Sales Starter plan includes Sequences, which do exactly this: timed emails sent from your own inbox, which stop when someone replies. It's no extra cost, and every buyer lands in your CRM.

### One-time setup in HubSpot

- Automation → Sequences → Create sequence → "Health Check follow-up".
- Add four automated email steps with these delays: Day 2, Day 5, Day 9, Day 14 (counted from enrollment, which is the day you send the report).
- Settings: business days only (on), unenroll when contact replies (on), unenroll when meeting booked (on).
- Paste in emails 2–5 below. Use the `{{contact.firstname}}` token for the first name.

### One-time setup in Netlify

- Forms → Form notifications → Add notification → Email → `nelvin@givingbridgeconsulting.com` for form `health-check`.

---

## The five emails

Write these in your own voice. Brackets mark the parts to fill in.

### Email 1: Day 0 (send manually with the PDF)

**Subject:** Your Fundraising Health Check, [Organization]

Hi [First name],

Your Health Check is attached.

The short version: your strongest area is **[strongest area]**, and the place I'd focus first is **[weakest link]**. The report walks through why, and lists the three changes I'd make, in order.

A few things to know as you read it:

- It's built entirely from your answers, so where something sounds off, it's usually a sign the data's fuzzy. That's worth knowing too.
- The first action item is the one I'd do this month, even if you do nothing else.
- If you want to talk any of it through, reply here or grab 15 minutes on my calendar: https://calendar.app.google/1Do2GPcDJhYSkQES9
- If you decide to book the Donor Strategy Sprint or the AI Fundraising Sprint within 60 days (by [date]), your $79 comes off the price.

Thanks for trusting me with an honest look at your fundraising.

Nelvin

---

### Email 2: Day 2

**Subject:** The most common gap I see

Hi {{contact.firstname}},

After reading a lot of these, one pattern shows up more than any other: **[the #1 issue you're seeing across Health Checks this month, e.g. "first-time donors who never hear from the organization again until the next ask"]**.

It's rarely about effort. Most teams are working hard. It's that nobody owns the moment between the first gift and the second ask, so it quietly doesn't happen.

One small fix: **[one concrete, do-it-this-week step, e.g. "a personal call or handwritten note within 48 hours of every first gift, owned by one named person"]**.

If that's the gap your report flagged too, you're in good company, and it's very fixable.

Nelvin

---

### Email 3: Day 5

**Subject:** What fixing it actually looks like

Hi {{contact.firstname}},

Diagnosing the problem is the easy part. The hard part is building the system that keeps it fixed when the year gets busy.

When I work with a team on this, it comes down to three things:

1. **Know who's who.** Donors grouped by capacity and engagement, so the right people get a personal touch and nobody gets ignored.
2. **Know what happens next.** A simple journey from first gift to renewal to upgrade, with a clear next step at each stage.
3. **Know when.** A 90-day calendar sized to the people you actually have, so it survives a hard month.

That's exactly what the Donor Strategy Sprint builds, in three weeks, for a flat $1,200: https://givingbridgeconsulting.com/sprint/

No pressure. Even if you build it yourselves, those three pieces are the place to start.

Nelvin

---

### Email 4: Day 9

**Subject:** A Donor Strategy Sprint for [Organization]?

Hi {{contact.firstname}},

I'll be direct: if your Health Check pointed to donor retention, cadence, or relationships that stall, the Donor Strategy Sprint is built for exactly that.

In three weeks you get:

- Donor segments by capacity and engagement
- A donor journey map, from first gift through lapse recovery
- A 90-day engagement calendar your team can keep
- A working session with your team to put it in motion

It's $1,200 flat, with no retainer, and your $79 Health Check comes off the price if you book by [date, 60 days from purchase]. If the Week 2 drafts aren't on track, I refund the full fee. I only take a few sprints each month so each one gets real attention.

If you'd like to see whether it's a fit, book a 15-minute scoping call: https://calendar.app.google/1Do2GPcDJhYSkQES9

Nelvin

---

### Email 5: Day 14

**Subject:** Closing the loop

Hi {{contact.firstname}},

I won't keep filling your inbox. I just wanted to close the loop on your Health Check.

If now isn't the right time, that's completely fine. The report is yours to keep, and the first action item is still the best place to start.

If things change, or you just want a second opinion on a fundraising question, reply anytime. I read everything.

Rooting for you,
Nelvin

P.S. If you're looking for trainings for your team this year, I keep a free calendar of nonprofit events at https://tovera.org.
