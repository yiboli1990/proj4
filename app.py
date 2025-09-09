LDN NM Bermudan Callables Summary
	•	Since Oct 2023, desk trades SSA callables with EBRD, mainly in TRY; also expanded to ZAR and MXN. Business generated ~$60mm PNL.
	•	Typical structure: 10yNC1, GS pays TRY zero coupon, receives USD floating, holds call option; new trades accrete ~20%.
	•	Early trades (7yNC1y) had ~40% accretion, almost always called at first date.
	•	Smaller GS-issued callable notes in ZAR, HUF, PLN, RUB traded pre-EBRD, minor size.
	•	Mar 2024: +$1.7mm from correcting MEE window pricing; Aug 2025: -$2.8mm modeling losses (mean reversion, calibration, zero-coupon Berm approach).

Would you like me to make an even shorter 3-bullet executive version for senior management decks?



I apologize for the oversight. Let’s correct that.

For Kainan as a colleague:

1. What are this person’s top strengths that make them effective in their role?

Kainan exhibits an exceptional technical aptitude that has been foundational to our team’s accomplishments. Her ability to communicate complex ideas succinctly is noteworthy. Her invaluable contributions, especially in areas such as transaction waivers, various reporting decks, and Model IT matters, underline her comprehensive skill set.

2. What is at least one thing this person should consider doing to increase their effectiveness?

While Kainan’s collaborations within the team are commendable, a minor suggestion would be for her to further extend her interactions with colleagues beyond our direct team. By broadening her outreach, she can glean diverse insights and viewpoints, potentially enriching our team’s approach and solutions. This slight expansion in networking can further enhance her already significant impact.


This structure is intended as flexible guidance. You do not need to strictly follow it — adapt bullets and ordering depending on the model or context.


Perfect — thanks for sharing the full draft and the screenshots. I’ve polished your prompt engineering template to make it more formal, structured, and comprehensive, while staying close to your intent. I also expanded the guidance where helpful (e.g., wording discipline, optional additions, handling multiple models).

Here’s an improved version you can use:

⸻

📑 Prompt Engineering Template for MRM Validation Summaries

[ROLE / CONTEXT]

You are a Risk Manager in Goldman Sachs’ Model Risk Management (MRM) team, preparing a bi-weekly update for senior management. The material summarizes validation approvals and related activities for models used by the Global Banking & Markets (GBM) division.

⸻

[TASK]

Summarize the validation information provided into structured, professional bullet points suitable for reporting.

⸻

[FORMAT]
	•	Start with one clear title (model approval, extension, or enhancement).
	•	Follow with bullet points (and sub-bullets if needed).
	•	Maintain a consistent, professional tone.

⸻

[CONSTRAINTS]
	•	Keep each bullet point under 30 words.
	•	Keep factual; avoid subjective or extreme terms (e.g., avoid “significant”, “critical”).
	•	Use consistent tense (“We have approved…”, “During validation, MRM conducted…”).
	•	Acronyms (e.g., CLN, IRP, CVA) may be used without definition, assuming senior audience familiarity.
	•	Where findings are noted, mention their severity (Sev1–3) and the theme (documentation, calibration, etc.), but avoid unnecessary detail.

⸻

[CONTENT STRUCTURE]

Title Options:
	•	Approval of the [Model Name] Model
	•	[Model Name] Model Extension for [Coverage/Payoff]
	•	Enhancements to the [Model Name] Model

Bullets:
	1.	Approval Statement
	•	“We have approved the Tier [1/2/3] [Model Name] model used to [primary purpose].”
	•	OR “We have approved the extension to the Tier [1/2/3] [Model Name] model to support [coverage].”
	•	OR “We have approved enhancements to the Tier [1/2/3] [Model Name] model to [change].”
	2.	Purpose / Business Rationale
	•	“The model was developed to [replace old model / enable business / align with program / remediate waiver].”
	•	OR “This extension resolved [waiver/limitation].”
	•	OR “These enhancements improve [specific model feature, e.g., calibration consistency, hedging accuracy].”
	3.	MRM Validation Analysis
	•	“During validation, MRM conducted independent analyses, including:”
	•	Sub-bullets: benchmarking, back-testing, sensitivity, replication, documentation review.
	•	OR “MRM’s analysis focused on [specific tests].”
	4.	Findings Raised (Optional)
	•	“MRM raised [number] [severity] findings related to [theme].”
	•	If applicable: note whether remediation is closed, in progress, or planned.

⸻

[EXAMPLES]

# Approval of the CD CLNICSL Model
	•	We have approved the Tier 1 CD CLNICSL model, used to price Credit-Linked Notes (CLNs) and implemented in CSL.
	•	The purpose of this model is to price callable CLNs using hazard rate and interest rate dynamics.
	•	During validation, MRM conducted sensitivity analysis across risk factors and parameters.
	•	MRM raised one Sev1 finding on documentation (remediated) and two Sev2 findings on validation checks and IR calibration (remediation in progress).

⸻

# Approval of IRP CVA Cxl Berm and IRP CVA Ctl Berm Swo Models
	•	We have approved two Tier 1 models for XVA computation in USD swaps and Bermudan swaptions.
	•	The models address XVA exposure of life trades by computing XVA for such trades.
	•	During validation, MRM independently assessed exposures, tradeability, MEE windows, and option valuation.
	•	MRM raised two Sev2 findings on implementation and regressions; remediation is ongoing.

⸻

🔧 Additional Guidance
	•	Consistency across multiple approvals: If reporting several models in one update, ensure uniform formatting to improve readability.
	•	Optional grouping: Where multiple approvals belong to one theme (e.g., Callable Structures, XVA Models), a grouped title with sub-sections may be used.
	•	Tone discipline: Keep the voice neutral (no marketing language). Use “enable,” “support,” “address,” “remediate,” instead of “enhance competitiveness” or “significantly improve.”
	•	Flexibility: The template is guidance; adapt wording for clarity but keep structure intact.

⸻

👉 This version is formal, precise, and extensible — you can apply it to any validation summary, whether approvals, extensions, or enhancements.

Would you like me to also create a “bad vs. good” side-by-side example sheet (e.g., too vague vs. properly structured) so your team can quickly see how to apply the template?



[ROLE / CONTEXT]  
You are a risk manager preparing material for a senior executive.  

[TASK]  
Write one sentence describing the root cause of a $1.2m operational risk loss.  

[FORMAT]  
Respond in one sentence, plain English.  

[CONSTRAINTS]  
Keep it under 25 words. Emphasize the system mismatch (fast vs. slow).  

[EXAMPLE]  
Example of a good output:  
“Connecting a fast auto-hedging system with a slow risk feed caused timing mismatches and duplicate trades.”  


[ROLE / CONTEXT]  
You are [who should the AI act as? e.g., risk manager, Python tutor, travel guide].  

[TASK]  
Your task is to [specific action: summarize, explain, draft, calculate].  

[FORMAT]  
Respond in [bullets / table / one sentence / paragraph / code].  

[CONSTRAINTS]  
Keep it [under X words / formal tone / plain English / include examples / no jargon].  

[EXAMPLES (optional)]  
Example of a good output: “...”  



Great question — think of prompt engineering as designing instructions for an AI the way you’d design requirements for a junior analyst: clear, structured, and contextual.

Here’s a practical framework you can use:

⸻

🔑 Steps to Construct a Good Prompt
	1.	Set the Role / Context
	•	Tell the model who it should act as and what the situation is.
	•	Example: “You are a risk manager summarizing an operational loss for senior management.”
	2.	Specify the Task Clearly
	•	State exactly what you want (summarize, draft, translate, compute, etc.).
	•	Example: “Write a one-sentence description of the root cause.”
	3.	Define the Format / Style
	•	Indicate whether you want bullets, tables, headlines, code, formal/informal tone.
	•	Example: “Respond in 3 concise bullets, using plain English.”
	4.	Add Constraints / Rules
	•	Set length, scope, or exclusions.
	•	Example: “Keep under 20 words. Do not mention technical system names.”
	5.	Provide Examples (if possible)
	•	Show the model what “good” looks like.
	•	Example: “Good example: ‘System integration caused a timing mismatch leading to losses.’”
	6.	Iterate & Refine
	•	Start broad, then tighten.
	•	Treat it like coaching: you give feedback, and the prompt evolves.

⸻

🧩 Prompt Template You Can Reuse

Role/Context: “You are [X] working on [Y]…”
Task: “Please [do Z]…”
Format: “Respond in [bullets / table / one sentence / code].”
Constraints: “Keep under [N words / no jargon / include examples].”
Examples (optional): “For example: [give 1-2 good outputs].”

⸻

✅ Example for your op risk case:
“You are a risk manager preparing material for a senior exec. Write one sentence describing the root cause of the $1.2m op risk event. Keep it plain English, under 25 words, and emphasize system mismatch (fast vs. slow).”

⸻

Do you want me to create a cheat sheet of reusable prompt templates (e.g., summarize, draft, explain, code, translate) that you can copy-paste for different tasks?

Here’s a slightly tightened and polished version of your draft. I kept your structure but improved flow, readability, and consistency:

⸻

Top of Mind®
	•	MRM MRA Remediation (Annual Review): Remediation remains on track, with infrastructure enhancements and training completed ahead of the Sep 30 deadline
	•	Rollout is underway, with reviews for ~700 models to be completed under the enhanced framework by Dec 19
	•	We plan to schedule time with the FRB in the coming weeks to review the approach for addressing incremental CCAR feedback

Artificial Intelligence
	•	Validation is in progress for the Tier 1 Compliance surveillance AI used to review insider trading cases and narrow the scope of matters escalated for human review
	•	First AI model with fully agentic components, where the system both determines workflow and executes tasks
	•	Notable recent validations include:
	•	Equity Share Buyback Pricer: Revalidation of the first Tier 1 GBM Public machine-learning pricer; approval of 13 additional exotic features frequently requested by clients
	•	Model leverages a neural network to fair-value equity share buyback transactions, improving execution and client pricing competitiveness
	•	Fast Quoting (Agni Sharkfin): Approval of Tier 2 GBM Public neural network pricer that reduces quoting time by 72% for equity structured product charges

Validation Activities
	•	Approved migration of the mortgage prepayment model to the Delphi framework for pricing PWM mortgages
	•	Addresses a validation finding and aligns methodology across AWM and GBM
	•	Approved enhancements to the commodity margin shortfall model for GSEC clients, following annual review assessments in Q1
	•	Enhancements include recalibrated Cocoa shocks after recent volatility, plus new ongoing monitoring for missing Delta and Vega liquidation charges

Regulatory Updates
	•	FRB held the soft-close call last week for the Transaction Banking AML Remediation Verification Event (RVE)
	•	Confirmed all findings, including one on Compliance models requiring development and testing enhancements, are expected to close with no new findings
	•	NFA 2025 Swap Dealer Exam: Initial response submitted Sep 5
	•	Questionnaire requested pricing/risk model inventory and policy breaches; awaiting scope clarification from NFA
	•	Compliance expects heightened focus on model governance in this year’s exam
	•	PRA Periodic Summary Meeting (PSM): E&Y audit of model changes under IMM and IRB approaches completed
	•	Six preliminary findings identified on model change notification process, covering missing notifications, process scope, governance, and documentation

⸻

Would you like me to make this more executive-friendly (shorter, more headlines, fewer details), or keep it in this technical but polished format for internal tracking?




Here’s a concise draft you can paste into Outlook/Gmail:

⸻

Subject: Updates & asks: AI tooling feedback, surveillance AI, and PRC cadence change

Hi Bill,

Quick heads-up and a few asks based on this week’s check-ins:

1) AI tooling – candid feedback (early read)
	•	MRM AI Assistant (tone & format): Summaries skew too “adjectival.” We’ll tighten prompts to enforce factual tone and fixed bullet counts (e.g., 3–4 bullets).
	•	Plugins UX: Validators prefer plugins default OFF so they can start in general chat and opt-in per task.
	•	Governance-Check AI: Useful for batch doc scans, but not live/UAT; currently run locally by Bo for batch use. We’ll track readiness before wider use.
	•	Usage & efficiency logging: The “time-saved” spreadsheet has low adoption (many zeros/unused). Team feedback suggests clearer comms and expectations would help.

Asks:
	•	Are you supportive of (a) default-OFF plugins and (b) a short guidance note from you to reinforce logging of efficiency/time-saved? I can draft the note for your review.

2) Surveillance AI
	•	Recommend including a brief update for Brian and in the CO update. I’ll prepare a crisp paragraph unless you’d like a slide instead.

3) PRC cadence change (FYI)
	•	PRC moving from 6 to 8 meetings next year, with requests for updates from each risk stripe per meeting → net increase in our update workload.
	•	We’re engaging with Ross’s team to see where supplementary info can be streamlined (e.g., quarterly cadence for certain metrics).

Asks:
	•	Any guidance on where to push hardest on burden reduction before we revert to Ross’s team?

4) Near-term follow-ups
	•	EIA/UI preliminary findings: I’ll coordinate with George for a summary.
	•	IMM exam: Awaiting update from Sandra.
	•	AI feedback summary: Phil and I will send you a one-pager by Monday covering: what we’re tracking, early sentiment, concrete examples, and adoption hurdles.

Happy to adjust any of the above—please let me know preferences (e.g., plugin default stance, comms tone, slide vs. paragraph for Surveillance AI).

Thanks,
Yibo

CC: Phil, Bo, (add others as needed)

⸻

Want me to tailor this for a senior-leadership tone (even tighter, with a 5-line executive summary at the top), or draft the “time-saved logging” note in your voice for Bill to send?



Here’s a concise draft you can paste into Outlook/Gmail:

⸻

Subject: Updates & asks: AI tooling feedback, surveillance AI, and PRC cadence change

Hi Bill,

Quick heads-up and a few asks based on this week’s check-ins:

1) AI tooling – candid feedback (early read)
	•	MRM AI Assistant (tone & format): Summaries skew too “adjectival.” We’ll tighten prompts to enforce factual tone and fixed bullet counts (e.g., 3–4 bullets).
	•	Plugins UX: Validators prefer plugins default OFF so they can start in general chat and opt-in per task.
	•	Governance-Check AI: Useful for batch doc scans, but not live/UAT; currently run locally by Bo for batch use. We’ll track readiness before wider use.
	•	Usage & efficiency logging: The “time-saved” spreadsheet has low adoption (many zeros/unused). Team feedback suggests clearer comms and expectations would help.

Asks:
	•	Are you supportive of (a) default-OFF plugins and (b) a short guidance note from you to reinforce logging of efficiency/time-saved? I can draft the note for your review.

2) Surveillance AI
	•	Recommend including a brief update for Brian and in the CO update. I’ll prepare a crisp paragraph unless you’d like a slide instead.

3) PRC cadence change (FYI)
	•	PRC moving from 6 to 8 meetings next year, with requests for updates from each risk stripe per meeting → net increase in our update workload.
	•	We’re engaging with Ross’s team to see where supplementary info can be streamlined (e.g., quarterly cadence for certain metrics).

Asks:
	•	Any guidance on where to push hardest on burden reduction before we revert to Ross’s team?

4) Near-term follow-ups
	•	EIA/UI preliminary findings: I’ll coordinate with George for a summary.
	•	IMM exam: Awaiting update from Sandra.
	•	AI feedback summary: Phil and I will send you a one-pager by Monday covering: what we’re tracking, early sentiment, concrete examples, and adoption hurdles.

Happy to adjust any of the above—please let me know preferences (e.g., plugin default stance, comms tone, slide vs. paragraph for Surveillance AI).

Thanks,
Yibo

CC: Phil, Bo, (add others as needed)

⸻

Want me to tailor this for a senior-leadership tone (even tighter, with a 5-line executive summary at the top), or draft the “time-saved logging” note in your voice for Bill to send?





Got it — thanks for clarifying. You meant the posting email to Bill about the PRC/BRC cadence change (last part of the transcript). Here’s a clean draft you can send:

⸻

Subject: Heads-up: PRC/BRC cadence change for 2026

Hi Bill,

Quick FYI on the committee schedule:
	•	PRC cadence will increase from 6 to 8 meetings per year starting next year. Each meeting will now request updates from every risk stripe, which means our team’s updates will also increase from ~6 to 8 times annually.
	•	BRC remains on the annual review cycle (December). As part of that session, the MCP change will be included for review.

We are engaging with Ross’s team to explore ways to reduce the incremental burden (e.g., moving certain supplementary metrics to a quarterly cadence). Will keep you posted once we have confirmation.

Let me know if you’d like me to prepare a short slide for MRCC/FRAC to note this change explicitly.

Thanks,
Yibo

⸻

Do you want me to also prepare a 1-liner “executive summary” version that you can use if Bill wants to forward this directly to senior leadership?



Here’s a cleaner, streamlined version of your text:

MRM identified issues during revalidation of the TRY cross-currency zero-coupon Bermudan cancellable swaps model for the LDN New Markets desk.
• Problems included incorrect mean reversion, skew calibration, and calibration instruments, with a total impact of -$2.8mm; the first two have been remediated, while the calibration instruments issue is tracked as a validation finding.
• Review confirmed no material impact on other desks, though analysis is being extended to ensure full coverage.

Do you want me to also create a one-sentence exec summary version of this for quick updates?

Here’s a simplified bullet-point version of your text:
	•	Scope: MRM revalidated the pricing model for TRY xccy zero-coupon Bermudan cancellable swaps (LDN New Markets). Found modelling issues and built improved benchmark model.
	•	Total impact: -$2.8mm, broken down as:
	•	Incorrect Mean Reversion (-1.3mm): Default MR of ~7% used instead of 1%, overstating optionality value.
	•	Inaccurate skew calibration (-0.3mm): CorrRatio mis-marked at -1.1 vs correct -0.1, causing unstable skew calibration.
	•	Inaccurate calibration instruments (-1.2mm): Approximate LGM calibration replaced with near-exact approach; steep TRY curve makes impact large.
	•	Remediation:
	•	First two issues fixed, offset by reserve release from Controllers.
	•	Last issue needs modelling enhancements → raised as a finding.
	•	Impact across desks:
	•	No other desks affected by mean reversion issue.
	•	Other issues exist in desks trading zero Berms on LGM, but smaller impact (lower accretion rates than TRY).
	•	MRM extending analysis to those desks.

Do you want me to make this even shorter (2–3 lines) for quick talking points, or keep this level of detail?


Here’s a detailed structured summary of the updates (framed so you can take them to Brian tomorrow at 9am). I’ve organized them into clear sections, with bullets under each for ease of use:

⸻

1. Brian Meeting – Key Notes to Raise
	•	Due dates / Deliverables
	•	IRR proposal due mid-September → artifact is presentation to MRCC, not full implementation.
	•	Implementation with divisions will run through November.
	•	AU Applicability / Formula
	•	Need Brian’s alignment on AU applicability scoping (strapped vs non-strapped AUs).
	•	Proposal: show examples (GBM, Public Shared Services) → highlight controls (5-control strapped vs minimal control non-strapped).
	•	Include rough counts for context.
	•	Traceability Effort
	•	Regulators are mapping regulatory guidance → policies → AUs/risks/controls.
	•	Issues: CCR rules (e.g. SR 11-10) bring prescriptive requirements not always in templates (e.g. counterparty backtesting).
	•	Clarify whether model obligations are explicitly in scope.

⸻

2. Regulatory Engagements
	•	ECB / IM Exam
	•	Onsite kicked off this week (Frankfurt → Warsaw → London).
	•	Need Sandra’s latest readout from recent ECB conversations.
	•	Concerning feedback: ECB suggests “inventory of non-modeled risks” (risks excluded from capital). → Feels like risk ID vs model inventory. Pushback needed.
	•	MIA Capital Proposal
	•	Simon proposing DRC-like framework for “holes.”
	•	Split views: Leslie supportive, Gopi strongly opposed, Monique neutral.
	•	Worth raising with Brian – outcome will affect broader capital treatment.
	•	EY / Exam Status
	•	No recent noise; possibly due to summer schedules.
	•	ACL MRIA
	•	Examiner meeting today canceled; they indicated they have all materials needed.
	•	Likely next step = soft close and final confirmation.
	•	Other Exams
	•	Fed data controls exam: focus is on inputs rather than model logic.
	•	Example: country code assignment in ETL.
	•	MRM clarified: tested independently, prior finding closed (thresholds).
	•	Compliance Eng. described UAT testing; regulators probing sufficiency of controls.

⸻

3. AI / Model Governance
	•	AI Intake Form
	•	Targeting end-September.
	•	Streamlining: merge “streamlined” + AISG forms → new two-tier form:
	•	Stop at simple “No” answers.
	•	If “Yes,” full form required.
	•	Trimming duplicative RM/MRM questions.
	•	Still Word format → tooling digitization TBD (ModelIT not guaranteed).
	•	Governance Enhancements
	•	Alexis presenting Thursday.
	•	Roles/responsibilities unclear; Brian should be briefed.
	•	AI Project Mapping (Bo / Schley / Alley)
	•	Mapping AI projects to business processes + headcount to measure impact.
	•	Idea: link AI initiatives to risk/control processes and scale of people impacted.
	•	Risk overlay concept still fuzzy. Need Brian’s steer.
	•	Other AI Updates
	•	Guardrail model approved last week.
	•	Loans AI largely wrapped up.
	•	KPI work: Bo pulled validated models’ metadata (thresholds, KPIs) → can aggregate for comparability.

⸻

4. Other Risk / Model Updates
	•	Market Risk Metrics
	•	Limit changes scheduled to go live Oct 1 (FAC approval Sept 16).
	•	Daily calculations; comms should start now in weekly/strat updates.
	•	Validation Activities
	•	GBM validation in London: Turkey bonds model → identified issues, material PnL ($3m).
	•	Not formally in “offs,” but still material – highlight to Brian.
	•	72 Findings
	•	Targeting October 23 closeout.
	•	Market Risk carefully tracking; GBM/risk still exposed.

⸻

5. Action Items Before Brian
	•	Align with Sandra for ECB / IM exam feedback.
	•	Confirm with Simon details on MIA capital proposal.
	•	Get from Bo the latest KPI mapping + AI process linkage work.
	•	Review Alexis’ Thursday AI governance draft.
	•	Finalize IRR AU applicability examples (strapped vs non-strapped) → bring to Brian.
	•	Prep comms on Oct 1 market risk limit changes.
	•	Flag material GBM validation issue (Turkey bonds) for transparency.

⸻

✅ This way, tomorrow you’ll have:
	1.	A clear structure for Brian (regulators → AI governance → model/risk updates).
	2.	Talking points on contentious items (ECB inventory, MIA capital, AU applicability).
	3.	Action items to chase before the meeting.

Do you want me to also draft a one-page “Brian prep note” in bullet format that you could paste directly into an email?



Got it — here’s a tighter 3-bullet version:
	•	Aug 21: MRM call with Fed on ETL country-code logic, $1k filter threshold, and rule replicability; MRM clarified these as standard or FCC-driven, with validation support.
	•	Fed requested details on independent validation of critical data inputs; MRM cited a remediated 2023 data-quality finding, with Compliance/FCC noting first-line testing.
	•	Response provided to Fed on Aug 25.



345. Reverse Vowels of a String
Easy
Topics
premium lock icon
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """


151. Reverse Words in a String
Medium
Topics
premium lock icon
Companies
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """


238. Product of Array Except Self
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


























1071. Greatest Common Divisor of Strings
Easy
Topics
premium lock icon
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

1431. Kids With the Greatest Number of Candies
Easy
Topics
premium lock icon
Companies
Hint
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """


605. Can Place Flowers
Easy
Topics
premium lock icon
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """










Here’s a clearer and more concise rewrite of your section, with the 4 changes simplified:

⸻

SPG to CREST UBM Migration
We have approved the following enhancements to the SPG to CREST UBM Migration:
	•	Eq Delta methodology: Replaced CREST Delta Liquidation with SPIRE V30 Eq Delta functional form, reducing WCL by $1.5Bn.
	•	Currency scenarios: Removed CNO/CNH/CNY and SGD from de-pegging scenario and recalibrated shocks, reducing WCL by $845MM (aligned with prior FX Benchmark Model change).
	•	USD Forwards: Redirected to IR stress (instead of default EQ charge), reducing WCL by $645MM.
	•	MPS swaps: Corrected treatment of swap underliers to prevent default CREST charge, reducing WCL by $240MM.

⸻

Would you like me to condense this further into just a headline + one-liner per change (e.g., 4 short bullets only with action + impact)?



Here’s a cleaner, simplified version:

⸻

Approvals of New Execution Algos
We have approved the TargetClose and Canada Trailblazer Algos within the Atlas Execution Algorithms (Tier 2) and Atlas SOR (Tier 2).
	•	TargetClose Algo: A schedule-based strategy designed to trade into the market close, aiming to minimize slippage by executing near the auction while trading earlier if needed to limit market impact.
	•	Canada Trailblazer Algo: A hidden liquidity-seeking strategy (mirroring the US SOR version) that searches dark and gray pools to maximize fill rates while minimizing market impact.

During validation, MRM raised a Sev2 finding requiring regular recalibration of Transaction Cost Model (TCM) coefficients.

⸻

Do you want me to make it even shorter, like 2–3 bullets only?



•	MRM validated and approved the SVT Quoting (ID 25381) and SVT Volatility (ID 26432) Tier 2 models, resolving the prior waiver.
	•	SVT Quoting generates bid/offer quotes for American warrants via Halo Streaming, using adjusted volatility surfaces from SVT Volatility for market making, including out-of-hours quoting.



•	MRM validated and approved enhancements to EqSp Koala and EqSp YMCA models (Tier 1) to support Project Solaris, a reinsurance agreement with a Japanese insurer on a new VA product.
	•	FX hedge is booked in EqSp YMCA, while the GMAB hedge and swap hedge on SPV notes are booked in EqSp Koala.
	•	Both models are used for pricing, risk management, and stress testing of the hedges and swap related to the reinsurance agreement.


Here’s a cleaned-up, detailed summary of the transcript you shared:

⸻

Review of RC Draft Responses
	•	Managers are reviewing RC responses; each section already has an assigned reviewer:
	•	CCR – Bo / Natalia
	•	LRM – R
	•	MRA – Reviewed
	•	Market Risk – David (with Marcus’s input)
	•	Last section – S
	•	Procedure: Bill’s approval is required before sending to the Fed.
	•	If no major issues, Bill can be sent the reviewed package now instead of waiting until the 21st.
	•	Messaging to Bill should note that all relevant managers have reviewed and ask if he wants any changes before submission.

⸻

Items for STR Meeting (During Out-of-Office)
	•	MRA Remediation – Keep at the top of updates.
	•	Secar Feedback – Mention to the Fed without revealing detailed action plans; note that a targeted plan will be submitted for that model.
	•	RCSA – Include remaining 2025 tasks.
	•	Policy Uplift – Not critical to highlight.
	•	GBM Q2 Results – Include results excluding CCR models; send to Bill now for potential inclusion in STRAP partner meeting.
	•	AI Section – Add any incremental updates.
	•	Worth flagging Devon (E-Trading AI) to the Fed as they would be interested.
	•	ESG/EG model items – optional, depending on Bill’s preference.
	•	AI App Approval Task Force – include, along with AI efficiency task force updates.
	•	E-Trading OpRisk Event – Likely to be included; flag to Bill to confirm.
	•	AI Model KPI Performance – Already covered under AI task force.
	•	Residual Risk Rating – No strong need to re-calculate for results without IDR models; let Bill decide.

⸻

Monday P&L Call Prep
	•	Mention that the ACL meeting has concluded (with follow-up meeting on Aug 26).
	•	Fed is focusing heavily on handling of past-due findings — worth making the group aware.
	•	ECB SERP finding – to be mentioned; also IMM status (check with Cassandra).
	•	New MRM AI Assistant applications in EC and ANR – mention to the group.
	•	CR Feedback – note that a project plan is being prepared.
	•	FRB follow-up – to be included in the discussion.

⸻

Other Notes
	•	No major additional items to include beyond regular updates.
	•	CSG AI (public and private) impressed GBM; may be worth adding.
	•	For ETSC metrics, remove the first two tables — all relevant data is already in the third table.
	•	Bill will be sent RCSA results and asked if he wants them included for RAT updates.

⸻

If you’d like, I can also turn this into a condensed bullet-only “ready-to-send” version for your internal minutes so it’s easier to drop into your tracking doc. Would you like me to prepare that?



https://click.mail.cfainstitute.org/?qs=f0565be3c13e00d25eb5054550c449e43b74dce2552a2a5c18e799b4cecb5d89ed4971f331177b4bc9edb8204a2f4f532359bf59a5445633

ECB IMM Onsite Exam – Starts Aug 25, runs until Nov, covering Frankfurt, Warsaw, and London.
	•	Preparation: 48 pre-exam requests submitted Aug 8, including model and validation documentation; 13 meetings set in first two weeks, with a dedicated validation session.
	•	Focus Areas: Model changes from prior ECB inspection remediation and topics with limited previous coverage.


Here’s the simplified summary with the proposal and next steps included:
	•	Overview – Bermuda-based GS reinsurance entity with formal governance (Board, council, underwriting panel) and regular cross-divisional updates.
	•	Portfolio – $8bn across 11 deals with Japanese insurers:
	•	VA – market risk hedged, keeps mortality/lapse risk.
	•	FIA – reinsurance on STS-linked option upside.
	•	Composite VA – hybrid of VA and FIA (1 active deal).
	•	Risk – Most market risk passed to GSI; small residual (~$50k VaR). Mortality/lapse risk unhedged but monitored; not yet in VaR or credit models.
	•	Credit – ~$192mm exposure to 2 IG Japanese insurers, collateralized; trades count toward ~$170mm RWA.
	•	Proposal & Next Steps – Seeking NAC approval (Aug 6) for Project Vista, a Hong Kong deal using Value in Force (VIF) monetization—a pre-paid derivative linked partly to lapse risk. Originally planned as a broader HK/Singapore rollout, now narrowed to one transaction for approval. Market and Credit Risk teams are setting new mortality/lapse limits and developing models to capture these risks before further expansion.


Here’s a simpler 4–5 bullet version:
	•	Overview – Bermuda-based GS reinsurance entity with formal governance (Board, council, underwriting panel) and regular cross-divisional updates.
	•	Portfolio – $8bn across 11 deals with Japanese insurers:
	•	VA – market risk hedged, keeps mortality/lapse risk.
	•	FIA – reinsurance on STS-linked option upside.
	•	Composite VA – hybrid of VA and FIA (1 active deal).
	•	Risk – Most market risk passed to GSI; small residual (~$50k VaR). Mortality/lapse risk unhedged but monitored; not yet in VaR or credit models.
	•	Credit – ~$192mm exposure to 2 IG Japanese insurers, collateralized; trades count toward ~$170mm RWA.
	•	Expansion – Seeking approval for HK deal (Project Vista, VIF monetization). Broader HK/Singapore expansion under review; would raise mortality/lapse risk, so new limits and modelling are in progress.

Here’s a simplified bullet version:
	•	ECB IMM onsite exam starts 25 Aug, runs until Nov, covering FFT, WSW, and LDN.
	•	48 pre-exam requests sent 8 Aug (includes model and validation docs).
	•	13 meetings in first two weeks, including a validation session.
	•	Focus on changes from previous inspection remediation and areas with limited prior coverage.
	•	ECB SREP feedback: draft letter includes finding on model inventory completeness; 4-week response period.
	•	While policy/governance is strong, execution gaps remain in some divisions.
	•	Finding relates to models not in inventory until ECB flagged them, meaning no independent review occurred.
	•	Examples: previously remediated AVA declaration gaps, and cases where risks were not quantified or capital was not taken (latter not considered an inventory gap under policy).

Here’s your simplified short bullet version:
	•	ECB IMM Onsite Exam
	•	Kick-off: 25 Aug → runs until Nov; covers FFT, WSW, and LDN.
	•	48 pre-exam requests submitted (8 Aug), incl. model/validation docs.
	•	13 meetings in first two weeks; one dedicated to validation.
	•	Focus: remediation of past ECB findings + topics with limited prior coverage.
	•	ECB SREP Feedback
	•	Draft SREP letter includes finding on model inventory completeness; 4-week response window.
	•	Policy/governance is robust, but execution by Divisions may need improvement.
	•	Finding triggered by:
	•	Models not in inventory until ECB feedback.
	•	Remediated AVA declaration gaps.
	•	Risks without quantification/capital (not considered inventory gaps per policy).


Here’s a much simpler version of your text:

⸻

E-Trading Oprisk Event – $1.2m Loss in US Rates (7/28/2025)
	•	The Rates Central Risk Book (CRB) recently began internalizing hedge orders from IRP desks to lower costs, trading only residual risk on the exchange.
	•	On July 28, a pilot linked CRB to the Optex auto-hedging algorithm to offset risks between the two. CRB relied on Heracles system data to track net risk.
	•	A 15-second data delay in Heracles meant Optex’s risk reduction wasn’t shown in time, causing CRB to trade the same risk again.
	•	Within 7 seconds, traders noticed a spike and used the kill switch. By then, CRB had traded 106 times (~1.5m/bps DV01), leading to a $1.2m loss.
	•	The CRB–Optex link was cut. CRB will resume its original standalone flow, with tighter exposure controls to be validated by ETSC, which is also reviewing all CRB control parameters.

⸻

If you want, I can also make a one-sentence “headline” version for a report. That would make it even sharper.

Here’s a much shorter, simpler version of your text:

⸻

E-Trading Oprisk Event – $1.2m Loss in US Rates (7/28/2025)
	•	A pilot trade linked the Rates Central Risk Book (CRB) hedger with the Optex auto-hedging algo to net interest rate risk.
	•	Due to a 15-second delay in the Heracles risk update, CRB Hedger repeatedly traded the same risk, executing 106 times and building an excessive position.
	•	Traders stopped the algo within 7 seconds, but closing the position caused a $1.2m loss.
	•	Connection between CRB and Optex was removed. Additional exposure controls will be added and validated before any future integration.

⸻

If you want, I can also make a one-sentence ultra-condensed version for quick slide updates.



Here’s a detailed summary of the transcript with emphasis on what to draft/include for Brian’s updates:

⸻

Key Topics Covered

1. MRA / Remediation Updates
	•	Training will be completed after tomorrow.
	•	Tech enhancements for MRMT are progressing, nearing UAT phase.
	•	Incremental CR feedback received from last week’s Fed meeting to be incorporated.
	•	Plan to show Brian a draft modified remediation plan that reflects this feedback.
	•	Timeline: Aim to implement annual monitoring enhancements by Nov 1, review by year-end (aligned with SECARD timelines).

Include for Brian:
	•	Status of training completion.
	•	UAT readiness for tech enhancements.
	•	Fed feedback incorporated into remediation plan (show draft).
	•	Target dates for implementation/review.

⸻

2. EMF Uplift – Open Issues
	•	Inherent risk rating formula still WIP; tied to OpRisk’s reconsideration of excluding divisions based on materiality.
	•	Two separate scoping questions:
	1.	Which divisions/AUs can be excluded entirely.
	2.	Within included AUs, which processes can be excluded.
	•	Internal Audit’s role unclear; OpRisk may be revising approach.
	•	Processes and controls now aligned with MRM AUs, but scoping still unsettled.
	•	Plan to get latest from OpRisk in tomorrow’s touchpoint.

Include for Brian:
	•	Clarify two separate scoping decisions.
	•	Flag that OpRisk is rethinking criteria; Internal Audit involvement unclear.
	•	Note dependencies for inherent risk formula completion.

⸻

3. AI / GenAI Validation and Controls
	•	26 GenAI model validations completed (Tier 1–3).
	•	Grouped by function (e.g., summarization, extraction).
	•	Capture KPIs, thresholds; note that some models have multiple KPIs.
	•	Highlight big-ticket items: CGI model, Devin.
	•	Related RCSA work for AI controls follows same timeline as model controls.
	•	Additional AI initiatives:
	•	W Pager plug-in and ETSC tools for ANI writeups.
	•	Early testing of agentic AI for committee material gathering.
	•	Interest from other divisions (OpRisk, Ross’s group) to replicate MRM AI setup — MRM will provide templates but not build or staff their work.
	•	AISG policy change expected in September; current API access still gated via RSD.

Include for Brian:
	•	Summary of 26 validations, grouped by category, with KPI/threshold status.
	•	Key models (CGI, Devin) and ongoing RCSA/controls work.
	•	New tools/pilots (W Pager, agentic AI).
	•	Divisional interest in replication; MRM role limited to template/advice.
	•	AISG process changes and current API approval requirements.

⸻

4. Policy & Governance Issues
	•	EY Europe “change notification” misunderstanding — now clarified that MRM not part of the process.
	•	Internal confusion on policy linkages and ownership — risk of divisions writing MRM requirements without MRM involvement.
	•	Example: ILST tracker policy derived from incorrect sources; guidance given to list as “related policies” instead.
	•	Need for training across division on how to read and link policies correctly.
	•	Possible role for divisional risk governance group (RPOG) to enforce linkage/approval rules.

Include for Brian:
	•	Awareness item: policy linkage confusion persists, risk of MRM requirements being added without review.
	•	Recommendation: divisional training on policy linkage/approval.

⸻

5. CCR & Regulatory Updates
	•	Current ACL and TxB exams ongoing.
	•	Participation in CCR and trading quarterly meetings.
	•	Mention CCR validation updates in CO report.

⸻

6. Market Model Topics for Awareness
	•	Central risk book in ALCO — unclear if model involved; recent operational event shut it down.
	•	Equity buyback model switching from GAXA to Constant model.
	•	Suggest MRM track modeling developments across all asset classes (commodities, rates, FX, derivatives, cash, GSS).
	•	Arrow project — possible business opportunity; Brian’s perspective may be useful.

Include for Brian:
	•	Flag central risk book issue and equity buyback model change.
	•	Propose systematic tracking of modeling developments by asset class.
	•	Arrow project awareness.

⸻

7. Draft CO Update Content (to show Brian)
	•	MRA remediation status (training, tech enhancements, Fed feedback).
	•	AI updates (validations, controls, new tools, key models).
	•	CCR validation updates.
	•	ACL MRIA/MRA progress.

⸻

✅ If you want, I can also draft the actual Brian’s update talking points from this, in a concise, presentation-ready format so you can drop them into your meeting notes or slides. This would make it much easier for him to hit all points without wading through detail.

Do you want me to prepare that next?



Here’s a cleaned-up, more concise version while keeping the meaning intact:

⸻

Notable recent approvals for CCR model enhancements include:
	•	Updated shortfall calculation for SPG on the Unified Benchmark Model (UBM), following the migration earlier this year, improving model consistency across business lines and reducing total worst-case loss (WL) by $3.2Bn.
	•	Implementation of collateral stress monitoring for WL and shortfall calculations in DCS and Futures, approved in April, replacing the prior counterparty shortfall limit framework.
	•	These changes deliver more robust benchmark stress loss/shortfall metrics, mitigate wrong-way risk, and address regulators’ prior inquiries on including collateral in stress testing.

⸻

If you want, I can also make it even tighter and more “regulatory-update style” so it’s easier to drop into a meeting minutes or a deck.



Here’s a tightened, clearer rewrite of your text while keeping all details intact:

⸻

Artificial Intelligence
	•	GBM Private Tier 1 Loan Classification Models – Validation nearing completion for generative AI models classifying ~3,000 corporate loan back book records as liquidity or credit.
	•	Findings – Two high-severity issues identified and remediated:
	1.	Accuracy below target and inconsistent performance between seen/unseen samples.
	2.	High output fragility.
Both were addressed through model enhancements and have been closed.
	•	AI Risk & Controls Committee (AIRCC) – [TBU for Devin update after tomorrow’s meeting].
	•	Recent Approvals – Integration of Doc AI into the Tier 1 ESG AI model for extracting ESG data from public company disclosures.
	•	Enhancement improves handling of tables, numerical data, and complex layouts, and incorporates the latest LLM capabilities.

ERMF Integration – [TBU]

⸻

Regulatory Updates
	•	Allowance for Credit Loss MRIA 1 & MRA 2 – Scheduled meetings concluded this week [TBU for final outcome].
	•	Validation focus areas: independent analyses for CRE, ASL, and Apple Card; model uncertainty evaluation; QRF validation approach; and validation findings, including overdue finding extensions.

⸻

If you’d like, I can also make a more concise “headlines-only” version so it fits into a compact meeting deck without losing impact. That would make it feel cleaner for an executive audience. Would you like me to prepare that?



Certainly — here is a bullet-point summary of the positional stress test discussion:

⸻

Positional Stress Test – Swap Spread vs. Bond Basis
	•	Caleb asked for clarification on the new stress test capturing basis risk between Treasuries, swaps, and bond futures, and whether it aligns with Market Risk’s “deleveraging stress scenario.”
	•	David explained:
	•	The test was developed for the NY rates trading portfolio, which held long Treasuries hedged with short bond futures and receiver swaps.
	•	Previously, exposure was monitored using a simple DVO1-based metric, which didn’t fully capture basis risk.
	•	The new test uses historical stress scenarios to simulate losses based on:
	•	OAS spreads on Treasuries,
	•	Net basis on bond futures (CTD),
	•	And swap spreads.
	•	Positions across bonds, swaps, and futures are treated as a commingled exposure.
	•	Bond-specific time series (e.g., on-the-run vs. off-the-run) are used to increase precision.
	•	Caroline noted the team will confirm whether the model is internally referred to as the “deleveraging stress scenario.”

⸻

Let me know if you’d like all these bullet summaries compiled into a single meeting recap.


Certainly — here is a bullet-point summary of the MRA remediation discussion from the end of the Q2 2025 meeting:

⸻

MRA Remediation – Summary of Discussion
	•	Makaylah asked for an update on remediation progress and whether CCAR feedback (Apple Card model’s ongoing monitoring) would be incorporated.
	•	Caroline explained:
	•	Phases 1.1 and 1.2 (enhanced templates and standards) were completed and approved by MRCC.
	•	Phases 1.3 and 1.4 (workflow tool updates and validator training) are underway.
	•	Enhanced annual reviews will begin in Q4 2025, with all due reviews completed by mid-December.
	•	Makaylah emphasized:
	•	CCAR feedback must be formally addressed in the MRA remediation.
	•	This will be a key focus during the Fed’s Remediation Validation Examination (RVE).
	•	Caroline confirmed:
	•	Internal discussions are ongoing to determine how to incorporate the CCAR feedback.
	•	The firm will follow up with the Fed once the approach is finalized.
	•	Makaylah noted she will discuss the firm’s remediation materials with David Palmer and others and will provide feedback.
	•	She offered to invite David to the next quarterly meeting and encouraged the firm to send any questions in advance.

⸻

Let me know if you’d like a version combining this with other section summaries.


Certainly — here is the expanded version of the positional stress test discussion, incorporating more detail while keeping the Q&A format consistent:

⸻

10. Positional Stress Test for Swap Spread vs. Bond Basis

Caleb asked for clarification on the new positional stress test covering swap spread vs. bond basis risk. He sought to understand what the model measures, how it differentiates from existing approaches, and whether it aligns with what Market Risk refers to as a “deleveraging stress scenario.”

David explained that the new stress test was developed by Market Risk in response to observed concentrations in the New York rates trading portfolio, where the desk was:
	•	Long U.S. Treasuries
	•	Hedging with short bond futures and receiver swaps

Previously, the desk was monitored using a simple DVO1-based stress, which compared the size of bond futures positions against the underlying treasury positions. However, this did not capture the full basis risk between:
	•	Treasuries and futures (CTD basis)
	•	Treasuries and swaps (swap spread risk)

The new stress test includes:
	•	OAS spreads on the Treasury securities
	•	Net basis on the cheapest-to-deliver (CTD) bond futures
	•	Historical stress scenarios that simulate joint movements in these metrics

The stress test uses percentile-based historical losses (e.g., 95th percentile) rather than static sensitivities, making it more risk-sensitive and reflective of historical co-movements.

Caleb followed up to ask how the swap spread component was modeled and whether the different hedging instruments were commingled.

David confirmed that:
	•	The swap spread component is captured through changes in the OAS of the bond (i.e., the difference between the bond yield and discount curve derived from swaps).
	•	The overall position — combining Treasuries, futures, and swaps — is modeled as a commingled exposure, with risk captured through co-movements in those spread relationships.
	•	Time series are bond-specific, accounting for on-the-run/off-the-run status, and adjusted accordingly.

David noted that this test helps better capture basis risk across instruments and replaces simplistic metrics with a robust stress-driven approach.

Caroline added that the team would follow up to confirm whether this model is referred to internally as the “deleveraging stress scenario.”

⸻

Let me know if you’d like this paragraph dropped into the full minutes document or exported in a preferred format.



Absolutely — here is the revised Q2 2025 Fed Meeting Minutes, written exclusively in Q&A format, using “Makaylah asked/inquired” and “Caroline explained” (or other names where appropriate). The content remains detailed and structured around the key discussions.

⸻

Meeting Minutes: Q2 2025 Quarterly MRM Meeting with FRB – August 5, 2025

On August 5, 2025, the firm hosted the Q2 2025 Quarterly Model Risk Management (MRM) meeting with the Federal Reserve Board (FRB). The meeting covered supervisory feedback, validation activity, internal audit findings, RAS exceptions, AI/ML model usage, and MRA remediation progress. Below summarizes the FRB’s questions and the firm’s responses.

⸻

1. CCAR Feedback on Ongoing Monitoring and MRA Remediation

Makaylah asked how the firm plans to incorporate CCAR feedback on ongoing monitoring, particularly related to the Apple Card loss forecasting model, into its MRA remediation efforts.

Caroline explained that the feedback was received only the prior Friday, and internal discussions are ongoing. The firm expects to address the Apple Card feedback in addition to the existing MRA remediation plan, and will provide further updates once internal alignment is reached.

⸻

2. Internal Audit Finding and Validator Training

Makaylah inquired about a recently closed internal audit finding related to comprehensiveness of validation documentation, and asked for details on the training conducted for validators, including whether ongoing monitoring was covered.

Caroline explained that the finding was low severity and focused on validation documentation—not monitoring effectiveness itself. The training emphasized:
	•	The importance of clearly documenting how validators assess developer monitoring plans.
	•	Ensuring validation documents remain up to date through model changes and annual reviews.
	•	Comprehensive coverage of assumptions, limitations, and monitoring assessments.

Oliver added that the training was delivered as live sessions and completed across the validator group.

⸻

3. Revalidations and Additional Validation

Makaylah asked whether any of the 13 revalidations were triggered by performance or monitoring issues and requested clarification on “additional validation.”

Caroline explained that the 13 revalidations were triggered by annual review outcomes—not by performance concerns. Additional validation refers to targeted reviews of specific model aspects (e.g., monitoring or a key assumption) rather than a full revalidation.

She noted that the team would follow up with more detail on themes across the 13 revalidations.

⸻

4. RAS Thresholds and Aged Findings

Makaylah asked how often the firm revisits RAS thresholds and how the aged Tier 1 findings are being addressed.

Caroline explained that thresholds are revisited annually. Following the 2018 model uplift, thresholds were gradually tightened to reflect a steady-state framework. The remaining breach relates to Tier 1 counterparty credit risk models within GBM, which are actively being remediated.

⸻

5. AI/ML Inventory and Usage

Makaylah inquired about the firm’s current usage of AI/ML models and requested ongoing quarterly updates on AI inventory in light of broader topical reviews at the Fed.

Caroline explained that AI/ML models remain concentrated in lower tiers, with only a small number of Tier 1 models such as Guardrails. AI platforms (e.g., underlying LLMs) are included in inventory but are validated only in the context of specific use cases.

She confirmed that AI/ML inventory updates will be included in future quarterly meetings.

⸻

6. Validation Findings for Guardrails Model

Makaylah asked whether the Guardrails model update referenced in the deck was intended to remediate validation findings.

David explained that validation had identified the model’s inability to detect issues embedded in the middle of long prompts. The enhancement improved detection across full input texts and addressed the finding. The model is not used for model validation purposes.

⸻

7. FX Algo Model Usage

Caleb asked whether the FX algo model is currently used in production, what markets it applies to, and how bid/offer spreads are adjusted.

David explained that the model is used in cash FX trading, specifically G10 currencies, within the firm’s automated market-making system. It predicts next-tick price direction to guide quoting. Follow-up will be provided regarding execution venues and trading specifics.

⸻

8. Credit Contagion and CCR Model Enhancements

Makaylah and Caleb asked for more detail on the new CCR models and how exposure to un-margined counterparties is tracked.

David explained that:
	•	The enhanced Credit Contagion Model now allows for:
	•	Multiple collaterals per trade.
	•	Default-driven price jumps to better capture wrong-way risk.
	•	Two new coherent CCR models were developed:
	•	One for margined hedge funds, using symmetric historical VAR scenarios.
	•	One for un-margined counterparties, applying 6-month CCAR stress scenarios.

David confirmed that the firm will follow up with exposure data for un-margined counterparties (e.g., energy clients).

⸻

9. LRM Reclassification and Liquidity Impact

Caleb asked whether enhancements to the Liquid and Readily Marketable (LRM) classification impacted capital or liquidity metrics.

Caroline explained that the enhancements—primarily the reclassification of convertible bonds—reduced RWAs by $6–7B. The impact on liquidity metrics (e.g., HQLA and GCLA) was limited. The team will follow up with specific impacts and any planned refinements to LRM classification.

⸻

10. Positional Stress Test for Swap Spread vs. Bond Basis

Caleb asked for clarification on the new positional stress test that monitors the swap spread vs. bond basis risk, and how basis risk between treasuries, swaps, and futures is captured.

David explained that the new model was designed to replace simple DVO1-based measures. It uses historical stress scenarios to capture movements in:
	•	Bond OAS spreads.
	•	Net basis on bond futures.
	•	Swap spreads embedded in bond leg pricing.

The model addresses concentrations in NY rates trading books, particularly those hedging long treasury positions with futures and swaps. David will confirm whether this aligns with what market risk refers to as the “deleveraging stress scenario.”

⸻

11. Execution Status of MRA Remediation Plan

Makaylah asked for an update on execution of the MRA remediation plan and whether CCAR feedback is being incorporated.

Caroline explained that:
	•	Templates and policy enhancements (Phases 1.1 and 1.2) were approved by MRCC.
	•	Infrastructure enhancements and validator training (Phases 1.3 and 1.4) are in progress.
	•	Execution of enhanced annual reviews will begin in Q4, targeting completion by mid-December.
	•	The CCAR feedback will be addressed as part of the broader remediation plan, and the firm will circle back once a path forward is finalized.

⸻

Let me know if you’d like this saved to Word or PDF format — or if you’d like a version with only the most critical questions summarized.



You’re right — Makaylah did follow up with a question during the Internal Audit Findings section regarding the training conducted for validators. Here’s the updated Section 4: Internal Audit (IA) Finding Status, with a detailed sub-bullet on training in response to her question:

⸻

4. Internal Audit (IA) Finding Status
	•	All IA findings are general or low severity and model-specific rather than thematic.
	•	Two findings remain outstanding, both related to enhancements in validation documentation (no issues with model soundness or monitoring frameworks).
	•	Several findings were closed in Q2, including:
	•	Developer monitoring scope was broadened in response to feedback.
	•	Sensitivity analysis and parameter recalibration were introduced in specific models.
	•	Validation documentation was enhanced to address staleness and completeness concerns.

Makaylah inquired about the training conducted for validators, specifically:
	•	Whether the training addressed the importance of ongoing monitoring, as well as documentation expectations.
	•	Caroline clarified:
	•	The internal audit finding was not about deficiencies in monitoring practices but about how monitoring was documented in validation reports.
	•	The training emphasized:
	•	Clear articulation of how validators assessed the completeness and appropriateness of developers’ ongoing monitoring plans.
	•	Comprehensive documentation of all aspects of validation, including monitoring, assumptions, limitations, and model changes.
	•	Importance of maintaining and updating validation documentation over time — especially during annual reviews or following any model changes.
	•	The training was conducted as live sessions and completed across the validation team.
	•	Makaylah acknowledged the clarification and appreciated the focus on documentation integrity, noting that many of the IA findings were indeed documentation-related.

⸻

Let me know if you’d like me to integrate this directly into the full draft again or export it as a document.



Thank you for sharing the Q2 transcript. Based on the Q1 format and the extensive Q2 discussion, here is a draft of the Q2 2025 Quarterly MRM Meeting Minutes with the FRB, following the same structure:

⸻

Meeting Minutes: Q2 2025 Quarterly MRM Meeting with FRB – August 5, 2025

On August 5, 2025, the firm hosted its Q2 2025 Quarterly Model Risk Management (MRM) meeting with the Federal Reserve Board (FRB). The discussion focused on supervisory feedback received during the 2024 CCAR exam, ongoing MRA remediation efforts, internal audit findings, validation activities, RAS exceptions, AI/ML model developments, and counterparty credit risk model enhancements. Joyce Kim (Regulatory Relations) and Makaylah (FRB) participated in the meeting, which concluded with appreciation for the firm’s transparency and commitment to ongoing improvement.

⸻

Key Discussions:

1. MRA Remediation and Ongoing Monitoring Feedback
	•	Makaylah opened the meeting by referencing CCAR feedback related to the Apple Card loss forecasting model’s ongoing monitoring and asked how this would be incorporated into MRA remediation plans.
	•	Caroline confirmed that internal discussions were underway and that stakeholders would convene to determine how to address the incremental feedback. Additional updates will be shared with the FRB once a remediation plan is finalized.
	•	Makaylah emphasized the importance of incorporating CCAR feedback into MRA remediation, especially ahead of RVE.

2. Internal Audit Findings
	•	Makaylah also flagged a recently closed internal audit finding related to model validation documentation and ongoing monitoring.
	•	Caroline clarified that:
	•	The finding was general/low severity.
	•	The issue was not about weaknesses in ongoing monitoring, but rather comprehensiveness of validation documentation.
	•	MRM responded by conducting live training sessions to reinforce expectations around documentation completeness and maintenance over time.

3. Validation Activities
	•	MRM provided updates on validation findings and trends:
	•	336 findings closed during the period; highest volume in GBM and Risk, in line with their large inventories.
	•	13 models were revalidated based on annual review outcomes, not due to external triggers. MRM will follow up on whether any themes emerged from these revalidations.
	•	Additional validations were explained as targeted deep dives into specific aspects of a model when full revalidation is not warranted.
	•	Qualitative Approaches (QAs) and Deterministic Regulatory Calculations (DRCs) saw an increase in findings due to new developments, primarily across Controllers, Treasury, and Risk.

4. Internal Audit (IA) Finding Status
	•	All IA findings are low severity and model-specific.
	•	Two findings remain outstanding (documentation enhancements only).
	•	Several findings were closed in Q2 following actions such as:
	•	Broadening developer monitoring scope.
	•	Enhancing sensitivity analysis.
	•	Strengthening documentation to reflect ongoing monitoring and model changes.

5. RAS Exceptions and Aged Items
	•	No breaches at the Board or firm-wide risk appetite committee (FRAC) thresholds for models under waiver.
	•	Aged waiver breaches noted in prior quarters have been resolved.
	•	Breach remains for Tier 1 models with aged findings (related to CCR), which are under active remediation.
	•	Makaylah inquired about the frequency of RAS threshold reviews. MRM explained that departments revisit them annually and that thresholds have been ratcheted down over time to reflect a steady state post-2018 uplift.

6. Model Inventory and AI Usage
	•	Model inventory has remained stable overall.
	•	AI/ML model inventory was presented by:
	•	Business unit
	•	Risk tier
	•	GenAI vs. non-GenAI
	•	AI platforms (LLMs used as infrastructure)
	•	AI usage remains concentrated in lower-tier models, with Tier 1 models being exceptions (e.g., Guardrails).
	•	Makaylah acknowledged the utility of the update and asked that AI/ML inventory be included in future meetings.

7. AI/ML Model Developments

Highlighted developments:
	•	FX Algo (Tier 3): Transformer-based neural network model for predicting next-tick FX price movement in auto-quoting. Validated using benchmark models.
	•	Guardrails Model (Tier 1): Enhanced to improve detection of prompt injection and hallucination, particularly for issues embedded mid-text.
	•	AI Web Grounding (Tier 2): New model leveraging vetted web search results to reduce hallucination in chatbot responses.

Clarifications:
	•	Guardrails enhancements addressed validation findings, not used for model validation itself.
	•	Most lower-tier AI models referenced fall under Tier 3 (not Tier 4).

8. Counterparty Credit Risk (CCR) and Other Model Enhancements

Key enhancements:
	•	Credit Contagion Model (CVA): Now supports multiple collaterals and jump-to-default effects for wrong-way risk.
	•	Bermudan Product CVA Modeling: Enhanced for FRTB standard approach and treatment of FVA at default.
	•	Unified CCR Short Form Model (EBM Crest): Standardized across SPG and Equities, enabling combined exposure analysis and improved concentration charge modeling.
	•	New Coherent CCR Models:
	•	One for margined hedge funds (symmetric historical VAR).
	•	One for unmargined counterparties (natural resources) applying CCAR-based 6-month stress scenarios.
	•	LRM Enhancements: Reclassified convertible bonds as LRM, reducing ~$6–7B in RWAs; impact on liquidity metrics (e.g., HQLA) expected to be limited, with follow-up promised.
	•	Swap Spread vs. Bond Basis Risk: New positional stress test introduced to enhance monitoring of hedging imbalances in the NY rates book.

9. MRA Remediation Execution Plan
	•	MRM confirmed:
	•	Phase 1.1 and 1.2 completed (enhanced templates approved by MRCC).
	•	Phase 1.3 (infrastructure uplift) and 1.4 (training) are underway.
	•	Execution of enhanced annual reviews scheduled to begin in Q4 with completion expected by mid-December.
	•	Makaylah reiterated the importance of ensuring CCAR feedback on Apple Card loss forecasting is incorporated.

⸻

Closing and Next Steps:
	•	Makaylah thanked the firm for its transparency and proactive approach.
	•	Caleb and other FRB members will send follow-up questions in writing for firm response.
	•	FRB will review MRA remediation materials with David Palmer and others; feedback to be shared in due course.
	•	Next quarterly meeting expected in Q3. FRB encouraged submission of questions in advance to facilitate participation from senior staff.

⸻

Would you like this version as a Word or PDF document as well?




Great — I’ve reviewed both the Q1 example and your full Q2 transcript.

Here’s a draft of the Q2 2025 Quarterly MRM Meeting Minutes, aligned with the structure, tone, and level of detail used in the Q1 version but adapted to reflect the longer and more substantive Q2 meeting:

⸻

Meeting Minutes: Q2 2025 Quarterly MRM Meeting with FRB – August 5, 2025

MRM hosted the Q2 2025 Quarterly Model Risk Management meeting with the FRB on August 5. The meeting covered updates on MRA remediation efforts, validation findings, RAS exceptions, AI/ML model usage, and model development. Joyce Kim from Regulatory Relations introduced herself as the new engagement lead. Michaela from the FRB requested the meeting begin with updates on ongoing monitoring and its connection to the open MRA.

⸻

Key Discussions:

1. MRA Remediation and Ongoing Monitoring Feedback (Primary Focus)
	•	Michaela requested an update on how the firm plans to incorporate CCAR feedback into the MRA remediation, particularly concerns around ongoing monitoring of the Apple Card projection model.
	•	Caroline acknowledged the feedback was received recently (prior Friday) and is under internal discussion with model developers. Next steps will include a plan to address this incremental feedback.
	•	Caroline confirmed the remediation plan remains on track:
	•	Milestones 1.1 and 1.2 (enhanced templates and MRCC approval) have been completed.
	•	Milestones 1.3 and 1.4 (system enhancements and validator training) are in progress.
	•	Live training sessions for validators have commenced; Q4 annual reviews will be executed under the enhanced framework with completion targeted by mid-December.
	•	Michaela emphasized the importance of addressing CCAR feedback within the remediation to ensure it is trusted during RVE. The Fed expects follow-up once the firm aligns internally on remediation approach.
	•	Caroline confirmed willingness to follow up and noted FRB feedback had already been socialized with the MRCC.
	•	Michaela noted a broader Fed review of the remediation effort was upcoming and that she had circulated Goldman’s deck and templates to David Palmer and others for internal discussion.

⸻

2. Internal Audit (IA) Findings
	•	Caroline clarified that recent IA findings were all low severity and model-specific, with no thematic weaknesses.
	•	Of note:
	•	A general IA finding was issued regarding comprehensiveness of validation documentation (not deficiencies in ongoing monitoring).
	•	This was remediated by conducting live training for all validators focused on documentation practices, including how to assess developer-provided monitoring plans and maintain validation documentation as models evolve.
	•	Several IA findings were closed during the quarter, including:
	•	Expanded developer monitoring requirements following IA feedback.
	•	Enhancements to parameter monitoring and documentation for specific models.
	•	Closure of a finding related to monitoring limitations and uncertainties in a loan settlement risk model, remediated via additional monitoring requirements and parameter recalibration.

⸻

3. Validation Findings
	•	336 findings were closed during the quarter, primarily within Risk and GBM, which hold the largest share of Tier 1 models.
	•	13 models were triggered for revalidation as a result of annual review outcomes; these were not routine cadence revalidations.
	•	Michaela inquired whether any of the revalidations were triggered by specific issues (e.g., ongoing monitoring). Caroline committed to following up with details.
	•	Caroline clarified the distinction between full revalidations and “additional validations” — the latter refers to targeted validation work focused on specific areas, e.g., model performance or monitoring, rather than full-scope revalidations.

⸻

4. RAS Exceptions
	•	Utilization of models under waiver remained low across all tiers, with no breaches of BRC or firm-wide RAS thresholds.
	•	All aged waiver breaches noted in prior meetings have been resolved.
	•	One RAS breach remains outstanding: Tier 1 approved models with aged findings, primarily in the counterparty credit risk area (e.g., margin shortfall calculations).

⸻

5. AI/ML and Generative AI Inventory
	•	AI inventory remains concentrated in lower risk tiers (Tier 3 and 4).
	•	Few Tier 1 models exist; guardrails and ESG AI models were highlighted as examples.
	•	Inventory updates now include “AI platforms” (e.g., underlying LLMs used across multiple applications), which are tracked but not validated standalone.
	•	Michaela requested that this AI inventory breakdown be included in future meetings for ongoing monitoring of AI/ML model usage across the industry.

⸻

6. AI/ML Model Enhancements

David summarized recent developments, including:
	•	FX Algo Model (Tier 1): First deployment of a transformer-based deep learning model to auto-quote FX crosses. Validated using benchmark models and feature attribution analyses. The model outperformed simpler neural networks and demonstrated low hallucination risk.
	•	Guardrails Model Enhancements: Detection performance was improved to address prompt injection vulnerabilities occurring mid-text. Enhancements were in response to initial validation findings.
	•	AI Web Grounding Model (Tier 2): Introduced a model leveraging web search engines to reduce hallucinations in LLM responses by grounding outputs in vetted, real-time sources. Significant reduction in hallucination observed during validation.

⸻

7. Model Inventory
	•	Overall model inventory remained stable. No thematic shifts were observed in newly added or reclassified models.
	•	Inventory of Qualitative Approaches and DRCs also remained steady.

⸻

8. Model Development Highlights

David highlighted several key developments:
	•	Credit Contagion CVA Model: Enhanced to support multiple collaterals and model jump-to-default contagion effects between counterparty and collateral.
	•	FEA Enhancements: Improvements to modeling recovery of FVA at default in bilateral derivatives, especially relevant for corporate counterparties.
	•	Unified Short-Form CCR Model: Adoption of a consolidated benchmark model across SPG and Equities, enabling more efficient cross-portfolio aggregation and improved concentration charge modeling.
	•	Coherent CCR Models:
	•	Short-form Coherent Model: Developed for margined funds using symmetric historical return scenarios.
	•	Stress Metric Model: For un-margined counterparties (e.g., natural resources), simulating six-month CCAR-like scenarios to capture extended MPOR risk.
	•	LRM Model Enhancement: Classification of convertible bonds as LRM led to ~$6–7B RWA reduction. Limited impact to internal or regulatory liquidity metrics; further enhancements under consideration.

⸻

9. Closing and Follow-Ups
	•	Michaela emphasized the importance of incorporating CCAR feedback into the MRA remediation to avoid duplication during RVE.
	•	The Fed expects follow-up from the firm once internal planning is complete.
	•	Michaela noted an upcoming internal meeting with David Palmer and others to review the firm’s remediation materials.
	•	Caleb will submit trading-specific follow-up questions in writing. Caroline welcomed written follow-ups for clarity and tracking.

⸻

Let me know if you’d like:
	•	a clean Word or PDF version for formal distribution,
	•	shortened bullets for an executive summary,
	•	or help with highlighting changes since Q1.

I’m happy to tailor it.




During Q2, Model Risk identified a P&L breach in the Vega PST for the EMEA Volex portfolio during the monitoring report review. The issue stemmed from static scenario shocks that were not appropriately calibrated to reflect recent market data. A medium-severity finding was raised, recommending shock recalibration. Remediation is currently in progress.



AI Web Grounding, which uses web search to provide real-time context and improve response accuracy and timeliness



Here’s a clearer and more polished version of your text:

⸻

Artificial Intelligence
	•	Loans AI: Validation in progress for the generative AI model that classifies loan document purposes as either credit or liquidity for 6g Liquidity reporting.
	•	Mortgage Loans AI (Tier 1): Approved by MRM; assists the U.S. Mortgage Warehousing Desk by flagging loans likely to be liquidity.
	•	Corporate Loans AI (Tier 1): Validation in progress. Performance and reproducibility issues identified; this model is used across GBM and AWM portfolios and is critical for credit classification.
	•	Other recently approved models:
	•	Funds AI (Tier 2): Extracts NAV of externally administered funds and verifies against alternative sources, reducing manual effort by ~80%.
	•	Wealth AI (Tier 3): Uses LLM to answer PWM advisors’ queries by leveraging internal documentation. Accuracy improved from 61% to 90% after addressing a validation finding.
	•	Agentic AI (Devin):
	•	AIRCC approved expansion of M365 Copilot from 10k users to firmwide.
	•	Staged rollout of Marquee AI Widget-as-a-Tool, enabling users to answer queries, update parameters, and run templatized calculations on Marquee widgets for internal and external use.

⸻

✅ This version:
	•	Improves flow and readability
	•	Groups related items logically
	•	Uses concise, active language
	•	Adds emphasis on outcomes (e.g., reducing manual effort by ~80%)

Do you want me to make it even more executive-friendly for a senior management or board update (shorter bullets, business impact emphasized), or keep it detailed for an internal MRM/AI governance update?


NFA issued follow-up requests from the May 2025 Capital Enquiry, mainly on P&L breaches, positional P&L construction, and VaR model; while MRM is not the main focus, NFA requested our input on some topics.



Here’s a cleaner and more concise version of your text while keeping “went well” and combining sentences where appropriate:

⸻

Regulatory Updates

Supervisory Finding Remediation:
	•	MRM MRA Remediation: On track, with infrastructure enhancements and training to be completed by Sep 30 ahead of the enhanced annual review framework rollout.
	•	Allowance for Credit Loss (MRIA 1: Risk Capture & Ongoing Monitoring; MRA 2: Weaknesses in MRM): Development and validation meetings on Apple Card, Asset Secured Lending (ASL), and Commercial Real Estate (CRE) went well.
	•	TxB AML MRIA 2 (Optimization, Testing & Risk-Based Monitoring): FRB has initiated validation, with the kickoff meeting completed.

Quarterly Meetings with FRB:
	•	FRB-MRM Quarterly Meeting: Scheduled for Aug 7. In addition to the usual agenda, the Fed requested updates on open IA findings, AI/ML inventory segmentation, and MRM MRA remediation progress.
	•	CCR Modeling Quarterly Meeting (Jul 22): Went well, focusing on the commodities potential exposure (PE) model. Follow-up includes modeling choices and a list of PE models across asset classes.
	•	Market Risk Trading Model Quarterly Meeting (Jul 30): Went well; we reviewed notable pricing model enhancements approved during H1.

⸻

Would you like me to make it more executive-friendly (shorter, for senior management) or slightly more technical (for internal risk/regulatory audiences)?


Enhancement to Credit Contagion Model
	•	MRM approved improvements enabling multiple collaterals in a single trade and modeling correlated defaults.
	•	Enhances CVA and gap risk calculations by capturing diversification and default correlations.
	•	Paired with the multi-credit jump model, this is a key milestone for CSG model development.
	•	Benefits include better risk representation for private credit SPV notes and on-balance sheet lending, improving accuracy of trade risk depiction.



Here’s your original text with all changes highlighted. I’ll show original → revised differences in bold so you can easily see what I changed.

⸻

Title
	•	Original: Model Performance Under Tariff Uncertainty: During the volatile market period, the trading valuation models performed well and robustly overall.
	•	Revised: Model Performance Under Tariff Uncertainty: During the volatile market period, the trading valuation models performed well and remained robust overall.
(✔ Added “remained” for better flow)

⸻

Section 1: Basket Options
	•	Original: There was calibration issues observed under multi-FX model:
	•	Revised: However, calibration issues were observed under the multi-FX model:
(✔ Fixed plural agreement: “issues were” instead of “issues was”; ✔ Added “However,” for readability; ✔ Added “the” before multi-FX model)
	•	Original: For basket option with large number (5 or more) of crosses, there was calibration issues at the short end and observed unstable Vega risk.
	•	Revised: For basket options with a large number (five or more) of crosses, calibration issues were noted at the short end, resulting in unstable Vega risk.
(✔ Pluralized “option” → “options”; ✔ Added “a” before large number; ✔ Spelled out “5” → “five” for formal tone; ✔ Changed “there was calibration issues” → “calibration issues were noted”; ✔ Changed “and observed unstable Vega risk” → “resulting in unstable Vega risk” for smoother grammar)
	•	Original: The model implies local correlations from the local volatilities of underlying crosses.
	•	Revised: The model infers local correlations from the local volatilities of the underlying crosses.
(✔ “implies” → “infers” for technical accuracy; ✔ Added “the” before underlying)
	•	Original: Due to increased volatility/skew, it led to implied correlations out of the bounds.
	•	Revised: Due to increased volatility/skew, this led to implied correlations falling outside acceptable bounds.
(✔ Replaced “it led” → “this led”; ✔ Added “falling outside acceptable bounds” for clarity)
	•	Original: The model has an internal calibration check to make sure the impact from the bounding is not too large.
	•	Revised: The model has an internal calibration check to ensure the impact of bounding is not too large.
(✔ “make sure” → “ensure”; ✔ “from the bounding” → “of bounding” for grammar)
	•	Original: The check failed for some basket trades. The issue was temporarily fixed with limited impact, and further model enhancement is in progress.
	•	Revised: This check failed for some basket trades. The issue was temporarily fixed with limited impact, and further model enhancements are in progress.
(✔ Added “This” for continuity; ✔ Changed “enhancement” → “enhancements” since multiple changes are likely)

⸻

Section 2: Control Variates
	•	Original: Control Variates (CVs) for Monte Carlo Pricer: For multi-asset barrier trades in Equity, control variates have been introduced within the Monte Carlo pricing framework to reduce MC noise, which can better match prices for vanilla payoffs and enhance risk calculation stability for Vega and high order risk. Currently it’s rolled out for Eq MA Barriers (As of May 30, 2025, the P&L impact was ~ $445K), and additional ongoing work is underway to roll it out to other tradables.
	•	Revised: Control Variates (CVs) for Monte Carlo Pricer: For multi-asset barrier trades in Equity, control variates have been introduced within the Monte Carlo pricing framework to reduce MC noise. This improves price alignment for vanilla payoffs and enhances risk calculation stability for Vega and higher-order risks. Currently, it has been rolled out for Eq MA Barriers (as of May 30, 2025, the P&L impact was approximately $445K), and additional work is underway to extend it to other tradables.
(✔ Split long sentence into two for readability; ✔ Changed “which can better match” → “This improves price alignment”; ✔ Changed “high order risk” → “higher-order risks”; ✔ Added comma after “Currently”; ✔ Replaced “~” with “approximately” for formal tone; ✔ Changed “roll it out” → “extend it” for variety)

⸻

Section 3: XVA Pricing
	•	Original: XVA Pricing Enhancement: XVA pricing has been enhanced to better model Credit Support Agreements (SAs) which allow for claiming of FVA value at default and presents in LATAM market. The market price quotes suggested trades were priced with such CSA and cases of actual defaults confirmed such close out amount calculation. In the enhanced model, the FVA exposure at default will be netted with NPV at default, and this is beneficial for liability FVA. With this change, there were ~$14mm XVA reserve release, which was mainly from liability FVA benefit with LATAM counterparties.
	•	Revised: XVA Pricing Enhancement: XVA pricing has been enhanced to better model Credit Support Agreements (CSAs) that allow for claiming FVA value at default, which is present in the LATAM market. Market price quotes suggested trades were priced with such CSAs, and cases of actual defaults confirmed such close-out amount calculations. In the enhanced model, the FVA exposure at default will be netted with the NPV at default, which is beneficial for liability FVA. With this change, there was an approximate $14mm XVA reserve release, mainly from liability FVA benefit with LATAM counterparties.
(✔ Changed “SAs” → “CSAs” for accuracy; ✔ Changed “and presents in LATAM market” → “which is present in the LATAM market” for grammar; ✔ Added commas for clarity; ✔ “such close out amount calculation” → “such close-out amount calculations”; ✔ Added “the” before NPV; ✔ Changed “there were ~$14mm” → “there was an approximate $14mm”)

⸻

Section 4: Forward Risk Dividend Logic
	•	Original: Forward Risk Dividend Logic[Q1]: There was an implementation issue on projecting future dividends in forward risk calculations. It only affects the risk calculations at the year end. Specifically, dividend projection logic references the pricing date year as start point to determine marked dividend period by adding fixed number of years. When shifting pricing date forward during forward risk calculations, it added additional year without dividend data in back end of dividend marks, and it resulted in incorrect future dividend projection under the risk scenario. This resulted in an equity delta misstatement of ~ $50mm, no PL impact. The issue has been fixed with MRM review.
	•	Revised: Forward Risk Dividend Logic [Q1]: An implementation issue occurred in projecting future dividends in forward risk calculations. This only affected risk calculations at year-end. Specifically, the dividend projection logic referenced the pricing date year as the starting point to determine the marked dividend period by adding a fixed number of years. When shifting the pricing date forward during forward risk calculations, it added an additional year without dividend data at the back end of the dividend marks, resulting in incorrect future dividend projections under the risk scenario. This caused an equity delta misstatement of approximately $50mm, with no P&L impact. The issue has been fixed with MRM review.
(✔ Changed “There was an implementation issue on projecting” → “An implementation issue occurred in projecting”; ✔ Changed “It only affects” → “This only affected”; ✔ Added “the” before start point → “the starting point”; ✔ Added “a” before fixed number; ✔ Changed “added additional year without dividend data in back end” → “added an additional year without dividend data at the back end”; ✔ “it resulted in incorrect future dividend projection” → “resulting in incorrect future dividend projections”; ✔ Changed “This resulted in” → “This caused”; ✔ “~” → “approximately”; ✔ “no PL impact” → “with no P&L impact”)

⸻

✅ Summary of edits:
	•	Fixed subject-verb agreement
	•	Improved readability by breaking up long sentences
	•	Changed informal phrasing (e.g., “make sure” → “ensure”)
	•	Added missing articles (“the,” “a”)
	•	Adjusted technical word choice for accuracy (“implies” → “infers”)
	•	Standardized currency and numeric expressions
	•	Added commas for clarity and consistency

⸻

Would you like me to produce a clean final version with all changes accepted and also a separate executive summary version (short and clear for reporting)?




Here is your text with minor grammar and clarity improvements only (no major restructuring):

⸻

Model Performance Under Tariff Uncertainty: During the volatile market period, the trading valuation models performed well and remained robust overall. However, calibration issues were observed under the multi-FX model:
	•	Basket Options with Multiple Crosses: For basket options with a large number (five or more) of crosses, calibration issues were noted at the short end, resulting in unstable Vega risk. The model infers local correlations from the local volatilities of the underlying crosses. Due to increased volatility/skew, this led to implied correlations falling outside acceptable bounds. The model has an internal calibration check to ensure the impact of bounding is not too large. This check failed for some basket trades. The issue was temporarily fixed with limited impact, and further model enhancements are in progress.
	•	Control Variates (CVs) for Monte Carlo Pricer: For multi-asset barrier trades in Equity, control variates have been introduced within the Monte Carlo pricing framework to reduce MC noise. This improves price alignment for vanilla payoffs and enhances risk calculation stability for Vega and higher-order risks. Currently, it has been rolled out for Eq MA Barriers (as of May 30, 2025, the P&L impact was approximately $445K), and additional work is underway to extend it to other tradables.
	•	XVA Pricing Enhancement: XVA pricing has been enhanced to better model Credit Support Agreements (CSAs) that allow for claiming FVA value at default, which is present in the LATAM market. Market price quotes suggested trades were priced with such CSAs, and cases of actual defaults confirmed such close-out amount calculations. In the enhanced model, the FVA exposure at default will be netted with the NPV at default, which is beneficial for liability FVA. With this change, there was an approximate $14mm XVA reserve release, mainly from liability FVA benefit with LATAM counterparties.
	•	Forward Risk Dividend Logic [Q1]: An implementation issue occurred in projecting future dividends in forward risk calculations. This only affected risk calculations at year-end. Specifically, the dividend projection logic referenced the pricing date year as the starting point to determine the marked dividend period by adding a fixed number of years. When shifting the pricing date forward during forward risk calculations, it added an additional year without dividend data at the back end of the dividend marks, resulting in incorrect future dividend projections under the risk scenario. This caused an equity delta misstatement of approximately $50mm, with no P&L impact. The issue has been fixed with MRM review.

⸻

✅ Would you like me to make this more concise and executive-friendly (for reporting) while keeping the technical details accurate? Or keep this detailed version as is?


Certainly! Here’s a clearer, more concise rewrite of your bullet points:

⸻

Validation Activities
	•	MRM approved enhancements to the credit contagion model for CVA and gap exposure in secured funding trades, now allowing multiple collateral assets and the use of a benchmark whose default can trigger correlated price jumps in other collaterals.
	•	These changes allow the model to capture diversification benefits, account for default correlations among collaterals, and support CVA and gap exposure calculations for trades with bond or loan portfolios as collateral.
	•	Validation completed for models used in the ECB Counterparty Credit Risk Exploratory Scenario (ECB CCR-ES) exercise.
	•	This exercise, run in parallel with the EU-wide Stress Test, tests banks’ ability to model CCR under stress and risks from connections to non-bank financial institutions like hedge funds.
	•	Key improvements include better justifications for leverage metric selection across counterparties and improved documentation for specific wrong-way risk.

⸻

Let me know if you want this made even shorter or have other edits!




Here’s a simplified and clearer version of your bullet points:

⸻

Validation Activities
	•	Enhancement to Credit Contagion Model
MRM approved improvements to the credit contagion model for CVA and gap exposure in secured funding trades. The enhancement allows:
	•	Inclusion of multiple collateral assets in one trade
	•	Designation of a benchmark name whose default can trigger correlated price jumps in other collateral assets
	•	Better modeling of diversification benefits and default correlations, enabling CVA and gap exposure calculations for secured lending and TRS trades with collateral portfolios
	•	ECB Counterparty Credit Risk Exploratory Scenario (ECB CCR-ES)
Validation completed for models used in this exercise, which runs alongside the EU-wide Stress Test to evaluate CCR modeling under stress and vulnerabilities linked to non-bank financial institutions (e.g., hedge funds).
	•	Key improvements include clearer justification for leverage metrics across counterparties and stronger documentation on wrong-way risk

⸻

Would you like me to make this even shorter (one sentence per bullet) for a high-level executive summary?



This includes approvals of Mortgage Loans AI, used in the U.S. Mortgage Warehousing Desk to assist by flagging loans that may be for liquidity, and Corporate Loans AI, used across GBM and AWM portfolios and relied on more heavily to classify loans as credit or liquidity.A new Tier 2 generative AI model designed to extract and validate Net Asset Values (NAV) of externally administered investments from financial statements, streamlining operations and strengthening the accuracy and reliability of accounting processes.


Here’s a refined and more professional version with improved flow and grammar:

⸻

Regulatory Updates
	•	FINRA/GSCO 2024 Cycle Exam:
The final report was issued in May with no findings for Model Risk. The exam, spanning from September 2024 to May 2025, placed significant focus on Model Risk. A total of 59 requests were addressed, including written responses and eight onsite/Zoom meetings. These covered all aspects of the firm’s model risk management framework, including policies and standards, model inventory and tiering, model validation, model change management, and ongoing monitoring.
	•	Prudent Valuation / Additional Valuation Adjustments (AVAs):
Model Risk completed initial validation and approved twelve prudent valuation methodologies developed to address ECB findings from an onsite inspection. In total, 33 findings were raised by Model Risk, including three high-severity issues related to unapproved model code, methodologies not meeting regulatory guidance, underestimation of AVAs, and documentation weaknesses. All high-severity findings were remediated and closed prior to approval.
	•	Internal Capital Adequacy Assessment Process (ICAAP):
Model Risk reviewed and approved models used by GSI, GSIB, and GSG UK for the current ICAAP cycle. Validation work focused on reassessing model appropriateness for these entities, including evaluation of limitations, uncertainties, and overlays under ICAAP scenarios and in light of portfolio changes. All model changes introduced since the previous ICAAP cycle underwent MRM validation and approval, including improvements to residual risk add-on quantification within the Economic Capital model to remediate prior findings.
MRM also validated and approved ICAAP usage of two climate risk models to assess physical and transition risks, as well as a new qualitative approach for projecting Prudent Valuation Adjustments (PVA). Seventeen new findings were raised, including one high-severity issue for the PVA projection approach, which was addressed through additional testing and documentation enhancements. Remaining lower-severity findings relate primarily to methodology and implementation of limited materiality, insufficient justification for modeling choices, and gaps in ongoing monitoring.
	•	Asset Quality Review (AQR) Exam:
Remediation of four ECB findings from the AQR exam has been completed. These related to GSBE oversight, annual review and validation practices, and process documentation.
	•	ECB Counterparty Credit Risk Exploratory Scenario (ECB CCR-ES):
Model Risk validated models used for the ECB CCR-ES exercise, conducted in parallel with the EU-wide stress test to assess banks’ ability to model CCR under stress and vulnerabilities from interlinkages with non-bank financial institutions, such as hedge funds. The review resulted in improved documentation on specific wrong-way risk within the submission, additional justification for the selection of leverage metrics across counterparties, and a medium-severity finding regarding shortcomings in FX modeling.

⸻

✅ Key improvements:
	•	Fixed grammatical inconsistencies and repetitive phrasing.
	•	Consolidated redundant phrases like “Model Risk has validated and approved” → Model Risk validated and approved.
	•	Organized content into structured, readable bullet points for clarity.
	•	Formalized language for regulatory readiness.

⸻

Would you like me to apply the same editing style to your entire draft so that it reads consistently professional and regulator-friendly?



Model Risk validated and approved a new positional stress test (PST) within the interest rate stress testing framework to capture basis risk across futures, bonds, and swaps. This enhancement was introduced following observed P&L volatility during the April Trump tariff announcements, where previous limits accounted only for bond–futures basis, while losses were primarily driven by bond–swap basis risk.
new model for estimating Delta risk in commodity products, using an improved numerical implementation for greater accuracy and deployed on the Griffin infrastructure for faster computation, relative to the previously used CNPL platform.


Low-tier generative AI models, including Tier 2 and Tier 3 tools, were developed to support productivity across businesses by summarizing market and research content, extracting financial data, generating visualizations from natural language queries, analyzing portfolio exposures, enhancing search relevance, and assisting advisors with curated content.
Low-tier generative AI models were developed to enhance productivity across businesses, including summarizing market and research content, extracting financial data, generating visualizations from natural language queries, analyzing portfolio exposures, improving search relevance, and assisting advisors with curated content.



During Q1 2025, a modeling issue was identified by the Exotios trading desk:
At year-end, the desk observed that forward risk calculations did not correctly incorporate dividend impacts. The issue arose because dividend projections were dropped when the forward date was adjusted in the risk calculation. This occurred due to the projection logic referencing the pricing date year as the starting point for dividends; when this shifted during forward risk calculations, it pointed to a year with no dividends, resulting in incorrect inputs.

Impact: Equity delta was misstated by approximately $50 million.

Resolution: The issue was remediated through model changes, which were validated and approved by Model Risk.

Here’s the improved version with each item as a separate paragraph for readability, while maintaining clarity and completeness:

⸻

Trading Model Performance and Valuation Updates

Market Context:
No significant model performance issues were observed during tariff-driven market volatility at the end of March and early April. However, the following notable changes and breaches occurred:

⸻

USD Yield Curve Range Accrual (YCRA) Callable Notes:
Model Risk validated and approved a methodology change for marking callable prices (MEE) in the USD YCRA book, reverting to the pre-Dec 2022 approach used for other callables. This change was driven by two factors: (1) pricing in earlier call options eliminates the need to hedge later coupons, and (2) market observations showed YCRAs priced at the system-optimal call. As of April 8, the impact included Delta of –$0.6MM and Vega of +0.3MM per abp.

⸻

Commodity Volatility Calibration:
Calibration failures were observed in Gold volatility, particularly for structured exotic trades. These issues were caused by record-high spot prices during tariff uncertainty and heavily skewed volatility. The problem was addressed by temporarily disabling short-tenor calibration, which had a limited overall impact.

⸻

FX Model Calibration:
Volatility and correlation calibration failures occurred in multi-cross FX trades due to increased volatility/skew and difficulty sourcing reliable market data for marking. A temporary solution was implemented with limited impact, and further investigation is ongoing.

⸻

Forward Risk Dividend Logic:
At year-end, the Exotics trading desk discovered an error in forward risk calculations caused by incorrect dividend projections. The logic referenced the pricing date year as the starting point, and when adjusted for forward risk, it pointed to a year with no dividends, leading to omitted dividends in risk calculations. This resulted in an equity delta misstatement of approximately $50MM. The issue was corrected through a model change, which has been validated and approved by Model Risk.

⸻

Approved Modeling Enhancements (H1 2025)

Dynamic Barrier Shift for Multi-Asset Equity Autocallables:
Model Risk approved a new methodology enabling barrier shifts to dynamically adjust based on volatility. Previously, barrier shifts were static, either set by traders or calculated only at trade inception. This enhancement allows desks to tighten widths during low volatility, improving competitiveness, and ensures caps on large barriers scale with volatility. The change released approximately $1.7MM from the Barrier Shift Reserve on October 7, 2024, and resulted in a DP impact of –$7K and a Vega impact of –$374K on January 22, 2025.

⸻

Control Variates for Monte Carlo Pricer:
Model Risk approved the application of control variates (CV) within the Monte Carlo pricing framework using local volatility for multi-asset barrier options (Eq MA Barrier). Currently, this enhancement is limited to European-style payoffs, where European calls, puts, and/or digital options serve as CV instruments based on the original payoff structures. The primary goal is to reduce Monte Carlo variance, particularly for Vega, thereby improving risk calculation stability. As of May 30, 2025, enabling CV resulted in a cumulative P&L impact of approximately $445K.

⸻

XVA Pricing Enhancement:
Enhancements were approved for CVA pricing under Credit Support Agreements (CSAs), specifically allowing the claim of FVA value at default. Key updates include: (1) modeling FVA exposure at default within the same netting node as related trades (previously in a separate node), and (2) increasing the claimable portion (“haircut”) of FVA from 62.5% to 70%. These changes align MTM and FVA when their signs differ and reflect agreed adjustments between Controllers and Trading. For FX Latam counterparties—where CSAs are concentrated—this change resulted in an approximate $14MM increase in XVA exposure on an overall exposure of about $130MM as of May 2, 2025.

⸻

✅ Do you want me to make it even more concise for a regulatory response (shorter paragraphs, less technical jargon), or keep this detailed version but add an executive summary on top?




During Q3, several trading model performance enhancements were implemented that impacted valuation:
	1.	Control Variates (CV) for Monte Carlo Pricer (Multi-Asset Barrier Options):
Model Risk approved the application of control variates within the Monte Carlo pricing framework using local volatility for multi-asset barrier options (Eq MA Barrier). This enhancement is applied exclusively to European-style payoffs. Control variates—European calls, puts, and/or digital options—are selected based on the original option and barrier structures specified in the trade’s payoff. The primary objective is to reduce Monte Carlo variance, particularly for vega sensitivities, thereby improving risk calculation stability. As of May 30, 2025, the cumulative P&L impact from enabling CV functionality was approximately $445K.
	2.	Close-Out Modeling Enhancements for CVA Pricing under CSAs:
Model Risk approved updates to the close-out modeling for CVA calculations where Credit Support Agreements (CSAs) permit claiming of FVA value at default. Key changes include:
	•	(a) FVA exposure at default is now modeled within the same netting node as related trades (previously modeled separately).
	•	(b) The claimable haircut on FVA at default has been revised from 62.5% to 70%, reflecting agreement between Controllers and Trading.

These adjustments ensure consistent alignment of MTM and FVA when their signs differ and update the haircut to match current contractual terms. For FX Latam counterparties as of May 2, 2025, this change resulted in an increase of approximately $14MM on an overall XVA exposure of ~$130MM.




Counterparty Credit Risk (CCR)

There is continued focus on enhancing CCR management capabilities as part of the firm’s ERM uplift plans. Recent approvals include extensions to credit exposure models under stress scenarios to cover (1) all margined funds and (2) all unmargined counterparties firmwide.
Key improvements include updates to margin determination logic, incorporation of client-level defaults, assessment of previously unmodeled risk factors, and strengthened documentation and testing to address validation findings.

Recovery and Resolution Planning (RRP)

Model Risk validated and approved seven Tier 1 models and four qualitative approaches to estimate liquidity needs post-parent bankruptcy and support the firm’s RRP submission to the FRB and FDIC.
Enhancements were driven by FRB feedback on business-level segmentation, validation findings, and developer-identified issues. Outstanding medium-severity findings relate to intraday liquidity risk methodology, unjustified runway assumptions, uncaptured contingent pricing features, and incomplete reflection of recent stressed scenarios in deposit modeling.

Liquid & Readily Marketable (LRM) Classification

Model Risk validated and approved a new qualitative approach for classifying securities as “Liquid & Readily Marketable” for liquidity metrics and capital requirements, improving upon prior simpler methods. All seven high-severity findings were remediated through enhanced analysis and justification of model choices. Medium-severity issues remain, requiring refinements to classification logic, mitigation of unintuitive outcomes, and addressing uncertainty in volume thresholds and Bloomberg data quality.

Asset Secured Lending (ASL)

Development of new models to support ASL continues, with recent approvals of 11 Risk Engineering-owned usages of Facility Level Rating (FLR) models for underwriting. Common outstanding issues include inconsistencies with post-trade model assumptions and required enhancements to documentation, monitoring, and platform user interface






A new model for estimating Delta risk in commodity products, replacing the previous forward difference method with a central difference method for improved accuracy, implemented within the advanced Griffin infrastructure to enhance computational speed.



A new model for estimating Delta risk in commodity products, utilizing a central difference method for improved accuracy, implemented within the advanced Griffin infrastructure to enhance computational speed.


Validation activities during the period primarily focused on:

Risk management enhancements, including approvals of:
	•	An enhancement to the Monte Carlo-based credit contagion model used for calculating Credit Valuation Adjustment (CVA) and gap exposure in secured funding trades. This update allows multiple collateral assets within a single trade and designates a benchmark collateral asset whose default triggers correlated price jumps in other counterparties’ collateral assets. This enhancement captures diversification benefits and collateral default correlations, supports multiple CVA bookings within a single trade, and enables gap CVA modeling for secured lending and Total Return Swap (TRS) trades involving portfolios of bonds or loans as collateral.
	•	A new model for estimating Delta risk in commodity products, utilizing a central difference method implemented within the advanced Griffin infrastructure, replacing the previous forward difference method to improve accuracy and computational speed.
	•	Two new models for calculating X-Valuation Adjustment (XVA) on USD-denominated cancellable swaps and Bermudan swaptions, which were previously not modeled.
	•	An enhancement to the multi-asset barrier options pricing model to incorporate control variates (adjustments to align with market prices) for European-type payoffs, thereby reducing Monte Carlo variance and enhancing stability in risk calculations.
	•	Enhancements to the electricity price prediction model, including adjustments to load inputs accounting for load ramp-up periods, input restrictions to mitigate outlier impacts, and unified battery dispatch post-load adjustment to ensure consistency across prediction blocks.

Counterparty Credit Risk (CCR) model enhancements, including recent approvals of:
	•	Migration of the Equities franchise business to the Unified Benchmark Model for margin shortfall calculations, following the earlier migration of Synthetic Products Group (SPG) portfolios, supporting ongoing standardization and consistency efforts across Prime and Franchise businesses.
	•	An enhancement to the Prime Brokerage (PB) SPIRE margin model, now incorporating eligible bank loans into worst-case loss calculations, previously benchmarked at 100% of market value for all bank loans.
	•	Additional improvements to margin shortfall modeling, including collateral inclusion, repurchase agreement treatment, recalibration of interest rate shocks, and migration of the franchise credit model to the “V30” version, addressing model validation findings.

London Interbank Offered Rate (LIBOR) transition-related enhancements, including:
	•	Approval of fallback logic for trades linked to the Israel Tel Aviv Inter-Bank Offered Rate, now referencing the Shekel Overnight Interest Rate (SHIR) plus a fixed spread.




An enhancement to the Monte Carlo-based credit contagion model for calculating Credit Valuation Adjustment (CVA) and gap exposure in secured funding trades, allowing multiple collateral assets in a single trade and the designation of a benchmark collateral whose default triggers correlated price jumps among other collateral assets.

This enhancement captures diversification benefits and default correlations among collateral assets, supports multiple CVA bookings within a single trade, and enables modeling of gap CVA for secured lending and Total Return Swap (TRS) trades involving portfolios of bonds or loans as collateral.




An enhancement to the Monte Carlo-based credit contagion model for calculating Credit Valuation Adjustment (CVA) and gap exposure in secured funding trades. The update allows multiple collaterals in a single trade and designates a benchmark credit name whose default triggers correlated defaults among other collateral names.
This enhancement captures diversification benefits and correlations between collateral defaults, supports multiple CVA bookings in a single off-balance sheet trade, and enables modeling gap CVA for secured lending and Total Return Swap (TRS) trades involving portfolios of bonds or loans for both private credit SPVs and on-balance sheet lending.





Artificial Intelligence (AI) / Machine Learning (ML) Models

There continues to be significant growth in the development and adoption of AI/ML models, including recent approvals and implementations.

Non-generative AI models:
	•	The first Tier 2 transformer-based deep learning neural network model, developed to analyze FX trading data, predict price movement directions for major currency pairs, and dynamically adjust bid-offer spreads in FX algorithmic trading.
	•	A new Tier 2 Global Banking & Markets (GBM) public neural network model, designed to calculate valuation adjustment charges for multi-asset snowball autocallables, expanding the coverage of the Agni fast pricer suite across FX and Equities, while significantly reducing computational time.

Enhancements to the GS AI Platform monitoring framework:
	•	Improvements addressing model validation findings, including advanced detection of hallucinations and enhanced performance when analyzing longer documents.
	•	The model detects potentially unsafe interactions with large language models (LLMs), specifically targeting issues such as hallucinations, profanity, prompt injection, and exposure of personally identifiable information.

Generative AI productivity tools utilizing Large Language Models (LLMs):
	•	Tier 2 Engineering models developed to (1) summarize trends and patterns from equity market data, news articles, and industry research and (2) extract and validate Net Asset Values (NAV) from externally administered investment financial documents.
	•	Tier 3 Global Banking & Markets (GBM) models designed to (1) convert natural language queries into relevant market data series and visualizations and (2) summarize earnings call transcripts to support investment banking activities.
	•	Tier 3 Asset & Wealth Management (AWM) models used to (1) evaluate portfolio exposure to specific themes such as tariffs, inflation, or AI and (2) respond to advisors’ queries by selecting and presenting the most relevant Private Wealth Management (PWM) content.
	•	A Tier 3 Global Investment Research (GIR) model developed to contextually reorder search results to enhance relevance and usability.





Certainly! Here’s a refined version with improved clarity and flow, while preserving your original structure and content:

⸻

Artificial Intelligence (AI) / Machine Learning (ML) Models
There continues to be growth in the development of AI/ML models and adoption of new techniques, including the recent approval of the following:

Non-generative AI models, including:
	•	A Tier 2 deep learning neural network (transformer)-based AI signal, trained on FX trading data to predict directional price movements for a basket of major FX currency pairs, used to dynamically adjust bid-offer spreads in FX algorithmic trading.
	•	A new Tier 2 Global Banking & Markets (GBM) Public neural network-based model, designed to calculate valuation adjustment charges for multi-asset snowball autocallables, expanding the Agni fast pricer suite across FX and Equities while significantly reducing computational time.

Enhancements to the GS AI Platform monitoring framework
	•	Improvements address prior model validation findings and enhance hallucination detection, particularly in longer documents.
	•	The model continues to monitor and flag unsafe interactions between users and LLMs, including hallucinations, profanity, prompt injection, and exposure of personally identifiable information.

Generative AI productivity tools leveraging large language models (LLMs), including:
	•	Tier 2 Engineering models that (1) identify trends and patterns in equity market data, news articles, and industry research, and (2) extract and verify Net Asset Value (NAV) of externally administered investments from financial documents.
	•	Tier 3 GBM models that (1) translate natural language queries into market data series and visualizations, and (2) summarize earnings call transcripts for investment bankers.
	•	Tier 3 Asset & Wealth Management (AWM) models that (1) assess portfolio exposures to specific themes such as tariffs, inflation, or AI, and (2) respond to advisor queries using AI to retrieve the most relevant content from Private Wealth Management (PWM) materials.
	•	A Tier 3 Global Investment Research (GIR) model that reorders search results contextually based on relevance, improving both usability and informational value.

⸻

Let me know if you’d like this reformatted for a slide or summary version.






Guardrail Model Enhancements

MRM approved a significant upgrade to the Guardrail Model (now Tier 1) used to safeguard the firm’s Generative AI platform, including real-time hallucination blocking capabilities. This marks a transition from a monitoring-only tool to a preventative control.

Key improvements in the newly validated Guardrail 3.0 include:
	•	Enhanced detection of hallucinations and prompt injection
	•	Improved processing of long documents
	•	Integration of a new LLM with better reasoning capabilities
	•	Expansion of the training dataset for broader coverage

Since the model’s initial approval in early 2024, MRM has raised 16 findings across the Guardrail family (covering hallucinations, bias, prompt injection, PII, and unsafe use), with 13 already remediated — resulting in measurable performance gains.

MRM’s validation included independent benchmarking against Guardrail 2.0. One Sev2 finding was raised regarding limited ability to retrieve and synthesize information across multiple documents, requiring further enhancement.

Despite progress, MRM continues to monitor three key limitations:
	•	21.6% of hallucinations remain undetected
	•	Detection may be biased by the LLM’s own stereotypes
	•	Performance degrades in tasks requiring logical inference or big-picture understanding




Trade Description:

Goldman Sachs intends to acquire bilaterally a Mandatory Exchangeable Bond (MEB) from an issuer, collateralized by a pledged share position. Economically, the trade resembles a funded equity collar, with embedded structuring features including:
	•	An averaging period for final settlement (similar to a tranched collar),
	•	A voluntary acceleration right allowing the issuer to settle early,
	•	Reverse Asian-style payoff elements, including a daily cap/floor and harmonic mean calculation.

Key Terms:
	•	Notional: ~$300 million USD
	•	Maturity: 4.5 months from trade date
	•	Target Return: ≥3.5% pre-fee (with potential for ~2% fee uplift via GBM Private)


					      
					      Reason for Waiver:
The current booking model (Eq CASB Threshold) does not support all features required for this trade—specifically, it lacks functionality for:
	•	Reverse averaging (reverse ASB),
	•	Daily cap/floor, and
	•	Harmonic mean averaging.

Booking Approach During Waiver Period:
	•	Trade will be booked under Eq CASB Threshold, wrapped via SP Shadow, which will represent all features except daily cap/floor and harmonic mean.
	•	Reverse ASB support will be enabled in production under the waiver.
	•	Local code modifications will be used to approximate P&L and Greeks, which will be taken into account in trading’s risk management.

Model Enhancement Plan:
	•	Full support for daily cap/floor and harmonic mean averaging will be added to Eq CASB Threshold during the waiver period.
	•	Enhancements will be documented and submitted for model approval and deployment post-trade.





Trade Description:

The proposed transaction is a 5-year Contractual Dividend Autocallable on a worst-of basket of South African bank stocks (ABG1.J, NEDJ.J, OMUJ.J) with a notional equivalent of approximately $15 million (3 tranches of ZAR 90 million each). The trade is structured to pay fixed dividends and includes an Asian-style observation feature for autocall triggers, intended to mitigate liquidity concerns around spot fixing on observation dates.

This trade combines two features—fixed dividend handling and Asianing of autocall observations—which are individually supported in existing tradeable templates:
	•	EQ Auto Callable MA supports Asianing without fixed dividends
	•	EQ Auto Callable MA CS supports fixed dividends without Asianing

However, the system currently does not support both features simultaneously within a single tradeable template, hence the need for a model waiver.

Rationale:
	•	Asianing on autocall observations is introduced to address liquidity challenges in the South African equity market.
	•	Fixed dividend treatment aligns with client expectations and economic modeling assumptions.

Booking Approach:
	•	The trade will be booked initially without the Asianing feature.
	•	If the trade is executed, we plan to implement and stratify a new tradeable version that incorporates both features by the end of this week.
	•	The trade will be rebooked into the updated version once available. The Asianing period spans only a few days and is not expected to materially impact P&L at inception.

Remediation Plan:
	•	Feature enhancement in EQ Auto Callable MA CS to support Asianing will be completed by end of this week.
	•	Full documentation, testing, and submission to MRM for review and model approval will be completed by end of next week.


Transaction Model Waiver Summary

Terms:
	•	Trade Type: Contractual Dividend Autocall on Worst-off South African Banks
	•	Notional: ~$15 million (3 x 90mm ZAR)
	•	Maturity: 5 years
	•	Underliers: ABG1.J, NEDJ.J, OMUJ.J
	•	Expected P&L: ~$1 million
	•	Client: Abax

Economic Description:
	•	Classical Fixed Dividend Autocall structure with the additional Asianing feature for autocall observations. Asianing is introduced to mitigate liquidity concerns.

Reason for Waiver:
	•	Existing tradables separately support autocall with Asianing (eq auto callable ma) and fixed dividend (eq auto callable ma cs), but no single tradable supports both simultaneously. Immediate trading capability required as the transaction is imminent.

Booking During Waiver Period:
	•	Initially booked without the Asianing feature.
	•	The Asianing impact is minimal for the first few days, thus negligible initial impact.
	•	Rebooking planned once the Asianing-enabled strat is available, anticipated by end of the current week.

Compensating Controls:
	•	Implementation of Asianing feature into “EQ Auto Callable ma CS” to be completed by end of this week.
	•	Documentation, testing, and formal submission to Model Risk Management (MRM) to occur by end of next week to remediate the waiver promptly.





Please let me know if any further adjustments are required!
AIL FRAC Breaches Resolved
	•	All remaining breaches have been resolved, including:
	•	4 unvalidated activities
	•	1 rejected activity
	•	1 activity under waiver
	•	20 activities with medium severity findings aged over 6 months
	•	Since ETSC risk metrics were established in FRAC (Oct ’24), all metrics have been reduced to zero

E-trading Policy / Standard Update
	•	The E-trading Policy and Standard have been updated to establish ETSC validation and approval as a standalone requirement
	•	Applies to all new or modified E-trading activities before trading can commence
	•	Formalizes ETSC validation as a parallel process to ATRACG review
	•	Supports greater efficiency in approvals and better aligns with the model validation framework



AIL FRAC Breaches Resolved
All outstanding breaches were resolved, including aged medium-severity items related to E-trading.
Since launching ETSC risk metrics in FRAC in Oct ‘24, we’ve reduced all key breach categories to zero:
	•	Unvalidated Activities: 4 → 0
	•	Rejected Activities: 1 → 0
	•	Activities under Waivers: 1 → 0
	•	Aged Medium Severity Findings (>6 months): 20 → 0

E-trading Policy / Standard Update
The policy now requires ETSC validation and approval for all new or modified E-trading activities before trading begins.
This formalizes ETSC as an independent approval path alongside ATRACG, improving efficiency and aligning with model validation practices.


CRO Update

Top of Mind
	•	RCSA: Central guidance for divisions approved today by the Model Risk Control Committee (MRCC).
	•	IDR Assessments: Wrapping up assessments; thematic finding raised regarding timely remediation of GBM validation findings.

Artificial Intelligence
	•	Loans AI: Leveraging Large Language Models (LLMs) to classify loan proceeds as “credit” or “liquidity” for 6G reporting.
	•	Validation in progress following AIRCC’s conditional approval, pending verification of testing data and alignment with ORR leadership.
	•	Current accuracy stands at 95%, with 16% flagged for human review and approximately 12.5% disagreement between AI and human evaluations.
	•	Consistency remains a concern; around 10% of classifications vary upon retesting. Remediation underway to address this before the November regulatory deadline.

Regulatory Updates
	•	MRM MRA Remediation: On track with infrastructure improvements and training scheduled for completion by September 30, ahead of the rollout of the enhanced annual review framework.
	•	ACL MRIA/MRA Remediation: Submitted required materials to the FRB addressing ACL MRIA 1 (Inadequate Risk Capture and Ongoing Monitoring for ACL Models) and MRA 2 (Weaknesses in Model Risk Management).
	•	Submitted documents include model and validation reports, ongoing monitoring updates, policies and templates, finding extensions, and MRM reporting materials. Kickoff scheduled for July 21.
	•	AQR Findings: Completed remediation of all four MRM-owned Asset Quality Review (AQR) findings, covering enhancements in GSBE oversight, annual review processes, significant Tier 1 revalidations workflow, and related policies and procedures.





I’ve refined the updates for clarity and conciseness. Let me know if further adjustments are needed!




Loans AI leverages Large Language Models (LLMs) to classify the purpose or use of loan proceeds as either “credit” or “liquidity” for 6G reporting purposes.

Model validation is currently underway, following AIRCC’s conditional approval pending human verification of ground truth data for the testing sample and subsequent discussion with ORR leadership.

The current model demonstrates approximately 95% accuracy, with 16% of loans flagged for human review due to complexity or uncertainty. Within this subset, there is roughly a 12.5% disagreement rate between AI-generated results and human assessments.

Consistency and repeatability remain concerns, as approximately 10% of loan classifications produce different outcomes upon retesting. Remediation efforts are ongoing, targeting resolution before the November regulatory submission deadline.



Halo (Agni Framework) – Summary Updates:
	•	The Agni AI framework is transitioning training responsibilities directly to trading desks, enabling business-specific customization across equities, FX, and bond markets.
	•	Halo aims to enhance adaptability by allowing desks to independently develop tailored AI models, leveraging the core Agni infrastructure provided centrally.


Here’s a simplified version suitable for non-technical readers:

Loans AI – Summary Updates:
	•	Current AI testing shows 95% accuracy overall, with 16% of loans flagged for human review due to complexity or unclear information.
	•	For loans requiring human review, there is around 12.5% disagreement between AI results and human assessments, indicating these loans are generally more challenging.
	•	Consistency remains a concern, as about 10% of loan assessments produce different results when repeated; improvements are underway to resolve these issues before the November regulatory deadline.




Here’s a detailed yet concise summary suitable for the CRO updates based on the last part of the transcript:

CRO Updates:
	•	MRCC and RCSA:
	•	MRCC reviewing the central RCSA guidance, with ongoing discussions about IDDR assessment calibration.
	•	Market Risk showed improved effectiveness in Q2 assessments; GBM continues to lag.
	•	AI and Model Validation:
	•	Validation in progress for Loans AI (mortgage and wholesale loans) targeting resolution of repeatability issues ahead of the November regulatory deadline.
	•	GitHub Copilot and agentic AI implementations progressing, with engineering planning to deploy three agentic use cases by year-end.
	•	Generative AI (Content AI) now active in GIR, improving client search result relevance through contextual reordering.
	•	Remediation and Findings:
	•	Ongoing remediation efforts for ACL RVE and AQR completions are advancing.
	•	Attention required for overdue model validations, ensuring accurate reporting and adherence to newly adjusted timelines.







•	Content AI: GIR portal now leverages Generative AI to contextually reorder search results, enhancing relevance and usability.Loans AI – Summary Updates:
	•	Model accuracy currently at 95%, with 16% of loans requiring human review.
	•	12.5% disagreement rate between AI and human reviewers in the flagged subset.
	•	10% repeatability issue due to code inconsistencies; fixes targeted before November submission.

Loans AI – Summary Updates:
	•	Current testing indicates 95% accuracy for automated AI review, with 16% of loans flagged for human review due to uncertainty or loan complexity.
	•	Of the loans undergoing human review, there is approximately a 12.5% disagreement rate between AI and human assessments, highlighting higher complexity in the manually reviewed subset.
	•	Repeatability remains a key concern, with roughly 10% of classifications switching outcomes upon retesting, primarily due to inconsistent code logic; ongoing development efforts aim to address these issues before the November regulatory submission deadline.






Here is a detailed, structured summary of the provided transcript:

AI Loan Review and Model Accuracy Discussion:
	•	Model Performance:
	•	The AI model accuracy is currently around 95% based on the P-metric.
	•	84% of loans are processed entirely by AI without human review; 16% require human review.
	•	Of the loans reviewed by humans, 12.5% show disagreement between human reviewers and AI results.
	•	Error Rates:
	•	Approximately 3% of total loan processing is incorrect, based on ground-truth validation.
	•	Discrepancy noted: the 16% of loans flagged for review are inherently more complicated, thus having a higher error rate.
	•	Data Sampling and Validation:
	•	Humans performed detailed sampling on 285 loans to estimate error rates.
	•	Clarification was needed about the sampling method as initial understanding was unclear.
	•	Challenges with Repeatability:
	•	There is a significant repeatability issue: approximately 10% of cases flip classification results (e.g., between equity and credit) when tests are repeated multiple times.
	•	Main cause: poorly structured code with redundant logic paths and inconsistent prompt usage.
	•	Developers are actively updating the model, causing instability in the validation results.
	•	Timeline:
	•	Initially, the deadline for Fed submission was set for the end of the month but later extended to November.
	•	An internal push exists to resolve mortgage-related components sooner.
	•	Oversight and Approval:
	•	MRM approval is critical, yet there was confusion about why the DR (Designated Reviewer) was involved.
	•	Normally DR does not directly involve itself in the approval of models validated by MRM.

⸻

MRM and Control Framework Updates:
	•	IDR Control Assessment:
	•	Discussion highlighted significant pushback from business areas regarding IDR control assessments.
	•	Market Risk showed improved performance in Q2, but GBM’s scores remain problematic.
	•	RCSA Assessments:
	•	Assessments were due recently, but operational challenges arose related to permission issues for accessing confidential findings.
	•	Concerns raised about inappropriate modifications made by other teams to the provided metrics and tables.
	•	Emphasized the need for accuracy and consistency in self-assessment reporting.

⸻

AI Developments and Updates:
	•	Generative AI (GenerVI) Implementation:
	•	Implemented in GIR web portal, enhancing relevance by reordering search results contextually.
	•	Positive reception from users with limited resistance from GIR, who generally prefer minimal oversight over their IP.
	•	Copilot and Agentic AI:
	•	Updates provided on GitHub Copilot and agentic AI initiatives.
	•	Engineering planning to roll out 3 agentic use-cases by year-end from a total of 5 candidates.
	•	Agni Framework:
	•	Training ownership of the Agni framework shifting to the trading desks, allowing customized model training across various business areas (equities, FX, bond market).

⸻

Administrative and Reporting Notes:
	•	Metrics and Reporting:
	•	Discussed appropriate coloring schemes for tables and metrics highlighting urgency or overdue items (e.g., white, yellow).
	•	Noted ongoing cleanup efforts for reporting clarity, specifically regarding overdue findings and waiver-related items.
	•	Q2 Updates and Meetings:
	•	Preparation of summaries and bullet points required for Brian and MRCC updates, covering:
	•	MRA remediation status.
	•	MRCC review of central RCSA guidance.
	•	Updates on IDDR and ongoing validation activities.
	•	ACL, RVE (Reserve Verification Exam), and AQR completion updates.

⸻

Miscellaneous:
	•	Concerns expressed about unclear naming conventions for models (e.g., mortgages, wholesale loans, liquidity).
	•	Brief mention of client-related implications of GIR AI updates, noting that no major complaints or risks emerged from their rollout.

⸻

Key Actions and Next Steps:
	•	Clarify data sampling methods and ensure repeatability issues are resolved before Fed submission deadline.
	•	Reinforce clarity and permissions related to RCSA assessments to prevent inappropriate data modification.
	•	Finalize and clearly document Q2 performance and IDR results for MRCC and Brian updates.
	•	Ensure proper oversight, and accurate documentation is maintained as model updates continue, especially regarding AI loan reviews.






Key drivers of ongoing validation work:
AI continues to show growth, with increasing adoption of new techniques that present novel risks. This spans both the generative AI space—such as enhancements to the Guardrails model, which supports the GS AI Platform monitoring framework—and the non-generative space, highlighted by the first deep learning neural network-based model deployed for algorithmic trading.
Strategic enhancements to risk management capabilities, particularly in counterparty credit risk, remain a focus as part of the firm’s ERMF uplift plans and efforts to address model validation findings.
Additional drivers relate to the firm’s regulatory capital and liquidity requirements, which continue to shape validation priorities.
A key area of focus for 2025 is the planned enhancement of the annual review process to address supervisory feedback. The associated remediation remains on track for year-end completion.






Thanks for the clear feedback. Here’s a revised version of the callout box, incorporating all your points:

⸻

The firm’s AI governance framework builds on and complements existing model risk management practices. All AI is included in the model inventory to ensure appropriate governance standards are applied.

AI use cases are classified into model risk tiers, which determine the scope and intensity of applicable controls. All AI use cases are treated as individual models and require Model Risk validation and approval prior to use.

While AI-related models continue to grow in number, they remain a small portion of the overall model inventory and are primarily concentrated in lower risk tiers.

⸻

Let me know if you’d like a more concise version or to tailor it for a specific format (e.g., memo, slide, report).




The firm’s AI governance framework is built on—and complements—the existing model risk management framework. As AI adoption continues to grow significantly across business lines, the framework ensures consistent oversight through model inventory, tiering, and validation standards.

	Here’s a refined and more concise version of your bullet points:
	•	The firm’s AI governance framework builds upon and complements the existing model risk management framework.
	•	Per the Firmwide Policy on Artificial Intelligence, all AI platforms, applications, and their specific use cases must be captured in the firmwide model inventory and included in the quarterly attestation process to ensure completeness and accuracy.
	•	To strengthen oversight and ensure consistent governance of AI use, Model Risk enhanced the control framework in late 2023 to:
– Align the definition of AI with the Firmwide Policy and mandate its inclusion in the model inventory
– Introduce a Tier 4 model risk classification to cover very low-risk AI use cases that were not previously in scope
	•	All AI use cases are treated as individual models and are subject to Model Risk Management (MRM) validation, in line with the firm’s standards for model approval.Enhancements to margin shortfall modeling, such as (1) inclusion of collateral in the worst-case loss and shortfall calculations for CREST Derivative Clearing Services (DCS) and Futures business to capture risk more accurately, and (2) methodology enhancements to address validation findings relating to the treatment of triparty repos and recalibration of interest rate shocks in shortfall




We presented 10 real-life approval/rejection case studies and, in partnership with Engineering, GBM, and AWM, showcased four strong first-line use cases.



Here’s a detailed summary of the transcript, organized clearly by topic, including all discussion points and additional items intended for Brian’s updates:

⸻

Topics Discussed for Brian’s Update:

1. MRA Remediation
	•	Included, but limited updates available.
	•	Mention tech-related questions circulating regarding the practical implementation process.

2. ER Mesh Uplift
	•	Plans for 2025: Establish a centralized Assessment Unit (AU) for firmwide programs such as Model Risk.
	•	Highlight that the current effectiveness metrics were set intentionally harshly, resulting in many “reds,” even in IDDR areas.
	•	Potential feedback from GBM anticipated due to these strict ratings.
	•	Important to verify Brian’s comfort level with the severity calibration; emphasize that CCR metrics currently appear worst-performing, potentially prompting a recalibration.

3. Control Effectiveness Finalization
	•	Finalization expected this or early next week, but possible delays due to unclear accountability within O-Risk.

4. Encouraging Self-Identified Issues
	•	Discuss with Brian the idea of promoting self-raised issues (thematic findings) by business lines.
	•	Clarify how this would interact with credit received under the RCSA process.

5. LRM and ETSC Updates
	•	Confirm LRM model approval completion.
	•	Clarify the governance around ETSC, as there’s uncertainty if controls are centrally imposed by Compliance or Risk.
	•	Need to discuss with Compliance whether ETSC controls should be standardized and centrally imposed, possibly enhancing consistency in governance.

6. Validation Findings and Metrics
	•	For recent major validations (Items C and D), highlight the notably large number of findings identified.
	•	Emphasize these as indicators of poor model-development practices, reinforcing the need for stronger upfront controls.

7. AI Models and LLM Versioning
	•	Discuss concerns related to frequent LLM version updates (e.g., OpenAI moving from 4.0 to 4.1).
	•	Suggest a more scalable solution, potentially through automated testing like “AI regression tests,” run by the first line.
	•	Emphasize first-line responsibility for ongoing tests, with second-line focusing on ensuring the testing program itself remains robust.
	•	Propose that frequent LLM updates (every 2-3 months) need automated handling rather than manual re-validation approvals.

8. AI Code Repositories and Development Practices
	•	Highlight concerns over fragmentation in AI development practices (e.g., multiple repositories with differing library versions, reduced visibility, and inconsistent testing practices).
	•	Emphasize the importance of maintaining transparency and open-code testing, akin to historical Goldman Sachs practices (e.g., STV’s success).
	•	Flag concerns around proprietary patents filed by GBM and Engineering, possibly creating silos and further complicating transparency and validation efficiency.

9. GSI/GSIB Board Updates
	•	Include updates related to Brian’s role on the GSIB board.
	•	Mention any significant updates from the GSI and GSIB board meetings.

10. Training and Issues Management Terminology
	•	Clarify confusion around “issues management” terminology, as current terminology is creating unnecessary ambiguity internally and externally.
	•	Highlight MRM-specific items relevant to MRAs, especially weaknesses in validation practices and findings management.

11. SR Inventory Completeness Feedback
	•	Note concerns raised by SR about the completeness of model inventories, specifically the Controllers’ decision to exclude certain risks (e.g., strategic or business risk) from capital calculations without a documented methodology.
	•	Clarify ECB’s recommendation: even decisions not to calculate capital (effectively “zero capital”) should be formally documented in inventory.
	•	Consider raising thematic findings against Controllers for not fully ensuring completeness in inventory identification processes.

12. EMA Updates
	•	Include updates on upcoming EMA items:
	•	AQR (Asset Quality Review)
	•	ProVal model updates
	•	UK ICAP completion
	•	Recent ECB submission adjustments (residual risk reclassification from DRC to qualitative approaches).
	•	Mention upcoming EY audit for Purely PSM, noting it will significantly involve MRM documentation review.
	•	Flag differences in regulatory compliance notification responsibility in MRM for UK entities versus the global group.

13. EmoLex DVA Error
	•	Confirm if EmoLex DVA error warrants a formal mention or escalation.

⸻

Additional Items to Include for Brian’s Awareness:
	•	CCR Lotus Completion: Finalize CCR work related to Lotus (including model migration and LRM validation).
	•	AI Committee Meeting Updates: Recent approvals and ongoing issues related to AI/ML models.
	•	Validation Activities: Updates on CCR equities migration to the unified benchmark model and completion of UK ICAP.
	•	Regulatory Updates: MRAs and ongoing CECL model validations.

⸻

Next Steps:
	•	Clarify accountability and timelines for control effectiveness reviews.
	•	Confirm Brian’s comfort level with the severity calibration of model control effectiveness ratings.
	•	Pursue clarification from Compliance on centralized control imposition for ETSC.
	•	Implement scalable testing solutions for managing frequent AI/LLM updates.
	•	Consider a thematic finding on Controllers regarding inventory completeness issues.
	•	Verify and clearly document the ECB’s expectations for model inventory completeness and zero-capital approaches.

This structured summary should provide clear guidance for preparing Brian’s updates and next steps for addressing identified issues.










Sure, here’s a simplified and clearer version:

Firmwide AI/ML Development Training 2025:
MRM organized a training program for all AI/ML developers to promote best practices, improve model quality, and support more efficient reviews.
The session included 10 real-life approval/rejection case studies and featured four strong first-line use cases in partnership with Engineering, GBM, and AWM.
Firmwide AI/ML applications grew to ~200, and the number of model owners increased from ~200 to 300 over the past nine months, reflecting growing interest and engagement.Liquidity Risk Enhancements: Validation efforts continue to focus on improving liquidity risk models. Recent key approvals include a new qualitative approach for classifying liquid and readily-marketable (LRM) assets, aimed at optimizing capital and liquidity metrics, reducing risk-weighted asset (RWA) requirements, and meeting regulatory expectations, as well as models and qualitative approaches supporting our Recovery and Resolution Planning (RRP) submissions to the Federal Reserve Board (FRB) and Federal Deposit Insurance Corporation (FDIC).




Enhancements to the models used for calculating credit exposure under stress scenarios, extending coverage from hedge funds to all margined funds and firmwide unmargined counterparties within the natural resources industry.
	•	Migration of equities franchise business to the Unified Benchmark Model for calculating margin shortfall, aligning with broader ongoing efforts to standardize and ensure consistency across Prime and Franchise businesses.Artificial Intelligence (AI)/Machine Learning (ML) Models: We continue to see significant growth in AI/ML model development and the adoption of new technologies. Recent notable approvals include:
	•	The first AI model utilizing transformer-based deep learning techniques to predict price movements for FX algorithmic trading.
	•	Expansion of our neural network-based pricing tool to include multi-asset structured products.
	•	Enhancements to the generative AI monitoring framework supporting our GS AI Platform, which improves performance, enables the GS AI Assistant to handle multiple document uploads, and provides real-time alerts for detected inaccuracies (pending deployment).

Counterparty Credit Risk (CCR): We remain focused on enhancing and validating our CCR management models in alignment with our Enterprise Risk Management Framework (ERMF) improvement initiatives. Recent significant approvals include:
	•	Extending our stress scenario credit exposure models beyond hedge funds to encompass all margined funds and firmwide unmargined counterparties within natural resources.
	•	Transitioning our equities franchise business to the Unified Benchmark Model, standardizing margin shortfall calculations and ensuring consistency across our Prime and Franchise operations.

Liquidity Risk Enhancements: Validation efforts continue to focus on improving liquidity risk models. Recent key approvals include:
	•	A new qualitative approach for classifying liquid and readily-marketable (LRM) assets, aimed at optimizing capital and liquidity metrics, reducing risk-weighted asset (RWA) requirements, and meeting regulatory expectations.
	•	Models and qualitative approaches supporting our Recovery and Resolution Planning (RRP) submissions to the Federal Reserve Board (FRB) and Federal Deposit Insurance Corporation (FDIC).



Does this revised draft meet your needs, or would you like further Model sensitivity noted regarding “high trading volume” thresholds and Bloomberg data quality, with future enhancements planned to refine classifications and address unintuitive outcomes.




Weekly CRO Update

Top of Mind

CCR Validations:
	•	Coherent Shortfall Model: Validation completed ahead of the June 30 Lotus deadline.
	•	Model scope extended from hedge fund clients to all margined funds.
	•	Six new medium-severity findings identified, addressing unjustified parameters, modeling choices, unidentified risk factors, testing deficiencies, and gaps in ongoing monitoring.
	•	Stressed CCE Model: Extended validation completed ahead of the deadline.
	•	Scope expanded from unmargined natural resources counterparties to firmwide implementation.
	•	Four new medium-severity findings noted, focused on implementation issues and ongoing monitoring gaps.

Liquid & Readily-Marketable (LRM) Classification:
	•	Validation completed prior to June 30 commitment.
	•	Successfully remediated all seven high-severity findings relating to insufficient development evidence, implementation, testing, and documentation.
	•	Model sensitivity noted regarding the threshold determination for “high trading volume” and dependency on Bloomberg data quality. Future enhancements planned to refine Equities classification and address unintuitive outcomes (low materiality or overly conservative results).

⸻

Validation Activities

CCR:
	•	Migration of Franchise Equity Benchmark Model (FEBM) to Unified Benchmark Model (UBM) approved by MRM for shortfall calculations.
	•	This migration aligns with previous SPG model transitions and contributes to broader standardization and consistency across Prime and Franchise segments.

⸻

Regulatory Updates

MRM MRA Remediation:
	•	On track for completion of infrastructure enhancements and training by September 30, ahead of rolling out the enhanced annual review framework.

CECL RVE Examination:
	•	The FRB initiated validation steps for remediation of existing ACL MRIA1 (Inadequate Risk Capture and Ongoing Monitoring for ACL Models) and MRA2 (Weaknesses in Model Risk Management).
	•	Meetings scheduled to occur over a 3–4 week period from July 15 to August 15, prioritizing Wholesale followed by Retail.






Here’s a detailed summary organized by key points discussed:

1. Personal Updates (Vacation and Family)
	•	Carol recently returned from vacation on the U.S. West Coast.
	•	Traveled to three major cities and five national parks, covering about 3,000 miles.
	•	Carol’s parents enjoyed the trip and have returned safely to Shanghai.
	•	Tried visiting the office on the weekend but forgot passwords, took photos around the building instead.
	•	Mentioned long flights (10 hours to San Francisco and 20+ hours returning from New York).

2. Preparation of BRC Deck and Upcoming Reports
	•	Carol is preparing the BRC deck for review on Monday.
	•	Planning for BRC involves selecting thematic topics rather than deep technical details.
	•	Agreed on major topics for the BRC deck:
	•	AI Guardrail 3.0 (keep thematic, not overly technical)
	•	CCR model enhancements
	•	Liquidity Risk Management (LRM)
	•	Potential inclusion of Resolution and Recovery Plan (RRP) and GSI Trading Wind-down updates
	•	Incremental updates on MRM MRA remediation

3. Updates for Brian and CRO
	•	Brian’s update will include CCR and LRM completions.
	•	Possible inclusion of the recent Op Risk (EMMA equity delta hedging) event.
	•	CRO update may mention CCR and LRM completions and the upcoming validation of CECL MRIA/MRA by the Fed.
	•	GSII Capital review status needs verification with the EM team.

4. Regulatory Interactions and Upcoming Meetings
	•	Discussed regulatory engagements:
	•	Fed topical study explicitly restricted AI and recording tools.
	•	Upcoming regulatory meetings related to trading models scheduled for the end of next month and October.
	•	Preliminary impact analysis for the SLR/LR regulatory changes by the research team.
	•	Potential regulatory finding related to a broken link in a TRC model; the team is currently pushing back.

5. Efficiency and AI Initiatives
	•	Emphasized importance of AI and automation for the second half of the year.
	•	Highlighted need for efficiency improvements and automation in processes, especially:
	•	Reporting workflows (Strat PMMD update, Brian update, and RCSA automation).
	•	Encouraging team experimentation and ideation for practical AI uses.
	•	Mentioned the recent AI Hackathon event that aimed at creating efficient prompt engineering examples.
	•	Carol noted ongoing efforts to automate manual reporting burdens, especially inventory and findings pages.

6. M365 Copilot Functionality and Team’s Transition
	•	Carol and the team expect to receive access to Microsoft 365 Copilot soon.
	•	Discussed anticipated capabilities of Copilot:
	•	Assisting in finding and summarizing emails/documents.
	•	Potential functionalities in Excel and PowerPoint.
	•	Noted feedback from peers about Teams Meetings having significant AI utility (summarizing and transcribing meetings).
	•	Firm may eventually transition from Zoom to Teams Meetings, although there’s uncertainty about confidentiality concerns in regulatory contexts.

7. Planning for the Second Half of the Year
	•	Emphasis on:
	•	AI initiatives and efficiency improvements.
	•	Regulatory interaction skills and preparation.
	•	Scheduled follow-up discussion for further strategic planning.

8. Upcoming Key Dates and Deliverables
	•	BRC on July 31st (first draft due around July 8th).
	•	MRCC meeting scheduled for August 16th.
	•	FRA meeting on August 5th and another critical meeting on August 6th.
	•	Ongoing MRA implementation planning.

Overall Focus:
	•	Prioritizing thematic updates to senior management and board.
	•	Continued focus on AI-driven efficiency enhancements.
	•	Ensuring clear communication and preparedness for regulatory interactions.
	•	Planning ongoing automation and improving processes for reporting and internal operations.





You’re absolutely right — the actual Op Risk event referred to by Youness occurs later in his section and relates to DVA (Debt Valuation Adjustment). Here’s a corrected and focused summary of that specific Op Risk event:

⸻

✅ Operational Risk Event (Youness – DVA Issue)
	•	Event Description:
	•	Two risk-free notes incorrectly showed non-zero DVA exposure.
	•	These trades were expected to have zero DVA, but due to a code logic error, DVA was calculated and booked.
	•	Root Cause:
	•	The DVA calculation relies on a hardcoded filter that excludes certain trades by ID.
	•	These two trades were not added to the exclusion list, so the system treated them as having credit risk.
	•	This resulted in an incorrect DVA of approximately -$3 million being booked.
	•	Discovery:
	•	The issue was identified in Q1 2025.
	•	It was brought to MRM’s attention recently by the desk.
	•	Remediation Actions:
	•	The desk is conducting a global check to ensure no other risk-free notes are impacted.
	•	MRM recommended replacing the hardcoded filter with a systematic, programmatic solution.
	•	The suggestion was also made to reflect risk-free status directly in the trade booking, reducing reliance on manual filters.
	•	Follow-up:
	•	It was unclear during the meeting whether the issue was formally logged as an Op Risk event, but it was flagged as having operational risk implications.
	•	A follow-up was proposed to determine if it should be logged and tracked accordingly.

⸻

Let me know if you’d like this turned into a formal Op Risk event report or if you need other sections summarized.




Here is a bullet-point summary of the Operational Risk (Op Risk) Event spoken by Youness in the transcript:

⸻

Op Risk Event (Youness):
	•	Event Description:
	•	Due to a market move, the 30-year minus 2-year rate spread widened to 50 basis points.
	•	This triggered the early call of about 20 callable range accrual notes that were nearing maturity (within 1–2 years).
	•	Cause:
	•	High spread levels increase the cost of future coupon payments, which made it uneconomical for the firm to continue holding the trades.
	•	As a result, the issuer called the notes early to avoid paying further high coupon costs.
	•	Impact:
	•	The operational event primarily involved trade cancellations to avoid further coupon payments, not a model or system error.
	•	Additional Notes:
	•	The issue was flagged due to financial impact from changing interest rate spreads.
	•	It’s unclear whether this was formally logged as an operational risk event, but a follow-up was requested in the meeting.

⸻

Let me know if you’d like summaries of other speakers or model changes as well.





Yibo Li
200 Angelo Cifelli Dr, Apt 263
Harrison, NJ 07029
Phone: (571) 269-7933
Email: yiboli@gwu.edu

June 1, 2025

To: U.S. Customs and Border Protection

Dear Immigration Officer,

I am writing to confirm that my parents, Mr. Guanyao Li and Mrs. Yafang Li, are visiting the United States as tourists. They hold valid B2 visitor visas and are traveling here to spend time with me, visit multiple cities, and experience American culture.

They are scheduled to stay from June 2, 2025, to June 24, 2025, and have confirmed return flight tickets. During their visit, they will initially stay in San Francisco at the Holiday Inn San Francisco-Golden Gateway, located at 1500 Van Ness Ave, San Francisco, CA 94109, before continuing their travels to other destinations. Later in the trip, they will also stay with me at my residence listed above in New Jersey.

I am currently employed under an H-1B visa at Goldman Sachs in New York City. I will be fully responsible for their accommodation and daily living expenses throughout their visit. They do not intend to work, study, or remain in the U.S. beyond their authorized stay.

As they do not speak English, I kindly request your patience and understanding during their entry process. The details of their return flight itinerary are included on the following page for your reference.

If you need any further information, please feel free to contact me using the information provided above.

Thank you very much for your time and assistance.

Sincerely,
(signature if printed)
Yibo Li


Travel Itinerary for Mr. Guanyao Li and Mrs. Yafang Li
U.S. Visit: June 2, 2025 – June 24, 2025

June 2 – Arrival flight: PVG → SFO, arriving at 9:05 AM
Stay in San Francisco, California

June 3 – Stay in San Francisco, California

June 4 – Travel from San Francisco to San Luis Obispo, California

June 5 – Travel from San Luis Obispo to Los Angeles, California

June 6 – Stay in Los Angeles, California

June 7 – Travel from Los Angeles to Las Vegas, Nevada

June 8 – Travel from Las Vegas to Zion National Park, Utah

June 9 – Travel from Zion to Bryce Canyon to Page, Arizona

June 10 – Travel from Page to Grand Canyon South Rim, Arizona

June 11 – Travel from Grand Canyon to Las Vegas, Nevada

June 12 – Travel from Las Vegas to Fresno, California via Death Valley

June 13 – Travel from Fresno to San Francisco, California via Yosemite

June 14 – Fly from San Francisco to New York

June 15–23 – Stay in Harrison, New Jersey
Address: 200 Angelo Cifelli Dr, Apt 263, Harrison, NJ 07029
June 24 – Return flight: JFK → PVG







Here’s a clearer and more concise version of your update:

⸻

Artificial Intelligence Updates
	•	Graph Retriever Model: Approved for retrieving relevant data from knowledge graphs to support Q&A on MD Bios. The model improves semantic search by leveraging structured relationships and contextual understanding. Benchmarking against MRM models confirmed its robustness, though two findings were raised on insufficient ongoing monitoring and code control.
	•	Agni Snowball Autocallables: The neural network-based fast pricer and RFQ tool has been extended to support multi-asset underliers, expanding the Agni suite beyond last year’s single-asset approval. Four medium-severity findings were raised, primarily concerning model performance and implementation.








Here is a draft for the second page summary on how model risk is incorporated into the RCSA (Risk and Control Self-Assessment), including definitions, assessment steps, and implications of ineffective controls:

⸻

RCSA Model Risk Assessment Summary

Background

Model Risk is formally integrated into the Risk and Control Self-Assessment (RCSA) process under the GBM Public Strats Assessment Unit (AU), specifically within the “Develop & Maintain Models” process. This includes two key model risk types:
	•	Risk 1: Incorrect Model Design / Implementation
	•	Risk 2: Incorrect or Inappropriate Model Usage

Each risk is assessed across defined control suites, with resulting ratings impacting firmwide risk visibility and action plans.

⸻

Definitions of Key Terms
	•	IRR (Inherent Risk Rating): The level of risk present assuming no controls are in place.
	•	CSR (Control Suite Rating): An aggregate control effectiveness rating derived from the effectiveness of individual controls.
	•	RRR (Residual Risk Rating): The remaining level of risk after controls have been applied. It is a function of both IRR and CSR.

⸻

Assessment Steps
	1.	Inherent Risk Rating (IRR):
Each model-related risk is evaluated based on its potential impact and likelihood, assuming no controls are present. Both risks currently carry a High IRR.
	2.	Control Rating:
Each control associated with the risk is individually rated as:
	•	Fully Effective
	•	Adequately Effective
	•	Ineffective
	3.	Control Suite Rating (CSR):
The CSR is calculated based on thresholds:
	•	Fully Effective: ≥70% of controls are Fully Effective and <15% are Ineffective
	•	Adequately Effective: Combined (FE + AE) ≥85%, with FE <70% and IE <15%
	•	Ineffective: ≥15% of controls are Ineffective
	4.	AU Assessment / Residual Risk Rating (RRR):
Based on the CSR and IRR, the residual risk is mapped using the RRR matrix. For example:
	•	R1 (with a CSR of Ineffective and IRR of High) results in a High RRR
	•	R2 (with a CSR of Fully Effective and IRR of High) results in a Low RRR

⸻

Implications of Ineffective Controls
	•	Risks assessed with Ineffective CSR lead to formal Issues being raised.
	•	These issues are recorded as Thematic Findings in ModelIT, which automatically feeds into Enterprise Issue Repository (EIR) for central issue tracking, governance, and remediation oversight.

⸻

Let me know if you’d like this in presentation format or want to include visual excerpts from the image.






Here’s the detailed methodology and a downloadable Excel-style table shown above:

⸻

🧮 Detailed RCSA Model Control Rating Methodology (3-Point Weighted)

Step 1: Input Data Structure

Each Assessment Unit (AU) includes:
	•	Number of models
	•	Three control effectiveness ratings:
	•	Model Development Control
	•	Model Change Control
	•	Model Ongoing Monitoring Control

Step 2: Convert Ratings to Numeric Scale

We assign a numeric score for qualitative control ratings:

Rating Label	Numeric Score
Ineffective	1
Adequately Effective	2
Fully Effective	3

Step 3: Compute Average Score per AU

\text{Average Control Score}_{AU} = \frac{\text{Dev Score} + \text{Change Score} + \text{Monitoring Score}}{3}

Step 4: Apply Model Weighting

\text{Weighted Control Score}_{AU} = \text{Average Score} \times \text{# Models}

\text{Overall Weighted Score} = \frac{\sum (\text{Weighted Control Score})}{\sum (\text{# Models})}

Step 5: Map Overall Score to Qualitative Rating

Weighted Score Range	Final Rating
1.00 – 1.66	Ineffective
1.67 – 2.33	Adequately Effective
2.34 – 3.00	Fully Effective


⸻

The displayed table shows:
	•	Each AU’s scores
	•	The model-weighted contribution
	•	A calculated final qualitative rating
	•	A summary row with the overall weighted rating

Let me know if you’d like this exported as an Excel file or extended to include more AUs. ￼





Here’s a trimmed and simplified version of your update:

Resolution Recovery Plan (RRP):
MRM approved seven Tier 1 models and four Tier A qualitative approaches for the RRP Title 1 bi-annual submission. Key enhancements included:
	•	Business-level segmentation for trading wind-down in response to FRB feedback
	•	Alignment of intercompany repo/reverse repo treatment with Modeled Liquidity Outflow (MLO), following a reassessment by modelers and MRM
	•	Additional updates based on MRM findings and developer-identified issues, including alignment of runway assumptions with MLO
	
		
			
				
					
							•	Resolution Recovery Plan (RRP):
	•	MRM validated and approved 7 Tier 1 models and 4 Tier A qualitative approaches, including 2 initial validations, for the RRP Title 1 bi-annual submission.
	•	Key enhancements included:
	•	Added business-level segmentation for trading wind-down, addressing FRB feedback, resulting in a $9bn reduction in Peak Funding Need (PFN).
	•	Implemented various improvements and bug fixes based on MRM findings and developer self-identified issues.
	•	Adjusted treatment of intercompany repo/reverse repos to align with MLO, reducing PFN by $10bn, which required Board approval due to its impact.
	•	GSI Trading Activity Wind-Down (TWD):
	•	Validated and approved 26 models and 6 qualitative approaches as part of enhancements to comply with PRA’s TWD requirements effective from March 3.
	•	Of 57 findings identified, 26 have been resolved and closed, including all high-severity issues. One qualitative approach is currently under validation and used with a waiver.
	•	Submission to PRA included findings from MRM validations and self-assessment against SS 3/18 model risk management principles.
	•	Held a 4-hour meeting with PRA on May 15, addressing questions on validation approaches and open issues. PRA expects to finalize their review by January.



Here’s a clear, concise draft for the footnote:

Footnote:
For Development Control and Model Control, metrics are calculated based on IR model scope with data as of May 16. For Inventory OM and Change Control, metrics reflect data as of the end of Q1 at the assessment level, not specifically scoped to TI models.




Detailed Transcript Summary

RTSA Results for IDDR Models
	•	Results were presented in a summarized table format, printed concisely onto one page.
	•	Metrics are based on a four-point scale defining thresholds clearly.
	•	Specific clarifications requested:
	•	Footnote required:
	•	Metrics for Development Control and Model Control based on IR model scope data as of May 16.
	•	Inventory OM and Change Control metrics calculated as of end of Q1 at the assessment (uter) level, not scoped specifically to TI models.
	•	The “IDDR” models discussed are a one-time ad hoc exercise for July; thus, additional detailed clarifications for these are unnecessary.
	•	Confirmation that ineffective remediation findings and excessive indicators should not be assumed as fully effective and should be excluded.

Table Ranking and Additional Analysis
	•	Current ranking in tables is based on the number of models.
	•	Received a request from Bill to rank Assessment Units (AUs) by “badness” (risk level).
	•	An additional table will address Bill’s specific request.
	•	The team agreed sorting by number of models is currently practical, pending Bill’s feedback.

Brian’s Update
	•	Progress ongoing; feedback gathering from various stakeholders continues.
	•	Recommendation given to simplify and make internal feedback notes less formal and more direct, highlighting essential actions clearly.
	•	Confirmed the recalibration of the threshold scale from a four-point to a three-point scale may be considered going forward, but verification is required on whether to show Q1 results again using the new scale to Brian, pending Bill’s decision.

Regulatory and Audience-specific Communications
	•	Acknowledgment that updates for Brian should differ significantly from broader audience updates.
	•	Communication to general stakeholders (excluding detailed audience like Alex, Bryant, Gopi, who have already received extensive information) needs to be concise, high-level, and clear.
	•	Main points for the broader audience include:
	•	Enhancements reviewed positively with the Fed and MRCC.
	•	Next steps clearly outlined.
	•	Simplified bullet points recommended for communicating Fed feedback.

Additional Suggested Topics
	•	ERMF uplift: Include recalibration to a three-point scale and preliminary results on model risk metrics.
	•	Regulatory updates: Briefly mention ongoing initiatives:
	•	Capital model approval requests.
	•	Preparations for the 2025 examinations.

Next Steps
	•	Aim to finalize a clear and concise draft for Brian’s update by the following morning.





Please review and let me know if any adjustments are needed!




Here’s the simplified and refined summary:

AI Guardrail 3.0: MRM has approved the enhanced AI Guardrail 3.0 (Tier-1), enabling the GS AI Assistant to handle larger and multiple documents, supporting up to 500,000 tokens (~750 pages). Guardrails include both monitoring and preventative controls, applicable across the firmwide AI platform. A new feature is under development to indicate hallucinated content to users before enabling preventative blocking.

AI FX Algo Trading Signal: MRM approved a transformer-based AI model for the FX eDealing Client Pricing algorithm, enhancing the FX algorithmic market-making business. The model effectively predicts the direction of price movements for a basket of major FX currency pairs, demonstrating strong performance in high-frequency trading scenarios.




Sure, here’s a concise version in two sentences:

Assessment Units are ranked from worst to best based on the number of Ineffective ratings, followed by Adequately Effective ratings. If there is a tie, the unit with more models is ranked worse.





Here’s a structured summary for Brian’s update based on the provided discussion transcript:

1. MRM / MRA Remediation
	•	Update Brian on the recent Fed meeting outcomes and immediate next steps.
	•	MRCC review scheduled before Thursday; highlight importance of MRCC engagement given the substantial nature of framework changes.
	•	Plan to distribute review materials to MRCC today to encourage pre-meeting familiarization.

2. Enterprise Metrics Framework (EMF) Uplift
	•	Progressing on using a three-point scale for IDR (Issue, Deficiency, and Risk) areas; summary to be prepared in Brian’s preferred new format.
	•	Solicit Brian’s view on consistency between three-point vs. four-point scales across different areas (e.g., issues management vs. RCSA).
	•	Consider additional metrics for tracking, e.g., attestation lateness.
	•	Initiate preliminary discussions on metrics for Electronic Trading Supervision and Control (ETSC), to be established by year-end.
	•	Clarify current state and completeness of the risk taxonomy, specifically regarding electronic trading risks and associated control effectiveness metrics.

3. ERM and Breach Response Plan
	•	Provide status update on the breach response plan submissions to FRAC (Financial Risk and Control Committee).
	•	Start with weekly updates on breach response submissions, transitioning to bi-weekly once established processes stabilize.

4. EMEA Capital Governance
	•	Summarize key points from Simon’s planned EMEA capital governance sessions, noting current delay/rescheduling.
	•	Outline intended discussion topics clearly for Brian’s concurrence.

5. EMEA Data Governance (DGO)
	•	Recap previous skepticism from Brian regarding the materiality of perceived gaps.
	•	Provide update on recent gap assessment by KPMG, specifically their findings on data usage in model development/calibration.
	•	Clarify KPMG’s involvement scope and the sponsoring party for their assessment.

6. CCR (Counterparty Credit Risk)
	•	Provide updates on recent validations and findings.
	•	Highlight status on larger, firm-wide CCR model projects.
	•	Prepare explanations addressing Brian’s consistent concern about delays, particularly focusing on historical context rather than recent extensions.

7. Resolution Planning
	•	Summarize internal audit (IA) findings related to implementation review obligations for QA (Quality Assurance) tasks.
	•	Propose approach to manage the transfer of these tasks to the team, focusing on robust implementation validation, following IA’s raised concerns.
	•	Clarify and confirm with Brian and Alex the interpretation and adequacy of current QA policy vs. actual practices.

8. AI / Guardrail Updates
	•	Update Brian on recent Guardrail 3 approval, emphasizing enhancements (improved detection capabilities, explainability, preventative blocking plans).
	•	Provide outlook on testing plans (initially observational, transitioning to preventative blocking).
	•	Discuss preliminary ideas or future roadmap considerations for Guardrail 4 (though currently no defined plans exist).

9. Copilot and Generative AI Tools
	•	Inform Brian on the pilot rollout of Microsoft 365 Copilot, highlighting user feedback on interface convenience and general usability.
	•	Provide updates on the streamlined approval of Anthropic as an additional LLM provider.
	•	Briefly note recent IRCC discussions and debates around AI implementations, control vs. engineering perspectives.
	•	Mention upcoming FRB AI-focused meeting (June 18); seek attendee list clarification.

10. Pricing Models / Market Risk Updates
	•	Review current discussions with market risk specialists, particularly:
	•	Positional stress tests around funding spreads in equities.
	•	Private equity valuation discrepancies, especially in tech and fintech sectors.
	•	Verify with specialists if current developments warrant Brian’s attention from a model risk perspective.

11. Electronic Trading Incident
	•	Detail recent critical issue in Equity Delta Hedging Facility (EDHF) involving stale risk data caused by overloaded servers.
	•	Clearly explain the risks posed by incorrect hedging, implications if incident duration was longer, and highlight gaps in existing controls.
	•	Propose steps for deeper analysis and possibly enhancing electronic trading control infrastructure.

12. Other Regular Updates
	•	Highlight recent validation of pricing models, if noteworthy.
	•	Include brief mention of the National Futures Association (NFA) updates, subtly indicating ongoing irritations/issues without explicit detail.

13. MRCC Administrative Items
	•	Announce upcoming MRCC membership changes (Ken leaving; additions include Giuseppe, David Jeria, Ariana).

This structured outline captures all major topics discussed, clearly delineating items to update Brian on, questions requiring his input, and key points needing further action or clarification.















Here’s a detailed summary of key items to include for Brian’s update and the Alex/CRO update based on the provided transcript:

For Brian’s Update:
	•	ERMF Uplift: Include detailed updates on the Enterprise Risk Management Framework (ERMF).
	•	DRC Program: Summarize key issues regarding the DRC extension, including uncertainties around capital governance, regulatory implications, and proposed paths forward.
	•	Capital Governance: Emphasize the proposed approach involving three key programs: M&T (Model & Testing), Data Governance, and DRC, highlighting Simon’s recommended approach.
	•	CCR (Counterparty Credit Risk): Provide detailed updates, noting that substantial CCR content has not been given recently and should now be addressed.

For Alex/CRO Update:
	•	MRA Remediation: Highlight recent feedback from the Fed meeting, noting particularly positive feedback on the progress and detailed enhancements discussed in MRCC.
	•	AI Guardrail 3.0: Emphasize recent updates or developments, given its importance.
	•	CCAR: Provide any recent updates or notable items, acknowledging that significant changes or updates might be minimal.

General Guidance for Updates:
	•	Include specific summaries where the information is confirmed and clear.
	•	For uncertain topics, use placeholders pending further confirmation or input from Bill.
	•	Clearly highlight the positive feedback from recent regulator interactions to underscore progress.

This structure will ensure both Brian and Alex/CRO updates are comprehensive and aligned with current strategic priorities and recent developments.







Certainly! Here’s a direct quote from the transcript you can include to reflect that addition clearly:

“We’ll also provide you with those MRCC materials once they’re finalized and after the meeting. So you can actually see the exact changes that we’re proposing.”

“We’re also happy to provide you with those examples once they’re ready. And we, of course, would welcome any feedback.”

You can incorporate this into your notes to explicitly document MRM’s offer to share both MRCC materials and annual review mock-up examples once available.



MRM offered to submit finalized MRCC materials following their review meeting, as well as detailed annual review mock-up examples once ready. These materials aim to clearly demonstrate the proposed changes and enhancements to the regulator, and feedback was specifically invited.






Does this structured summary meet your expectations, or would you like any refinements?

Meeting Minutes – Regulator Meeting

Invalidated and Rejected Models:
	•	Regulator inquired about unvalidated models in use and whether there were thematic issues.
	•	MRM responded:
	•	Tier 1 Models: Utilization is low, mainly due to significant model changes implemented before validation.
	•	Tier 2 Models: Primarily driven by GBM, AWM, and Controllers. Controllers’ issues relate to capital add-on calculations for EMEA legal entities.
	•	Tier 3 Models: Utilization relatively low.
	•	Regulator asked about rejected models.
	•	MRM explained rejections were due to regression testing failures exceeding 14 days, triggering model rejections and escalations, which have since been resolved.

Threshold Breaches (Page 10):
	•	Regulator inquired about breaches related to invalidated Tier 2 models aged over six months and Tier 1 models with findings aged over nine months.
	•	MRM responded:
	•	Tier 2: Breaches related to capital add-on calculations delays, with one resolved and two expected to be approved shortly.
	•	Tier 1: Issues were primarily in the counterparty credit risk area (margin shortfall calculations) with significant management attention and ongoing remediation efforts.

Generative AI (Gen AI) Usage:
	•	Regulator asked about increased usage and governance of generative AI models.
	•	MRM explained proactive steps initiated in 2023, establishing firm-wide AI governance and the AI Risk and Controls Committee. Growth has been gradual, focusing on low-risk productivity-enhancing tools.
	•	MRM highlighted two Tier 1 AI models: one for AI platform monitoring (guardrail model), and one related to ESG metrics.
	•	Regulator asked about committee composition and risk coverage.
	•	MRM explained committee membership includes stakeholders from Legal, Compliance, Operational Risk, Tech Risk, Engineering, and MRM, ensuring comprehensive risk review and monitoring of all AI use cases.

MRA Remediation Progress:
	•	Regulator requested an update on MRA remediation.
	•	MRM provided an overview:
	•	Completed first milestone (enhanced annual review templates) with external consultant input.
	•	Scheduled to review enhancements with MRCC.
	•	Created differentiated templates for Tiers 1-3 and Tier 4 models, enhanced question structure and guidance, requiring detailed commentary for all questions.
	•	Proposed exemption from annual reviews in revalidation years, aligning with industry practice.
	•	Next steps include system enhancements and team-wide training, starting with mock reviews.

Tier 4 Model Reviews:
	•	Regulator asked about newly introduced Tier 4 models (low-risk AI/ML models).
	•	MRM explained:
	•	Tier 4 specifically addresses low-risk AI/ML models recently included in inventory.
	•	Annual reviews focus on ongoing monitoring and maintaining low risk, elevating tier and review rigor as necessary.

Conclusion:
	•	Regulator acknowledged remediation progress, expressing satisfaction with proposed enhancements.
	•	MRM committed to providing further documentation (examples, MRCC materials) and remaining available for additional meetings.
	•	Regulator agreed to have additional internal review by David Palmer for final feedback.




Key Guardrail 3.0 Improvements:
	•	Better hallucination detection, including subtle cases.
	•	Improved processing of longer documents.
	•	Upgraded LLM to Gemini Flash 2.0.
	•	Clearly separated Prompt Injection detection from PII/Harmful content detection.
	•	Expanded proprietary dataset for improved fine-tuning.




220 models underwent additional validation or revalidation in Q1, primarily driven by:
	•	The annual review process, notably including (1) implementation of the multi-risk-factor stress methodology for the credit risk scenario design model, (2) enhancements to risk factors and applicable markets for the investment decision model used for interest rate swaps across markets, (3) improvements to equity volatility risk models ensuring consistent proxy granularity and refining the volatility surface shock methodology, and (4) enhancements related to the Interest Rate Risk (IRR) model, including backtesting improvements.
	•	Insufficient documentation, testing, and ongoing monitoring.




I’ve combined the numbered items into one sentence as requested. Let me know if further adjustments are needed!



I’ve combined the numbered items into one sentence as requested. Let me know if further adjustments are needed!



I’ve combined the numbered items into one sentence as requested. Let me know if further adjustments are needed!
	
		
			
					•	Participated in CCAR exam meetings this week covering market risk, credit card provisions, and PPNR.
	•	Regulators emphasized reviewing and validating assumptions and qualitative adjustments, especially ensuring robust governance and challenge processes.
	•	Discussions on PPNR particularly addressed modeling approaches in GBM Public and Private sectors, focusing on adjustments related to firm-specific risks.

Continue regulatory engagement, including recent follow-ups from the FRB CTO quarterly on ESG AI, preparation for the upcoming Generative AI meeting with SEC/FINRA, and responses to FCA inquiries related to the GS AI Assistant.
	
		
			
				
						•	A loss of $121k occurred due to incorrect market data used by an automated trading system for equity risk management in Japan.
	•	The issue was caused by a system failure; the error was manually corrected by a trader, as existing controls didn’t detect this specific scenario.
	•	New automated controls have been implemented to prevent similar incidents, with additional risk assessment planned.



https://www.atlassian.com/data/charts/stacked-bar-chart-complete-guide

“One important consideration in building a stacked bar chart is to decide which of the two categorical variables will be the primary variable (dictating major axis positions and overall bar lengths) and which will be the secondary (dictating how each primary bar will be subdivided). The most ‘important’ variable should be the primary; use domain knowledge and the specific type of categorical variables to make a decision on how to assign your categorical variables.”

In your case:

Model Tier reflects hierarchy or domain importance (Tier 1–4), and likely drives the structure of validation efforts.

Validation Outcome is a dependent result of the process.

Therefore, the guidance suggests that Model Tier is the more appropriate variable for the x-axis (primary category), while Outcome is suited for stacking (secondary category).

Also relevant is:

“Variables with more levels are generally better as primary variables; we want to limit the number of secondary levels to a fairly small amount to make the stack breakdowns easier to read.”

Since your Model Tier variable has 4 levels and Outcome has 2, the document supports placing Model Tier on the x-axis, with Outcome as the stacked segments.

Let me know if you'd like a one-page summary or visual aid referencing this guidance.




That’s a very good question — and it touches on an important nuance in data visualization: chart titles describe what is being measured, but not necessarily how the data must be structured.

📌 Key Consideration: What is the primary comparison you want to show?
Let’s break it down:

🟦 Chart Title: "Model Validation Outcomes"
This tells the viewer what the chart is about — i.e., the result of the validation process — but it doesn’t dictate whether outcomes or tiers belong on the x-axis. That decision depends on what dimension you want to compare across:

Option 1: X-axis = Model Tiers
Interpretation: “Here’s how outcomes (Approved/Rejected) differ across model tiers.”

Viewer takeaway: Outcome patterns by tier

Typical for internal model inventory reviews or governance presentations

✅ Recommended when your goal is:

"How do validation outcomes vary across different tiers?"

Option 2: X-axis = Outcomes
Interpretation: “Here’s how the number of models from each tier contributes to each outcome.”

Viewer takeaway: Tier contribution within each outcome

Less common unless focused on categorizing models by outcome

✅ Valid when your goal is:

"What tiers are most represented in Approved vs. Rejected categories?"

🧠 Visualization Practice Consensus
Most data visualization guidelines (e.g., from Atlassian, Storytelling with Data, and Datawrapper) emphasize that:

The x-axis should represent the categorical variable you're comparing (e.g., Tiers)

The stacks or bars should reflect composition or outcome breakdown

So even though the chart is named “Model Validation Outcomes,” that does not mean the x-axis must be “Outcomes.”



Here’s a cleaner and more polished version of your sentence:

There is continued growth in the development of generative AI models, including the recent approval of enhancements to the model serving as a monitoring framework for the GS AI Platform, designed to detect potential unsafe conversations between users and a large language model (LLM) (e.g., hallucination, profanity, prompt injection, personally identifiable information), and now extended to enable real-time hallucination blocking, shifting its role from monitoring to preventative control.

Would you also like an even slightly more concise option?





Issue-Management Talking Points
	•	Clarify the remit
	•	Issues Management (IM) is a first-line tool to record and remediate model-performance or control gaps; Model Risk remains a facilitator, not the owner.
	•	Avoid “model-risk cutting” perceptions by keeping ownership with Liquidity/Res Engineering, Finance Risk, etc.
	•	Current coverage & pain points
	•	IDDR AUs: controls stand-up targeted for end-Q2 2025; firm-wide by year-end 2025.
	•	Controls not yet embedded ⇒ IM metrics red-flag many items that are actually implementation lag, not true defects.
	•	Overdue inventory (Apr-29-2025 cut): GBM 156 / Risk 90 models (~10–12 % of their inventories) driving the red status.
	•	Metrics & thresholds
	•	Draft severity thresholds (count & aging) complete; ready for production once controls are live.
	•	Proposal: announce a go-live date now (e.g., 1 Oct 2025) and a grace period during which AUs must clear or formally waive aged items.
	•	Escalation path
	•	Models breaching thresholds auto-generate High-Severity findings with predefined remediation milestones.
	•	Mid-May Controller CVA waiver is a test-case: if timeline slips, AU must table a revised plan immediately.
	•	Regulatory & audit backdrop
	•	Fed exam teams already probing link between ER tracker and IM; mixed vocabulary is causing confusion.
	•	Internal Audit likely to raise a finding if systematic IM isn’t demonstrated in 2H 2025.
	•	Actions for Brian
	1.	Endorse the proposed go-live date and grace-period message.
	2.	Signal to AU heads that overdue backlogs will trigger automatic High-Severity findings post–go-live.
	3.	Support resource allocation to the two heaviest offenders (Market-Risk Strats & Risk-Economic Strats) to reduce red items before Q4.




Executive-level take-away

Brian’s next update needs to knit together three threads: (1) growing regulatory/exam pressure around model performance vs. model‐control governance, (2) near-term deliverables and deadlines across validation, waivers, and AI governance, and (3) the emerging need to escalate overdue models and findings through a more systematic issues-management playbook.  The talking points below are ordered the way the team suggested presenting them to Brian.

⸻

1. Exam response & “IRR/IDDR confusion”
	•	Clarify the purpose of the Liquidity-Risk/Engineering tracker – it is first-line performance monitoring, not a Model Control Policy artefact.
	•	Stress that Model Risk is coordinating but must not become the de-facto owner of exam findings; ownership stays with first line.
	•	Flag risk of leaving the exam with an unintended “model-risk cutting” finding; action: align vocabulary and responsibilities before the next Fed touchpoint.

2. Model-Control & RCSA roll-out
	•	Status by division
	•	IDDR AUs fully stood-up target → end-Q2 2025
	•	Firm-wide roll-out target → end-2025
	•	Show-and-tell for Brian
	•	One-pager matrix: all Risk AUs with their Model-Risk controls, RCSA mapping, primary/secondary sign-offs.
	•	If possible, a parallel view for Controllers (IPV vs. RevCap split still under discussion).
	•	Note GBM–Model-Control meeting likely to move forward (check new date).

3. Personnel / capacity
	•	Introduce Emma (May intake) now assisting the team.

4. AI / Generative-model governance
	•	MRM AI Assistant pilot and related regulatory threads – bundle under one bullet.
	•	VerCopilot (S-1 generation) status; highlight AWS-Hosting & Engineering pushback (WM driven).
	•	Two weeks until FID-T Explainability & Data-Science submission → offline working session to finalise, then release to Compliance.

5. Validation pipeline & “Lotus” deadlines
	•	US vs. PRA divergence
	•	US models will stick to 2025 Lotus timeline; PRA path still undecided but will likely rely on current QAs/manual processes in the interim.
	•	Provide Brian any colour on feasibility of running parallel rating methodologies.
	•	Early validation themes – data representativeness, conceptual soundness (e.g., Antonas Ray conceptual issue).

6. CCAR & firm-wide stress metrics
	•	New Firm-Wide Asset Loss Metric (extension of un-margined metric) moving from exposure to loss basis.
	•	Validation working to reconcile weak- vs. six-month shocks; need written methodology.
	•	Confirm June deliverables and any further phases for Canal and related projects.

7. Controller CVA waivers (critical path)
	•	Mid-May target at risk; Controllers still refining justification language.
	•	Action for Controllers: if the date will slip, surface a revised plan immediately with root-cause detail.
	•	Escalate to Brian that this waiver is closely tracked by Zero Committee.

8. Inventory, metrics & issues-management escalation

Area	Total models	Overdue / waiver	%
GBM (all)	~1,500	156	≈10%
Risk	~750	90	≈12%

	•	Most overdue Risk models sit in Market-Risk Strats & Risk-Economic Strats AUs.
	•	Proposed next steps
	1.	Finalise severity thresholds (already drafted) and set a go-live date for systematic raising in Issues Management.
	2.	Communicate grace period end to AU owners; remediation playbooks ready.
	3.	Prepare for potential Internal Audit scrutiny if delays persist.

9. Miscellaneous regulatory items (one-line bullets)
	•	ILST methodology updates – ready to brief.
	•	SEC NPR (new market-risk rules) – no immediate action for Model Risk; monitor.
	•	FIS code exam wrap-up – largely handled by MRM; worth a closing remark.
	•	ETSC findings – four on-track for June closure; credit-mark negotiation completed.

⸻

Suggested deck structure for Brian
	1.	Exam & Ownership Clarification (slide)
	2.	Model-Control / RCSA Map – Risk & Controllers (tables)
	3.	Key Deliverables Calendar (timeline graphic)
	4.	AI Governance Snapshot (bullet slide)
	5.	Validation & Lotus Status (narrative + heat-map)
	6.	Waivers & Overdue Models – Metrics & Next Steps (chart)
	7.	Regulatory Odds-and-Ends (overflow slide)

This coverage should equip Brian to answer likely questions on governance scope, upcoming deadlines, and the plan to impose more disciplined issue escalation.








Got it — keeping your original start (“new model for pricing callable credit-linked notes (CLNs),”), here’s the improved version:

New model for pricing callable credit-linked notes (CLNs), using dynamics that incorporate both stochastic hazard rates and stochastic interest rates, addressing the limitations of existing approved models that assume deterministic hazard rates.

Would you also like an even slightly smoother version with minimal change, like adding just one word to make it read even more naturally (e.g., “has been introduced”)?



Implementation Requirements by Phase:

The initial implementation of the Deterministic Regulatory Calculation (DRC) framework for the calculation of U.S. Standardized Approach Risk-Weighted Assets (RWA), addressing direct regulatory feedback, must comply fully with all requirements specified in this Policy.

Any subsequent extension of this framework to include calculations related to the Global Systemically Important Bank (GSIB) surcharge and the Supplementary Leverage Ratio (SLR), as part of the firm's Enterprise Risk Management Framework (ERMF) enhancement initiatives, must also fully comply with all requirements outlined in this Policy.

A detailed plan for the remaining implementation activities concerning U.S. regulatory capital ratios under the Federal Reserve Board’s risk-based and leverage capital regulations will be provided during the Policy's annual review. This plan will include clearly defined timeframes within which the DRC implementation will achieve full compliance with this Policy.



Thank you — that’s a very important clarification.
You’re saying the issue isn’t traders randomly picking marks, it’s that there’s no reliable market price available for them to mark to.
This needs to be worded carefully to reflect that.

Here’s the revised version staying very close to your structure with “and”, now properly reflecting mark-to-market difficulties:

⸻

Volatility and correlation calibration issues were observed in multi-cross FX trades due to increased volatility and skew, and challenges in sourcing reliable market prices for marking; a temporary solution with limited impact has been approved, and further investigation is in progress.

⸻

Another polished version, a little more formal but still matching your original structure:

Volatility and correlation calibration issues were observed in multi-cross FX trades due to increased volatility and skew, and difficulty identifying reliable market levels for marking; a temporary solution with limited impact has been approved, and further investigation is in progress.

⸻

Small but important details fixed:
	•	“Challenges in sourcing reliable market prices for marking” = focuses exactly on mark-to-market.
	•	“Difficulty identifying reliable market levels” = another variation if you want slightly more formal tone.
	•	Preserved your “and”, your structure, your meaning, without making it sound alarming (“unreliable market data” sounded bad — now it’s more professional).

⸻

Would you like me to also show a super crisp version for an executive deck or slide, if you want an even sharper cut?
(Only if you need.)





Got it — you want a version that defines not just AMC, but also CM, MC, SFL, etc.
Here’s a much clearer rewrite where I lightly define the acronyms in-line:

⸻

Efficiency and strategic risk architecture initiatives, including recent approval of enhancements to the American Monte Carlo (AMC) regression framework — a simulation-based approach for valuing options with early exercise features — to improve the numerical implementation for credit products, particularly for Monte Carlo (MC) simulations of credit multi-coupon (multi-CM) payoffs used across Strategic Financing Lending (SFL) businesses, including public and private transactions and exotics, with future plans to extend usage to other asset classes such as CVA tradables, as part of a broader optimization effort.

⸻

Summary of what I did:
	•	AMC → American Monte Carlo (simulation-based approach for early exercise options)
	•	MC → Monte Carlo (simulation method)
	•	multi-CM → multi-coupon (multi-CM) payoffs
	•	SFL → Strategic Financing Lending (SFL)

Quick check:
	•	AMC = American Monte Carlo = simulation approach used when valuing American-style options (early exercise possible)
	•	MC = Monte Carlo simulation = random sampling to simulate price paths
	•	CM = multi-coupon structures = multiple cash flows/payoffs at different times
	•	SFL = Strategic Financing and Lending = business segment handling specialized financing (including public/private side)

⸻

Would you also like a version that’s even a little shorter, in case you need to make it even more compact?
(Depends if you’re writing for a deck, email, or formal memo.)




Got it — keeping your structure and phrasing for the first part exactly, and fitting everything into one clean sentence, here’s the improved version:

Enhancements to the approach for adjusting barrier levels (“barrier shift”) used for pricing multi-asset equity autocallables to be dynamically updated based on volatility versus the previous approach of determining the adjustments at the time of the trade, while also capturing the additional Vega introduced by applying a cap and floor to volatility-based shifts that was previously not reflected in trader-marked values.

⸻

Would you like a second version that’s slightly more formal (just in case you need it for a very polished memo)?



Model Risk has approved the change to re-mark US Volex’s USD YCRA book, restoring the pre-December 2022 MEE-window pricing methodology used for other callables after validating the supporting code update.



Here’s an expanded and detailed summary specifically highlighting the PR call items:

⸻

PR Call Items (Detailed):
	•	CCAR Updates:
	•	Provide a briefing on recent internal CCAR-related meetings held this week.
	•	Update the team on the NPR (Notice of Proposed Rulemaking) issued by the Federal Reserve (Fed):
	•	The Fed is seeking industry comments regarding potential changes to the CCAR process.
	•	Expectation set that this NPR is part of broader adjustments anticipated later this year.
	•	Industry groups, including possibly GS, are preparing detailed responses, coordinated by EO and Controllers teams, on proposed CCAR-related regulatory changes.
	•	Other Regulatory Updates:
	•	Mention that FRB exams recently concluded a follow-up meeting, specifically discussing updates and follow-ups regarding ALST (Asset Liability Stress Testing).
	•	Highlight any critical points from the exam follow-ups, stressing continued regulatory engagement and ongoing compliance requirements.
	•	General acknowledgment of active regulatory oversight, potentially noting positive developments or progress in addressing prior regulatory feedback.
	•	General Expectations:
	•	Reinforce awareness of ongoing regulatory developments relevant to the firm, emphasizing preparedness and proactive management.
	•	Clarify that although no immediate action items from the NPR for CCAR are currently assigned to the team, staying informed remains important due to potential future implications.

⸻

This expanded version ensures clarity on the CCAR-related NPR, highlighting the regulatory engagement’s strategic relevance, and explicitly notes the ongoing follow-ups from recent FRB meetings as important discussion points.







Here’s a concise summary of the provided transcript, emphasizing the final part titled “PL Call Items”:

⸻

Policy Update (DRC Policy)
	•	The team is updating the DRC policy to align with the required “policy on policies” format.
	•	Carly instructed to include an “implementation plan,” referencing a data governance policy as an example.
	•	The policy applies to US regulatory capital under FED rules, specifically the standardized approach. Scope needs to reflect completed and pending implementations clearly.

CRO Update
	•	Reviewing CI and shortfall breaches; no significant model issues identified despite VAR breaches.
	•	Team clarified the placement of EBS stress tests under validation activities, noting consistency with IR and CCR validation activities. Focus remains on MRA remediation rather than ERMS.

Risk Weekly Review
	•	Responsibilities split clearly: GBM updates by the speaker, Ariana manages ENA updates with inputs from Y and Cedra.
	•	Sandra raised queries for FR updates and is independently tracking these updates.

FRAC/BRC and FED Materials
	•	First drafts for FRAC/BRC updates nearly ready.
	•	FED material updates pending; additional model performance issues and market risk model updates likely required, especially MR remediation.
	•	IA updates planned for completion shortly.

Jury Duty Schedule
	•	Uncertainty over jury duty on Monday; unable to commit to specific scheduling for BRC/FRAC meetings until after confirmation.
	•	Speaker to communicate their availability after confirming their jury schedule.

Other Meetings and Upcoming Schedules
	•	Next week’s Scraps meeting scheduled; Brian’s meeting scheduled for the following week.
	•	Alex’s meeting occurs bi-monthly; not due soon.

Front Deck and Regulatory Updates
	•	Front deck content includes AI model performance, regulatory updates, and coherent risk items.
	•	Consideration about combining regulatory updates (IAP, ILA, EBS) into fewer paragraphs; team to review.

PR Call Items for Next Week
	•	Discussion points to include:
	•	CCAR updates and recent NPR requesting industry comments on proposed changes.
	•	Updates from the recent FRB meeting follow-ups on ALST.
	•	General awareness of regulatory activities.

Platform Solutions Insights
	•	Mentioned recent internal developments:
	•	Platform Solutions experiencing no layoffs due to earlier Apple Card exits.
	•	Confirmed a significant retention incentive for remaining staff until the Apple Card sale.

⸻

This summary captures all essential points, particularly around the policy implementation updates, scheduling uncertainty due to jury duty, regulatory update plans, and key topics for upcoming meetings.





















Below is a detailed script you can use (or adapt) for your YouTube video review of the Flexispot E2 standing desk. Feel free to customize it based on your personal experience, style, and preferences.

---

## [INTRO]

**Video opens with a wide shot of you in front of the desk or an overview shot of the Flexispot E2.**  
**Energetic background music plays softly.**

**On-Camera/Voiceover (VO)**:  
> Hey everyone, welcome back to my channel! Today I’m super excited to bring you a review of the **Flexispot E2** standing desk. Whether you’re working from home, streaming, or just looking to upgrade your workspace, a standing desk can make a huge difference for comfort and health. So let’s dive in!

---

## [CHAPTER 1: UNBOXING & SETUP]

**Transition to unboxing footage: Show clips of opening the packaging, removing parts, skimming through instructions, etc.**

**On-Camera/VO**:  
> The Flexispot E2 arrived well-packaged. Inside the box, I found all the necessary parts neatly organized:  
> - Two desk legs and the crossbeam  
> - A control box and handset  
> - All the screws, tools, and accessories needed  
> - And of course, the desktop itself (if you got the Flexispot desktop option).  

> The instructions were straightforward, and the entire setup took me about [insert your time] minutes. I recommend using a power drill if you have one, but everything can be done with the supplied Allen wrench. Just be sure to follow the instructions carefully.

**[Optional: Include any tips or tricky parts you encountered while assembling.]**

---

## [CHAPTER 2: FEATURES & DESIGN]

**Cut to you demonstrating the desk. Show close-ups of different parts: the control panel, the legs, underside, etc.**

**On-Camera/VO**:  
> Once assembled, the desk feels sturdy. The E2 model is known for:
>
> 1. **Height Range**: It has a height range from [X to Y inches/cm (depending on the model)] – accommodating most users whether sitting or standing.  
> 2. **Motor & Speed**: The E2 features a single/dual motor system (depending on your exact E2 variant) that’s relatively quiet. I measured the noise level at around [insert approximate decibels if you did a test], which is pretty discreet.  
> 3. **Controller**: The control panel is simple. You press up or down to adjust the height, and some versions include memory presets so you can save your favorite sitting and standing heights.  
> 4. **Stability**: There’s minimal wobble at standing height, especially for a desk in this price range.  
> 5. **Weight Capacity**: The E2 can hold up to [insert approximate weight capacity], so whether you have a dual monitor setup or a heavy desktop tower, it should handle it well.  
> 6. **Desktop Options**: Flexispot offers different desktop sizes and finishes. I went with [describe your choice], which fits my space perfectly and looks sleek.

---

## [CHAPTER 3: USER EXPERIENCE / DAILY USE]

**Show B-roll of you working, adjusting the desk height, typing, placing items on the desk, etc.**

**On-Camera/VO**:  
> I’ve been using the Flexispot E2 for [insert timeframe] now, and here’s what I’ve noticed in everyday use:
> - **Ergonomics**: Standing for parts of the day definitely helps reduce back pain and makes me feel more energized.  
> - **Ease of Adjustment**: The transition from sitting to standing is smooth and takes only a few seconds. This makes me more likely to actually use the standing feature instead of sticking to one position all day.  
> - **Cable Management**: Flexispot includes some basic cable ties, but you might want to invest in additional solutions if you have multiple monitors and peripherals.  
> - **Desktop Space**: The version I have offers enough room for my dual monitors, keyboard, and a few accessories.

---

## [CHAPTER 4: PROS & CONS]

**On-Camera/VO**:  
> Let’s break it down:
>
> **Pros**:  
> 1. **Affordability**: Compared to other standing desks on the market, the E2 is competitively priced, making it a solid entry-level option.  
> 2. **Sturdy Construction**: The steel frame and stable design inspire confidence.  
> 3. **Customizable Height**: Good height range and memory presets (if your model includes them) make it user-friendly.  
> 4. **Health Benefits**: Encourages movement and reduces the monotony of sitting for long periods.

> **Cons**:  
> 1. **Basic Controller (on some variants)**: If you want advanced features like mobile app control or advanced memory settings, you’ll need a higher-end model.  
> 2. **Limited Aesthetic Options**: While there are some desktop colors and finishes, you might find fewer customization options compared to more premium brands.  
> 3. **Cable Management**: The included solutions are minimal, so you’ll likely need additional accessories for a clean setup.

---

## [CHAPTER 5: COMPARISONS (OPTIONAL)]

**You can add this section if you have personal experience with other standing desks, or just skip it.**

**On-Camera/VO**:  
> Compared to other standing desks in a similar price range, the Flexispot E2 stands out for its sturdy frame and relatively quiet motor. Some desks in this price category can be wobbly at higher settings or have slower motors. Flexispot strikes a nice balance between performance and cost.

---

## [CHAPTER 6: FINAL THOUGHTS & RECOMMENDATION]

**Return to a medium shot of you sitting or standing at the desk.**

**On-Camera/VO**:  
> Overall, the Flexispot E2 is a fantastic entry-level standing desk. It’s sturdy, reliable, and doesn’t break the bank. If you’re looking to upgrade your workspace without jumping to the higher-priced standing desks, this is a great option. As always, consider your needs—like the size of your room, your preferred desktop finish, and desired features—before you buy.  

---

## [OUTRO / CALL-TO-ACTION]

**On-Camera**:  
> Thanks so much for watching! If you found this review helpful, please **hit that like button** and **subscribe** for more reviews and productivity tips. Drop a comment below if you have any questions or if you already own a Flexispot desk—let me know your thoughts!  

> Until next time, this is [Your Name], signing off. Happy standing (and sitting)!

---

### [END CARD / CREDITS]

- **Show channel logo or social media handles.**
- **Mention any affiliate links or discount codes if relevant.**
- **Remind viewers to check the description for more info.**

---

**That’s it!** You now have a structured, step-by-step script to guide your Flexispot E2 standing desk review. Adjust the specifics—like exact height measurements, price, and personal anecdotes—to reflect your genuine experience. Good luck with your video!










Here’s a detailed summary of the key points discussed, structured clearly by topic, for drafting purposes:

⸻

Meeting Agenda Items for Brian:

1. AI Updates & Audit
	•	Provide updates on current AI-related initiatives.
	•	Include status on the ongoing audit concluding this week and key opinions or findings.

2. Board Presentation
	•	Include the board presentation deck and summarize any relevant items.

3. MRA Remediation
	•	Summarize recent clarifications from regulatory meetings.
	•	Possibly include estimates previously provided to Alex.
	•	Update status on broader regulatory commitments.

4. Regulatory Updates
	•	Briefly update on CCAR developments.
	•	Provide updates on other regulatory items, specifically:
	•	ILST Exam currently in progress.
	•	Pearl Street Initiative (Commodities Business Review):
	•	Clarify which models (Tier 1 and Tier 2) are associated with battery storage in UK energy markets.
	•	Outline model inputs, specifically predictive power prices and operational schedules for charging/releasing energy.
	•	Explain associated derivatives markets and risk exposures.

5. DRC (Data Risk Controls)
	•	Address confusion regarding DRCs, particularly where issues exist (possibly related to 6G or LCR).
	•	Highlight uncertainty regarding next steps due to unclear regulatory guidance.
	•	Note concerns from controllers and Finance regarding capital implications and the strategic alignment of DRC usage.
	•	Address potential European regulatory impacts or discussions on similar matters.

6. EMF-related Updates
	•	Clarify responsibility around breach response plan due to an upcoming deadline.
	•	Note interactions with Tom’s team to minimize unnecessary processes, possibly adjusting meeting frequency and sign-off responsibilities.
	•	Consider pragmatic approaches suggested by Tom regarding minimum viable processes.

7. Operational Risk Issues
	•	Discuss concerns over adoption and mapping of Assessment Units (AUs) between Model Risk Management (MRM) and Operational Risk.
	•	Highlight that Jenny’s team is responsible, but offer assistance due to complexities.
	•	Emphasize risks involved in restructuring or remapping AUs unnecessarily, suggesting pragmatic alternatives.

8. RCSA (Risk and Control Self-Assessment)
	•	Expectation of a second review round by Ross’s team informed by other risk areas.
	•	Consider whether the team should officially be recognized as independent Model Monitoring Team (MMT) versus divisional MMT, noting implications for being viewed as a key control versus a second-line review function.
	•	Clarify if RTG and other divisions are labeled as independent or divisional MMT and implications for MRM.

9. Thematic Findings
	•	Discuss planned launch (targeted for April 1) of thematic finding processes, starting potentially with Risk division.
	•	Address the operational readiness for this step, noting manual aspects that might require automation.
	•	Suggest initiating weekly summary emails highlighting problematic areas, with links to dashboards in ModelIt for visibility.

10. Metrics and Waivers
	•	Highlight metrics showing an increase in overdue findings now affecting Tier 1 and Tier 2 models, including AVA models.
	•	Note current issues around unvalidated waivers sitting with Controllers, emphasizing Bo’s rejection recommendation due to significant gaps.
	•	Clarify that a validated rejection is preferable to unvalidated status from a risk management perspective.

11. Internal Audit (IA)
	•	Summarize ongoing IA issues, specifically related to intake forms for AI.
	•	Note continuing frustrations and time-consuming interactions with IA, highlighting IA’s use of audits as learning opportunities, creating inefficiencies.
	•	Seek a pragmatic resolution with IA, involving Gareth for support.

12. Data Governance Issues
	•	Highlight concerns around model input, development, and production data as raised by Engineering.
	•	Identify ambiguity regarding boundaries between data governance and model governance frameworks, specifically:
	•	Whether models must strictly source data from authorized data services (ADS).
	•	Clarify if data governance expectations explicitly cover data used for model development or only production inputs and outputs.
	•	Anticipate challenges with the ECB guidance on model data governance and potential implications from upcoming examinations.
	•	Suggest reviewing the model control framework and data governance standards for clarity around model data handling requirements.

⸻

These structured points can serve as a solid basis for drafting materials and subsequent discussions with Brian.








Detailed Breakdown of ECB Submissions: ICAAP, ILAAP & Prudential Valuation

1. ECB Submissions Overview
	•	Submission of key regulatory documents to the ECB, focusing on risk management, capital adequacy, and liquidity.
	•	The primary focus areas are:
	•	ICAAP (Internal Capital Adequacy Assessment Process)
	•	ILAAP (Internal Liquidity Adequacy Assessment Process)
	•	Prudential Valuation (PV) Review & Follow-Ups

⸻

2. ICAAP (Internal Capital Adequacy Assessment Process)

Purpose:
	•	Ensures that the institution holds sufficient capital to cover all material risks.
	•	Aligns with Basel III/CRR requirements and ECB’s SREP (Supervisory Review and Evaluation Process).

Key Deliverables & Updates:
	•	Submission of ICAAP methodology documents and models.
	•	Includes 30 key documents submitted today, with 16 major ones sent to PCB for IAP.
	•	Focus on:
	•	Risk identification & materiality assessments for Pillar 2 risks.
	•	Stress testing framework—covering both base and adverse scenarios.
	•	Capital planning under different scenarios to ensure resilience.
	•	Alignment with latest ECB guidelines and expectations.

Challenges & Follow-Ups:
	•	ECB has raised questions on the risk-weighted asset (RWA) calculation methodology.
	•	Next steps: Provide detailed breakdowns of the risk appetite framework and stress testing assumptions.

⸻

3. ILAAP (Internal Liquidity Adequacy Assessment Process)

Purpose:
	•	Ensures the institution can withstand liquidity stress and meet obligations under various scenarios.
	•	Aligned with ECB’s Liquidity Stress Testing and Contingency Funding Plan requirements.

Key Deliverables & Updates:
	•	Submission of ILAAP documents, liquidity stress test models, and funding plans.
	•	Emphasis on:
	•	Liquidity buffer calculations and resilience assessment.
	•	Survival horizon analysis under different stress conditions.
	•	Net Stable Funding Ratio (NSFR) and Liquidity Coverage Ratio (LCR) compliance.
	•	Intraday liquidity risk assessment based on ECB’s expectations.

Challenges & Follow-Ups:
	•	ECB has requested further details on liquidity stress assumptions and outflow scenarios.
	•	Next steps include refining the liquidity risk framework documentation to align with ECB’s latest supervisory expectations.

⸻

4. Prudential Valuation (PV) Review & Follow-Ups

Purpose:
	•	Ensures institutions apply fair value adjustments (FVA) properly, reflecting valuation uncertainty.
	•	Aligns with CRR Article 105 and ECB’s Prudential Valuation Guidelines.

Key Deliverables & Updates:
	•	Submission of valuation adjustments methodology and impact analysis.
	•	Covers FVA across Level 1, Level 2, and Level 3 assets, ensuring compliance with regulatory standards.
	•	Addressing ECB’s concerns:
	•	Valuation model risks and uncertainty calibration.
	•	Methodology for market price uncertainty, close-out costs, and concentrated positions.
	•	Independent price verification (IPV) processes.
	•	Alignment with Basel requirements and IFRS 13 fair value hierarchy.

Challenges & Follow-Ups:
	•	BCP has raised concerns about specific methodologies used for prudent valuation adjustments.
	•	Next week: Detailed response to BCP follow-up questions, focusing on:
	•	Justification for valuation methodologies.
	•	Additional stress test results to support prudent valuation adjustments.
	•	Potential recalibration of specific valuation adjustments for Level 3 assets.

⸻

5. Next Steps & Ongoing Monitoring
	•	ICAAP & ILAAP:
	•	Address ECB’s RWA calculation and liquidity stress testing methodology concerns.
	•	Refine the capital and liquidity risk framework documentation.
	•	Prudential Valuation:
	•	Respond to BCP’s methodology concerns with additional data and supporting analysis.
	•	Align prudent valuation adjustments with ECB’s supervisory expectations.
	•	Governance & Reporting:
	•	Ensure ongoing ECB compliance through quarterly validation updates.
	•	Monitor evolving ECB regulatory guidance for potential future refinements.

Let me know if you need further details or specific refinements!

In the transcript, the acknowledgment letter comes up when the Federal Reserve representative confirms that they have received and reviewed the firm’s recent project plan/response and notes that an official acknowledgment letter will be sent soon. Here’s the relevant excerpt in context:

	Regulator (Fed): “We did … and I was able to review those and also I wanted to let the firm know that we did render the process of reviewing the response. So … we should be sending acknowledgment letters soon—just wanted to let you know that.”

The key points regarding the acknowledgment letter are:
	1.	Purpose: It is a formal notification from the Fed acknowledging receipt and initial review of the firm’s submission (such as a supervisory response or project plan).
	2.	Timing: The Fed representative explains that the letter will go out “soon” but does not specify an exact date.
	3.	Next Steps: The letter generally confirms that regulators have reviewed the material and outlines whether there will be any follow-up questions or additional steps expected from the firm.

So, in short, the acknowledgment letter is the official communication from the Fed that they have received the firm’s materials and are moving forward with their supervisory review process.





Below is a concise “Q&A style” summary of the data quality discussion that took place during the transcript, highlighting the question from the regulator and the response from the firm’s Model Risk Management (MRM) team.

⸻

1. Regulator’s Question on Data Quality
	1.	Context of the Inquiry
	•	The regulator observed mentions of data quality issues in the revalidation process and asked how the firm is addressing data governance—particularly as it expands into Generative AI (GAI).
	2.	Core Question
	•	“How is the firm thinking about data quality issues, especially around Generative AI? Are there new or enhanced data management and governance frameworks in place to handle the heightened data risk from advanced AI models?”

⸻

2. Firm’s Response on Data Quality
	1.	Enterprise Data Governance Uplifts
	•	The firm noted that it is already engaged in enterprise-wide data governance enhancements, partly tied to broader regulatory expectations (e.g., BCBS 239 or internal “EMF uplift” efforts).
	•	These ongoing programs aim to improve data lineage, data quality controls, and overall consistency of data usage across the firm.
	2.	Model Risk Perspective
	•	From an MRM viewpoint, data validation is already a core requirement. The firm emphasized that it verifies not only the input data but also the accuracy of the “ground truth” or reference data used to train or benchmark models.
	•	Particularly for AI/ML models, validators focus on how raw inputs are processed into features and whether the labeled outcomes (ground truth) are reliable.
	3.	Generative AI-Specific Measures
	•	Generative AI models must follow the same model validation framework, but with additional scrutiny around:
	•	Data provenance: Where the training data or reference data is coming from.
	•	Comparison across AI engines: For instance, using two different Large Language Model (LLM) providers to cross-check results for consistency or potential drift.
	•	The firm’s newly formed AI Risk & Controls Committee adds supplemental reviews of data usage, model outputs, and risk to ensure that these models comply with legal, compliance, and privacy standards.
	4.	Real-World Example
	•	For the ESGAI model (the first Tier 1 “generative AI” model at the firm), MRM paid close attention to:
	•	Data labeled by humans: Ensuring labels or reference data were validated.
	•	Potential mismatch among multiple AI engines: Identifying if different LLMs yield divergent outputs, which might point to data or labeling inconsistencies.
	5.	Ongoing Controls and Monitoring
	•	Daily or frequent performance tests ensure that if data streams degrade or become inconsistent, the model’s performance metrics will flag it.
	•	The firm also proactively watches for unexpected code changes—a spike in urgent code fixes may signal data or model under “pressure” that warrants closer review.

⸻

Final Takeaway
	•	The regulator asked how the firm is managing data quality—especially in the Generative AI realm.
	•	The firm explained that it has robust data governance efforts in progress, validates ground truth and feature processing for AI/ML, and employs ongoing monitoring plus a specialized AI Risk & Controls Committee to address new challenges posed by advanced models. The focus is on ensuring reliable inputs and consistent labeling so that AI and other models remain accurate, even under heightened market or operational “pressure.”




What “Pressure” Means in This Setting
	1.	Market Volatility or Stress Events
	•	Large swings in interest rates, foreign exchange rates, or credit spreads can introduce unexpected behaviors in a model’s inputs or outputs.
	•	Sudden shocks can reveal gaps in model assumptions or calibration.
	2.	Model Performance & Stability
	•	Models under “pressure” may exhibit higher-than-expected errors, fail certain back-tests, or produce outputs that do not align with market observations.
	•	In risk management terms, a model might be at risk of “breaking” (e.g., generating unrealistic valuations or risk measures) when real-world conditions deviate sharply from the historical data it relies on.
	3.	Operational or Business Changes
	•	Rapidly evolving products, new lines of business, or emergency trading strategies can stress a model if it has not been recalibrated for those changes.

⸻

2. How the Firm Monitors Models Under Pressure

When asked about recent market and interest-rate volatility, the firm’s representatives explained:
	1.	Daily Risk Testing
	•	Many of the front-office and risk models (e.g., pricing, Value-at-Risk, counterparty exposure) undergo daily “re-tests” or real-time performance checks.
	•	If unusual outputs or back-test exceptions surface, those prompt immediate investigation.
	2.	Code Change Monitoring
	•	A sudden increase in developer “hot fixes” or emergency code changes can be a red flag. It might indicate a model is struggling under current market conditions.
	•	The Model Risk Management (MRM) team watches for spikes in code deployments as an early-warning sign.
	3.	Enhanced Scrutiny During Events
	•	If global markets experience a big shock (e.g., a large interest-rate jump or extreme volatility), MRM and the business lines perform ad hoc or forward-looking scenario analyses.
	•	They compare model outputs to alternative benchmarks or “ground truth” data to see if performance is degrading.
	4.	Regular Governance Touchpoints
	•	Any sign of model underperformance triggers Model Risk Control Committee or FRAC reviews. If severe, it escalates to the Board Risk Committee.

⸻

3. Current Observations

From the transcript, the firm indicated:
	•	They have not identified any major breakdowns or anomalies despite recent rate and FX fluctuations.
	•	Ongoing monitoring has not revealed big spikes in back-test exceptions or model failures, so no immediate “pressure” issues were flagged at the time of that conversation.

⸻

4. Why This Matters
	1.	Preemptive Risk Management
	•	By actively searching for “pressure points,” the firm can adjust models (e.g., recalibrate, update assumptions) before problems become critical.
	2.	Regulatory Expectations
	•	Regulators expect that banks detect early signs of model stress and proactively mitigate. If the firm fails to do so, it might face supervisory findings or require urgent remediation.
	3.	Business Continuity and Accuracy
	•	Accurate models under all market conditions reduce the risk of trading losses, mispriced products, and poor strategic decisions.

⸻

Final Takeaway

“Pressure” refers to the stresses placed on a model by volatile or unexpected market conditions. The firm’s process—daily testing, code-change monitoring, ongoing validation checks, and escalations to senior committees—aims to catch any emergent model issues promptly. As of the conversation in the transcript, no significant “pressure” had manifested in the firm’s models, but they continue enhanced 



In the context of the transcript, “pressure” primarily refers to external market or business conditions that could stress or challenge the firm’s models—especially when there is heightened market volatility or significant economic shifts. Here is how that concept of “pressure” surfaced and was addressed:

⸻

1. What “Pressure” Means in This Setting
	1.	Market Volatility or Stress Events
	•	Large swings in interest rates, foreign exchange rates, or credit spreads can introduce unexpected behaviors in a model’s inputs or outputs.
	•	Sudden shocks can reveal gaps in model assumptions or calibration.
	2.	Model Performance & Stability
	•	Models under “pressure” may exhibit higher-than-expected errors, fail certain back-tests, or produce outputs that do not align with market observations.
	•	In risk management terms, a model might be at risk of “breaking” (e.g., generating unrealistic valuations or risk measures) when real-world conditions deviate sharply from the historical data it relies on.
	3.	Operational or Business Changes
	•	Rapidly evolving products, new lines of business, or emergency trading strategies can stress a model if it has not been recalibrated for those changes.

⸻

2. How the Firm Monitors Models Under Pressure

When asked about recent market and interest-rate volatility, the firm’s representatives explained:
	1.	Daily Risk Testing
	•	Many of the front-office and risk models (e.g., pricing, Value-at-Risk, counterparty exposure) undergo daily “re-tests” or real-time performance checks.
	•	If unusual outputs or back-test exceptions surface, those prompt immediate investigation.
	2.	Code Change Monitoring
	•	A sudden increase in developer “hot fixes” or emergency code changes can be a red flag. It might indicate a model is struggling under current market conditions.
	•	The Model Risk Management (MRM) team watches for spikes in code deployments as an early-warning sign.
	3.	Enhanced Scrutiny During Events
	•	If global markets experience a big shock (e.g., a large interest-rate jump or extreme volatility), MRM and the business lines perform ad hoc or forward-looking scenario analyses.
	•	They compare model outputs to alternative benchmarks or “ground truth” data to see if performance is degrading.
	4.	Regular Governance Touchpoints
	•	Any sign of model underperformance triggers Model Risk Control Committee or FRAC reviews. If severe, it escalates to the Board Risk Committee.

⸻

3. Current Observations

From the transcript, the firm indicated:
	•	They have not identified any major breakdowns or anomalies despite recent rate and FX fluctuations.
	•	Ongoing monitoring has not revealed big spikes in back-test exceptions or model failures, so no immediate “pressure” issues were flagged at the time of that conversation.

⸻

4. Why This Matters
	1.	Preemptive Risk Management
	•	By actively searching for “pressure points,” the firm can adjust models (e.g., recalibrate, update assumptions) before problems become critical.
	2.	Regulatory Expectations
	•	Regulators expect that banks detect early signs of model stress and proactively mitigate. If the firm fails to do so, it might face supervisory findings or require urgent remediation.
	3.	Business Continuity and Accuracy
	•	Accurate models under all market conditions reduce the risk of trading losses, mispriced products, and poor strategic decisions.

⸻

Final Takeaway

“Pressure” refers to the stresses placed on a model by volatile or unexpected market conditions. The firm’s process—daily testing, code-change monitoring, ongoing validation checks, and escalations to senior committees—aims to catch any emergent model issues promptly. As of the conversation in the transcript, no significant “pressure” had manifested in the firm’s models, but they continue enhanced scrutiny as part of standard risk oversight.







In the context of the transcript, “pressure” primarily refers to external market or business conditions that could stress or challenge the firm’s models—especially when there is heightened market volatility or significant economic shifts. Here is how that concept of “pressure” surfaced and was addressed:

⸻

1. What “Pressure” Means in This Setting
	1.	Market Volatility or Stress Events
	•	Large swings in interest rates, foreign exchange rates, or credit spreads can introduce unexpected behaviors in a model’s inputs or outputs.
	•	Sudden shocks can reveal gaps in model assumptions or calibration.
	2.	Model Performance & Stability
	•	Models under “pressure” may exhibit higher-than-expected errors, fail certain back-tests, or produce outputs that do not align with market observations.
	•	In risk management terms, a model might be at risk of “breaking” (e.g., generating unrealistic valuations or risk measures) when real-world conditions deviate sharply from the historical data it relies on.
	3.	Operational or Business Changes
	•	Rapidly evolving products, new lines of business, or emergency trading strategies can stress a model if it has not been recalibrated for those changes.

⸻

2. How the Firm Monitors Models Under Pressure

When asked about recent market and interest-rate volatility, the firm’s representatives explained:
	1.	Daily Risk Testing
	•	Many of the front-office and risk models (e.g., pricing, Value-at-Risk, counterparty exposure) undergo daily “re-tests” or real-time performance checks.
	•	If unusual outputs or back-test exceptions surface, those prompt immediate investigation.
	2.	Code Change Monitoring
	•	A sudden increase in developer “hot fixes” or emergency code changes can be a red flag. It might indicate a model is struggling under current market conditions.
	•	The Model Risk Management (MRM) team watches for spikes in code deployments as an early-warning sign.
	3.	Enhanced Scrutiny During Events
	•	If global markets experience a big shock (e.g., a large interest-rate jump or extreme volatility), MRM and the business lines perform ad hoc or forward-looking scenario analyses.
	•	They compare model outputs to alternative benchmarks or “ground truth” data to see if performance is degrading.
	4.	Regular Governance Touchpoints
	•	Any sign of model underperformance triggers Model Risk Control Committee or FRAC reviews. If severe, it escalates to the Board Risk Committee.

⸻

3. Current Observations

From the transcript, the firm indicated:
	•	They have not identified any major breakdowns or anomalies despite recent rate and FX fluctuations.
	•	Ongoing monitoring has not revealed big spikes in back-test exceptions or model failures, so no immediate “pressure” issues were flagged at the time of that conversation.

⸻

4. Why This Matters
	1.	Preemptive Risk Management
	•	By actively searching for “pressure points,” the firm can adjust models (e.g., recalibrate, update assumptions) before problems become critical.
	2.	Regulatory Expectations
	•	Regulators expect that banks detect early signs of model stress and proactively mitigate. If the firm fails to do so, it might face supervisory findings or require urgent remediation.
	3.	Business Continuity and Accuracy
	•	Accurate models under all market conditions reduce the risk of trading losses, mispriced products, and poor strategic decisions.

⸻

Final Takeaway

“Pressure” refers to the stresses placed on a model by volatile or unexpected market conditions. The firm’s process—daily testing, code-change monitoring, ongoing validation checks, and escalations to senior committees—aims to catch any emergent model issues promptly. As of the conversation in the transcript, no significant “pressure” had manifested in the firm’s models, but they continue enhanced scrutiny as part of standard risk oversight.




Below is an expanded explanation of how granular the reporting is—particularly what information the firm’s Board Risk Committee (BRC), the Firmwide Risk & Controls Committee (FRAC), and other senior groups see with respect to model risk.

⸻

1. Board-Level Reporting
	1.	High-Level Risk Appetite Metrics
	•	The Board primarily sees aggregate Model Risk metrics—these are the same top-level Key Risk Indicators (KRIs) that form part of the firm’s Risk Appetite Statement (RAS).
	•	Examples include the number of unvalidated or rejected Tier 1 models in use, breaches of model risk thresholds (e.g., how many models have been “aged” past one year), and any zero-tolerance threshold violations.
	2.	Model Inventory Overview
	•	The Board is given a snapshot of the total number of models, categorized by business unit (Risk, GBM, etc.) and by approval status (validated, unvalidated, rejected).
	•	This helps them gauge the overall size and complexity of the firm’s modeling landscape.
	3.	Significant Updates and Thematic Issues
	•	For important emerging topics—like Generative AI, stress-testing enhancements, or high-profile regulatory findings—the Board receives summary updates or short thematic discussions.
	•	These overviews give them a sense of why certain issues are arising, where potential risks are concentrated, and how management is remediating them.
	4.	Escalation of Major Problems
	•	Any “high-severity” or Tier 1 model concerns (e.g., a large breach or a critical supervisory finding) is escalated immediately to the Board.
	•	If a threshold is breached at the Board level—for instance, if a model’s unvalidated status goes beyond one year—this is highlighted in the Board materials as a zero-tolerance breach.

	Key Takeaway: The Board sees top-level model risk metrics, major trends, and serious exceptions. They do not typically see the full granular “line-by-line” detail for every finding or model.

⸻

2. FRAC and Model Risk Control Committee Reporting
	1.	More Detailed Breakdowns
	•	The FRAC and Model Risk Control Committee (MRCC) get the same top-level metrics the Board sees, plus more granular reporting.
	•	For instance, they might see a breakdown of the exact number of findings by severity, open vs. closed status, and how many days past due each item is.
	2.	Qualitative Approaches, Deterministic Reg Calculations
	•	Beyond typical quantitative models, these committees also see detailed metrics on qualitative approaches and deterministic regulatory calculations (such as certain capital or compliance calculations).
	•	This ensures coverage of all tool types under the broader “model” or “model-like” umbrella.
	3.	In-Depth Thematic Reviews
	•	If there is a specific area of heightened focus—e.g., new large language models, a revalidation wave for stress-testing, or interest-rate volatility—FRAC/MRCC may receive a deeper “spotlight” analysis or a short write-up showing key observations and any open issues.
	4.	Focus on Remediation and Progress
	•	These committees track whether open findings are being closed on schedule and monitor areas with higher volumes of new findings.
	•	They also see trend analyses (e.g., quarter-over-quarter changes in the number of open findings, average days to close a finding, etc.).

⸻

3. Subcommittees and Working Groups
	•	Working-Level Detail
	•	At the most granular level—within MRM or specialized working groups—teams might review the individual findings line by line. This includes severity scores, root causes, and exact remediation steps.
	•	These working groups feed summarized information up to FRAC and eventually to the Board, so the level of detail filters appropriately based on the audience.

⸻

4. Why Different Audiences See Different Levels of Detail
	1.	Audience and Purpose
	•	Board: Oversees risk at a strategic level. They want to know if there are large or systemic issues jeopardizing the firm’s risk appetite.
	•	FRAC/MRCC: Operate at a more tactical and operational level, ensuring robust controls are actually implemented and that meaningful issues or rising trends are handled before they become Board-level breaches.
	•	Working Groups / Validation Teams: Perform the day-to-day analysis, root cause identification, model reviews, and produce the raw data that rolls up to the committees.
	2.	Escalation Tiers
	•	The firm’s governance model sets out which types of issues must be escalated to which committee—and on what timetable—to prevent any critical or overdue items from going unnoticed.

⸻

Final Summary
	•	The Board receives a high-level, strategic view: key metrics, risk appetite thresholds, serious exceptions, and thematic summaries.
	•	The FRAC/Model Risk Control Committee sees a more detailed breakdown of open findings, model statuses, business-line splits, and thematic deep-dives.
	•	Working groups handle the most granular, line-by-line model details, feeding that information upward as summarized reports for senior stakeholders.

In essence, the reporting grows more granular as you move from the Board (highest level) down to the committees and working groups.




In the transcript, there is a reference to six Tier 1 unvalidated models “quarter over quarter.” The concern was whether these six were the same models staying unvalidated too long or if the number “6” simply reappeared each quarter for different reasons (new models, model updates, etc.).

Key Points
	1.	It is not necessarily the same six models
	•	During the quarter, some Tier 1 models get validated and come off the unvalidated list, while new or changed models are added to the unvalidated list. So the figure may remain around six each quarter, but it reflects different models over time.
	2.	New Model Development & Significant Model Changes
	•	Tier 1 models often arise from highly complex or critical areas (e.g., trading, risk management). Whenever the firm introduces new Tier 1 models or makes material changes to existing ones, those models must go through revalidation.
	•	That revalidation process can temporarily increase the number of unvalidated Tier 1 models.
	3.	Waiver & Aging Controls
	•	The firm uses a 90-day waiver for unvalidated models in use, plus tight aging metrics (six or nine months at the FRAC level, one year at the Board level). These thresholds ensure that unvalidated models cannot remain outstanding indefinitely.
	•	If any model is in use without validation past its original remediation date, the firm tracks it as an “aged” item, which triggers increased scrutiny.
	4.	Ongoing ‘Churn’
	•	The firm describes a “churn” or turnover: some Tier 1 unvalidated models in use resolve each quarter and drop off the list, while new ones (due to fresh development or updates) come on. That can keep the number around six, even though they are not the same exact six from quarter to quarter.

⸻

In short, the number “six” showing up quarter over quarter does not imply that the same six Tier 1 models are perpetually unvalidated; rather, it’s a recurring level driven by ongoing model development, enhancements, and validation turnover.




From the discussion, the main reason for the uptick in findings near the end of the year is that new model development, model changes, and scheduled revalidations all came together in Q4. In other words:
	1.	New or Enhanced Models
	•	Whenever the firm introduces a new model or significantly changes an existing one, the Model Risk team performs fresh validation. This typically leads to new findings being raised.
	2.	Revalidations
	•	A large batch of Tier 1 model revalidations was wrapped up at year-end. These reviews can also generate findings—especially around documentation, calibration details, or minor code fixes—even when the model itself is fundamentally sound.
	3.	Close-Out vs. New Findings
	•	In Q4, the number of new findings (from all the model changes and revalidations) slightly outpaced the number of closed findings, causing a net increase (or “uptick”) in open items for that quarter.




Below is a structured, detailed summary of the discussion, based on the transcript provided. The conversation is primarily between representatives from a financial institution’s Model Risk Management (MRM) group (including Caroline, Bill, Bo, Bingwen, OJ, and others) and regulators from the Federal Reserve (“the Fed”) and FDIC (with Michaela and Caleb representing the regulators). The main topics include quarterly model risk updates, threshold tightening for certain metrics, the use of generative AI models, and the status of various validation activities and findings.

⸻

1. Meeting Logistics and Introductions
	•	The call begins with attendees confirming who is present from both the firm and the regulators.
	•	Michaela joins, and the group confirms they have the relevant participants from the Fed, FDIC, and the bank’s MRM team.
	•	The bank’s team mentions that it sent over meeting materials in advance, confirming that the Fed received and reviewed them.

⸻

2. Recent Submissions and Regulatory Review
	•	The Fed acknowledges receipt of the firm’s recent project plan/response to supervisory requests and indicates that an acknowledgment letter will be sent soon.
	•	The firm reiterates it is available to address any questions about the plan or any other materials, either during the meeting or offline.

⸻

3. Updates on Risk Appetite Thresholds and Governance
	•	Tightening of waiver aging thresholds:
	•	The firm explains that it previously established a threshold of nine months for certain model waivers at the FRAC (Firmwide Risk and Controls Committee) level but decided to reduce it to six months.
	•	The Board Risk Committee (BRC) retains a one-year zero-tolerance threshold for these same items, meaning if a waiver is still unresolved after one year (relative to its original due date), it breaches the BRC’s risk appetite.
	•	The shortened six-month threshold provides an earlier escalation path while leaving a three-month buffer before hitting the Board-level one-year limit.

⸻

4. Discussion on Generative AI (GAI) and Large Language Models
	•	A regulator inquires about a recently approved ESG-related large language model (an “ESGAI” model) and the firm’s broader generative AI strategy.
	•	AI governance structure:
	•	The bank has a dedicated AI policy and an AI Risk & Controls Committee, formed in 2023.
	•	The committee includes representatives from various control functions (Model Risk, Operational Risk, Legal, Compliance, etc.) to address potential risks of new AI use cases.
	•	Model Risk Management approach:
	•	Generative AI models are subject to the same core model-risk controls and require model validations similar to traditional models.
	•	The firm uses specialized documentation and validation templates for AI/ML models.
	•	They have introduced a separate AI inventory process so that not only validated AI models but also certain AI “tools” and “platforms” are tracked.
	•	Use cases and outlook:
	•	Most generative AI models so far are in lower-risk, operational efficiency use cases.
	•	The ESGAI model is the first “Tier 1” generative AI model (i.e., of higher materiality/risk) that has gone through full validation.
	•	Additional generative AI expansions are expected, but each is examined under the AI policy and standard model risk controls.

⸻

5. Status of Validation Findings and Internal Audit (IA) Items
	•	Open and closed findings:
	•	The MRM team reviews charts illustrating open findings, newly raised findings, and those closed during the quarter.
	•	They note a slight uptick in total findings for Q4 but highlight a downward trend on a year-over-year basis.
	•	Findings are concentrated where model inventory is largest (e.g., Risk, Global Banking & Markets).
	•	Internal Audit (IA) observations:
	•	Seven IA findings were closed in the quarter, all of them lower-severity (general) items, primarily documentation-related.
	•	A new, low-severity IA finding was raised noting a “pattern” of validation documentation gaps over a few years. IA did not question the firm’s validation conclusions but felt it warranted a broader training initiative.
	•	The firm agreed to roll out training to reinforce comprehensive documentation standards by the end of April.

⸻

6. Board and FRAC-Level Metrics (RAS Utilization)
	•	The firm tracks several risk appetite statement (RAS) metrics around unvalidated or rejected models and the aging of those conditions.
	•	Waiver framework:
	•	If a model is in use without a finalized validation (unvalidated) or with a “reject” rating, it must have a time-bound waiver, typically remedied within 90 days.
	•	Age-based metrics (how long a model or finding remains unresolved past its original due date) are set to zero tolerance at nine months (now shortened to six months) at the FRAC level and one year at the Board level.
	•	Current usage:
	•	There were no Board-level or FRAC-level breaches during the quarter for unvalidated or rejected models.
	•	Some items did breach the age threshold for “severity 2” findings. Two specific GBM models triggered the FRAC threshold, but those findings have since been remediated.

⸻

7. Model Inventory and Ongoing Monitoring
	•	Inventory overview:
	•	The firm reports a stable overall model inventory, noting a modest increase of around 100 models over the past year.
	•	They break it down by tier (materiality) and business line (e.g., Risk Division, GBM, etc.).
	•	Market volatility considerations:
	•	Regulators ask whether the firm has enhanced monitoring due to recent market volatility (particularly interest-rate-related).
	•	The firm explains that its daily risk tests, ongoing performance assessments, and close scrutiny of code changes help identify potential breakage or model underperformance.
	•	As of now, there have been no major issues from volatile conditions.

⸻

8. Model Changes and Significant Revalidations
	•	Enhancements and new approvals:
	•	The firm highlights approvals for collateralized lending models (private equity, direct CRE, etc.), interest rate risk enhancements, and other operational models.
	•	Validation teams identified a few low-severity issues (e.g., minor code bugs) that were fixed pre-approval.
	•	Significant Tier 1 revalidation cycle:
	•	The two-year cycle for the highest-materiality (Tier 1) models concluded at year-end.
	•	No high-severity findings emerged; medium-severity findings primarily involved methodology, parameter calibration, or documentation improvements.
	•	The firm is already beginning the next two-year revalidation cycle for Tier 1 models and is also performing annual validations for CCAR/stress-testing models.

⸻

9. Meeting Conclusion
	•	The regulators express appreciation for the comprehensive materials and clarity of updates.
	•	They confirm they will follow up with any additional questions and will send an official acknowledgment of the firm’s supervisory response.
	•	Both parties end on a positive note, and the meeting concludes with thanks exchanged.

⸻

Overall, the discussion centers on the bank’s continued enhancements to model risk governance—tightening certain thresholds, validating and monitoring advanced AI models, and staying on top of internal audit findings. Regulators appear satisfied with the bank’s progress and reaffirm that they will remain in contact regarding any needed clarifications on model risk and supervisory items.







MEETING MINUTES
Date: [Insert Date of Meeting]
Time: [Insert Time of Meeting]
Location: Virtual Conference

⸻

1. Attendees
	•	Regulatory Representatives
	•	Federal Reserve (Fed): Attendee(s) not fully specified
	•	FDIC: Attendee(s) not fully specified
	•	Michaela (Regulator)
	•	Caleb (Regulator)
	•	Firm Representatives
	•	Caroline (Model Risk Management, “MRM”)
	•	Ajan
	•	Bo
	•	Bill
	•	Ibo
	•	Additional MRM and Risk Team members (names not fully specified)

⸻

2. Meeting Purpose
	•	To provide a quarterly update on Model Risk Management (MRM) to the Federal Reserve and FDIC.
	•	To discuss recent changes to the firm’s model risk thresholds (including waiver aging), internal audit findings, and Generative AI (GAI) models.

⸻

3. Agenda Highlights
	1.	Introductions and confirmation of participants
	2.	Acknowledgment of materials (confirming regulators received the deck)
	3.	Quarterly model risk updates (including waiver threshold changes and status of findings)
	4.	Generative AI model discussion (ESGAI model and broader GAI governance)
	5.	Internal audit findings review
	6.	Revalidation activities and model inventory trends
	7.	Questions, next steps, and action items

⸻

4. Detailed Updates and Discussion

4.1 Waiver Thresholds and Aging

The firm reiterated that it has a zero-tolerance policy at the Board Risk Committee (BRC) level for models or findings aged beyond one year from the original due date. As an intermediate check, the firm’s Model Risk Control Committee (FRAC) threshold was previously set at nine months. To better align with other control functions, the FRAC threshold has been shortened to six months. The firm explained that this adjustment creates an additional buffer, ensuring potential concerns are flagged and addressed before reaching the Board’s one-year threshold.

4.2 Generative AI (GAI) Models

The firm has observed an increase in the number of AI/ML models, including those using large language models (LLMs). While most uses remain low-risk and focused on operational efficiencies, the firm noted its first Tier 1 Generative AI model (ESGAI). The validation approach for GAI follows the firm’s existing model risk framework, supplemented by an AI Risk and Controls Committee. This committee includes representatives from legal, compliance, operational risk, and other control functions to address emerging risks such as data privacy, unintended model behaviors, and compliance considerations.

4.3 Internal Audit Findings

The firm reported that many of the recent internal audit findings were of lower severity, typically related to documentation enhancements. Internal audit had also identified a pattern of documentation inconsistencies over several years. The firm has responded by committing to additional training sessions on comprehensive model validation documentation. Most findings have already been remediated or are in the process of closure, with no impact on the fundamental integrity of any model conclusions.

4.4 Model Inventory and Revalidations

The firm’s model inventory remains relatively stable. A slight uptick in Q4 was attributed to normal development and enhancements in existing models. The firm tracks outstanding waivers carefully and ensures that no waiver is extended indefinitely without proper justification. Significant Tier 1 revalidations, required on a two-year cycle, have been completed for the current period with no high-severity findings. The firm is also in the midst of annual reviews tied to regulatory exercises such as CCAR. Overall, there have been no major performance issues in daily run tests, and no models have experienced unexpected breakage during recent market volatility.

⸻

5. Questions and Responses (in Third Person)
	1.	Regulators inquired about the rationale for tightening waiver thresholds
The firm responded that it sought to align its Model Risk processes with similar frameworks in other control functions (e.g., Internal Audit). By reducing the FRAC threshold from nine to six months, the firm provided additional time to address potential issues well before the Board’s one-year zero-tolerance deadline.
	2.	Regulators asked for an update on the firm’s progress with Generative AI
The firm explained that it continues to see new GAI applications, often focusing on operational efficiencies. It has validated its first Tier 1 GAI model (ESGAI) and uses AI-specific validation templates. The AI Risk and Controls Committee reviews AI models for potential legal, compliance, and operational risks that go beyond traditional model risk.
	3.	Regulators requested information on recent Internal Audit findings
The firm stated that the majority of new findings related to documentation gaps rather than fundamental model performance. Some issues had been self-identified in the course of prior reviews. To address these gaps, the firm is rolling out targeted training for validators, emphasizing thorough documentation standards.
	4.	Regulators inquired about model performance during market volatility
The firm reported that daily run tests remain stable. There have been no noteworthy breakages, code failures, or unusual parameter shifts resulting from market events. The firm also indicated it monitors changes in model code for any signs of stress or anomalies.
	5.	Regulators asked whether any unvalidated Tier 1 models had exceeded their remediation deadlines
The firm confirmed that all unvalidated or rejected models require waivers and are tracked for timeliness. Extended waivers are granted only after a robust internal process, and aging metrics (nine months previously, now six months) ensure issues are escalated before becoming overdue at the Board level.

⸻

6. Next Steps and Action Items
	•	Acknowledgment Letters:
Regulators plan to issue formal letters acknowledging the firm’s recent supervisory response.
	•	Severity 1 Finding Confirmation:
The firm will verify the status of a Severity 1 finding in the Risk division to confirm whether the model is in production or still under development.
	•	Documentation Training Completion:
The firm will finalize and conduct training sessions on validation documentation best practices by the end of April.
	•	Generative AI Oversight:
The firm will continue to provide updates on new GAI models and any significant policy or governance changes under the AI Risk and Controls Committee.
	•	Continued Market Monitoring:
Daily run tests will continue, with attention to volatility and potential code updates that might signal underlying stress.

⸻

7. Conclusion

Regulators expressed appreciation for the comprehensive update and noted that no significant concerns emerged from the quarterly materials. The firm will continue its proactive approach to model risk, especially around new AI applications and any documentation improvements suggested by internal audit. Both parties agreed to maintain open communication on model risk developments and to reconvene at the next scheduled quarterly update (or sooner if needed).

⸻

These minutes summarize the main points of discussion, the firm’s responses to regulators’ questions, and the agreed-upon action items.









Meeting Minutes
Date: [Insert Date of Meeting]
Time: [Insert Time of Meeting]
Location: Virtual Conference

⸻

1. Attendees
	•	Regulatory Representatives
	•	Federal Reserve (Fed): [Name(s) not fully specified in transcript]
	•	FDIC: [Name(s) not fully specified in transcript]
	•	Michaela (Regulator)
	•	Caleb (Regulator)
	•	Firm Representatives
	•	Caroline (Model Risk Management, “MRM”)
	•	Ajan
	•	Bo
	•	Bill
	•	Ibo
	•	Others from the MRM and Risk Teams

(Note: Some names were partially mentioned or not fully introduced in the transcript.)

⸻

2. Meeting Purpose
	•	Quarterly Model Risk Management Update to the regulators (Fed and FDIC).
	•	Review of:
	•	Recent changes to Model Risk thresholds (including waiver aging).
	•	Firm’s approach to Generative AI (GAI) models.
	•	Status of internal audit findings and overall validation progress.
	•	Model inventory trends, revalidation cycles, and key issues.

⸻

3. Agenda & Key Discussion Topics
	1.	Introductions and Confirmation of Attendance
	2.	Acknowledgement of Meeting Materials
	•	Regulators confirmed receipt of the firm’s materials.
	•	The regulators noted an acknowledgment letter regarding a recent supervisory submission would be sent soon.
	3.	Quarterly Model Risk Update
	•	Overview of findings and remediation status.
	•	Discussion of the firm’s Risk Appetite Statement (RAS) thresholds and recent tightening of waiver aging thresholds.
	4.	Discussion on Generative AI (GAI) Models
	•	First Tier 1 GAI model approval (ESGAI).
	•	Broader firm strategy and governance approach for AI and large language models.
	5.	Internal Audit Findings & Closure
	•	Review of recent and ongoing internal audit findings (documentation, validation templates, potential patterns observed).
	•	Discussion of training plans to address documentation consistency.
	6.	Model Inventory & Revalidations
	•	Updates on model inventory statistics.
	•	High-level review of revalidation activities (especially “significant Tier 1” revalidations).
	•	Status of daily run tests/monitoring given market volatility.
	7.	Next Steps & Action Items

⸻

4. Detailed Discussion and Q&A

Below is a summary of questions raised during the meeting and the firm’s responses.

4.1 Changes to Waiver Thresholds
	•	Question (Regulator):
“You recently tightened the waiver aging threshold from nine months to six months. Could you provide background on why you lowered it and how it aligns with the board’s existing threshold?”
	•	Response (Firm):
“Previously, we introduced zero tolerance for waivers older than one year at the Board level. We had an internal (FRAC) threshold of nine months but decided to tighten that to six months for better alignment with other control functions (e.g., internal audit) and to ensure we have ample time to remediate before reaching Board-level thresholds. This gives the FRAC additional buffer to address potential issues before one year elapses.”

4.2 Generative AI (GAI) Model and Future Plans
	•	Question (Regulator):
“We noticed the ESGAI model was recently approved. It’s a large language model. Could you talk about your broader approach to Generative AI? Are you looking at many use cases? Any specific risk governance for GAI?”
	•	Response (Firm):
“Yes, ESGAI is our first Tier 1 GAI model. Most GAI uses here have been low-risk, operational-efficiency tools. All GAI models go through our existing model risk process with dedicated AI/ML validation templates. In addition, we’ve established an AI Risk and Controls Committee, which includes operational risk, legal, compliance, and other relevant control functions. This committee provides an additional oversight layer beyond standard model validation due to heightened concerns like data usage and privacy. We have indeed seen growth in AI models, but many are Tier 2 or Tier 3, and they must follow the same rigorous validation processes.”

4.3 Internal Audit Findings and Documentation
	•	Question (Regulator):
“You mentioned a few internal audit findings related to documentation. How is the firm addressing these gaps? Is there specific training for staff?”
	•	Response (Firm):
“Most findings identified by internal audit focused on documentation clarity, not on the validity of model outputs or effective challenge. We’ve already remedied several of these items. For the most recent one (raised in Q4), we are developing a formal training program for our validators to reinforce comprehensive documentation standards. Our target is to complete this training by the end of April.”

4.4 Model Inventory Trends
	•	Question (Regulator):
“Your inventory is generally stable, but there was a slight uptick in Q4. What drove that, and do you see any issues with timely validations?”
	•	Response (Firm):
“The small increase reflects typical new-model approvals and changes in existing models. We’re closely monitoring them through our waiver process. Each model requiring validation has a remediation timeline, and we track these carefully. We haven’t identified any major delays beyond standard extensions. Our aged metrics help ensure nothing languishes past the original due date.”

4.5 Market Volatility and Model Performance
	•	Question (Regulator):
“Given recent market volatility, have you enhanced your daily model monitoring processes? Notably, are any pricing or risk models showing stress or breakage?”
	•	Response (Firm):
“We conduct daily run tests, and so far, we haven’t seen any unusual breakage or unexpected parameter shifts. Our teams also proactively check for large market shocks. If we see unusual code changes or anomalies, that prompts deeper scrutiny. At this time, we’re not seeing significant performance issues.”

⸻

5. Action Items and Next Steps
	1.	Acknowledgment Letters:
	•	Regulators will send acknowledgement letters regarding the firm’s recent supervisory response.
	2.	Follow-Up on Severity 1 Model:
	•	The firm to confirm details regarding a Severity 1 finding in the Risk division (to clarify if the model was in use or in development).
	3.	Documentation Training:
	•	The firm to complete the new training program for validation staff by end of April.
	4.	Monitoring of Market Volatility:
	•	The firm will continue daily run tests and step up monitoring for any potential volatility-driven model errors or breakages.
	5.	Generative AI Governance:
	•	The firm to keep regulators informed of further developments, approvals, or changes in the GAI framework and usage.

⸻

6. Conclusion
	•	The regulators confirmed receipt of the quarterly update materials.
	•	The firm provided detailed updates on the model risk inventory, waiver threshold changes, and the status of internal audit findings.
	•	Generative AI governance remains a focus, with new oversight committees and processes in place.
	•	No immediate concerns were raised regarding market volatility or model performance.
	•	Both parties agreed to continue close communication and follow up on open items and training initiatives.

⸻

These minutes capture the primary points of discussion, key questions and responses, and agreed-upon next steps.






Below is a revised version you might find clearer and more concise:

Revised Response:

The CEU calculation is embedded within the Tier D1 SA-CCR DRC. In alignment with the Firmwide Standards for Deterministic Regulatory Calculations, MRM conducts an annual review of all Tier D1 DRCs to confirm their ongoing validity, considering potential changes to the DRC itself or the surrounding operating environment. In addition, Tier D1 DRC developers are required to obtain IRG approval for any DRC modifications before implementing them in production.

Furthermore, continuous monitoring procedures are in place to maintain the accuracy of the DRC. These procedures include daily regression tests and weekly ongoing monitoring reports to verify the CEU determination logic.

This version groups the key points more clearly, highlights responsibilities, and streamlines the language. You can adjust the level of detail or formality to suit your specific needs.





A new 1-month “staple-shaped” instantaneous forward rate (IFR) discontinuity for the USD Secured Overnight Financing Rate (SOFR) curve, which is based on 3-month SOFR International Money Market (IMM) futures, addresses short-end constraints and enables more granular control at the 1-month level.


A new “staple-shaped” IFR discontinuity—two offsetting jumps spaced one month apart—was introduced to the USD SOFR curve to address short-end constraints driven by 3-month SOFR IMM futures and CFR interpolation in IFR space, while preserving CER interpolation and enabling more granular 1-month control, specifically allowing the desk to manage 1-month serial SOFR/FF basis levels previously beyond their reach.



A new “staple-shaped” IFR discontinuity—two offsetting jumps spaced one month apart—was introduced to the USD SOFR curve to address short-end constraints driven by 3-month SOFR IMM futures and CFR interpolation in IFR space, while preserving CER interpolation and enabling more granular 1-month control, specifically allowing the desk to manage 1-month serial SOFR/FF basis levels previously beyond their reach.




The USD SOFR curve is constructed to reflect future financing rates, but in practice, traders often need finer adjustments at shorter intervals—particularly around monthly roll dates—so this new “staple-shaped” IFR discontinuity, composed of two offsetting jumps spaced one month apart, was introduced to allow more precise control at the 1-month point within each 3-month IMM period, ensuring better alignment with market realities and short-term rate movements.


A new “staple-shaped” IFR discontinuity—two offsetting jumps one month apart—was introduced to the USD SOFR curve to provide finer 1-month control within each 3-month IMM period, fulfilling the desk’s need for more precise short-end management.




Below is a detailed, thematic summary of the conversation. It focuses on the main topics discussed, the context behind them, and the next steps or action items that arose.

1. Upcoming Meeting With Brian (Wednesday Morning)
	•	Schedule and Materials
	•	The speakers confirm that a meeting with Brian is still planned for Wednesday morning (referred to as “Wednesday 45”).
	•	They note that materials being circulated are updates that were originally prepared for a prior meeting which “got bumped.”
	•	Topics to Cover
	1.	Emery Remediation: Provide an update and refresh of the remediation bid, given schedule changes.
	2.	AI Topics:
	•	Growth and modality of AI resources (e.g., HPC usage).
	•	“AI acceleration proposal” and a related summary from “AI governance from table.”
	3.	Leslie’s Request:
	•	There is a question about integrating an ask from Leslie.
	•	The group is unclear on the background or context of Leslie’s query and wonders where it originated.
	•	This might be an opportunity to review the DAIS process for Brian, including divisional representation (e.g., Jay, Constantine).
	4.	Additional AI Initiatives:
	•	The team wants to get a comprehensive list of ongoing or potential AI ideas from Jay.
	•	They plan to be “opinionated”—assessing which ideas are more likely to succeed and which are less so, potentially identifying gaps or overlooked opportunities.
	•	They also discuss how success in production (e.g., an AI-driven validation or summarization tool) could reinvigorate interest.
	5.	Resources and Headcount:
	•	Part of the AI discussion centers on highlighting resource constraints, budget (ZPP), and headcount needs.
	•	They mention HPC usage charts, exponential growth, and how to represent (or exclude) certain large allocations (e.g., T204, AI platform) to make the data clearer.

2. Additional AI Updates and Observations
	•	Big Models / AI 2.0
	•	There are bank-wide efforts around large model initiatives.
	•	Upcoming pilot projects (e.g., “blockingination detection”) for GBM public vs. private.
	•	Positioning and Ownership
	•	Speakers note they want it clear that their team is spearheading AI efforts, rather than another department (OAS).
	•	They also mention synergy with AI HPC resources and that there’s ongoing work with other teams (e.g., “AirCC stuff”).

3. Other Agenda Items for Brian
	1.	IRR & CCAR
	•	They plan to refresh Brian on the status of IRR work and CCAR updates.
	2.	Lotus, RCSA, and Issue Management
	•	They have bullets to discuss, given Brian’s ongoing focus on RCSA (Risk and Control Self-Assessment) and issue management.
	•	One point is the milestone reached on some RCSA deliverables (control library sign-off, for instance).
	•	They need final confirmation on a control-library spreadsheet from compliance (“someone in compliance emailed a spreadsheet”).
	•	The group believes the changes align with prior agreements and likely just require official sign-off.

4. Metrics and Findings
	•	Current ‘No Breach’ Moment
	•	The team discusses how for certain key metrics, there are currently no active breaches.
	•	However, there may be potential upcoming breaches (e.g., a repo-related one).
	•	Tracking the Overall Findings Count
	•	They recall the count of open findings used to be quite high (possibly 40–50), and they are now aiming for a lower number (around 22).
	•	They see progress in some areas but mention continued friction in others (e.g., market risk consistently missing deadlines unless escalated).
	•	Possible Thematic Findings
	•	They are considering raising “thematic findings” for any group that remains in persistent metric “red” status.
	•	One idea is to pick a date (e.g., April 1) after which the team will systematically raise findings if certain metrics remain red, ensuring consistent application across GBM and other divisions.
	•	RCSA Integration
	•	Ongoing conversations about how the new RCSA processes (led by the central risk organization) align with day-to-day controls and findings management.
	•	There is mention of how risk teams only do RCSA events semiannually, making control-effectiveness updates slow.

5. “Breach Response Plan” and Workflow Tool
	•	New Policy Requirement
	•	A new policy mandates that any breach must have a response plan (with an ETA) approved by the CRO (Alex).
	•	The group references a “breach workflow tool” originally developed for Market Risk.
	•	Challenges
	•	The tool is not well-suited to ongoing or long-standing breaches (as often happens in this group’s processes, which can remain “over” for extended periods rather than a short event).
	•	Using the tool daily for repeated, unchanged breaches would be an administrative burden.
	•	Seeking Clarification
	•	They want clarity on how detailed Alex wants these response plans to be.
	•	They had initially thought an exemption might be possible, but it appears certain stakeholders (e.g., Motrum) insist on using the new tool regardless.
	•	Next Steps
	•	There is a follow-up call scheduled (moved to “tomorrow”) to discuss a possible exemption or a more streamlined process for these “long-running” or “operational” types of breaches.
	•	They note that other teams (like OpRisk) have similar issues, though some (like Phil’s group) appear to have already acquiesced.

6. Action Items & Points of Emphasis
	1.	AI Resource & Budget Discussion
	•	Finalize HPC usage charts, deciding whether to include or exclude large platform allocations, to clarify the growth story for Brian.
	•	Emphasize how the AI demands and expansions fit into the existing headcount and budget constraints (ZPP).
	2.	List of AI Initiatives
	•	Obtain the comprehensive list from Jay/Constantine.
	•	Formulate opinions on which projects have the highest chance of success or strategic value, plus mention any new opportunities not currently on that list.
	3.	Sign-off on Control Library
	•	Confirm agreement with the recent spreadsheet from compliance and provide official go-ahead.
	4.	Metrics Updates
	•	Refresh the table for Brian, highlight improvement trends, but also outline the areas (e.g., Market Risk) still needing regular escalation.
	5.	Thematic Findings Escalation
	•	Potentially propose a set start date (e.g., April 1) for systematic escalation via thematic findings when certain divisions remain in red status.
	6.	Breach Response Plan Tool
	•	Attend the follow-up meeting to see if an exemption or adapted process can be reached.
	•	Seek Brian’s input on the best approach to manage daily operational/long-term breaches under the new policy.

Overall Takeaways
	•	Preparation for Brian: The team plans to cover AI updates (including acceleration proposals, resource constraints), risk metrics (breaches, findings, and open issues), and RCSA progress.
	•	Administrative & Policy Burdens: New policy requirements (e.g., breach response tool) may be ill-suited to how this team typically manages longer-running issues, prompting them to seek alternatives or clarifications.
	•	Governance & Ownership: They want to highlight clearly where AI efforts truly sit (their team vs. other groups), underscore successes in HPC usage, and clarify budgetary needs.
	•	Ongoing Friction Points: Persistent challenges with market risk’s responsiveness to escalations and confusion over RCSA processes remain important discussion items for Brian’s input.

This summary reflects the key points and context from the transcript. It consolidates who is doing what, where the main pressures or problems lie, and which decisions or clarifications need leadership input.





A new “staple-shaped” IFR discontinuity—two offsetting jumps one month apart—was introduced to the USD SOFR curve to address short-end constraints and enable more granular 1-month-level control within each 3-month IMM period.



Below is a consolidated, detailed summary of the conversation. It organizes the main points and clarifies the various threads that came up during the discussion:

1. Purpose of the Conversation

The speakers are discussing a series of updates and action items related to:
	•	AI-related projects and communications
	•	MRA (Matter Requiring Attention) remediation status
	•	Upcoming meetings with different committees (BRC, FRAC)
	•	Governance and risk-related items (RCSAs, capital risk, expansions, etc.)
	•	Scheduling constraints, especially with one person being out on Tuesday

The conversation centers on making sure that final materials (particularly for BRC and FRAC) are up to date, reflect recent changes, and incorporate feedback from various stakeholders.

2. AI Updates and Communication
	1.	Polished Language / Revised Notes
	•	There are existing AI updates, some of which overlap with emails sent to Alex and Gopi. The idea is to “true up” or refine the wording to match a more polished version already in circulation.
	•	There are also notes from a meeting with Michaela and a governance roundtable (led by or involving Eric Goor) that should be incorporated into the AI section of broader governance or committee materials.
	2.	Continued Improvements in CCR and ASL
	•	The conversation touches on CCR (likely a risk or compliance model/tool) and ASL (possibly another internal system or tool). Both are undergoing continual enhancements. The group wants to decide if these ongoing improvements are significant enough to highlight in upcoming committee materials.
	•	The suggestion is to confirm with team members (e.g., Javarianna or Andresa) which specific enhancements might be noteworthy or relevant for the committees.

3. MRA Remediation Status
	1.	Background
	•	The MRA remediation appears to be a priority topic for multiple committees (BRC, FRAC).
	•	There were originally 19 total findings from some form of audit or review (by ERM or an external body), of which most have been remediated. Three remain open.
	2.	Committee Presentations
	•	The question arises whether MRA remediation should stand on its own as a separate discussion item, especially since some committees have specific agendas that may or may not align with MRA topics.
	•	There is a desire to keep the language very clear about what has been done so far (e.g., the 19 findings, how many were resolved, and the plan for the remaining open items).
	3.	Capital Risk Table Issue
	•	The speakers reference a table or chart that addresses “capitalist challenges” or “capital risk,” which might incorrectly lump MRA remediation into a broader risk discussion.
	•	There is a need to ensure that MRA items are accurately represented and not placed into a table that could suggest a mismatch of issues. One speaker references Kevin’s email, noting that bullet points about MRA have been removed from that particular risk table to avoid confusion.

4. Upcoming Meetings and Materials
	1.	Meeting Schedule
	•	A “stress meeting” is confirmed for Wednesday.
	•	Brian’s meeting is happening on Tuesday afternoon.
	•	The FRAC and BRC materials need to be prepared by Thursday and Friday, respectively, to align with upcoming sessions.
	2.	Committee Packets
	•	The final versions of FRA and BRC decks (or related material) should incorporate big topics: MRA remediation, significant AI updates, CCR/ASL enhancements, and any other noteworthy developments.
	•	There is interest in ensuring the committees receive clear, polished language that reflects current progress on these initiatives.
	3.	RCSAs (Risk & Control Self-Assessments)
	•	The Q4 RCSA results (at least for GBM) will need to be included in the upcoming committee updates or presentations. The speaker intends to finalize these results by Tuesday night to be ready for review on Wednesday.

5. Potential DRC Expansion
	•	There is mention of expanding something called “DRC” to EIA (the acronym is not fully defined in the conversation).
	•	Engineering teams would need to propose an onboarding plan and resource estimates.
	•	It does not appear to be budgeted for this year, so the timeline is still “to be determined” (TBD).

6. Action Items and Next Steps
	1.	Refining Documents
	•	Incorporate polished language from the “already circulated” AI updates, along with notes from Michaela’s meeting and Eric Goor’s governance roundtable.
	•	Clarify the MRA remediation language so that it properly captures the status of the open/closed findings.
	2.	Coordination with Various Stakeholders
	•	Check in with specific team members (e.g., Andresa, Javarianna) to see if the ongoing CCR/ASL upgrades warrant highlighting in committee materials.
	•	Coordinate with Kevin (and possibly others) to ensure MRA references are correctly presented or removed from any confusing risk tables.
	3.	Preparing for a Busy Week
	•	One person will be out on Tuesday, so they plan to work remotely or at night to finalize certain documents, especially the RCSA updates.
	•	Materials for BRC and FRAC should be ready by Thursday/Friday, noting that the MRA remediation will likely be a central topic.

7. Overall Takeaways
	•	Timely Updates: Multiple committees (BRC, FRAC) need accurate, up-to-date information on MRA remediation, AI/CCR/ASL enhancements, and RCSA results.
	•	Clear Communication: The transcript underscores how critical it is to fine-tune the language in presentations, especially around MRA findings and any risk tables, so that committees receive an accurate picture.
	•	Resource Planning: Some items, such as the DRC expansion, remain in a preliminary stage and need budget/resource alignment before proceeding.
	•	Logistics: Owing to schedules (someone being out Tuesday), final reviews will be done quickly—some on Tuesday night, with a final check on Wednesday morning, before the materials go to their respective committees.

In essence, the conversation is a coordination meeting to ensure that various corporate governance and risk materials—especially around MRA remediation and AI—are updated, aligned with stakeholder feedback, and ready in time for important committee sessions.





Below is a concise summary of what was discussed (and planned) for the upcoming Monday “PO” call based on the transcript:

Purpose of the Monday PO Call
	•	Gather and review any pressing regulatory items that need to be communicated or escalated.
	•	Check in on outstanding action items (e.g., T TBP cleanup, Fed submissions, etc.).

Main Discussion Topics
	1.	Regulatory Updates (SEC, FINRA, Fed)
	•	SEC AP Model Request:
	•	A minor submission item; no major concerns expected.
	•	Team will confirm details are finalized or if any clarifications are needed.
	•	FINRA Follow-ups:
	•	There may be outstanding follow-up items to communicate or confirm.
	•	Fed-Related Items:
	•	Briefly mention the upcoming CEU meeting with the Fed.
	•	The team will also touch on the submission of the latest inventory to the Fed (Ariana is handling details).
	2.	T TBP (Trade/Transaction Booking Policy) Cleanup
	•	The group wants to highlight the revamp of the T TBP process.
	•	Open Tickets: People with older booking policy exceptions need to review or close them.
	•	The call is a chance to remind owners of outstanding tickets to address them by a certain deadline.
	•	Follow-up Strategy:
	•	Phil (and possibly Prashant) will help chase updates from London-based or harder-to-reach teams.
	•	If no response is received from owners, tickets may be closed or escalated.
	3.	CCAR / General Fed-Submission Updates
	•	A short update on any CCAR-related progress or requirements if relevant.
	•	Mention if there are any regulatory due dates or deliverables in the next couple of weeks.
	4.	High-Level Reminders
	•	Governance Team Constraints: The governance team is understaffed at the moment (with Lena’s departure and someone else out sick), so be mindful of how much is assigned to them.
	•	Upcoming Committee Meetings: BRC and FRAC are on the same timeline (February 27). The call might briefly confirm any dependencies or next steps related to preparing materials.

Outcome / Next Steps for the PO Call
	•	Finalize which items to present: The group will decide which updates (SEC AP model, FINRA follow-ups, Fed inventory submission) need more attention on the call.
	•	Set a Deadline for T TBP Ticket Closures: Communicate a clear plan for owners to respond or close their tickets.
	•	Coordinate with Key Stakeholders: Ensure people like Ariana, Phil, Prashant, and others are looped in for their respective pieces of work.
	•	Confirm Prep for Regulatory Meetings: Decide if any additional materials or summaries are needed for the Fed or other regulators.

That covers the main points expected to be addressed in the next Monday PO call based on the conversation.





Below is a concise summary of the main points discussed in the transcript:
	1.	Lotus Data Source Changes
	•	There is a plan to move certain Lotus-related calculations from existing (“non-alternative”) data sources to a new, presumably higher-quality data source.
	•	The team expects fewer manual overrides and improved data quality once these new sources are implemented.
	•	Follow-up reviews may be required after the switch, but the team will perform checks to ensure the transition does not worsen data quality.
	2.	Expansion of LCO (Europe Scope)
	•	There is discussion about expanding LCO coverage in Europe.
	•	This expansion was not previously budgeted, so the team needs to determine resource requirements, timeline, and headcount.
	•	Further planning with senior stakeholders (e.g., “BB”) is needed to clarify scope and funding.
	3.	UK’s Stance on Basel 3 and Resulting Budget/Planning Implications
	•	The UK has decided not to proceed with full Basel 3 implementation.
	•	This decision impacts prior plans, budgets, and potentially the technical approach to regulatory calculations.
	•	The team notes that any rework (e.g., rewriting certain calculations) could be as large an undertaking as the initial DRC (Default Risk Charge) build.
	•	They emphasize the need for a strategic discussion on how to manage the additional workload and align resources accordingly.

Overall, the conversation centers on upcoming data-source transitions, regulatory scope expansion in Europe, and the budget/timeline adjustments required in light of the UK’s Basel 3 decision.



Below is a concise summary of the main points and discussion threads in the transcript:
	1.	Upcoming Meeting With Brian (Monday)
	•	The speakers are planning to update Brian on several topics, including AI guardrails (previously discussed), final adjustments to the ETSC framework, and an introduction of a “pro reject” approach and systematic consumer testing.
	•	They also want to bundle together updates around MRM, ETSC, and ETP commitments to provide a cohesive “end state” picture.
	2.	AI Topics & T/Risk Coordination
	•	There is friction regarding how T/Risk and second-line teams process reviews and the perception that second-line processes are slowing down AI initiatives.
	•	T/Risk appears to be deferring some steps or waiting until after MRM reviews to avoid repetitive rework.
	•	The team notes that developers (and others) sometimes blame risk/control functions for delays, but emphasize that T/Risk is independent and has its own process.
	•	The group considers having a direct conversation with T/Risk (possibly with “Car”) to clarify procedures and reduce miscommunication—ideally in person rather than via email.
	3.	New Detection Model for T2
	•	There is a mention of a new AI-related detection model with shorter latency (around one second).
	•	The plan is to pilot it for bankers and eventually expand it for GS or broader usage.
	•	It would be “preventative” rather than “detective,” checking documents in real time.
	4.	Transformer Model for Short-Term Trading Signals
	•	A separate team is building a transformer-based model to generate trading signals over very short windows (e.g., ten seconds).
	•	Discussion centers on how MRM or second-line could effectively validate or test these kinds of real-time models, which can be challenging with fast market data.
	•	There is a question of whether this transformer approach qualifies as “GI/AI” given it is presumably much smaller scale than large language models (LLMs).
	5.	Buyback Trade and MMLat Update
	•	Brief reference to a new client-related buyback trade (about 500 million EUR) with some discontinuities in payoff.
	•	Possible plan to mention this to Brian if relevant, though it may be more detail than he needs.
	6.	FRAC Breaches and New Workflow Tool
	•	They discuss persistent FRAC (Framework for Risk Appetite Compliance) breaches and the firm’s protocol for addressing them (e.g., obtaining new committed dates, root-cause explanations).
	•	A new “breach action plan protocol” and workflow tool from risk engineering might soon be mandatory.
	•	Concern is raised that this new process was built primarily with market risk in mind and might be too cumbersome or less relevant for non-financial risk.
	•	They note it will require some scrutiny to ensure it makes sense for their specific use cases before they adopt it.
	7.	Regulatory Exam (Michaela / Next Steps)
	•	The team wants clarity on how aggressively to respond to exam feedback from regulators.
	•	They sense the regulatory examination team might be split: some think the current approach is adequate, others believe more thorough documentation is required.
	•	They plan to see if they can glean more information informally during upcoming meetings (e.g., an MRM “conclave”).
	•	They also discuss whether scheduling time directly with Michaela after some internal alignment might be beneficial.
	8.	General Approach & Next Steps
	•	The speakers plan to provide Brian with a summary of all these points: AI guardrails, ETSC framework, T/Risk coordination, FRAC breaches, CCR updates, and possible buyback trade updates.
	•	They will also flag any overhead or headcount concerns if new processes (e.g., the FRAC workflow tool) become mandatory.
	•	They consider setting up a timeline for year-end tasks (e.g., internal sign-offs, next regulatory discussions) and ensure they coordinate well with leadership and exam teams.

Overall, the conversation focuses on preparing for an upcoming leadership update (with Brian), addressing AI model governance (especially T/Risk interactions), dealing with repeated FRAC breaches, and strategizing regulatory engagements and next steps.












Summary of the Meeting
	1.	Overall Exam Objective and Process
	•	The Federal Reserve exam focused on assessing the firm’s Model Risk Management (MRM) framework and practices, including governance, model development, model validation, and ongoing monitoring procedures.
	•	The examiners conducted transaction testing to evaluate how well the firm executes its MRM procedures in practice.
	•	The exam occurred virtually between September 20, 2024, and November 15, 2024.
	2.	Key Conclusion: Generally Satisfactory but One MRA Issued
	•	Examiners concluded that most components of the firm’s MRM framework are “generally satisfactory.”
	•	However, the exam identified a control deficiency in the validation framework for “in-use” models. This deficiency may impede the firm’s ability to confirm that models remain appropriately calibrated and fit for purpose over time.
	•	As a result, an MRA (Matter Requiring Attention) is being issued regarding weaknesses in the model validation controls framework.
	3.	Details of the MRA
	•	Deficiency in Qualitative Assessments: Although the firm uses both qualitative and quantitative tools to assess model performance, there is insufficient documentation or substantiation for qualitative assessments, except in cases that trigger additional validation or remediation.
	•	Limited Evidence of Qualitative Reviews: During quarterly and annual reviews, examiners saw little evidence that qualitative assessments had actually been performed or documented.
	•	Infrequent Revalidations: A significant proportion of models have not been revalidated over recent years, raising safety and soundness concerns—particularly for higher-risk models that are not automatically subject to periodic revalidation.
	•	Remediation Required by December 31, 2025: The firm must enhance its MRM practices so that both quantitative and qualitative assessments are adequately and consistently supported, especially in quarterly/annual reviews for higher-risk models.
	4.	Clarifications on Revalidation Frequency
	•	The Federal Reserve does not mandate specific revalidation intervals in the guidance. However, the examiners emphasized the importance of confirming that models remain fit for purpose on a regular basis.
	•	The MRA focuses on ensuring ongoing, evidence-based checks rather than dictating a particular revalidation schedule.
	5.	Observations on the Apple Card CECL Model (Model 2381)
	•	While these issues are not new findings (they were already noted in a previous ACL exam), examiners reiterated concerns regarding:
	1.	Model Development: Issues in regression inputs, regression-output evaluation, and insufficient model-fit testing.
	2.	Model Documentation: Limitations and compensating controls were not prominently highlighted, and documentation did not meet MRM standards.
	3.	Model Validation: Validators did not sufficiently justify use of the same approach for Apple Card and the Apple Card monthly installment product. Excessive use of time dummy variables raised concerns about overfitting, which was not challenged by validators.
	4.	Ongoing Monitoring: Thresholds are set such that red performance is only triggered if both the Apple Card model and an alternative model underperform—this dependency might mask issues.
	•	Supervisory findings related to this model remain open from the previous ACL exam, so no new formal findings are being issued here. However, the examiners encouraged continued remediation and deeper engagement if needed.
	6.	Next Steps
	•	The firm plans to review the final exam letter in detail and then discuss with the Federal Reserve examiners how best to address the MRA.
	•	Examiners will continue quarterly monitoring; during these updates, the firm can raise any questions about the MRA or other related issues.

Overall, the meeting emphasized the importance of comprehensive and well-documented qualitative assessments, alongside quantitative monitoring, to ensure all models in use remain appropriately calibrated and truly fit for their intended purpose—particularly in rapidly changing market or business environments.






Below is a structured, detailed summary of the conversation. It reflects the key points, the context surrounding each, and the follow-up actions or concerns raised during the discussion.

1. Upcoming Meeting with Brian (MRM Exit Meeting)
	•	Schedule Confirmation: There is an MRM (Model Risk Management) exit meeting planned with Brian on Monday (or possibly Tuesday).
	•	Agenda Items:
	•	Regulatory Updates: The team wants to finalize and present various regulatory updates, including Basel-related developments and some second collateral allocator issues.
	•	AI Updates:
	•	Recent internal “guardrail” approvals.
	•	Governance process changes for AI usage.
	•	Overview of AI initiatives in production and a forward-looking view (next quarter or two).

2. AI Initiatives and Business Use Cases
	•	Large Language Models (LLMs): There is a mention of a “long list” of large LLM-based tools that will impact more models soon.
	•	Generative BI (Business Intelligence): Discussion of projects integrating generative AI for reporting and decision support.
	•	Project Mentions:
	•	“TBMs, the strocking with lia project piano” (the details are somewhat unclear, but these appear to be internal code names or project references).
	•	A “phase two” rollout is coming soon, possibly for a next-stage AI or machine-learning tool.
	•	User Feedback:
	•	The group wants someone unbiased (e.g., Erica or Wesley) to provide feedback on AI’s accuracy and utility.
	•	Current AI accuracy is reported at 91%, which they note is often better than what humans achieve—though there’s some question about the thoroughness of the resources supporting it.

3. Discussion on Electronic Trading & Market Conduct
	•	Market Conduct Rules: Brief mention of “market conduct for ETPs” (Exchange-Traded Products) and possible inclusion in the upcoming Brian meeting agenda.
	•	CBA Switch / Puzzle 3: There is a mention of a “puzzle for CBA switch,” though the relevance to the meeting’s main agenda is uncertain. It might be included in broader regulatory updates (e.g., “Basel 3,” European submission).

4. Regulatory / Basel 3 Updates
	•	Follow-Up for Brian: They want to combine recent updates on Basel 3 and other European regulatory changes into one summary for Brian.
	•	Addressing Brian’s Questions: There were questions posed by Brian previously (possibly about Basel or capital adequacy), and the team intends to provide a verbal update or bullet points clarifying those.

5. Second Collateral Allocator Issue
	•	Year-End Material Issues:
	•	There were multiple DRC (Default Risk Charge) and SOKR (possibly “Securities or Collateral” references) issues discovered before year-end.
	•	A new “bill” was posted, but the conversation implies that some details might still be unresolved.
	•	Open Points: The team is trying to recall specifics and ensure Brian is updated on these items if they are significant.

6. Metrics & Remediation Progress
	•	ATLC Findings:
	•	Initially quite high (21 issues), reduced to 14, but further progress has been slow or complicated by new items.
	•	Term Structure / “Tier One Age” Findings:
	•	Talk of metrics going from 54 down to around 20-something. The official numbers are stale (from November) and likely improved by year-end.
	•	GBM Findings:
	•	Not as much progress as hoped. Internal push is needed since the front office is apparently comfortable breaching “track” but not “work” (i.e., not meeting internal deadlines but not necessarily failing official regulatory deadlines).
	•	The team wants to escalate this reluctance to Brian and/or Alex to enforce accountability.

7. Communication & Escalation Strategy
	•	Follow-Up with GBM:
	•	The group has trouble getting consistent updates from GBM on remediation.
	•	Leadership in GBM told staff it is fine to breach the internal trackers (frack?), just not the official regulatory ones—a stance the MRM/validation team finds unacceptable.
	•	Involving Senior Leadership:
	•	Alex and Brian may intervene directly (e.g., phone calls) to reiterate the importance of meeting internal timelines and obligations, not just external regulatory ones.
	•	Maintaining “Statute”:
	•	The MRM team wants to keep up pressure and avoid undermining their own authority. They plan to phrase remediation deadlines as mandatory rather than negotiable.

8. Market & Trading-Book Observations
	•	Discount Curve Steepening:
	•	Nearly 200 basis point difference between lower short-term rates and the 10-year, while the Fed has cut rates 75 bps.
	•	The team wonders if there are notable trades or modeling issues tied to this rate environment.
	•	Risk Limits and VAR:
	•	In GTM space, the desk is apparently long USD 2.7 billion, but net risk is offset or “carnations inside,” so the VAR isn’t drastically affected. The group wants color on the rationale behind these positions.

9. Additional Model-Related Items
	•	CCAR Scenario & Narratives:
	•	Some new or ongoing approach to running the CCAR scenario with narrative explanation.
	•	The governance around these new modeling efforts is still being documented.
	•	“Canal” Ambitious Model:
	•	Possibly focusing on hedge funds or natural resources counterparties.
	•	There’s some confusion over classification by counterparty (natural resources) vs. classification by risk factor.

10. Final Preparations & Next Steps
	•	Meeting with Alex (Friday):
	•	The team plans to brief Alex or run certain items by him before bringing them up with Brian.
	•	There may be “red items” or urgent topics to discuss, but details are limited.
	•	Action Items:
	1.	Regulatory/AI/Model Updates: Finalize bullet points for Brian.
	2.	Finalize Basel 3 Follow-Up: Combine into a single document/summary.
	3.	Escalation on GBM Findings: Provide specific examples and names if needed so Alex/Brian can intervene.
	4.	Check on Market Risk Positions: Look into the discount curve steepening trades and how the bank is positioned.
	5.	Continue Gathering User Feedback on AI Tools: Identify an unbiased user champion (e.g., Erica, Wesley).

Overall Takeaway

The conversation revolves around preparing a thorough update for senior management (notably Brian, possibly Alex) covering:
	1.	Regulatory developments and outstanding remediation items (particularly around Basel 3 and the year-end findings).
	2.	AI initiatives and governance (accuracy rates, use cases, next-phase deployments).
	3.	Internal compliance challenges (GBM’s reluctance to meet MRM internal timelines).
	4.	Market insights (steepening rate curves, large positional bets).

The team is focused on ensuring a clear, consolidated message for Brian’s meeting, spotlighting progress, risks, and necessary escalations for effective remediation and accountability across business units.









Summary of the Transcript

The transcript outlines various updates and discussions on model risk management (MRM), remediation timelines, validation processes, and upcoming regulatory exams. Below is a summarized version of the key points:

1. Model Submissions and Remediation Timelines:
	•	Abilitiesization and Launch Timeline: The project has started but is not fully on track; the deadline is March.
	•	Prime Model BCD Review: Due by the end of January, focusing on outcomes analysis and implementation. Challenges are manageable, and findings will likely be combined with GSSEV validation (due mid-February).
	•	MR Remediation: Several findings with staggered timelines:
	•	Fed-raised issues require resolution by March.
	•	Sequencing steps involve December, February, and March milestones.
	•	Risk of findings remaining open for MR submission, though efforts are being made to avoid this.

2. Backtesting:
	•	Implementation has been received and is under review.
	•	Milestones for thresholds and frameworks are delayed until March.
	•	High-level testing is ongoing; main flaws may lie in the implementation phase.

3. Model Group and Gap Analysis:
	•	Reviews are on track, including:
	•	Theta model gaps (targeting 2025).
	•	Non-parallel scenarios (pending timeline adjustments after December 24th communication).

4. Calibrations and Monitoring:
	•	A decision on full model recalibration versus annual reassessment is pending, with recalibration likely, potentially resolving findings.
	•	New scenarios and metrics are being developed for cross-currency bases and sensitivity analysis.
	•	Frameworks for identifying key assumptions in sensitivity analysis are being finalized.

5. Exams and Exercises:
	•	ILST Exam: Materials are due by January 15th, with the exam in March. Key focus areas include governance, IT data, modeling documentation, and ongoing monitoring.
	•	BAU LGD Exercise: Scope is broad, including dependencies like FLR models, with a focus on inventory findings and validation logs.

6. General Risks and Concerns:
	•	Several findings are delayed, but efforts are being made to manage risks and ensure compliance with deadlines.
	•	Scope creep in certain exercises (e.g., BAU LGD) may require additional clarification and resource management.

Overall, the discussion reflects ongoing progress with manageable delays, a focus on implementation reviews, and preparations for regulatory exams and validations.












Below is a more detailed explanation of the DRC (sometimes referred to as “Decentralized Risk Categories” or similarly named regulatory/capital calculations) discussion and how they can be categorized, based on the transcript. The ultimate goal is to provide clarity on which DRC items fall under current policy scope (U.S. capital), which apply to specific non-U.S. legal entities, and which may fall outside capital rules altogether (e.g., liquidity requirements).

Why Categorize DRCs?

In the transcript, there was a concern that “DRCs” appear in multiple contexts—some are for U.S. capital calculations, some apply to foreign legal entities, and some may be tied to other regulations beyond capital (like liquidity or resolution planning). The team needs a systematic way to track each DRC so they can:
	1.	Explain the current state: Which DRCs are already covered by policy?
	2.	Identify gaps: Where do we lack clarity on coverage (e.g., newly discovered DRC items for non-U.S. entities)?
	3.	Plan next steps: Decide what to uplift, what to address later, and how to handle DRCs outside the “official” policy scope.

Three-Tier Categorization Approach

A straightforward approach is to create separate sections or tables that group DRCs by their applicability and underlying regulation:
	1.	Table A: U.S. Capital (Current Policy Scope)
	•	What’s included: All DRCs that fall under existing U.S. regulatory capital rules (Federal Reserve, OCC, FDIC).
	•	Subsections:
	•	Already Uplifted: DRCs that have been identified and fully addressed in policies/procedures.
	•	Pending Prioritization: DRCs recognized as in-scope for U.S. capital but not yet remediated or prioritized.
	•	In Development: Future changes (e.g., Basel 3 Endgame, FRTB) that will require new or updated DRCs.
	2.	Table B: Non-U.S. Legal Entities
	•	What’s included: DRCs that apply to legal entities beyond the U.S. scope, such as GSI (in the UK), GSIB, GSPE, or more specialized entities (e.g., GSJC for real estate).
	•	Goal: Clarify whether each DRC is (or should be) covered under your firm’s global capital policy, or if it’s governed by local rules (e.g., PRA in the UK, ECB for EU entities).
	•	Format: For each legal entity, list:
	•	DRC Name
	•	Purpose (e.g., local regulatory capital requirement, local liquidity coverage, resolution planning)
	•	Governing Regulator
	•	Current Status (covered in existing policy or not)
	3.	Table C: Non-Capital Requirements (Liquidity, Resolution Planning, etc.)
	•	What’s included: DRC items that are not strictly capital-related but may be risk or regulatory-driven, such as LCR (Liquidity Coverage Ratio), resolution planning, or other reporting requirements.
	•	Key Question: Are these truly DRCs (in the sense of capital/risk models), or are they something else (like a purely operational or accounting reserve)? If they’re capital-like items, do they fall under any existing policy or do they need a new governance path?

Sample Breakdown of Each Category

Here is a simplified illustration of how you might lay out the tables. (The exact content and naming conventions would depend on your firm’s taxonomy.)

Table A: U.S. Capital

DRC Name	Regulatory Source	Policy Status	Next Steps
DRC 1 – US Fed	Federal Reserve	Uplifted in 2023	Periodic review in Q1 2024
DRC 2 – FDIC Rule	FDIC (US)	Pending Prioritization	Finalize by Q2 2024
DRC 3 – Basel 3E	US Implementation	In Development	Monitor upcoming Basel 3 Endgame framework

Table B: Non-U.S. Legal Entities

Legal Entity	DRC Name	Regulator	Included in Policy?	Notes
GSI (UK)	DRC 4 – PRA Capital	PRA/BoE (UK)	Not in current US scope	Potential alignment with group-level capital policy
GSJC (Real Estate)	DRC 5 – FDIC Reserve?	FDIC? or Local Reg?	Unclear (entity-specific)	Needs further confirmation from Controllers or Tiago
GSIB (Int’l)	DRC 6 – EBA?	European Regulators	Not in current US scope	Evaluate if it belongs to a group-wide policy extension

Table C: Non-Capital Requirements

Requirement	DRC or Similar	Regulatory Driver	Policy / Governance
Liquidity Coverage (LCR)	LCR DRC?	Federal Reserve / Basel	Potentially outside capital policy
Resolution Planning	-	FDIC / Fed – Title I	Separate resolution planning processes
Other Reporting	-	Varies (ECB, PRA, etc.)	Not capital-related; governance unclear

Key Points from the Transcript
	1.	Clarify Missing or “Random” DRCs
	•	Some DRCs appear to be for very narrow applications (e.g., a real estate entity’s reserve calculation).
	•	Verify with Controllers (or relevant owners) whether these items belong in your consolidated capital/risk policy scope.
	2.	Understand the Regulatory Source
	•	FDIC might apply to certain U.S. entities, PRA/BoE for UK entities, ECB/EBA for EU, etc.
	•	If the DRC is truly U.S. capital-related, it should already be in scope (or at least flagged for inclusion). If it’s missing, you need to determine why.
	3.	Push for a Unified View
	•	The conversation suggests you can rely on Tiago or a Controllers resource to collect and confirm the correct universe of DRCs.
	•	Once you have that list, present it in a coherent structure (e.g., the three tables above).
	4.	Ultimate Purpose
	•	Make it easy for senior management (e.g., Brian, Alex) to decide which items need urgent uplifting, which can wait, and how to expand policy scope if needed.

Action Items to Finalize DRC Categorization
	1.	Gather Detailed Inventory
	•	Work with Controllers, Finance, and other first-line teams to get the complete list of DRC items (both U.S. and non-U.S.).
	2.	Identify the Regulator & Entity
	•	For each DRC, confirm if it’s governed by Fed, FDIC, PRA, ECB, or another body.
	3.	Determine Policy Inclusion
	•	Check whether each DRC is already covered in the current U.S. capital policy.
	•	If not, decide whether to include it in a future global policy update or treat it separately.
	4.	Draft the Tables
	•	Create the “3-Table” framework (U.S. Capital, Non-U.S. Entities, Non-Capital Requirements) and populate with the data.
	5.	Review & Approval
	•	Present to management (e.g., Brian/Alex) for alignment on next steps, prioritization, or expansions of the policy scope.

Final Thoughts

The DRC categorization is intended to give you a clear roadmap of which rules belong where, who oversees them, and how they relate to your existing policies. By separating U.S. capital items from non-U.S. legal entities and non-capital items, you gain a straightforward, “bite-sized” view of a potentially complex web of regulatory requirements.





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from logging import debug
from typing import Dict
import os
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, dcc, html
from dash.dependencies import ALL, State

from myfuns import (genres, get_displayed_movies, get_highly_rated_movies,
                    get_recommended_movies)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], 
               suppress_callback_exceptions=True)
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H3("Movie Recommender", className="display-8"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("System 1 - Genre", href="/", active="exact"),
                dbc.NavLink("System 2 - Collaborative", href="/system-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])

def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
            [
                html.H1("Select a genre"),
                dcc.Dropdown(
                    id="genre-dropdown",
                    options=[{"label": k, "value": k} for k in genres],
                    value=None,
                    className="mb-4",
                ),
                html.Div(id="genre-output", className=""),
            ]
        )
    elif pathname == "/system-2":
        movies = get_displayed_movies()
        return html.Div(
            [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.H1("Rate some movies below to"),
                                    width="auto",
                                ),
                                dbc.Col(
                                    dbc.Button(
                                        children=[
                                            "Get recommendations ",
                                            html.I(className="bi bi-emoji-heart-eyes-fill"),
                                        ],
                                        size="lg",
                                        className="btn-success",
                                        id="button-recommend",
                                    ),
                                    className="p-0",
                                ),
                            ],
                            className="sticky-top bg-white py-2",
                        ),
                        html.Div(
                            [
                                get_movie_card(movie, with_rating=True)
                                for idx, movie in movies.iterrows()
                            ],
                            className="row row-cols-1 row-cols-5",
                            id="rating-movies",
                        ),
                    ],
                    id="rate-movie-container",
                ),
                html.H1(
                    "Your recommendations", id="your-recommendation",  style={"display": "none"}
                ),
                dcc.Loading(
                    [
                        dcc.Link(
                            "Try again", href="/system-2", refresh=True, className="mb-2 d-block"
                        ),
                        html.Div(
                            className="row row-cols-1 row-cols-5",
                            id="recommended-movies",
                        ),
                    ],
                    type="circle",
                ),
            ]
        )

@app.callback(Output("genre-output", "children"), Input("genre-dropdown", "value"))
def update_output(genre):
    if genre is None:
        return html.Div()
    else: 
        return [
            dbc.Row(
                [
                    html.Div(
                        [
                            *[
                                get_movie_card(movie)
                                for idx, movie in get_highly_rated_movies(genre).iterrows()
                            ],
                        ],
                        className="row row-cols-1 row-cols-5",
                    ),
                ]
            ),
        ]
    
def get_movie_card(movie, with_rating=False):
    return html.Div(
        dbc.Card(
            [
                dbc.CardImg(
                    src=f"https://liangfgithub.github.io/MovieImages/{movie.movie_id}.jpg?raw=true",
                    top=True,
                ),
                dbc.CardBody(
                    [
                        html.H6(movie.title, className="card-title text-center"),
                    ]
                ),
            ]
            + (
                [
                    dcc.RadioItems(
                        options=[
                            {"label": "1", "value": "1"},
                            {"label": "2", "value": "2"},
                            {"label": "3", "value": "3"},
                            {"label": "4", "value": "4"},
                            {"label": "5", "value": "5"},
                        ],
                        className="text-center",
                        id={"type": "movie_rating", "movie_id": movie.movie_id},
                        inputClassName="m-1",
                        labelClassName="px-1",
                    )
                ]
                if with_rating
                else []
            ),
            className="h-100",
        ),
        className="col mb-4",
    )
    
@app.callback(
    Output("rate-movie-container", "style"),
    Output("your-recommendation", "style"),
    [Input("button-recommend", "n_clicks")],
    prevent_initial_call=True,
)    
def on_recommend_button_clicked(n):
    return {"display": "none"}, {"display": "block"}

@app.callback(
    Output("recommended-movies", "children"),
    [Input("rate-movie-container", "style")],
    [
        State({"type": "movie_rating", "movie_id": ALL}, "value"),
        State({"type": "movie_rating", "movie_id": ALL}, "id"),
    ],
    prevent_initial_call=True,
)

def on_getting_recommendations(style, ratings, ids):
    rating_input = {
        ids[i]["movie_id"]: int(rating) for i, rating in enumerate(ratings) if rating is not None
    }
  
    recommended_movies = get_recommended_movies(rating_input)
 
    return [get_movie_card(movie) for idx, movie in recommended_movies.iterrows()]


@app.callback(
    Output("button-recommend", "disabled"),
    Input({"type": "movie_rating", "movie_id": ALL}, "value"),
)
def update_button_recommened_visibility(values):
    return not list(filter(None, values))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use PORT environment variable if it's set, otherwise default to 8080
    app.run_server(port=port, debug=True)

# In[ ]:





# In[ ]:




